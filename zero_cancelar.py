N = int(input())
entrada = 0
X = []
S = 0

limite_minimo_numeros = 1
limite_maximo_numeros = 1000000
limite_minimo_entrada_do_numero = 0
limite_maximo_entrada_do_numero = 1000000
flag_de_cancelamento = 0


if(N >= limite_minimo_numeros and N <= limite_maximo_numeros):
    for i in range(N):
        entrada = int(input())
        if(entrada >=limite_minimo_entrada_do_numero and entrada <=limite_maximo_entrada_do_numero):
            if(entrada == flag_de_cancelamento):
                X.pop()
                N-=1
            else:
                X.append(entrada)
    
    for i in range(len(X)):
        if(S >= 0 and S <= 1000000):
            S += X[i]
        
print(S)
    

    

