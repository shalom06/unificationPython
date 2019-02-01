#created by -Shal
#take the input and converts it into the format required by algorithm
#  http://www.cs.trincoll.edu/~ram/cpsc352/notes/unification.html
# example CONVENTIONAL NOTATION     LIST NOTATION
# ---------------------     -------------
# p(a,b)                    (p a b)
# p(f(a),g(X,Y))            (p (f a) (g X Y))
import re
from collections import OrderedDict
import unifyFunctions as unify

class unification:
    def __init__(self, firstTerm, secondTerm):
        #Intilization of class variables
        self.firstTerm = firstTerm
        self.firstTermCopy = firstTerm
        self.errorList=["Violates Occurs Check","Nope , Cannot  cannot be unified!"]

        self.secondTerm = secondTerm
        self.secondTermCopy = secondTerm
        self.firstTermType = "unknown"
        self.secondTermType = "unknown"
        self.firstTermList = []
        self.secondTermList = []
        self.atomList = []
        self.variableList = []
        self.functionList = []
        self.getTheTypeOfTerms()
        self.checkIfUnified()

    def checkIfUnified(self):
        if self.firstTermType is 'atom':
            self.getAtoms(1)
        if self.secondTermType is 'atom':
            self.getAtoms(2)
        if self.firstTermType is 'variable':
            self.getVariables(1)
        if self.secondTermType is 'variable':
            self.getVariables(2)
        if self.firstTermType is 'complex':
            self.getComplex(1)
        if self.secondTermType is 'complex':
            self.getComplex(2)
        self.initilize()
        self.createList()

        res = unify.unifyWithOccursCheck(self.firstTermList, self.secondTermList,self.functionList,self.variableList,self.atomList)


        if self.functionList:
            print("Yes ,Unification Is Possible")
            res.printResult(self.functionList)
        else:
            print("Yes ,Unification Is Possible")
            res.printResult()
        # print(self.functionList)



    def checkifAtom(self):

        if (self.firstTerm[0].islower() or self.firstTerm[0] == "'") and ("(" and ")" not in self.firstTerm):
            self.firstTermType = "atom"

        if (self.secondTerm[0].islower() or self.secondTerm[0] == "'") and ("(" and ")" not in self.secondTerm):
            self.secondTermType = "atom"

    def checkIfVarible(self):
        if self.firstTermType is 'unknown':
            if (self.firstTerm[0].isupper() or self.firstTerm[0] == "_") and ("(" and ")" not in self.firstTerm):
                self.firstTermType = "variable"

        if self.secondTermType is 'unknown':
            if (self.secondTerm[0].isupper() or self.secondTerm[0] == "_") and ("(" and ")" not in self.secondTerm):
                self.secondTermType = "variable"



    def checkIfComplexTerm(self):
        if self.firstTermType is 'unknown':
            if "(" and ")" in self.firstTerm:
                self.firstTermType = 'complex'
        if self.secondTermType is 'unknown':
            if "(" and ")" in self.secondTerm:
                self.secondTermType = 'complex'

    def getTheTypeOfTerms(self):
        self.checkifAtom()
        self.checkIfVarible()
        self.checkIfComplexTerm()

    #gets atoms/constants from
    def getAtoms(self, flag):
        if flag == 1:
            atomList = []
            atomList = re.findall(r"\b[^A-Z\s\d]+\b", self.firstTerm)
            atomList = list(OrderedDict.fromkeys(atomList))
            self.atomList = self.atomList + atomList
        elif flag == 2:
            atomList = []
            atomList = re.findall(r"\b[^A-Z\s\d]+\b", self.secondTerm)
            atomList = list(OrderedDict.fromkeys(atomList))
            self.atomList = self.atomList + atomList
    #gets Variables using regex
    def getVariables(self, flag):
        if flag == 1:
            variableList = []
            variableList = re.findall(r"\w*[A-Z]+\w*", self.firstTerm)
            variableList = list(OrderedDict.fromkeys(variableList))
            self.variableList = self.variableList + variableList
            self.variableList = list(OrderedDict.fromkeys(self.variableList))
        elif flag == 2:
            variableList = []
            variableList = re.findall(r"\w*[A-Z]+\w*", self.secondTerm)
            variableList = list(OrderedDict.fromkeys(variableList))
            self.variableList = self.variableList + variableList
            self.variableList = list(OrderedDict.fromkeys(self.variableList))

    def getComplex(self, flag):
        if flag == 1:
            self.getFunctions(1)
            self.firstTerm = self.removeBracketsAndCommas(self.firstTerm)
            self.getAtoms(1)
            self.getVariables(1)
            self.removeAtomsWhichAreFucktions()

        if flag == 2:
            self.getFunctions(2)
            self.secondTerm = self.removeBracketsAndCommas(self.secondTerm)
            self.getAtoms(2)
            self.getVariables(2)
            self.removeAtomsWhichAreFucktions()
    #gets function in terms using regex
    def getFunctions(self, flag):
        if flag == 1:
            functionList = []
            functionList = re.findall(r"\w+(?!\s*\w+)(?=\s*\w*\((?!\s*[\w\*]+\s+[\w\*]+))", self.firstTerm)
            # functionList = list(OrderedDict.fromkeys(functionList))
            functionList = self.remove_duplicates(functionList)
            self.functionList = self.functionList + functionList
        if flag == 2:
            functionList = []
            functionList = re.findall(r"\w+(?!\s*\w+)(?=\s*\w*\((?!\s*[\w\*]+\s+[\w\*]+))", self.secondTerm)
            # functionList = list(OrderedDict.fromkeys(functionList))
            functionList = self.remove_duplicates(functionList)
            self.functionList = self.functionList + functionList
    # removes duplicates from list
    def remove_duplicates(self, lst):
        res = []
        for x in lst:
            if x not in res:
                res.append(x)
        return res
    #removes brackets and commas
    def removeBracketsAndCommas(self, dataRemove):
        dataRemove = str(dataRemove).replace(",", " ")
        dataRemove = str(dataRemove).replace("(", " ")
        dataRemove = str(dataRemove).replace(")", " ")
        return dataRemove
    #removes incorrect function assignments as atoms
    def removeAtomsWhichAreFucktions(self):
        self.atomList = list(set(self.atomList) - set(self.functionList))


    #intilize the variables
    def initilize(self):

        # x=self.functionList[0]
        if self.functionList:
            globals()[str(self.functionList[0])] = str(self.functionList[0])

        if len(self.functionList) > 1:
            for i in range(1, len(self.functionList)):
                # print(i)
                globals()[str(self.functionList[i])] = str(self.functionList[i])
        if self.variableList:
            for v in self.variableList:
                globals()[v] = v
        if self.atomList:
            for a in self.atomList:
                globals()[a] = a


    #creates the required list
    #yes i know alot of pattern matching is involved

    def createList(self):
        if self.functionList:
            for indexVar in self.functionList:
                self.firstTermCopy = str(self.firstTermCopy).replace("" + indexVar + "(", "(" + indexVar + ",")
                self.secondTermCopy = str(self.secondTermCopy).replace("" + indexVar + "(", "(" + indexVar + ",")
        self.firstTermCopy = str(self.firstTermCopy).replace(",", ", ")
        self.secondTermCopy = str(self.secondTermCopy).replace(",", ", ")
        self.firstTermCopy = str(self.firstTermCopy).replace("(", "[")
        self.secondTermCopy = str(self.secondTermCopy).replace("(", "[")
        self.firstTermCopy = str(self.firstTermCopy).replace(")", "]")
        self.secondTermCopy = str(self.secondTermCopy).replace(")", "]")

        exec('self.firstTermList=eval(self.firstTermCopy)')
        exec('self.secondTermList=eval(self.secondTermCopy)')
        # self.firstTermList = self.firstTermCopy
        # self.secondTermList=self.secondTermCopy
