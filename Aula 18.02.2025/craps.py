import random

class Craps:
    def __init__(self):
        # Atributos para armazenar o estado do jogo
        self.point = None  # O ponto do jogador, que será atribuído quando um valor de 4, 5, 6, 8, 9 ou 10 for rolado
        self.game_over = False  # Flag que indica se o jogo acabou ou não

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def play_game(self):
        print("Iniciando o jogo de Craps...")

        # Primeira jogada (primeiro lançamento de dados)
        first_roll = self.roll_dice()
        print(f"O jogador rolou {first_roll}.")

        # Condição de vitória (Natural)
        if first_roll == 7 or first_roll == 11:
            print("Parabéns! Você venceu com um Natural!")
            return

        # Condição de derrota (Craps)
        elif first_roll == 2 or first_roll == 3 or first_roll == 12:
            print("Você perdeu! Craps!")
            return

        # Caso contrário, o valor se torna o ponto do jogador
        else:
            self.point = first_roll
            print(f"O ponto foi estabelecido! O valor do ponto é {self.point}.")
            self.continue_game()

    def continue_game(self):
        print("O jogo continua...")

        while not self.game_over:
            # O jogador continua rolando até que vença ou perca
            roll = self.roll_dice()
            print(f"O jogador rolou {roll}.")

            # O jogador vence se rolar o valor do ponto novamente
            if roll == self.point:
                print("Parabéns! Você venceu!")
                self.game_over = True

            # O jogador perde se rolar um 7 antes de rolar o ponto novamente
            elif roll == 7:
                print("Você perdeu! Rolou um 7 antes de repetir o ponto.")
                self.game_over = True

# Simulação do jogo
jogo = Craps()  # Criando uma instância do jogo
jogo.play_game()  # Iniciando o jogo
