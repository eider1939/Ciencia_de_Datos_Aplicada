

def read_texto():
    #
    # * Esta funcion lee el archivo data.csv
    # @Return matriz  matriz con cada linea de data.csv en un lista
    #
    lineas_texto=[]
    with open("data.csv", "r") as file:
        data = file.readlines()
    for line in data:
        line = line.replace('\n','')
        row = line.split(sep='\t')
        lineas_texto.append(row)
    return lineas_texto

def reducer(sequence):
    counter = {}
    for key, value in sequence:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)
    return sorted([(key, counter[key]) for key in counter])

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data=read_texto()
    counter=[]
    for i in range(0,len(data)):
        letter=data[i][0] #valor de la perimera columna
        #convertirmos la columan  5 de data.csv de jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        #a [['jjj', '12'], ['bbb', '3'], ['ddd', '9'], ['ggg', '8'], ['hhh', '2']]
        columna_4=list(subString.split(":") for subString in data[i][4].split(","))
        #recorremos las matriz columna_4 para sumar los valores de cada de la segunda columna
        suma_columna_4=sum([int(columna_4[j][1]) for j in range(len(columna_4))])
        #se agrega a counter un tupla con el la letra y la suma de la columna 4
        counter.append((letter,suma_columna_4))
    #se llama a reducer para que cuente las cpincidencias
    cantidad=reducer(sequence=counter)
    #reducer de vuelve una lista de tupla asi que convertimos esa lista en un dicc y retornamos 
    return {cantidad[i][0]:cantidad[i][1] for i in range(len(cantidad))}
#print(pregunta_12())
print(reducer(sequence=[('A',3),('B',4),('B',3),('A',10)]))
