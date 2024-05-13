import numpy as np

class ConnectFour:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=str)
        self.board[:] = ' '
        self.player = 'X'
        self.moves_left = rows * cols

    def print_board(self):
        print("\n".join([" | ".join([cell for cell in row]) for row in self.board]))
        print(" " + "  ".join([str(i + 1) for i in range(self.cols)]))  # Numeración de columnas del 1 al 8

    def make_move(self, col):
        if not 1 <= col <= self.cols:
            print("Columna fuera de rango.")
            return False
        col -= 1  # Ajuste para que la columna sea un índice válido
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player
                self.moves_left -= 1
                return True
        print("Columna llena.")
        return False

    def check_winner(self):
        # Check horizontal, vertical, and diagonal wins
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == self.player:
                    # Check horizontal
                    if col + 3 < self.cols and all(self.board[row][col + i] == self.player for i in range(4)):
                        return True
                    # Check vertical
                    if row + 3 < self.rows and all(self.board[row + i][col] == self.player for i in range(4)):
                        return True
                    # Check diagonal (top-left to bottom-right)
                    if row + 3 < self.rows and col + 3 < self.cols and \
                            all(self.board[row + i][col + i] == self.player for i in range(4)):
                        return True
                    # Check diagonal (bottom-left to top-right)
                    if row - 3 >= 0 and col + 3 < self.cols and \
                            all(self.board[row - i][col + i] == self.player for i in range(4)):
                        return True
                    # Check L shapes: 1x3
                    if col + 2 < self.cols and row - 1 >= 0:
                        if self.board[row][col + 1] == self.player and self.board[row][col + 2] == self.player:
                            if row + 1 < self.rows and self.board[row + 1][col] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col + 1] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col + 2] == self.player:
                                return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col + 1 < self.cols and self.board[row][col + 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 1][col - 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col + 1 < self.cols and self.board[row + 1][col + 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                    # Check L shapes: 1x3 (mirror image)
                    if col - 2 >= 0 and row - 1 >= 0:
                        if self.board[row][col - 1] == self.player and self.board[row][col - 2] == self.player:
                            if row + 1 < self.rows and self.board[row + 1][col] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col - 1] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col - 2] == self.player:
                                return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col - 1 >= 0 and self.board[row][col - 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 1][col + 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col - 1 >= 0 and self.board[row + 1][col - 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
                    # Check L shapes: 1x3 (reflecting in Y-axis)
                    if col + 2 < self.cols and row - 1 >= 0:
                        if self.board[row][col + 1] == self.player and self.board[row][col + 2] == self.player:
                            if row + 1 < self.rows and self.board[row + 1][col] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col - 1] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col - 2] == self.player:
                                return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col - 1 >= 0 and self.board[row][col - 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 1][col - 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col + 1 < self.cols and self.board[row + 1][col + 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                    # Check L shapes: 1x3 (mirror image, reflecting in Y-axis)
                    if col - 2 >= 0 and row - 1 >= 0:
                        if self.board[row][col - 1] == self.player and self.board[row][col - 2] == self.player:
                            if row + 1 < self.rows and self.board[row + 1][col] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col + 1] == self.player:
                                return True
                            if row + 1 < self.rows and self.board[row + 1][col + 2] == self.player:
                                return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col + 1 < self.cols and self.board[row][col + 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 1][col + 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                        if row + 2 < self.rows:
                            if self.board[row + 1][col] == self.player and self.board[row + 2][col] == self.player:
                                if col - 1 >= 0 and self.board[row + 1][col - 1] == self.player:
                                    return True
                                if col - 1 >= 0 and self.board[row + 2][col - 1] == self.player:
                                    return True
                                if col + 1 < self.cols and self.board[row + 2][col + 1] == self.player:
                                    return True
        return False

    def play_game(self):
        print("¡Bienvenido a 4 en línea!")
        self.print_board()
        while self.moves_left > 0:
            col = int(input(f"Turno del Jugador {self.player}. Elige una columna (1-{self.cols}): "))
            if self.make_move(col):
                self.print_board()
                if self.check_winner():
                    print(f"¡Jugador {self.player} ha ganado!")
                    break
                self.player = 'O' if self.player == 'X' else 'X'
        else:
            print("¡Empate!")

# Función para elegir el tamaño del tablero
def choose_board_size():
    while True:
        print("Elige el tamaño del tablero:")
        print("1. 8x8")
        print("2. 6x6")
        print("3. 7x6")
        choice = input("Ingrese el número de opción: ")
        if choice == "1":
            return 8, 8
        elif choice == "2":
            return 6, 6
        elif choice == "3":
            return 7, 6
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    rows, cols = choose_board_size()
    game = ConnectFour(rows, cols)
    game.play_game()
