![GitHub top language](https://img.shields.io/github/languages/top/minhphd/Namesake-Scoped?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/minhphd/Namesake-Scoped?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/minhphd/Namesake-Scoped?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/minhphd/Namesake-Scoped?style=for-the-badge)

# Namesake-Scoped

Namesake-Scoped is a fork of the Namesake repository with additional features. 

Namesake is an open-source tool for assessing confusing naming combinations in Python programs.
Namesake flags confusing identifier naming combinations that are similar in:
* orthography (word form)
* phonology (pronunciation)
* or semantics (meaning).

Namesake-Scoped is an improve version of Namesake with the ability to only check identifiers with same scope. It also checks for identifer quality as according to PEP8 and best programming practices for python.

## 💡 What is Lexical Similarity in Code?
Lexical access describes the retrieval of word shape (orthography), pronunciation (phonology), and meaning (semantics) from memory during reading for comprehension. 


**Orthographic similarity** focuses on the the similarity in word form on the level of letters. Not to be confused by editing distance or Levenshtein's distance, where one letter is replaced by another, orthographic similarity focuses on the similarities between letters shapes.  A good example is the confusion between 'O' and 'C' as individual letters or within words and sentences. Here's a common exmple in code:


<p align="center">
  <img width="400" height="360" src="/documentation/imgs/ortho_example.drawio.png">
</p>


**Phonological similarity** describes two words that share a similar or identical pronunciation, also known as homophones:


<p align="center">
  <img width="400" height="290" src="/documentation/imgs/real_phono.drawio.png">
</p>


**Semantic similarity** describes words that share a meaning (synonyms):


<p align="center">
  <img width="400" height="350" src="/documentation/imgs/semantic.drawio.png">
</p>

## 💡 What is the criterias for identifiers naming?
In our checker, we get list method names and variable names from a python file and check it according to these criterias.

## <p align='center'> Variable naming criterias</p>
<div align="center">
  
|Criteria| Describtion |
|--------------|----------------------------------------------|
| Naming Style | The variable name should be in snake_case style or should be in uppercase if it's a constant or has only been assigned once |
| Verb Phrase  | The variable name should be a noun or noun phrase                                                                               |
| Dict. Terms  | The variable name should not contain any unrecognized words                                                                     |
| Full Words   | The variable name should not contain any single-letter words or numbers                                                         |
| Idioms/Slang | The variable name should not contain any idioms or slang                                                                          |
| Abbrev.      | The variable name should not conflict with any Python built-in identifiers                                                        |
| Length       | The variable name should not exceed 79 characters                                                                                 |

</div>
  
## <p align='center'> Method naming criterias </p>
<div align="center">
  
|Criteria| Describtion |
|--------------|----------------------------------------------|
| Naming Style | The method name should be in snake_case style |
| Verb Phrase  | The method name should be a verb or verb phrase |
| Dict. Terms  | The method name should not contain any unrecognized words |
| Full Words   | The method name should not contain any single-letter words or numbers |
| Idioms/Slang | The method name should not contain any idioms or slang |
| Abbrev.      | The method name should not conflict with any Python built-in identifiers |
| Length       | The method name should not contain more than 7 words |
 
</div>

## Usage
To use Namesake-Scoped, you can follow these steps:

1. Clone the Namesake-Scoped repository using git clone https://github.com/minhphd/Namesake-Scoped.git
2. Navigate to the directory where Namesake-Scoped is cloned using 

`cd Namesake-Scoped`

3. Install any necessary dependencies using 

`pip install -r requirements.txt`

4. Run Namesake-Scoped using the command 

`python3.9 namesake_with_scope.py [path to your code file]`. 

The threshold for orthographic, phonological, and semantic warnings are set at .45, .8, and .9 respectively. Thresholds can be changed manually through editing line 309, 310, and 311 in the namesake_with_scope.py file.

5. To check for identifiers naming quality, run 

`python3.9 identifiers_quality_checkers.py [path to your code file]`

## 👀 Example Running Namesake-Scoped:
<p align="center">
  <img width="880" alt="Screen Shot 2023-05-08 at 13 07 03" src="https://user-images.githubusercontent.com/92499186/236886380-9dcef869-0ad6-4498-8c7e-0d4a9ec9a52f.png">
</p>

## 👀 Example Running Identifers quality checker:
<p align="center">
  <img width="1085" alt="Screen Shot 2023-05-08 at 13 08 30" src="https://user-images.githubusercontent.com/92499186/236886633-e6f93121-4a82-447a-bf5d-b585813d9fa6.png">
</p>


## 📝 Citation:
[Naser Al Madi. 2022. Namesake: A Checker of Lexical Similarity in Identifier
Names. In Proceedings of The 37th IEEE/ACM International Conference on
Automated Software Engineering Workshops (ASEW 2022).](https://www.researchgate.net/publication/363207604_Namesake_A_Checker_of_Lexical_Similarity_in_Identifier_Names)

[R. S. Alsuhaibani, C. D. Newman, M. J. Decker, M. L. Collard and J. I. Maletic, "An Approach to Automatically Assess Method Names," 2022 IEEE/ACM 30th International Conference on Program Comprehension (ICPC 2022).](https://ieeexplore.ieee.org/document/9796230)


## ⚖️ License:

 **MIT (Free Software, Hell Yeah!)**
