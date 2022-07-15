import pygame
import math

# CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VELOCITY_X = .5
VELOCITY_Y = .15
VELOCITY_Z = .1

# creating a window
WIN_WIDTH = 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))

# pygame clock
clock = pygame.time.Clock()
FPS = 20

# cube parameters
cube_x = WIN_WIDTH/2
cube_y = WIN_WIDTH/2
cube_z = 0
cube_size = WIN_WIDTH/4

verticies = [
	#[x, y, z]
	[cube_x - cube_size, cube_y - cube_size, cube_z - cube_size],
	[cube_x + cube_size, cube_y - cube_size, cube_z - cube_size],
	[cube_x + cube_size, cube_y + cube_size, cube_z - cube_size],
	[cube_x - cube_size, cube_y + cube_size, cube_z - cube_size],
	[cube_x - cube_size, cube_y - cube_size, cube_z + cube_size],
	[cube_x + cube_size, cube_y - cube_size, cube_z + cube_size],
	[cube_x + cube_size, cube_y + cube_size, cube_z + cube_size],
	[cube_x - cube_size, cube_y + cube_size, cube_z + cube_size]
]
edges = [ # lists of connected points 
	[0, 1], [1, 2], [2, 3], [3, 0], # back face
	[4, 5], [5, 6], [6, 7], [7, 4], # front face
	[0, 4], [1, 5], [2, 6], [3, 7]  # connecting sides
]


"""
x, y, z : current vertex coordinates
new_x, new_y, new_z : new vertex coordinates, a frame ahead of the old ones
θ : given angle

X AXIS ROTATION
new_y = y * cos(θ) - z * sin(θ)
new_z = z * cos(θ) + y * sin(θ)

Y AXIS ROTATION
new_x = x * cos(θ) - z * sin(θ)
new_z = z * cos (θ) + sin(θ)

Z AXIS ROTATION
new_x = x * cos(θ) - y * sin(θ)
new_y = y * cos(θ) + x * sin(θ)
"""

# rotate along the x axis
def rotate_x():
	angle = FPS * 0.001 * VELOCITY_X * math.pi * 2
	for vertex in verticies:
		y = vertex[1] - cube_y
		z = vertex[2] - cube_z
		new_y = y * math.cos(angle) - z * math.sin(angle)
		new_z = z * math.cos(angle) + y * math.sin(angle)
		vertex[1] = new_y + cube_y
		vertex[2] = new_z + cube_z


# rotate along the y axis
def rotate_y():
	angle = FPS * 0.001 * VELOCITY_Y * math.pi * 2
	for vertex in verticies:
		x = vertex[0] - cube_x
		z = vertex[2] - cube_z 
		new_x = x * math.cos(angle) - z * math.sin(angle)
		new_z = z * math.cos(angle) + x * math.sin(angle)
		vertex[0] = new_x + cube_x
		vertex[2] = new_z + cube_z


# rotate along the z axis
def rotate_z():
	angle = FPS * .001 * VELOCITY_Z	* math.pi * 2 
	for vertex in verticies:
		x = vertex[0] - cube_x
		y = vertex[1] - cube_y
		new_x = x * math.cos(angle) - y * math.sin(angle)
		new_y = y * math.cos(angle) + x * math.sin(angle)
		vertex[0] = new_x + cube_x
		vertex[1] = new_y + cube_y


def update(win):
	win.fill(BLACK)

	# rotating the cube
	rotate_x()
	rotate_y()
	rotate_z()

	# drawing the cube
	for edge in edges:
		pygame.draw.line(win, WHITE, (verticies[edge[0]][0], verticies[edge[0]][1]), \
						(verticies[edge[1]][0], verticies[edge[1]][1]), 20)

	pygame.display.update()
	clock.tick(FPS)


def main():
	run = True
	while run:
		update(WIN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	pygame.QUIT

if __name__ == "__main__":
	main()
