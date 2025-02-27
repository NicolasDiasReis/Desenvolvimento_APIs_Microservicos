from random import randint
from time import sleep

class Player:
    def __init__(self, name):
        self.name = name

    def play(self, total_rocks, min_rocks, max_rocks):
        while True:
            try:
                remove_rocks = int(input("How many rocks do you want to remove: "))
                # Corrigido para garantir que a quantidade de pedras removidas esteja entre os limites
                if min_rocks <= remove_rocks <= min(total_rocks, max_rocks):
                    return remove_rocks
                else:
                    print(f"You can remove rocks between {min_rocks} and {min(total_rocks, max_rocks)}")
            except ValueError:
                print("Invalid number!")  # Corrigido para capturar ValueError de forma mais específica

class CPU(Player):
    def __init__(self):
        super().__init__("CPU")

    def play(self, total_rocks, min_rocks, max_rocks):
        removed_rocks = randint(min_rocks, min(total_rocks, max_rocks))  # Ajustado para escolher aleatoriamente dentro do intervalo
        print(f"CPU removed {removed_rocks}")
        return removed_rocks

class Game:
    def __init__(self):
        self.total_rocks = 0
        self.min_rocks = 0
        self.max_rocks = 0
        self.player1 = None

    def start_game(self):
        # Adicionada validação de entrada para garantir que o número de pedras seja válido
        while True:
            try:
                self.total_rocks = int(input("Input how many rocks are in the game: "))
                if self.total_rocks <= 0:
                    print("The number of rocks must be greater than zero!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Validação para os limites de pedras
        while True:
            try:
                self.min_rocks = int(input("Input the min rocks: "))
                self.max_rocks = int(input("Input the max rocks: "))
                if self.min_rocks > self.max_rocks:
                    print("Min rocks cannot be greater than max rocks.")
                    continue
                break
            except ValueError:
                print("Please enter valid numbers for min and max rocks.")
        
        self.player1 = Player(input("1st Player, write your nick: "))

    def winner(self, player):
        print(f"\n ✨ WINNER: {player.name}")

    def play_game(self, player1, player2):
        print(f"\n{player1.name} VS {player2.name}\n")

        players = [player1, player2]
        current_round = 0
        current_player = 0

        while self.total_rocks > 0:
            print(f"\nRound {current_round + 1}: {players[current_player].name}")
            print(f"Available rocks: {self.total_rocks}")
            print(f"You can remove rocks between {self.min_rocks} and {min(self.total_rocks, self.max_rocks)}")
            remove_rocks = players[current_player].play(self.total_rocks, self.min_rocks, self.max_rocks)
            
            self.total_rocks -= remove_rocks
            current_round += 1
            current_player = current_round % 2

            # Mudança para verificar após o turno do jogador, antes de declarar vencedor
            if self.total_rocks <= 0:
                self.winner(players[current_player])

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
                self.start_game()
                self.player_vs_cpu()
                return 0
            elif escolha == "2":
                self.start_game()
                self.player_vs_player()
                return 0
            elif escolha == "3":
                print("\nExiting game...\n")
                return 1
            else:
                print("\nInvalid option. Try again.\n")
                return 0


return_of_game = 0
while return_of_game == 0:
    game = Game()
    return_of_game = game.view_menu()
