import tkinter as tk
from game import Game2048

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("2048 Game")
        self.grid_cells = []
        self.init_gui()

    def init_gui(self):
        background = tk.Frame(self.root, bg='azure3', width=400, height=400)
        background.grid()

        for i in range(4):
            grid_row = []
            for j in range(4):
                cell = tk.Frame(background, bg='azure4', width=100, height=100)
                cell.grid(row=i, column=j, padx=5, pady=5)
                t = tk.Label(master=cell, text='', bg='azure4', justify=tk.CENTER, font=('Arial', 22, 'bold'), width=4, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
        self.update_grid_cells()

    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                if self.game.board[i][j] == 0:
                    self.grid_cells[i][j].configure(text='', bg='azure4')
                else:
                    self.grid_cells[i][j].configure(text=str(self.game.board[i][j]), bg='light goldenrod')
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    game = Game2048()
    app = GameGUI(game)
    app.run()
