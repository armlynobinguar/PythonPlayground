from .player import MazePlayer

from maze_solver.game import MazeGame

# Usage example
if __name__ == "__main__":
    # Create MazePlayers
    player1 = MazePlayer(name="Player 1", color="Red", start_position=(0, 0))
    player2 = MazePlayer(name="Player 2", color="Blue", start_position=(0, 0))

    # Create MazeGame with players
    game_players = [player1, player2]
    game = MazeGame(maze=None, players=game_players)

    # Start the game
    game.start_game()
