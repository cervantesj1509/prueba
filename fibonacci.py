repeticiones=int(input("Ingrese el numero de repeticiones: "))

a=1
b=0
c=0
i=0
while i <= repeticiones:
    c=a+b
    a=b
    b=c
    i+=1
    print(b)