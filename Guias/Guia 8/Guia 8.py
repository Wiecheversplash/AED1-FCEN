#Ejercicio 1)

#1)

def pertenece1(x:list,y:int)->bool:
    for i in x:
        if y==i:
            return True
        else: 
            return False
        
def pertenece2(x:list,y:int)->bool:
    z=0
    while z<len(x):
        if x[z]==y:
            return True
        else:
            z+=1
    return False

def pertenece3(x:int,y:list)->bool:
    return x in y

def pertenece(x,y)->bool:
    return x in y

#2)

def divideATodos(x:list,y:int)->bool:
    for i in x:
        if i%y != 0:
            return False
    return True


#3)

def sumaTotal(x:list)->int:
    y:int=0
    for i in x:
        y += i
    return y

#4)

def ordenados(x:list)->bool:
    for i in range(len(x)-1):
        if x[i]>=x[i+1]:
            return False 
    return True

#5)

def palabra7(x:list)->bool:
    for i in x:
        if len(i)==7:
            return True
    return False

#6)

def esPalindroma(x:str)->bool:
    for i in range(len(x)/2):
        if x[i] != x[-i-1]:
            return False
    return True

#7)

def analizarContraseña(password:str)->str:
    
    def tieneMiniscula(password:int)->bool:
        a:list = list(password)
        for i in a:
            if pertenece3(i,list("abcdefghijklmnñopqrstuvwxyz")):
                return True
        return False

    def tieneMayus(password:str)->bool:
        a:list = list(password)
        for i in a:
            if pertenece3(i,list("ABCDEFGHIJKLMÑOPQRSTUVWXYZ")):
                return True
        return False
    
    def tieneDigito(password:str):
        a:list=list(password)
        for i in a:
            if pertenece3(i,[1,2,3,4,5,6,7,8,9]):
                return True
        return False

    
    if len(password)>8 and tieneMiniscula(password) and tieneDigito(password) and tieneMayus(password):
        return "Verde"
    if len(password)<5:
        return "Roja"
    else:
        return "Amarilla"

#8)

def saldo(a:list)->int:
    saldo:int=0
    for i in a:
        if i[0]=="I":
            saldo+=i[1]
        else:
            saldo-=i[1]
    return saldo

#9)

def tresVocales(a:int)->bool:
    b:list=list(a)
    c:int=0
    for i in a:
        if  pertenece(i,list("aeiouAEIOU")):
            c+=1
    if c>=3:
        return True
    else:
        return False

#Ejercicio 2)

#1)

def borrarPosParesInOut(a:list)->list:
    for i in range(0,len(a),2):
        a[i] = 0
    return a 

#2)

def borrarPosParesin(a:list)->list:
    b:list = []
    for i in range(0,len(a)):
        if i%2==0:
            b.append(0)
        else:
            b.append(a[i])
    return b 

#3)

def quitarVocales(a:str)->str:
    b:list = []
    a:list = list(a)
    for i in range(0,len(a)):
        if not(pertenece(a[i],list("AEIOUaeiou"))):
            b.append(a[i])
    c:str = ""
    for palabra in b:
        c+=palabra
    return c

#4)

def reemplazaVocales(a:str)->str:
    b:list = []
    a:list = list(a)
    for i in range(0,len(a)):
        if (pertenece(a[i],list("AEIOUaeiou"))):
            b.append("-")
        else:
            b.append(a[i])
    c:str = ""
    for letra in b:
        c+=letra
    return c

#5)

def daVueltaStr(a:str)->str:
    b:list=[]
    a:list = list(a)
    for i in range(-1,-len(a)-1,-1):
        b.append(a[i])
    c:str=""
    for i in b:
        c+=i
    return c

#Ejercicio 3)

#1)

def estudiantes()->list:
    a:str=input()
    b:list=[]
    while a!="listo":
        b.append(a)
        a = input()
    else:
        return b

#2)

