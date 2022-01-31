import csv

def datos ():
    pais = input("ingrese el pais a analizar: ")
    N = int(input("ingrese el numero de partidos a analizar : "))
    with open("partidos.csv", 'r',encoding="utf8") as file:
        #date,home_team,away_team,home_score,away_score,tournament,city,country,neutral
        csvreader = csv.reader(file)   
        next(csvreader) # Leo el header para saltearlo
        rows = [row for row in csvreader]
        file.close()
    #print(rows)
    pais_comparacion = input("ingrese el pais a comparar con : " )
    victorias_local= 0
    victorias_visitante = 0
    derrotas_local = 0
    derrotas_visitante= 0
    
    # Filtro la lista quedandome solo con los partidos de ese pais (ya sea de visitante o local)
    rows_equipo = []
    for row in rows:
        if pais == row[1] or pais == row[2]:
            rows_equipo.append(row)
    
    # Doy vuelta la lista para facilitar el analisis de los ultimos 10 en la consigna 3
    rows_equipo_reverse = list(reversed(rows_equipo))

    # Consignas 1, 2, 3
    victorias_N = 0
    derrotas_N = 0
    empates_N = 0
    empates_general =0
    ultimo_local = None
    ultimo_visitante = None
    gano = 0
    perdio = 0
    empato= 0

    for index, row in enumerate(rows_equipo_reverse):
        if pais == row[1]:
            if row[3] > row[4]: #si pais gano de local
                        if ultimo_local is None:
                            ultimo_local = row[2] # equipo que jugo de visitante en su contra
                        victorias_local += 1 
                        if index < N:
                            victorias_N += 1
            elif row[3] < row [4]:# si pais perdio de local        
                derrotas_local += 1
                if index < N:
                    derrotas_N += 1
        elif pais == row[2]:                 
            if row[3]< row[4]:  #si pais gano de visitante
                    if ultimo_visitante is None:
                        ultimo_visitante = row[1]
                    victorias_visitante += 1
                    if index < N:
                        victorias_N += 1        
            elif  row[3] > row[4]: # si pais perdio de 
                        if ultimo_visitante is None:
                            ultimo_visitante = row[1]
                        derrotas_visitante += 1
                        if index < N:
                            derrotas_N += 1                                        
        if row[3] == row[4]:  # si hubo empate
            if index <N:
                empates_N += 1
            empates_general += 1

        if row[1] == pais and row[2] == pais_comparacion or row [1] == pais_comparacion and row [2] == pais:
            if pais == row [1]:
                 if row [3] > row [4]:
                     gano +=1
                 elif row [3] < row [4]:
                    perdio += 1
            elif pais == row[2]:
                 if row [3] > row [4]:
                     perdio += 1
                 elif row [3] < row [4]:
                    gano += 1
            if row [3] == row [4]:
                empato += 1        

                

    # TODO Imprimir victorias ultimos N 
    # TODO Imprimir empates ultimos N
    # TODO Imprimir derrotas ultimos N

    # Lo mismo pero generales

    print( " las victorias de local de ", pais ,"son : " ,victorias_local)
    print(" las victorias de visitante de :", pais , " son :", victorias_visitante)
    print (" las derrotas de local de : ", pais , " son :", derrotas_local)
    print( " las derrotas de visitante de :", pais , "son : " , derrotas_visitante)
    print ("analizamos los ultimos  ",N , "partidos de : " , pais )
    print(" en los ultimos : ", N, "partidos gano : ", victorias_N)
    print(" en los ultimos :" , N , "partidos perdio :" , derrotas_N)
    print ( " ultimo pais de local " ,ultimo_local , "y ultimo pais de visitante " , ultimo_visitante)
    print( " tiene un total de : ", empates_general , " empates generales  y " , empates_N , "en los ultimos ",N ,"partidos"  )
    print( "en la comparacion :  gano " , gano , " perdio ", perdio , " y empato " , empato)
    
    






if __name__ == '__main__':
    print("Bienenidos a otra clase de Inove con Python")
    datos ()

    


