import random

class Craps:
    def __init__(self, num_players=2):
        # Atributos para armazenar o estado do jogo
        self.players = [f"Jogador {i+1}" for i in range(num_players)]  # Lista de jogadores
        self.current_player_index = 0  # Índice do jogador atual
        self.point = None  # O ponto do jogador, que será atribuído quando um valor de 4, 5, 6, 8, 9 ou 10 for rolado
        self.game_over = False  # Flag que indica se o jogo acabou ou não

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def play_game(self):
        print("Iniciando o jogo de Craps...")

        # Jogo continuará até que um jogador vença ou perca
        while not self.game_over:
            current_player = self.players[self.current_player_index]  # Jogador atual
            print(f"\nVez do {current_player}.")

            # Primeira jogada (primeiro lançamento de dados)
            first_roll = self.roll_dice()
            print(f"O jogador rolou {first_roll}.")

            # Condição de vitória (Natural)
            if first_roll == 7 or first_roll == 11:
                print(f"Parabéns, {current_player}! Você venceu com um Natural!")
                self.game_over = True
                return

            # Condição de derrota (Craps)
            elif first_roll == 2 or first_roll == 3 or first_roll == 12:
                print(f"{current_player}, você perdeu! Craps!")
                self.game_over = True
                return

            # Caso contrário, o valor se torna o ponto do jogador
            else:
                self.point = first_roll
                print(f"O ponto foi estabelecido! O valor do ponto é {self.point}.")
                self.continue_game(current_player)

            # Alterna para o próximo jogador
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def continue_game(self, current_player):
        print(f"O jogo continua para o {current_player}...")

        while not self.game_over:
            roll = self.roll_dice()
            print(f"O jogador rolou {roll}.")

            # O jogador vence se rolar o valor do ponto novamente
            if roll == self.point:
                print(f"Parabéns, {current_player}! Você venceu!")
                self.game_over = True

            # O jogador perde se rolar um 7 antes de rolar o ponto novamente
            elif roll == 7:
                print(f"{current_player}, você perdeu! Rolou um 7 antes de repetir o ponto.")
                self.game_over = True

# Simulação do jogo com 2 jogadores (você pode mudar o número de jogadores)
num_players = 2  # Número de jogadores
jogo = Craps(num_players=num_players)  # Criando uma instância do jogo
jogo.play_game()  # Iniciando o jogo