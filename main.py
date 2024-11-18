import pygame
import sys
import time

# Constants for the GUI
WIDTH, HEIGHT = 600, 600  # Window size
ROWS, COLS = 8, 8  # Chessboard dimensions
SQUARE_SIZE = WIDTH // COLS  # Size of each square

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Queens Problem Simulation")
clock = pygame.time.Clock()

# Board for visualization
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_board(board, current_row=None, current_col=None):
    """Draws the chessboard and queens."""
    for row in range(ROWS):
        for col in range(COLS):
            # Alternate colors for chessboard squares
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Draw queen if present
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen, BLACK,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    SQUARE_SIZE // 3
                )
            
            # Highlight the current cell being evaluated
            if row == current_row and col == current_col:
                pygame.draw.rect(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

def is_safe(board, row, col):
    """Checks if placing a queen at board[row][col] is safe."""
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, COLS)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    """Backtracking algorithm with visualization."""
    if row >= ROWS:  # Base case: All queens are placed
        return True

    for col in range(COLS):
        # Check if placing the queen is safe
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            draw_board(board, row, col)  # Draw the updated board
            pygame.display.flip()  # Update the display
            time.sleep(0.5)  # Pause for visualization
            
            if solve_nqueens(board, row + 1):  # Recur to place the rest
                return True
            
            # Backtrack
            board[row][col] = 0
            draw_board(board, row, col)  # Draw the updated board
            pygame.display.flip()  # Update the display
            time.sleep(0.5)  # Pause for visualization

    return False

def main():
    running = True
    solving = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if solving:
            draw_board(board)
            pygame.display.flip()
            solve_nqueens(board, 0)
            solving = False  # Stop solving once completed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
