import pygame

pygame.init()

longueur, largeur = 600, 600
screen = pygame.display.set_mode((longueur, largeur))
pygame.display.set_caption("Morpion de polo")

red = (41,41,232)
green = (255,80,149)
black = (8,8,12)
linesize = 10

font = pygame.font.Font(None, 74)

def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, green, (0, x * 200), (longueur, x * 200), linesize)
        pygame.draw.line(screen, green, (x * 200, 0), (x * 200, largeur), linesize)

def draw_symbols(board):
    for row in range(3):
        for col in range(3):
            x, y = col * 200, row * 200
            if board[row][col] == "X":
                pygame.draw.line(screen, black, (x + 50, y + 50), (x + 150, y + 150), linesize)
                pygame.draw.line(screen, black, (x + 150, y + 50), (x + 50, y + 150), linesize)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, black, (x + 100, y + 100), 50, linesize)

def get_cell(pos):
    x, y = pos
    row, col = y // 200, x // 200
    return row, col

def check_victory(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[row][col] != "" for row in range(3) for col in range(3))

def display_message(message):
    screen.fill(red)
    text = font.render(message, True, black)
    text_rect = text.get_rect(center=(longueur // 2, largeur // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2500)

def reset_game():
    return [["" for _ in range(3)] for _ in range(3)], "X", False 

board, current_player, game_over = reset_game()
run = True

while run:
    screen.fill(red)
    draw_grid()
    draw_symbols(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            row, col = get_cell(pos)
            if board[row][col] == "":
                board[row][col] = current_player
                if check_victory(board, current_player):
                    display_message(f"Joueur {current_player} win !")
                    board, current_player, game_over = reset_game() 
                elif check_draw(board):
                    display_message("Match nul !")
                    board, current_player, game_over = reset_game() 
                else:
                    current_player = "O" if current_player == "X" else "X"  
                    
    pygame.display.update()

pygame.quit()