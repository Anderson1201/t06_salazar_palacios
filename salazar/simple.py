import os

cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

monto=precio*cantidad

comprador_compulsivo=monto>100

print("cliente:",cliente)
print("producto:",producto)
print("cantidad:",cantidad)
print("monto total:",monto)


if(comprador_compulsivo==True):
    print("se ha ganado una tarjeta dorada")

