import sys
import ast
from spiral import ronin
import nltk
import re
from IdentifiersTree import Tree
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

# define regex patterns for naming convention
snake_case_pattern = '^(?<!_)(?:(?<=_)[a-z]+|[a-z]+)(?:_(?!$)|(?<!_)_[a-z]+)*$'
camel_case_pattern = '^[a-z]+([A-Z][a-z]*)*$'
pascal_case_pattern = '^[A-Z][a-z]*([A-Z][a-z]*)*$'

# get a list of all names in the built-in scope
builtins = dir(__builtins__)

# filter out the names that don't start with an underscore (these are typically not methods)
builtins_identifiers = set([name for name in builtins if not name.startswith('_')])


def is_slang(word):
    for synset in wn.synsets(word):
        if "english slang" in synset.lexname():
            return True
    return False

def main():
    # check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 {} <target_file>".format(sys.argv[0]))
        sys.exit(1)

    # open a file passed by the command line
    file = open(sys.argv[1])
    code = file.read()
    class MyVisitor(ast.NodeVisitor):
        def __init__(self):
            self.tree = Tree()
            self.parent_stack = ['main']

        def visit_FunctionDef(self, node):
            self.parent_stack.append(node.name)
            self.tree.add_node(node.name, self.parent_stack[-2], node.lineno, 'function')
            self.generic_visit(node)
            self.parent_stack.pop()

        def visit_Assign(self, node):
            target = node.targets[0]
            if isinstance(target, ast.Name):
                self.tree.add_node(target.id, self.parent_stack[-1], node.lineno, 'variable')
            self.generic_visit(node)
            
        def get_identifiers_tree(self):
            return self.tree
            
        def __str__(self):
            return self.tree.__str__()

    tree = ast.parse(code)

    # create the visitor instance and visit the tree
    visitor = MyVisitor()
    visitor.visit(tree)
    myIdentifiersTree = visitor.get_identifiers_tree()



    print('''

IDENTIFIER QUALITY CHECKER:
Author: Minh Pham Dinh

          ''')
    
    def check_errors(node):
        if node.type == 'function':
            # Naming Style
            if not bool(re.match(snake_case_pattern, node.value)):
                node.error['NamingStyleError'] = True
                print(f"method '{node.value}' does not conform to snake_case naming style. (Line(s): {node.lines})")
            
            # we first split the method name
            words = ronin.split(node.value)
            tagged_words = nltk.pos_tag(words)
                
            # Verb Phrase
            if not any(tag.startswith('VB') for word, tag in tagged_words):
                print(f"Method name '{node.value}' is not a verb or verb phrase. (Line(s): {node.lines})")
                node.error['NotVerb'] = True
                
            # Dictionary Terms
            is_excluded = lambda tag: tag in ['DT', 'IN', 'PRP', 'CC', 'RP']
            if any((is_excluded(tagged_words[i][1]) or len(wn.synsets(words[i])) == 0) for i in range(len(words))):
                print(f"Method '{node.value}' contains unrecognized words. (Line(s): {node.lines})")
                node.error['UnrecognizableWord'] = True
                
            # Full Words
            if any(len(word) == 1 for word in words):
                print(f"Method '{node.value}' contains single-letter words or number. (Line(s): {node.lines})")
                node.error['NotFullWord'] = True
        
            # Idioms and Slang
            if any(is_slang(word) for word in words):
                print(f"Method '{node.value}' contains idioms or slang. (Line(s): {node.lines})")
                node.error['IsSlang'] = True
            
            # Abbreviations
            if any(word in builtins_identifiers for word in words):
                print(f"Method name '{node.value}' is already used as part of python's built-in identifiers. (Line(s): {node.lines})")
                node.error['builtInNameMisMatched'] = True
            
            # Length
            if len(words) > 7:
                print(f"Method '{node.value}' contains more than 7 words (Line(s): {node.lines})")
                node.error['MaximumLengthReached'] = True
                
        if node.type == 'variable':
            # Naming Style
            if len(node.lines) == 1:
                if not node.value.isupper():
                    node.error['NamingStyleError'] = True
                    print(f"Variable '{node.value}' is a constant (or has only been assigned once in the program in scope of {node.parent}), but not written in uppercase (Line(s): {node.lines})")
            else:
                if not bool(re.match(snake_case_pattern, node.value)):
                    node.error['NamingStyleError'] = True
                    print(f"Variable '{node.value}' does not conform to snake_case naming style. (Line(s): {node.lines})")
                
            # we first split the node.value name
            words = ronin.split(node.value)
            tagged_words = nltk.pos_tag(words)
            
            # Verb Phrase
            if not any(tag.startswith('NN') for word, tag in tagged_words):
                print(f"Variable name '{node.value}' is not a noun or noun phrase. (Line(s): {node.lines})")
                node.error['NotNoun'] = True
                
            # Dictionary Terms
            is_excluded = lambda tag: tag in ['DT', 'IN', 'PRP', 'CC', 'RP']
            if any((is_excluded(tagged_words[i][1]) or len(wn.synsets(words[i])) == 0) for i in range(len(words))):
                print(f"Variable '{node.value}' contains unrecognized words. (Line(s): {node.lines})")
                node.error['UnrecognizableWord'] = True
                
            # Full Words
            if any(len(word) == 1 for word in words):
                print(f"Variable '{node.value}' contains single-letter words or number. (Line(s): {node.lines})")
                node.error['NotFullWord'] = True
        
            # Idioms and Slang
            if any(is_slang(word) for word in words):
                print(f"Variable '{node.value}' contains idioms or slang. (Line(s): {node.lines})")
                node.error['IsSlang'] = True
            
            # Abbreviations
            if any(word in builtins_identifiers for word in words):
                print(f"Variable name '{node.value}' is already used as part of python's built-in identifiers. (Line(s): {node.lines})")
                node.error['builtInNameMisMatched'] = True
            
            # Length
            if len(node.value) > 79:
                print(f"Variable '{node.value}' contains more than 79 characters (Line(s): {node.lines})")
                node.error['MaximumLengthReached'] = True
        
    myIdentifiersTree.DFS_traverse(check_errors)
    # print(myIdentifiersTree)
    
if __name__ == '__main__':
    main()