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
        return self.varName if self.valuation==None else str(self.valuation)
    
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
        self.arrayTree = [None] # Array represenation of the Binary Decision Tree
        self.variables = [] # Keep track of member variables

    def readCSV(self, path: str):
        # Read Truth table from csv
        with open(path, "r") as data:
            truthTable = list(csv.reader(data))
        self.variables += truthTable[0][0:-1]
        
        '''Build Tree in Array Form'''
        for i in range(len(self.variables)):
            self.arrayTree += ([self.variables[i]] * 2**i)
        
        '''Add in function valuation nodes'''
        for i in range(1, len(truthTable)):
            self.arrayTree += truthTable[i][-1]

    def buildBDD(self):
        '''Constructs a Binary Tree from array represenataiotn'''
        nodes = [None]
        for i in range(1, len(self.arrayTree)):
            if not self.arrayTree[i].isdigit():
                new_node = Node(self.arrayTree[i])
                if i != 1:
                    if i % 2 == 0:
                        nodes[i//2].setLeft(new_node)
                    else:
                        nodes[i//2].setRight(new_node)
                nodes.append(new_node)
            else:
                if i%2 == 0:
                    if self.arrayTree[i] == '1':
                        nodes[i//2].setLeft(self.one)
                    else:
                        nodes[i//2].setLeft(self.zero)
                else:
                    if self.arrayTree[i] == '1':
                        nodes[i//2].setRight(self.one)
                    else:
                        nodes[i//2].setRight(self.zero)
        nodes += [self.one, self.zero]
        self.nodes = nodes

BDD = BinaryDecisionDiagram()
BDD.readCSV("Python Implementation/tt.csv")
BDD.buildBDD()