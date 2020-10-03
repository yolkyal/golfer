import pygame, sys, math, time
from golfer import Golfer
from golfer_controller import GolferController
from golfer_drawer import GolferDrawer
from hole import Hole
from hole_drawer import HoleDrawer
from ball import Ball
from ball_drawer import BallDrawer
from wall import Wall
from wall_drawer import WallDrawer

BG_COL = (0, 200, 100)


def main():
	pygame.init()
	size = width, height = 400, 400
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	ball = Ball()
	golfer = Golfer(ball)
	golfer_controller = GolferController(golfer)
	walls = [Wall((100, 25), (300, 25)), Wall((300, 25), (300, 375)), Wall((300, 375), (100, 375)), Wall((100, 375), (100, 25))]
	
	ball_start_pos = (200, 325)
	hole_pos = (200, 75)
	golfer_start_direction = -math.pi/2

	hole = Hole(ball_start_pos, hole_pos, golfer_start_direction, walls)

	golfer_drawer = GolferDrawer()
	ball_drawer = BallDrawer()
	hole_drawer = HoleDrawer()
	wall_drawer = WallDrawer()

	ball.pos = hole.ball_start_pos
	golfer.direction = hole.golfer_start_direction

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
				golfer_controller.handle_event(event)
				
		golfer.update()
		hole.update(ball, delta_ms)

		d_surf.fill(BG_COL)
		hole_drawer.draw(d_surf, hole)
		for wall in walls:
			wall_drawer.draw(d_surf, wall)
		golfer_drawer.draw(d_surf, golfer)
		ball_drawer.draw(d_surf, ball)
		
		if hole.is_complete(ball):
			time.sleep(1)
			pygame.quit()
			sys.exit()

		pygame.display.update()


if __name__ == '__main__':
	main()