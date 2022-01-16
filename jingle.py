notas = {
    'W': 1,  
    'H': 1/2,  
    'Q': 1/4,  
    'E': 1/8,
    'S': 1/16, 
    'T': 1/32,  
    'X': 1/64 
}
compassos = input("Digite seus compassos separados por barras: ").upper()
compassos_lista = compassos.split('/')
compassos_corretos = [compasso for compasso in compassos_lista if sum([notas[identificador] for identificador in compasso]) == 1]
compassos_incorretos = [compasso for compasso in compassos_lista if compasso not in compassos_corretos and compasso != '']

print(f"Quantidade de Corretos: {len(compassos_corretos)}")
if len(compassos_incorretos) >= 1:  
    print(f"Incorretos: {'/'.join(compassos_incorretos)}")