z = 1
sumatoria = 0
cantidadInt = int(input('¿Cantidad de lectura? -> '))
while z <= cantidadInt:
    sumatoria += int((cantidadInt + 100000000) * (z * 10000))
    print(sumatoria) 
    z+=1