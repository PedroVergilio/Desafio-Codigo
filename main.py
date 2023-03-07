
#Exercicio 2 -
num = int(input("Digite um número: "))

fib = [0, 1]


while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")



# Exercicio 3 -
#a) 9,
#b) 128,
#c) 49,
#d) 100,
#e) 13,
#f) 200.


# Exercicio 4 - 

# velocidades em km/h
velocidade_carro = 110
velocidade_caminhao = 80

# distância entre as cidades em km
distancia_cidades = 300

# tempo que leva para os veículos se encontrarem
tempo = distancia_cidades / (velocidade_carro + velocidade_caminhao)

# distância percorrida por cada veículo
distancia_carro = velocidade_carro * tempo
distancia_caminhao = velocidade_caminhao * tempo

if distancia_carro < distancia_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

# a) 
# velocidades em km/h
velocidade_carro = 110
velocidade_caminhao = 80

# distância entre as cidades em km
distancia_cidades = 100

# tempo que leva para os veículos se encontrarem
tempo = distancia_cidades / (velocidade_carro + velocidade_caminhao)

# distância percorrida por cada veículo
distancia_carro = velocidade_carro * tempo
distancia_caminhao = velocidade_caminhao * tempo

if distancia_carro < distancia_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

#b) 
# velocidades em km/h
velocidade_carro = 110
velocidade_caminhao = 80

# distância entre as cidades em km
distancia_cidades = 100

# tempo que leva para o caminhão passar pelos pedágios
tempo_pedagios = 2 * 5 / 60   # tempo total gasto nos dois pedágios, em horas

# tempo que leva para os veículos se encontrarem
tempo = distancia_cidades / (velocidade_carro + velocidade_caminhao)

# tempo total que o caminhão leva para percorrer a distância com os pedágios
tempo_caminhao = tempo + tempo_pedagios

# distância percorrida por cada veículo
distancia_carro = velocidade_carro * tempo
distancia_caminhao = velocidade_caminhao * tempo_caminhao

if distancia_carro < distancia_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

#c) Para Obter o resultado, basta calcular a distancia percorrida por cada veiculo e verificar qual percorreu uma distancia menor, Adicionando o tempo dos pedagios o resultado pode mudar
# já que o camnhão leva mais tempo para percorrer uma distância total.


#Exercicio 5 -
string = "exemplo"


lista_caracteres = list(string)


tamanho = len(lista_caracteres)


for i in range(tamanho // 2):
    lista_caracteres[i], lista_caracteres[tamanho - i - 1] = lista_caracteres[tamanho - i - 1], lista_caracteres[i]


string_invertida = "".join(lista_caracteres)


print(string_invertida)