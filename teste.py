letras = {'a':1,'A':1,'b':1,'B':2,'e':1,'d':1,'g':1}
frutas = ('banana','BANANA','melancia','Pera','Abacaxi')

def escolha():
    for f in frutas:
        buraco(f)

def buraco(f, buraco=0):
    for l in f:
        if l in letras:
            buraco = buraco + letras[l]
    print ('fruta %s tem %s buracos' %(f, buraco))


if __name__ == "__main__":
    escolha()
