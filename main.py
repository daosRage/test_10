import pygame
import random

pygame.init()

FPS = 60
size_window = (800, 500)

#COLOR
bg_color = (100, 150, 100)
yellow = (255, 215, 95)
black = (0,0,0)
green = (9, 255, 107)
red = (255, 73, 91)

test_string = "owtrffff jjjj ffjj fjfj fjjf jffj dddd kkkk ffdd jjkk ffkk jjdd ddkk kkdd dkkd kddk dfjk kjfd"
write_text = ""
index = 0

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("FAST CLICKER")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 35)
render = font.render(test_string, True, black)
w_h_long = (380, 60)
w_h_short = (20,60)
write_line_rect = pygame.Rect(10, size_window[1] // 2 - w_h_long[1] // 2, w_h_long[0], w_h_long[1])
write_letter_rect = pygame.Rect(10 + w_h_long[0], size_window[1] // 2 - w_h_short[1] // 2, w_h_short[0], w_h_short[1])
write_line = pygame.Rect(10 + w_h_long[0] + w_h_short[0], size_window[1] // 2 - w_h_long[1] // 2, w_h_long[0], w_h_long[1])


start_time = 0
end_time = 0
game_over = 0
game = True
while game:
    window.fill(bg_color)
    pygame.draw.rect(window, (204, 244, 251), write_line_rect)
    pygame.draw.rect(window, (249, 229, 251), write_letter_rect)
    pygame.draw.rect(window, (196, 250, 213), write_line)
    window.blit(render, 
                (write_letter_rect.x - font.size(test_string[:index])[0], 
                 write_letter_rect.y))
    
    #демонстрація на екран рахунку та часу
    #зміна надпису та його відображення на картках
    #замальовування карток кольором
    if game_over == 0:
        pass

    #перевірка на програш та перемогу, у двох випадках має вивести 
    # на екран відповідний текст
    if game_over == -1:
        lose_text = font.render("Час вийшов, ти програв!", True, black)
        window.blit(lose_text, (size_window[0] // 2 - 200, size_window[1] // 2))
    if game_over == 1:
        win_text = font.render("Ти переміг!", True, black)
        window.blit(win_text, (size_window[0] // 2 - 100, size_window[1] // 2))

    
    #тут перевіряємо всі події що надходять з зовнішнього світу
    #в тому числі натиснення на картки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            write_text = event.unicode
            if write_text == test_string[index]:
                index += 1



        
    clock.tick(FPS)
    pygame.display.flip()