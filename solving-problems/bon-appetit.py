#https://www.hackerrank.com/challenges/bon-appetit/submissions/code/339495758
def bonAppetit(bill, k, b):
    soma = 0
    for i in range(len(bill)):
        if i != k:
            soma += bill[i]
         
    div = b - (soma/2)
    #print(f"div: {int(div)}")
    if  div > 0:
        print(f"{int(div)}")
    else:
        print("Bon Appetit")