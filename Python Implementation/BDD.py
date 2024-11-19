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
        self.root = None

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
                # Add all non leaf nodes to the tree
                new_node = Node(self.arrayTree[i])
                if i != 1:
                    if i % 2 == 0:
                        nodes[i//2].setLeft(new_node)
                    else:
                        nodes[i//2].setRight(new_node)
                nodes.append(new_node)
            else:
                # Maintain only one set of zero and one nodes and reuse them
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
        self.root = self.nodes[1]

    def simplifyBDD(self):
        '''Simplifies the BDD'''
        self.__removeRedundant()
        self.__removeDuplicates()

    def __removeRedundant(self):
        '''Removes redundant Nodes, i.e last but one level nodes with same left and right function valuation'''
        nodes_to_delete = []
        for i in range(1, len(self.nodes)):
            if self.nodes[i].left != None and self.nodes[i].right != None:
                if (self.nodes[i].left==self.nodes[i].right==self.one) or (self.nodes[i].left==self.nodes[i].right==self.zero):
                    nodes_to_delete.append(self.nodes[i])
        
        for node in nodes_to_delete:
            parent = node.parents[0]
            child = node.left
            child.parents.remove(node)
            if parent.left == node:
                parent.setLeft(child)
            else:
                parent.setRight(child)
            self.nodes.remove(node)

    def __removeDuplicates(self):
        '''Remove all those nodes which are duplicates, i.e 2 different nodes with the same children'''
        nodes_to_remove = []
        for i in range(1, len(self.nodes)):
            for j in range(1, len(self.nodes)):
                if i != j and (self.nodes[i].left, self.nodes[i].right, self.nodes[j].left, self.nodes[j].right)!=(None, None, None, None):
                    if (self.nodes[i].left, self.nodes[i].right) == (self.nodes[j].left, self.nodes[j].right):
                        node_pair = {self.nodes[i], self.nodes[j]}
                        if node_pair not in nodes_to_remove:
                            nodes_to_remove.append(node_pair)
        
        # Remove the dulicate nodes
        for node_pair in nodes_to_remove:
            original, duplicate = node_pair
            # Make the duplicate node disown it's children
            duplicate.left.parents.remove(duplicate)
            duplicate.right.parents.remove(duplicate)
            if duplicate.parents[0] == duplicate:
                duplicate.parents[0].setLeft(original)
            else:
                duplicate.parents[0].setRight(original)
            self.nodes.remove(duplicate)

BDD = BinaryDecisionDiagram()
BDD.readCSV("Python Implementation/tt2.csv")
BDD.buildBDD()
BDD.simplifyBDD()
print()