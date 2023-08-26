
#arrumar
def knapsack(capacidade, arr_pesos, arr_valores):
    n = len(arr_valores)
    arr_x = []

    arr_meio = [(arr_valores[i]/arr_pesos[i], arr_valores[i], arr_pesos[i],i) for i in range(n)]
    arr_meio.sort(reverse=True)

    print(f"arr_meio: {arr_meio}")
    peso_total,valor_total = 0,0
    for meio, valor, peso, item in arr_meio:
        if peso_total + peso <= capacidade:
            arr_x.append((item,valor, peso));
            peso_total += peso
            valor_total +=valor  

    arr_x.sort()
    
    print(f"peso_total: {peso_total}")
    print(f"valor_total: {valor_total}")
    print(f"arr_x: {arr_x}")

    return 

capacidade = 100
arr_pesos = [15,18,13,23,9,10,11,5,14,5]
arr_valores = [5,7,6,10,8,3,4,1,7,3]
# itens levados: 1, 2, 3, 4, 5 , 9 e 10
knapsack(capacidade, arr_pesos, arr_valores)