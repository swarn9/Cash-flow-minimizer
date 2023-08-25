import os
import string

bank_list = ["Bank_of_America",
             "Wells_Fargo",
             "Royal_Bank_of_Canada",
             "Westpac",
             "Goldman_Sachs",
             "National_Australia_Bank"]

paymentModes = ["Google_Pay", "AliPay", "Paytm"]

#net amount = Sum pf all credits(amounts ot be recieved) - Sum of all debits(amounts to pay)
"""_summary_
GS, BA, 100; GS, WF, 200
b1: p1,p2
b2: p3,p4
    
"""
#GS, BA, 100; GS, WF, 200
#b1: p1,p2
#b2: p3,p4
def main():

    #tranDict = getTransaction()
    #print(tranDict)
    
    cash = [[0, 2000, 4000],
[0, 0, 3000],
[0, 0, 0]];

    min_cash(cash)

# amount is stroing net amount to be settled
# to-from person p(i). if amount(p) is +, then ith person gives amount[i].
# otherwise amount[p] gives -amount[i]
def minCashFlow(amount):
    maxCredit = max(amount)
    maxCIndex = amount.index(maxCredit)
    maxDebit = min(amount)
    maxDIndex = amount.index(maxDebit)
    
    #results in 0
    if(amount[maxCIndex] == 0 and amount[maxDIndex] == 0):
        return
    
    #Find minimum of two amounts
    minumum = min(-amount[maxDIndex], amount[maxCIndex])
    amount[maxCIndex] -=minumum
    amount[maxDIndex] +=minumum
    
    print("Person " + str(maxDIndex) + " pays " + str(minumum) + " to person " + str(maxCIndex))
    
    #recursion for reamining people
    minCashFlow(amount)
       
       
def min_cash(graph):
    amount = [0] *3
    for s in range(0,3):
        for i in range(0,3):
            amount[s] += graph[i][s] - graph[s][i]

    minCashFlow(amount)
           
           
#ignore this 
def getBanks():
    str = """Enter the details of the banks and transactions as stated\n
        BankName: Payment1, payment2, payment3
          """
    print(str)
    contents = []
    #getInput(contents)
    
    dict = {}

    for i in range(len(contents)):
        contents[i].translate({ord(c): None for c in string.whitespace})
        line = contents[i].split(':')
        dict[line[0]]= line[1].split(',')

    return dict
 
    
def getTransaction():
    str = """Enter the details of the banks and transactions as stated\n
        BankName, BankName, amount; bankName, bankName, amount; 
          """
    print(str)
    contents = []
    
    while True:
        try:
            line = input()
            if len(line) > 0:
                line = line.replace(" ", "")
                contents.append(line)
            else:
                break
        except:
            print(os.strerror("Error in Main:"))
            break
    
    dict = {}
    arr = contents[0].split(';')
    for i in range(len(arr)):
        line = arr[i].split(',')
        pair = line[0], line[1]
        dict[pair] = line[2]
        print(pair)
           
    return dict
    
 
main()



