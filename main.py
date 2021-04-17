#INTRODUÇÃO
print("OLÁ, ESTE PROGRAMA RETORNA TODOS OS NUMEROS PARES ENTRE 2 VALORES.");

#VARIÁVEIS
INICIAL = int(input("Insira o valor inicial.\n"))
FINAL = int(input("Agora, insira o valor final.\n"))


#TESTE LÓGICO
print("Os números pares, entre os inseridos são: \n")
for Contador in range (INICIAL, FINAL + 1):
  if Contador % 2 == 0: print(Contador)
