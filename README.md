
# BDD-A boolean logic function Synthesiser
## Consider the following Truth Table:

| x1 | x2 | x3 | f |
| :---| :---| :---| :-- |
| `0` | `0` | `0` | `0` |
| `0` | `0` | `1` | `1` |
| `0` | `1` | `0` | `1` |
| `0` | `1` | `1` | `0` |
| `1` | `0` | `0` | `1` |
| `1` | `0` | `1` | `0` |
| `1` | `1` | `0` | `1` |
| `1` | `1` | `1` | `1` |

- f is a function of x1, x2, and x3.
- BDD or Binary Decision Diagram is an efficient Data structure to store and manage such boolean functions and truth tables.



## Demo

- The truth table can be passed into the program as a csv file.
- THe program can synthesize a boolean algebra function for the truth table and output it in either SOP(sum of products) or POS(product of sums) form

### SOP Expression
`x3'x2' + x3x2' + x3x2 + x2 + x1`

### POS Expression
`( x3 + x2 ) . ( x3 + x2' ) . x1'`

## Run Locally

Clone the repo

```bash
git clone https://github.com/karthik-saiharsh/BDD.git
```

Go to the project directory

```bash
cd BDD
```

Create a python file (preferable in the same directory)

```bash
touch main.py
```

Import BDD Class into the newly created Python file

```python
from BDD import *
```

Create a BDD Class and call the `generateExpressionFromCSV` method

```python
BDD = BinaryDecisionDiagram()
BDD.generateExpressionFromCSV("truthTable.csv", isSOP=False)
```
## Authors

- [@karthik-saiharsh](https://github.com/karthik-saiharsh)

