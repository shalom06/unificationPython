#created By -Shal
#contains the implementation of the algorithm and related to the algorithm


from unify import unify


#checks if both lists are empty
def checkIfEitherEmpty(E1, E2):
    if not E1 or not E2:
        return True
    else:
        return False

#checks if the data is valid
def checkIfValid(data,functionList, variableList, atomList):
    if str(data) in functionList or str(data) in variableList or str(data) in atomList:
        return True
    else:
        return False

#main algorithm
#algorithm can be found at http://www.cs.trincoll.edu/~ram/cpsc352/notes/unification.html

def unifyWithOccursCheck(E1, E2, functionList, variableList, atomList):
    # check if empty List
    if checkIfEitherEmpty(E1, E2,):
        return unify(None,None,variableList)


    if checkIfValid(E1,functionList, variableList, atomList) or checkIfValid(E2,functionList, variableList, atomList):
        if E1 == E2:
            return unify(None,None,variableList)

        if str(E1) in variableList:

            if E1 in E2:
                #assignment  will lead to infinite loop hence exit with occurs check error
                return exit("Violates Occurs Check ")
            else:
                return unify(E2, E1,variableList)
        if str(E2) in variableList:

            if E2 in E1:
                # assignment  will lead to infinite loop hence exit with occurs check error
                return exit("Violates Occurs Check ")
            else:
                return unify(E1, E2,variableList)
        if not E1 in variableList and not  E2 in variableList:
            return exit("Nope , cannot be unified!")
    # recusrisve funtion to get assignments
    SUBS1 = unifyWithOccursCheck(E1[0], E2[0], functionList, variableList, atomList)

    TE1 = SUBS1.unifyTerms(E1[1:])
    TE2 = SUBS1.unifyTerms(E2[1:])
    #recusrisve funtion to get assignments
    SUBS2 = unifyWithOccursCheck(TE1, TE2, functionList, variableList, atomList)

    return SUBS1.unifyTerms(SUBS2)
