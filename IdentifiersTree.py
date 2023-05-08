import pprint

class Node:
    def __init__(self, value, parent, line, node_type):
        self.value = value
        self.lines = [line]
        self.parent = parent
        self.childrens = []
        self.type = node_type
        self.error = {
                        'NamingStyleError': False,
                        'NotNoun': False,
                        'UnrecognizableWord': False,
                        'NotFullWord': False,
                        'IsSlang': False,
                        'builtInNameMisMatched': False,
                    }
    
class Tree:
    def __init__(self):
        self.root = Node('main', None, None, None)
        
    def add_node(self, value, parent, line, node_type):
        parent_node = self.find_parent(self.root, parent)
        if parent_node == None:
            print(f'could not locate parent {parent} of {value}')
        for child in parent_node.childrens:
            if (value == child.value):
                child.lines.append(line)
                return
        parent_node.childrens.append(Node(value, parent, line, node_type))


    def find_parent(self, node, parent):
        if node.value == parent:
            return node
        
        for child in node.childrens:
            result = self.find_parent(child, parent)
            if result != None:
                return result
        return None

    
    def find_node(self, value):
        return self.find_node_driver(self.root, value)

    
    def find_node_driver(self, node, value):
        if node.value == value:
            return node        
        for child in node.childrens:
            result = self.find_node_driver(child, value)
            if result != None:
                return result
        return None
 
    
    def DFS_traverse(self, func):
        self.DFS_traverser(self.root, func)

    
    def DFS_traverser(self, node, func):
        func(node)
        if node.childrens == {}:
            return
        for child in node.childrens:
            self.DFS_traverser(child, func)

            
    def traverse_layers(self, func):
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.childrens:
                for child in curr_node.childrens:
                    queue.append(child)
                func([(child.value, child.lines) for child in curr_node.childrens], curr_node)


    def to_dict(self):
        return {'root': self.to_dict_traversal(self.root)}

    
    def to_dict_traversal(self, node):
        res_dict = {}
        if node.childrens == {}:
            return
        else:
            for child in node.childrens:
                res_dict[child.value] = self.to_dict_traversal(child)
            return res_dict

        
    def __str__(self):
        return pprint.pformat(self.to_dict())