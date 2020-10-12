import pygame, sys, math, time
from golfer import Golfer
from golfer_controller import GolferController
from golfer_drawer import GolferDrawer
from hole import Hole
from hole_drawer import HoleDrawer
from ball import Ball
from ball_drawer import BallDrawer
from wall import Wall, WallBuilder
from wall_drawer import WallDrawer
from course import Course
from game import Game
from game_drawer import GameDrawer


BG_COL = (0, 200, 100)


def main():
	pygame.init()
	size = width, height = 400, 400
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	golfer = Golfer(Ball())
	walls1 = WallBuilder((100, 25), (300, 25), (300, 375), (100, 375)).build()
	hole1 = Hole((200, 325), (200, 75), -math.pi/2, walls1)
	game = Game(golfer, Course([hole1]))

	game_drawer = GameDrawer(BallDrawer(), GolferDrawer(), HoleDrawer(), WallDrawer())

	golfer_controller = GolferController(golfer)

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
				golfer_controller.handle_event(event)
				
		game.update(delta_ms)

		d_surf.fill(BG_COL)
		game_drawer.draw(d_surf, game)
		
		if game.is_complete():
			time.sleep(1)
			pygame.quit()
			sys.exit()

		pygame.display.update()


if __name__ == '__main__':
	main()