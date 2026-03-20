def solution(a, b):
    # Variable donde voy a guardar la suma total
    total = 0

    # Recorro ambas listas al mismo tiempo usando índices
    for i in range(len(a)):
        
        # Resto los valores correspondientes
        diferencia = a[i] - b[i]
        
        # Saco el valor absoluto (quito negativos)
        valor_absoluto = abs(diferencia)
        
        # Elevo al cuadrado la diferencia
        cuadrado = valor_absoluto ** 2
        
        # Sumo ese resultado al total
        total += cuadrado

    # Calculo el promedio dividiendo entre la cantidad de elementos
    promedio = total / len(a)

    # Retorno el resultado final
    return promedio