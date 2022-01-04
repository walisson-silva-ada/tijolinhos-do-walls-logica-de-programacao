def find_greater_number(lista_de_numeros, n):
    if n == 1:
        return lista_de_numeros[n-1]
    else:
        numero_anterior = find_greater_number(lista_de_numeros, n-1)
        numero_atual = lista_de_numeros[n-1]
        
        if numero_anterior > numero_atual:
            return numero_anterior
        else:
            return numero_atual


numeros_do_user = []
tamanho_da_lista = int(input("Digite o tamanho do array de numeros: "))

for i in range(tamanho_da_lista):
    current_number = int(input(f"Digite o {i+1}° numero do array: "))
    numeros_do_user.append(current_number)

if tamanho_da_lista == 0:
     print("Não há elementos!")
else:
    print("O maior número do array é: ",find_greater_number(numeros_do_user, tamanho_da_lista))