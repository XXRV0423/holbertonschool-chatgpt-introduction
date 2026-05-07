#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines_count = mines  # ✅ FIX: store total mines for win condition
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))

        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                if dx == 0 and dy == 0:
                    continue  # ✅ FIX: avoid counting the current cell as a neighbor

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1

        return count

    def reveal(self, x, y):
        # ✅ FIX: prevent crash when user enters out-of-bounds coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            return None

        # ✅ FIX: prevent re-revealing same cell (avoids unnecessary recursion)
        if self.revealed[y][x]:
            return True

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)

        return True

    def has_won(self):
        # ✅ FIX: added win condition check
        revealed_count = 0

        for y in range(self.height):
            for x in range(self.width):
                if self.revealed[y][x]:
                    revealed_count += 1

        safe_cells = self.width * self.height - self.mines_count
        return revealed_count == safe_cells

    def play(self):
        message = ""  # ✅ FIX: store messages so they don't disappear after clear_screen

        while True:
            self.print_board()

            if message:
                print(message)  # ✅ FIX: show error messages after screen refresh

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                result = self.reveal(x, y)

                if result is None:
                    message = "Invalid coordinates. Try again."  # ✅ FIX: handle out-of-bounds input
                elif result is False:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                elif self.has_won():
                    # ✅ FIX: detect and display win condition
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break
                else:
                    message = ""

            except ValueError:
                # ✅ FIX: handle non-numeric input without crashing
                message = "Invalid input. Please enter numbers only."


if __name__ == "__main__":
    game = Minesweeper()
    game.play()