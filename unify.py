#created By -Shal
#contains the implementation of the unify function of algorithm
#also recurisively changes assigned values


class unify():
    def __init__(self, E1=None, E2=None, variableList=None):
        if E1 and E2:
            #if both E1 and E2 are not  empty
            self.termsToUnify = [(E1, E2)]
            self.varibleList = variableList
        else:
            #both empty
            self.termsToUnify = []
            self.varibleList = variableList
    #print the result
    def printResult(self, functionList=None):
        if not self.termsToUnify:
            return 'Invalid ,Nothing To Unify'
        striingToPrint = ""

        for t in self.termsToUnify:
            if functionList:
                for indexVar in functionList:
                    temp1 = str(t[1]).replace("['" + indexVar + "',", "" + indexVar + "[")
                    temp1.replace("[", "(")
                    temp1.replace("]", ")")
                    temp2 = str(t[0]).replace("['" + indexVar + "',", "" + indexVar + "[")
                    temp2 = temp2.replace("[", "(")
                    temp2 = temp2.replace("]", ")")
                striingToPrint = striingToPrint + repr(temp1) + '='
                striingToPrint = striingToPrint + repr(temp2) + '  '
            else:

                    striingToPrint = striingToPrint + repr(t[1]) + '  =  '
                    striingToPrint = striingToPrint + repr(t[0]) + ' '
        print(striingToPrint)

    def unifyTerms(self, secondData):

        #check if both
        if isinstance(secondData, unify):

            if secondData.termsToUnify:
                for j in range(len(secondData.termsToUnify)):
                    for i in range(len(self.termsToUnify)):
                        #assignment to varibles
                        if self.termsToUnify[i][1] == secondData.termsToUnify[j][1]:
                            self.termsToUnify[i] = (self.termsToUnify[i][0], secondData.termsToUnify[j][0])
                    self.termsToUnify.append(secondData.termsToUnify[j])
            return self
        elif isinstance(secondData, list):
            # Backtrack And replace all terms with assigned variables
            tempList = []
            for element in secondData:
                if str(element) in self.varibleList:
                    flagReplace = False
                    for s in self.termsToUnify:
                        if s[1] == element:
                            tempList.append(s[0])
                            # replace Taken place
                            flagReplace = True
                    if not flagReplace:
                        tempList.append(element)
                elif isinstance(element, list):
                    tempList.append(self.unifyTerms(element))
                else:
                    tempList.append(element)
            return tempList
        else:
            True
