#created by -Shal
#
# this is the the runner file
#
#just takes input from user
#

from unification import unification

#take input from user
term1 = input(" Enter First Term : ex : f(f(X,Y),X) ")
term2= input("Enter Second Term : ex : f(f(X,Y),X)")
print()

print()
term1=term1.replace(" ", "")
term2=term2.replace(" ","")
print("First Term=  "+term1)
print("Second Term=  "+term2)
print()
check=unification(term1,term2)
