import random

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def jogar(self):
        """Simula uma jogada, podendo cair um número de 1 à 6."""
        ponto = random.randint(1, 6)
        self.pontos += ponto
        print(f"{self.nome} tirou {ponto}. Total: {self.pontos}\n")

class CPU(Player):
    def __init__(self):
        super().__init__("CPU")

class Game:
    def __init__(self):
        self.player1 = Player(input("Write your nick: "))

    def winner(self, player1, player2):
        if player1.pontos > player2.pontos:
            print(f"\n{player1.nome} win with {player1.pontos} points!\n")
        elif player2.pontos > player1.pontos:
            print(f"\n{player2.nome} win with {player2.pontos} points!\n")
        else:
            print("\nDraw!\n")
    
    def play_game(self, player1, player2):

        # Resetando as pontuações no começo de cada partida
        player1.pontos = 0
        player2.pontos = 0

        print(f"\n{player1.nome} VS {player2.nome}\n")

        for play in range(1, 4):
            print(f"\nRound {play}\n")
            player1.jogar()
            player2.jogar()
        self.winner(player1, player2)
    
    def player_vs_cpu(self):
        cpu = CPU()
        self.play_game(self.player1, cpu)
    
    def player_vs_player(self):
        player2 = Player(input("Enter the nick of the 2nd player: "))
        self.play_game(self.player1, player2)

    def view_menu(self):
        while True:
            print("\nMenu:")
            print("1 - Player VS CPU")
            print("2 - Player VS Player")
            print("3 - Exit")
            escolha = input("Choose one option: ")

            if escolha == "1":
                self.player_vs_cpu()
            elif escolha == "2":
                self.player_vs_player()
            elif escolha == "3":
                print("\nExiting game...\n")
                break
            else:
                print("\nInvalid option. Try again.\n")

game = Game()
game.view_menu()