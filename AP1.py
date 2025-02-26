import random
from time import sleep

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def play(self):
        """Simula uma jogada, podendo cair um número de 1 à 6."""
        point = random.randint(1, 6)
        self.points += point
        print(f"{self.name} tirou {point}. Total: {self.points}\n")

class CPU(Player):
    def __init__(self):
        super().__init__("CPU")

class Game:
    def __init__(self):
        self.player1 = Player(input("Write your nick: "))

    def winner(self, player1, player2):
        if player1.points > player2.points:
            print(f"\n{player1.name} win with {player1.points} points!\n")
        elif player2.points > player1.points:
            print(f"\n{player2.name} win with {player2.points} points!\n")
        else:
            print("\nDraw!\n")
    
    def play_game(self, player1, player2):

        # Resetando as pontuações no começo de cada partida
        player1.points = 0
        player2.points = 0

        print(f"\n{player1.name} VS {player2.name}\n")

        for play in range(1, 4):
            print(f"\nRound {play}\n")
            player1.play()
            player2.play()
            sleep(2)
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