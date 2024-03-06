#criar uma funcao sem e com retorno

lista = [38 ,32 , 43, 54, 62]

def calcular_media (lista):
    if len(lista) == 0:
      return 0 
    return sum(lista) / len(lista)
print (calcular_media(lista))











