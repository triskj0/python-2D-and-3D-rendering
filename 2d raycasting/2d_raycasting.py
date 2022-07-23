#!/usr/bin/env python

import pygame
import math 

pygame.init()
clock = pygame.time.Clock()
FPS = 30

# create a pygame window, constants
HEIGHT = 750
WIDTH = 1200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("raycasting")

FOV = math.pi*2 # field of view = 360°
CASTED_RAYS = 150 # number of rays we're casting
STEP_ANGLE = FOV/CASTED_RAYS # space between rays
MAX_DEPTH = WIDTH # maximum length of a ray

# color constants
BLACK = (0, 0, 0)
DARK_GREY = (90, 90, 90)
LIGHT_GREY = (150, 150, 150)
WHITE = (255, 255, 255)

# size of squares in the 2d map
SQUARE_SIZE =  HEIGHT//20

# the game map
# I chose a map of this specific size (32:20), because it goes well with the window dimensions
# (WIDTH/HEIGHT) 1200/750 can be simplified to 8/5 and 32/20 is just a multiple of that
MAP = (
'################################',
'#                              #',
'#                              #',
'#          ###      #####      #',
'#          # #          #      #',
'#          ###          #      #',
'#   ####             #  #      #',
'#   #  #                #      #',
'#   #  #                       #',
'#   #  #                       #',
'#   #  #                       #',
'#   ####                       #',
'#               # # # # # # # ##',
'#          #    #              #',
'#          #    #              #',
'#        ###    #              #',
'#               #              #',
'#                              #',
'#                              #',
'################################'
)


def draw_map():
	for row in range(20):
		for col in range(32):
			
			# if it's a wall
			if MAP[row][col] == '#':
				pygame.draw.rect(WIN, BLACK, (SQUARE_SIZE*col, SQUARE_SIZE*row, SQUARE_SIZE, SQUARE_SIZE))
			else:
				pygame.draw.rect(WIN, LIGHT_GREY, (SQUARE_SIZE*col, SQUARE_SIZE*row, SQUARE_SIZE, SQUARE_SIZE))


def cast_rays(mouse_x, mouse_y):
	# angle of the current ray (gets incremented)
	ray_angle = 0

	for ray in range(CASTED_RAYS):
		for depth in range(MAX_DEPTH):
			target_x = mouse_x - math.sin(ray_angle)*depth
			target_y = mouse_y + math.cos(ray_angle)*depth

			# convert x, y coordinates to col, row
			col = int(target_x / SQUARE_SIZE)
			row = int(target_y / SQUARE_SIZE)

			if col > 31:
				col = 31

			if row > 19:
				row = 19

			# if the ray collides with a wall, we daw it
			if MAP[row][col] == '#':
				pygame.draw.line(WIN, WHITE, (mouse_x, mouse_y), (target_x, target_y), 5)
				break

		ray_angle += STEP_ANGLE


def update():
	WIN.fill(BLACK)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	draw_map()
	cast_rays(mouse_x, mouse_y)

	pygame.display.update()
	clock.tick(FPS)


def main():
	run = True
	while run:
		update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				run = False


if __name__ == '__main__':
	main()
