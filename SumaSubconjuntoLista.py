def solve(lista):
    # Variable donde voy a acumular el resultado final
    total = 0

    # Recorro todos los posibles puntos de inicio de sublistas
    for i in range(len(lista)):
        
        # Recorro todos los posibles puntos finales de sublistas
        for j in range(i, len(lista)):
            
            # Saco la sublista desde i hasta j
            sublista = lista[i:j+1]
            
            # Convierto la sublista a set para eliminar duplicados
            sublista_unica = set(sublista)
            
            # Sumo los elementos de la sublista sin repetidos
            suma_sublista = sum(sublista_unica)
            
            # Agrego esa suma al total general
            total += suma_sublista

    # Retorno el resultado final
    return total


lista = [1, 2, 1]

resultado = solve
(lista)

print("Resultado:", resultado)