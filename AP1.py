import random  # Importa a biblioteca para gerar números aleatórios

# Classe base para os jogadores
class Jogador:
    def __init__(self, nome):
        self.nome = nome  # Nome do jogador
        self.pontos = 0  # Inicializa a pontuação

    def jogar(self):
        """Simula uma jogada do jogador, sorteando um número entre 1 e 6."""
        valor = random.randint(1, 6)  # Sorteia um número entre 1 e 6
        self.pontos += valor  # Soma o valor sorteado ao total de pontos do jogador
        print(f"{self.nome} tirou {valor}. Total: {self.pontos}")  # Exibe o resultado da jogada

# Classe CPU herda da classe Jogador
class CPU(Jogador):
    def __init__(self):
        super().__init__("CPU")  # Define o nome como "CPU"

# Classe que gerencia o jogo
class Jogo:
    def __init__(self):
        """Inicializa o jogo, pedindo o nome do primeiro jogador."""
        self.jogador1 = Jogador(input("Digite seu nome: "))  # Cria o primeiro jogador com o nome digitado

    def determinar_vencedor(self, jogador1, jogador2):
        """Compara a pontuação dos jogadores e determina o vencedor."""
        if jogador1.pontos > jogador2.pontos:
            print(f"\n{jogador1.nome} venceu com {jogador1.pontos} pontos!")  # Jogador 1 venceu
        elif jogador2.pontos > jogador1.pontos:
            print(f"\n{jogador2.nome} venceu com {jogador2.pontos} pontos!")  # Jogador 2 venceu
        else:
            print("\nEmpate!")  # Caso ambos tenham a mesma pontuação

    def jogar_partida(self, jogador1, jogador2):
        """Executa a partida entre dois jogadores, alternando as jogadas."""
        print(f"\n{jogador1.nome} vs {jogador2.nome}\n")  # Exibe os jogadores que vão competir

        for rodada in range(1, 4):  # São 3 rodadas
            print(f"\nRodada {rodada}:")  
            jogador1.jogar()  # Jogador 1 joga
            jogador2.jogar()  # Jogador 2 joga

        self.determinar_vencedor(jogador1, jogador2)  # Verifica quem ganhou após as rodadas

    def jogar_contra_cpu(self):
        """Inicia uma partida entre o jogador e a CPU."""
        cpu = CPU()  # Cria a CPU
        self.jogar_partida(self.jogador1, cpu)  # Chama a função para jogar

    def jogar_contra_jogador(self):
        """Inicia uma partida entre dois jogadores humanos."""
        jogador2 = Jogador(input("Digite o nome do segundo jogador: "))  # Pede o nome do segundo jogador
        self.jogar_partida(self.jogador1, jogador2)  # Chama a função para jogar

    def mostrar_menu(self):
        """Exibe o menu do jogo e gerencia as escolhas do jogador."""
        while True:
            print("\nMenu:")
            print("1 - Jogar contra a CPU")
            print("2 - Jogar contra outro jogador")
            print("3 - Sair")
            escolha = input("Escolha uma opção: ")  # Usuário escolhe a opção

            if escolha == "1":
                self.jogar_contra_cpu()  # Inicia jogo contra CPU
            elif escolha == "2":
                self.jogar_contra_jogador()  # Inicia jogo contra outro jogador
            elif escolha == "3":
                print("Saindo do jogo...")  # Mensagem de saída
                break  # Sai do loop e encerra o jogo
            else:
                print("Opção inválida. Tente novamente.")  # Mensagem de erro caso a opção seja inválida

# Executa o jogo
jogo = Jogo()  # Cria uma instância do jogo
jogo.mostrar_menu()  # Inicia o menu do jogo