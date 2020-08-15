import datetime

def encontrar_valor(dataset):
    start = datetime.datetime.now()
    with open(dataset+'.csv') as myfile:
        data = myfile.read().split('\n')[:-1]
    n = data[0]
    t = int(data[1])-1
    D = data[2:]
    print(data)
    print(D)
    for i in range(t):
        if D[i] == n:
            #para testar a contagem dos milisegundos
            #for i in range(999):
            #    pass
            end = datetime.datetime.now()
            timedif = end - start
            file = open('resposta-'+dataset+'.txt','w') 
            file.write('TRUE\n')
            file.write(str(i)+'\n')
            file.write(str(timedif.total_seconds() * 1000)) 
            file.close() 
            return dataset+' - TRUE - posição p = '+str(i)
    end = datetime.datetime.now()
    timedif = end - start
    file = open('resposta-'+dataset+'.txt','w') 
    file.write('FALSE\n')
    file.write('-1\n')
    file.write(str(timedif.total_seconds() * 1000)) 
    file.close()
    return dataset+' - FALSE - posição p = -1'


a = 'dataset-1-a'
b = 'dataset-1-b'
c = 'dataset-1-c'
print(encontrar_valor(a))
print(encontrar_valor(b))
print(encontrar_valor(c))