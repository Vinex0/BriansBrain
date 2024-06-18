import pygame
from grid import Grid

pygame.init()

n, m = 10, 20  
cell_size = 30   
width, height = m * cell_size, n * cell_size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Grid Visualization')

colors = {
    0: (0, 0, 0),       
    1: (128, 128, 128), 
    2: (255, 255, 255)  
}

gitter = Grid(n, m)

running = True
paused = True

UPDATEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATEEVENT, 300)  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // cell_size, pos[1] // cell_size
                if 0 <= x < m and 0 <= y < n:
                    gitter.erwacken(y, x)  
        elif event.type == UPDATEEVENT:
            if not paused:
                gitter.update()

    screen.fill((0, 0, 0))

    for i in range(n):
        for j in range(m):
            cell = gitter.grid[i, j]
            color = colors[cell.zustand]

            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

            pygame.draw.rect(screen, (50, 100, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    pygame.display.flip()

pygame.quit()
