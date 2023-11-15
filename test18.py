#Número Dorado =( año  mod 19) + 1
""" Normalmente diríamos que, por ejemplo, 14 dividido por 5 es 2,8. Pero cuando usamos la división de enteros, descartamos la fracción decimal y simplemente declaramos que 14 dividido por 5 es 2. """

def AnioPascua(anio): 

    tabla ={1:"-04-12",2:"-04-11",3:"-04-10",4:"-04-9",5:"-04-8" ,6: "-04-7" ,7:"-04-6" ,8:"-04-5",9:"-04-4",10:"-04-3",11:"-04-2",12:"-04-1",13:"-03-31",14:"-03-30",15:"-03-29",16:"-03-28",17:"-03-27",18:"-03-26",19:"-03-25",20:"-03-24",21:"-03-23",22:"-03-22",23:"-03-21",24:"-04-18",26:"-04-17",27:"-04-16",28:"-04-15",29:"-04-14",30:"-04-13"}

    #anio =2011
    VC=int((anio/100))
    VS=int((3*(VC+1))/4)
    VL=int((8*VC+13)/25)
    NumeroDorado = int((anio%19)+1)
    #Epact = (11 × ( Número Dorado  – 1)) mod 30
    #print(NumeroDorado)

    Epact=int((11*(NumeroDorado-1))%30)
    #print(Epact)
    if Epact==0:
        Epact=30

    FechaPascua= (Epact - VS + VL + 8) 
    if FechaPascua == 0:
        FechaPascua=1

    #print(FechaPascua)
    if FechaPascua in tabla:
        fechacalculada = tabla[FechaPascua]
        print(str(anio) + fechacalculada)
    else:
        if FechaPascua == 25:
            if FechaPascua > 11:
                fechacalculada = str(anio)  +"-04-17"
                
            else:
                fechacalculada =str(anio)  +"-04-18"
                
            
        print(fechacalculada)
        return fechacalculada

test = AnioPascua(2011)
