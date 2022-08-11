import collections
import math
import os
from builtins import print, float, enumerate, range
from decimal import Decimal
from operator import indexOf, le

from Tools.scripts.combinerefs import read
from setuptools._distutils.command.config import config
from itertools import chain
from collections import Counter

#list and get the name of all txt files in the directory and print nuber of files in it
list12 = os.listdir("D:\IR\Mycode\Documents")

number_files = len(list12)
print("Files Names : ")
print(list12)
print("Number of Files : ")
print(number_files)

#to read all the data from the files and put them in a 2d list
i=0
container=[]
while(i<number_files):
    location = "D:\IR\Documents" +"\\" + list12[i]
    file = open(location,"r")
    ready=file.read()
    container.append(ready)
    file.close()
    print("files have : " + list12[i])
    print("File : " + ready)
    i+=1


#to delete all stop words like ( ". and , and \n + ! ?")
token=[]
row=0
for i in container:
        token.append(container[row].replace(".",""))
        row+=1
token2=[]
row=0
for i in token:
        token2.append(token[row].replace(",",""))
        row+=1
row=0
token=[]
for i in token2:
        token.append(token2[row].replace('\n'," "))
        row+=1

token2=[]
row=0
for i in token:
        token2.append(token[row].replace("+",""))
        row+=1
row=0
token=[]
for i in token2:
        token.append(token2[row].replace("_",""))
        row+=1


token2=[]
row=0
for i in token:
        token2.append(token[row].replace("!",""))
        row+=1
row=0
token=[]
for i in token2:
        token.append(token2[row].replace("?",""))
        row+=1


token2=[]
row=0
for i in token:
        token2.append(token[row].replace("#",""))
        row+=1
row=0
token=[]
for i in token2:
        token.append(token2[row].replace("@",""))
        row+=1


token2=[]
row=0
for i in token:
        token2.append(token[row].replace("$",""))
        row+=1
row=0
token=[]
for i in token2:
        token.append(token2[row].replace("%",""))
        row+=1


token2=[]
row=0
for i in token:
        token2.append(token[row].replace("^",""))
        row+=1
#print(token2)
row=0
token=[]
for i in token2:
        token.append(token2[row].replace("&",""))
        row+=1




#to convert to a lower case all things
row =0
for i in token:
        token[row]=token[row].lower()
        row+=1


#split the lists into tokens
print("------------------------------------------------")
print("Files as terms after stop words . ")
row =0
token2=[]
for i in token:
        token2.append(token[row].split())
        print("file name : " + str(list12[row]) + str(token[row].split()))
        row+=1


#split it into 1d list to count and control it easily
d1list=[]
d1list=[x for sub in token2 for x in sub]

#how times every word repeated and return the value into a dictionary
count=Counter(d1list)

for key in count:
    b=0


#take the key in the list
alone=count.keys()


#know how many documents create the term
numitem=0
boollist=[]
listone = []
for i in alone:
    for j in token2:
        for x in j:
            if i==x:
                numitem+=1
                break
    boollist.append(numitem)
    numitem=0


#convert the alone terms into list instead of dictionry
mymy = []
for i in alone:
    mymy.append(i)

print("Terms in all Files : ")
print(mymy)
print("------------------------------------------")
print("Terms " + "\t" + "  Df  ")
for i in range(len(mymy)) :
    print(mymy[i] + "\t\t" + str(boollist[i]))


for x in token2 :
    b = 0
print("----------------------------------------------")
NumOfDocAndPosition = []
for i in mymy :
    listOfItem = []
    for itrr , x in enumerate(token2) :
        listOfDoc = []
        listOfDoc.append(itrr+1)
        for ind , j in enumerate(x) :
            if j == i :
                listOfDoc.append(ind + 1)

        if len(listOfDoc) != 1 :
            listOfItem.append(listOfDoc)

    NumOfDocAndPosition.append(listOfItem)

print("-------------------------------------------------")



IndexPostindsList = []
ItemList = []
int = 0
for i in mymy :
    ItemList = []
    ItemList.append(mymy[int])
    ItemList.append(boollist[int])
    ItemList.append(NumOfDocAndPosition[int])
    IndexPostindsList.append(ItemList)
    int +=1

print("List of Index Postings : ")

i = 0
for i in range(len(mymy)) :
    print( "< " + mymy[i] + " , " + " number of docs containing " + str(boollist[i]))
    for x in NumOfDocAndPosition[i] :
        if x[0] == 1 :
            print("Doc1 : ")
        if x[0] == 2 :
            print("Doc2 : ")
        if x[0] == 3 :
            print("Doc3 : ")
        if x[0] == 4 :
            print("Doc4 : ")
        if x[0] == 5 :
            print("Doc5 : ")
        if x[0] == 6 :
            print("Doc6 : ")
        if x[0] == 7 :
            print("Doc7 : ")
        if x[0] == 8 :
            print("Doc8 : ")
        if x[0] == 9 :
            print("Doc9 : ")
        if x[0] == 10 :
            print("Doc10 : ")
        for ite , y in enumerate(x) :
            if ite == 0 :
                b = 0
            else :
                print("position : " + str(x[ite]))
    print(">")
    i+=1


print("------------------------------------------------------------------------------------------")


print("all terms in Documents : ")
print(IndexPostindsList)



print("------------------------------------------------------------------------------------------")

currentNum = 0
Tf=[]
templist=[]
tmptf=[]
for x in NumOfDocAndPosition:
    for y in x:
        templist.append(y[0])
        templist.append(len(y)-1)
        tmptf.append(templist)
        templist=[]
    Tf.append(tmptf)
    tmptf = []

IDFList = []
for b in boollist :
    n= len(list12) / b
    p = math.log( n, 10)
    IDFList.append(p)

