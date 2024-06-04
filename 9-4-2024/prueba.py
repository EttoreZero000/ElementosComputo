

#def determinarMayorL(pentrada):
#    esMayor=0
#    for a in pentrada:
#        if esMayor<a:
#            esMayor=a
#    return esMayor
#
#print (determinarMayorL([76,876,45,0,65]))


#def mostrarParesL(pentrada):
#    for a in pentrada:
#        if esPar(a):
#            print(a)
#
#def esPar(pentrada):
#    if pentrada%2==0:
#        return True
#    else:
#        return False
#mostrarParesL([1,2,3,4,5,6,7,8])


#def mostrarCerosL(pentrada):
#    for a in pentrada:
#        if a==0:
#            return True
#        
#    return False
#
#print(mostrarCerosL([1,2,3,4,5,6,7,8]))

def multiplicarImparesL(pentrada):
    producto=1
    for a in pentrada:
        if not esPar(a):
            producto*=pentrada
        else:
            par+=a
    if esPar(par):
        return 
    

def esPar(pentrada):
    if pentrada%2==0:
        return True
    else:
        return False
    
print(multiplicarImparesL([1,2,3,4,5]))