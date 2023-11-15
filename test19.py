



def de(elementos,maximoPeso):
    listPeso=[]
    peso=0
    for elemento in elementos:
        wi=elemento[0]
        vi=elemento[1]
        #print(wi)
        peso += wi
        #print(f'peso: {peso}')
        if peso <= maximoPeso:
            limiteD = listPeso.append(elemento)
            #print(f'derechaaaaa{listPeso}')
        if peso == maximoPeso:
            break
        if peso > maximoPeso:
            limiteD=elemento
            #print(limiteD)
            break
    return limiteD , listPeso

def iz(elementos,maximoPeso):
    listPeso=[]
    peso=0
    for elemento in reversed(elementos):
        wi=elemento[0]
        vi=elemento[1]
        #print(wi)
        peso += wi
        #print(f'peso: {peso}')
        if peso <= maximoPeso:
            limiteIz = listPeso.append(elemento)
            #print(f'izquierdaa {listPeso}')
        if peso == maximoPeso:
            break
        if peso > maximoPeso:
            limiteIz=elemento
            #print(limiteIz)
            break
    return limiteIz , listPeso

 
def maletin(elementos,maximoPeso):

    for i in range(len(elementos) ):
        derecha, derechalist=de(elementos,maximoPeso)
        izquierda , izquierdalista =iz(elementos,maximoPeso)
        #print(f'derecha salida: {derecha}')
        #print(f'izquierda salida: {izquierda}')
        #print(f'derecha lista: {derechalist}')
        #print(f'izquierda lista: {izquierdalista}')


        if derecha==izquierda:
            if derecha== None and izquierda == None:
                maleta= derechalist
                #print(f'elementos Maleta 1: {maleta}')
                break
            
            elementos.remove(derecha)
        if izquierda ==None:
                maleta= izquierdalista
                #print(f'elementos Maleta: {maleta}')
        if derecha == None:
                maleta= derechalist
                
    print(f'elementos Maleta: {maleta}')
    return maleta
maleta=[]
#print(f'elementos Maleta: {maleta}')
elementos = [(2, 3), (3, 4), (4, 5), (5, 6)]
maximoPeso=9

grupo=maletin(elementos,maximoPeso)


"Se debe dejar la maleta vacia , dar elementos y maximoPeso"

     