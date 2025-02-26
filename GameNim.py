from random import randint
from time import sleep

class Player:
    def __init__(self, name):
        self.name = name

    def play(self, total_rocks, min_rocks, max_rocks):
        while True:
                try:
                    remove_rocks = int(input("How many rocks do you want to remove: "))
                    if remove_rocks >= min_rocks and remove_rocks <= min(total_rocks, max_rocks):
                        return remove_rocks
                    else:
                        print(f"You can remove rock between {min_rocks} and {min(total_rocks, max_rocks)}")
                except:
                    print("Invalid number!")
        

class CPU(Player):
    def __init__(self):
        super().__init__("CPU")

    def play(self, total_rocks, min_rocks, max_rocks):
        removed_rocks = 1
        if(total_rocks <= max_rocks):
            removed_rocks = max(min_rocks, min(total_rocks, max_rocks) - min_rocks)
        else:
            removed_rocks = randint(min_rocks, max_rocks)
        print(f"CPU removed {removed_rocks}")
        return removed_rocks

class Game:
    def __init__(self):
        return
    
    def start_game(self):
        self.total_rocks = int(input("Input how many rock are in the the game: "))
        self.min_rocks = int(input("Input the min rocks: "))
        self.max_rocks = int(input("Input the max rocks: "))
        self.player1 = Player(input("1st Player, write your nick: "))

    def winner(self, player):
        print(f"\n ✨ WINNER: {player.name}")

    #como funciona o sistema de rpetição de jogadas
    def play_game(self, player1, player2):
    
        print(f"\n{player1.name} VS {player2.name}\n")

        players = [player1, player2]
        current_round = 0
        current_player = 0

        while self.total_rocks > 0:
            print(f"\nRound {current_round + 1}: {players[current_player].name}")
            print(f"Avaliable rocks: {self.total_rocks}")
            print(f"You can remove rock between {self.min_rocks} and {min(self.total_rocks, self.max_rocks)}")
            remove_rocks = players[current_player].play(self.total_rocks, self.min_rocks, self.max_rocks)
            
            self.total_rocks -= remove_rocks
            current_round += 1
            current_player = current_round % 2
            if self.total_rocks <= self.min_rocks:
                self.winner( players[current_player] )
    
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
                break
            else:
                print("\nInvalid option. Try again.\n")
                return 0


return_of_game = 0
while return_of_game == 0:
    game = Game()
    return_of_game = game.view_menu()