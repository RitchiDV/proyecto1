def listas ():

    # lista = [i for i in range (1,100) if i%3 != 0]
    # print(lista)
    #--------------------------------------------------------------------------------------------
    # lista=[]
    # for i in range (1,100):
    #     if i%3 != 0:
    #         lista.append(i**2)
    #-------------------------------------------------------------------------------------
    # lista =[i for i in range (1,1000)))if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0) ]
    # print(lista)
    #       para i en el rango del 1 al 1000 solo se imprimira i si se cumple la condicion if
    #-----------------------------------------------------------------------------------------------
    lista =[i for i in range (1,int(input("digite un numero: "))) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0) ]
    print (lista)
def run ():
    listas()



if __name__=="__main__":
    run()