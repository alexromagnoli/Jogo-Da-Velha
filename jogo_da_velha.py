
'''
☐
◯
✖
'''
import random
import os
lista_de_coordenadas = [["1a","☐", 1], ["1b", "☐", 2], ["1c", "☐", 3],
                         ["2a", "☐", 4], ["2b", "☐", 5], ["2c", "☐", 6],
                           ["3a", "☐", 7], ["3b", "☐", 8], ["3c", "☐", 9]]

lista_ganhadora = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                   [1, 4, 7], [2, 5, 8], [3, 6, 9],
                   [1, 5, 9], [3, 5, 7]]
lista_de_jogadas_1 = []
lista_de_jogadas_2 = []
lista_total_de_jogadas = []
jogadas = []
numero_de_jogadas = 0

def mostrar_tabuleiro():
    cont = 0
    cont_print = 0
    print("  A  B  C")
    for coordenada in lista_de_coordenadas:
        if cont < 2:
            
            if cont == 0:
                cont_print += 1
                print(f"{cont_print} {coordenada[1]}", end="  ")
                cont += 1


            else:
                print(f"{coordenada[1]}", end="  ")
                cont += 1
        else:
            print(f"{coordenada[1]}")
            cont = 0

def atualizar_tabuleiro(jogadas_1, jogadas_2, jogada):
    for coordenada in lista_de_coordenadas:
        if coordenada[0] in jogadas_1:
            coordenada[1] = "✖"
            lista_de_jogadas_1.append(coordenada[2])
        if coordenada[0] in jogadas_2:
            coordenada[1] = "◯"
            lista_de_jogadas_2.append(coordenada[2])

        lista_total_de_jogadas.append(jogada)



def verificar_ganhador(lista_de_jogadas):

    for coordenada in lista_ganhadora:
        if set(coordenada).issubset(lista_de_jogadas):
            return True

def verificar_jogada(jogada):
    jogadas = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]
    
    if jogada in lista_total_de_jogadas:
        return False
    if jogada not in jogadas:
        return False
    return True

def jogada_1():
    global numero_de_jogadas
    global lista_de_jogadas_1

    jogada = str(input(f"Digite sua jogada, {primeiro}! (Em coordenadas): ").strip().lower())
    if not verificar_jogada(jogada):
            print("Digite um formato válido!(numero/letra)")
            return jogada_1()
    
    
    jogadas_1.append(jogada)
    atualizar_tabuleiro(jogadas_1, jogadas_2, jogada)
    numero_de_jogadas += 1
    return verificar_ganhador(lista_de_jogadas_1)
        
    
    
    
def jogada_2():
    global numero_de_jogadas
    global lista_de_jogadas_2
    
    jogada = str(input(f"Digite sua jogada, {segundo}! (Em coordenadas): ").strip().lower())
    
        
    if not verificar_jogada(jogada):
            print("Digite um formato válido!(numero/letra)")
            return jogada_2()

    
    jogadas_2.append(jogada)
    atualizar_tabuleiro(jogadas_1, jogadas_2, jogada)
    numero_de_jogadas += 1
    return verificar_ganhador(lista_de_jogadas_2)
    
    
def limpar_tela():
    os.system("cls")

jogador_1 = str(input("Digite o nome do jogador 1: ").strip().capitalize())
jogador_2 = str(input("Digite o nome do jogador 2: ").strip().capitalize())
nomes = [jogador_1, jogador_2]
primeiro = random.choice(nomes)

if primeiro == jogador_1:
    nomes.remove(jogador_1)
    jogador_1 = primeiro
    segundo = nomes[0]
else:
    nomes.remove(jogador_2)
    jogador_2 = primeiro
    jogador_1 = nomes[0]
    segundo = nomes[0]


limpar_tela()
print(f"O jogador {jogador_1} começa!")
mostrar_tabuleiro()
while True:
    
    jogadas_1 = []
    jogadas_2 = []
    if jogada_1():
        mostrar_tabuleiro()
        print(f"{jogador_1} Venceu!!!")
        break
    limpar_tela()
    mostrar_tabuleiro()
    
    if jogada_2():
        mostrar_tabuleiro()
        print(f"{jogador_2} venceu!!!")
        break
    limpar_tela()
    mostrar_tabuleiro()
    
    if numero_de_jogadas > 7 :
        print("VELHA!!!")
        break