print("Df and Tf in Documents -------------------------")
i = 0
for i in range(len(mymy)) :
    print( "< " + mymy[i] + " , " + "IDF is " + str(IDFList[i]))
    for x in Tf[i] :
        if x[0] == 1 :
            print("Doc1 : " + list12[x[0]-1])
        if x[0] == 2 :
            print("Doc2 : " + list12[x[0]-1])
        if x[0] == 3 :
            print("Doc3 : " + list12[x[0]-1])
        if x[0] == 4 :
            print("Doc4 : " + list12[x[0]-1])
        if x[0] == 5 :
            print("Doc5 : " + list12[x[0]-1])
        if x[0] == 6 :
            print("Doc6 : " + list12[x[0]-1])
        if x[0] == 7 :
            print("Doc7 : "+ list12[x[0]-1])
        if x[0] == 8 :
            print("Doc8 : " + list12[x[0]-1])
        if x[0] == 9 :
            print("Doc9 : " + list12[x[0]-1])
        if x[0] == 10 :
            print("Doc10 : " + list12[x[0]-1])
        for ite , y in enumerate(x) :
            if ite == 0 :
                b = 0
            else :
                print("number of Frequence (TF) : " + str(x[ite]))
                print("Tf Weight : " + " \t " + str(math.log( (1+x[ite]) , 10 ) ))
    print(">")
    i+=1
print("---------------------------------------------------")
#this is her we will show the weight vector model
print("--------------------------------------------------------------")
print("weight vector in Documents -------------------------")


ListWeight = []
listtemb2=[]
ListTemp = []
for o in range(len(mymy)):

    for x in Tf[o] :
        for itee , yy in enumerate(x):
            if itee == 0 :
                b = 0

            else:

                ListTemp.append(round(( math.log( 1 + yy , 10)) * IDFList[o],3))

    ListWeight.append(ListTemp)
    ListTemp = []
    listtemb2=[]


ListOfDocHave= []
for i in NumOfDocAndPosition :
    TempList = []
    for x in i :

        for ituu, y in enumerate(x) :
            if ituu == 0 :
                TempList.append(y)
            else:
                b = 0

    ListOfDocHave.append(TempList)


ListWeightAfterEdit = []
for o in range(len(mymy)) :
    TempListW = []

    for i in range(len(list12) + 1) :
        if i in ListOfDocHave[o] :
            num = ListOfDocHave[o].index(i)
            TempListW.append(ListWeight[o][num-1])
        elif i == 0 :
            continue
        else:
            TempListW.append(0.0)

    ListWeightAfterEdit.append(TempListW)

print( "\t\t\t" + str(list12) )
for i in range(len(mymy)) :
    print(mymy[i] + "\t\t" + str(ListWeightAfterEdit[i]) , sep="\t")
#this is document lenghth
print("---------------------------------------")
print("Length of each Document : ")
i = 0
for iuet , i in enumerate(ListWeightAfterEdit[0]) :
    print( "Document " +  str(list12[iuet]))
    sc = 0
    for iute2 , x in enumerate(mymy):
        sc = sc + math.pow(ListWeightAfterEdit[iute2][iuet] , 2 )
    print("Length : " + str(math.sqrt(sc)))




# this is query
print("---------------------------------------------------------------")
QueryList = []
Query = input("enter your free text : ")
if len(Query) != 0 :
    QueryList.append(Query.lower().split())

print(QueryList)

print("------------------------------------------------------------------------------------------")

TfForQuery = []

for i in range(len(QueryList[0])) :
    iii = 0
    for ity , x in enumerate(QueryList[0]) :
        if QueryList[0][i] == QueryList[0][ity] :
            iii = iii +  1
        else:
            b = 0
    TfForQuery.append(iii)


print("Query List : ")
print(QueryList)
print("Each Term in Query Tf is : ")
print(TfForQuery)
print("Each Term in Query Tf weight is : ")
TfForQueryWeight = []
for i in range(len(TfForQuery)) :
    TfForQueryWeight.append(math.log((1 + TfForQuery[i]) , 10))
print(str(TfForQueryWeight))



print("------------------------------------------------------------------------------------------")
print("Search Terms in Docs ")
docsThatHaveTerm = []
for x in QueryList :
    for y in x :
        for itur ,  z in enumerate(mymy) :
            if y == z :
                tempfounf = []
                tempdef = []
                tempdef.append(y)
                tempfounf.append(tempdef)
                tempdef = []
                tempdef.append(boollist[itur])
                tempfounf.append(tempdef)
                tempfounf.append(NumOfDocAndPosition[itur])
                docsThatHaveTerm.append(tempfounf)

print("List that have query and items and posetion ")
if len(docsThatHaveTerm) != 0 :
    print(docsThatHaveTerm)
else:
    print("no terms in document match that")

print("------------------------------------------------------------------------------------------")
#found tf for each terms in each document
print("find each term Tf in every documents : ")


for itur2 , x in enumerate(docsThatHaveTerm)  :
    ListTfForEachTerm = []
    for itur3 , y in enumerate(x) :
        if itur3 == 2 :
            for z in y :
                ListTfForEachTerm.append(len(z) - 1 )

    docsThatHaveTerm[itur2].append(ListTfForEachTerm)


print("each terms with [number of document] , [document and position ] , [tf for each document]")
print(docsThatHaveTerm)

print("------------------------------------------------------------------------------------------")
#Here is intersection
rep = []
for i in docsThatHaveTerm:
    for intr,x in enumerate(i):
        if intr == 2:
            for y in x :
                for qq,z in enumerate(y) :
                    if qq == 0 :
                        if z in rep :
                            b = 0
                        else:
                            print("Document Have Query " + list12[z-1])
                            rep.append(z)


