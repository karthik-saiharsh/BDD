import csv; # To read truth tables from csv files

class Node():
    '''Represents a single node unit used in the BDD'''
    def __init__(self, value: str):
        if value.isdigit():
            self.valuation: int = int(value)
            self.varName: str = None
        else:
            self.varName: str = value
            self.valuation: int = None
        self.left: Node = None # Left Child
        self.right: Node = None # Right Child
        self.parents: list[Node] = [] # Set of Parents

    def __repr__(self):
        return str(self.varName) if self.valuation==None else str(self.valuation)
    
    def setLeft(self, child):
        '''Sets node as left child'''
        child: Node = child
        self.left = child # Set node as left child
        if child != None:
            child.parents.append(self) # Add current node as parent to child

    def setRight(self, child):
        '''Sets node as left child'''
        child: Node = child
        self.right = child # Set node as right child
        if child != None:
            child.parents.append(self) # Add current node as parent to child


class BinaryDecisionDiagram():
    '''Binary Decision Diagram Class'''
    
    def __init__(self):
        self.nodes = [None] # Store all nodes of the BDD
        self.one = Node("1") # Terminal 1 Node
        self.zero = Node("0") # Terminal 0 Node
        self.arrayTree = [None]

    def buildTreeFromCSV(self, path: str):
        with open(path, "r") as data:
            truthTable = list(csv.reader(data))
        print(list(truthTable))

BDD = BinaryDecisionDiagram()
BDD.buildTreeFromCSV("./tt.csv")