import pygame
from grid import Grid

# Initialize Pygame
pygame.init()

# Set the dimensions of the grid and window
n, m = 10, 20  # Grid dimensions
cell_size = 30   # Size of each cell
width, height = m * cell_size, n * cell_size

# Create the Pygame screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Grid Visualization')

# Define colors
colors = {
    0: (0, 0, 0),       # Black for dead
    1: (128, 128, 128), # Gray for dying
    2: (255, 255, 255)  # White for alive
}

# Create a grid
gitter = Grid(n, m)

# Control variables
running = True
paused = True

# Set up a timer event for updating the grid
UPDATEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATEEVENT, 300)  # Set timer to 1000 milliseconds (1 second)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused  # Toggle pause when spacebar is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // cell_size, pos[1] // cell_size
                if 0 <= x < m and 0 <= y < n:
                    gitter.erwacken(y, x)  # Update neighbors
        elif event.type == UPDATEEVENT:
            if not paused:
                gitter.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid
    for i in range(n):
        for j in range(m):
            cell = gitter.grid[i, j]
            color = colors[cell.zustand]
            # Draw cell
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            # Draw cell border
            pygame.draw.rect(screen, (50, 100, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
