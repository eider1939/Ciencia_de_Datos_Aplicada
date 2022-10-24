def remove_space(data):
    data_sin_espacios=[]
    for i in range(0,len(data)):
        data_fila=[]
        for line in data[i]:
            if line != "" and line != " ":
                line=line.replace('_', ' ')
                data_fila.append(line.strip())
        data_sin_espacios.append(data_fila)
    return data_sin_espacios

def join_text(data_sin_espacios):
    cont_index=0
    list_index_pop=[]
    for j in range(0,len(data_sin_espacios)):
        if len(data_sin_espacios[j])>1:
            cont_index=j
        elif len(data_sin_espacios[j])==1:
            list_index_pop.append(j)
            texto=data_sin_espacios[cont_index][3]
            data_sin_espacios[cont_index][3]=str(texto)+' '+str(data_sin_espacios[j][0])
    return data_sin_espacios,list_index_pop

def remove_row_len_1(datos,list_index_pop):
    data_lista=[]
    for k in datos:
        if len(k)>1:
            data_lista.append(k)
    return data_lista

with open('clusters_report.txt') as f:
        data = [line for line in f.readlines()]
data = data[4:]
data = [line.replace('\n', '') for line in data]
data = [line.replace(' ', '_') for line in data]
data = [line.split("___",7) for line in data]
datos=remove_space(data)
datos,list_index_pop=join_text(datos)
data_lista=remove_row_len_1(datos,list_index_pop)
for i in data_lista:
    print(len(i))