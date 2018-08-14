#!/usr/bin/python3

import pygame
import re

pygame.init()

white = (255,255,255)
black = (0,0,0)
cursor_x = 36
cursor_y = 668
text = '.'
running = True
line_pos = 630
text_line = {}
n = 0

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Dungeons Of Daggorath - Python Port")

clock = pygame.time.Clock()

pygame.draw.rect(screen, white, (0,608,1024,32))
game_font = pygame.font.Font("TRS-80 Color Computer.ttf", 32)
cursor = pygame.Surface((26,4))
cursor.fill(white)
heart_lg = pygame.image.load('heart_lg.png')
heart_sm = pygame.image.load('heart_sm.png')

def heart(rate):
    gameDisplay.blit(heart_lg, (x,y))
    pygame.display.update()
    gameDisplay.blit(heart_lg, (x,y))
    pygame.display.update()

def update_lh(text):
    screen.blit(game_font.render(text, True, black), (0,596))
    pygame.display.update()

def update_rh(text):
    text_width, text_height = game_font.size(text)
    screen.blit(game_font.render(text, True, black), (1024 - text_width,596))
    pygame.display.update()

def evaluate(text):
    # Evaluate the syntax
    return True

# Initialize the game elements
update_lh("EMPTY")
update_rh("EMPTY")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                cursor.fill((0,0,0))
                screen.blit(cursor, (cursor_x, cursor_y))
                cursor_x = 36
                text = re.sub('\.', '', text)
                if not evaluate(text):
                    text += " ???"
                    screen.blit(game_font.render(text, True, white), (32, line_pos))
                text_line[n] = text
                if line_pos <= 700:
                    line_pos = line_pos + 32
                    cursor_y += 32
                    n += 1
                else:
                    # Scroll the text up one line at a time
                    text_line[0] = text_line[1]
                    text_line[1] = text_line[2]
                    text_line[2] = text
                    screen.fill(pygame.Color("black"), (30,640,1024,132))
                    screen.blit(game_font.render(text_line[0], True, white), (cursor_x, line_pos - 96))
                    screen.blit(game_font.render(text_line[1], True, white), (cursor_x, line_pos - 64))
                    screen.blit(game_font.render(text_line[2], True, white), (cursor_x, line_pos - 32))
                print(text)
                text = '.'
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from the text string
                text = text[:-1]
                # Overwrite the cursor pixels with black
                cursor.fill(black)
                screen.blit(cursor, (cursor_x, cursor_y))
                # Move the cursor starting position back one space
                cursor_x = cursor_x - 32
                # Overwrite the last character pixels with black
                screen.fill(black, (cursor_x, line_pos + 10, 32, 32))
            else:
                cursor.fill(black)
                screen.blit(cursor, (cursor_x, cursor_y))
                text += event.unicode
                cursor_x += 32

        #print(event)
    cursor.fill((255, 255, 255))
    screen.blit(cursor, (cursor_x, cursor_y))
    screen.blit(game_font.render(text, True, white), (0, line_pos))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
