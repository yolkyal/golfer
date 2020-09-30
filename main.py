import pygame, sys, math
from golfer import Golfer
from golfer_controller import GolferController
from golfer_drawer import GolferDrawer
from course import Course
from course_drawer import CourseDrawer
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

	ball = Ball((200, 325))
	golfer = Golfer(ball, direction=-math.pi/2)
	golfer_controller = GolferController(golfer)
	walls = [Wall((100, 25), (300, 25)), Wall((300, 25), (300, 375)), Wall((300, 375), (100, 375)), Wall((100, 375), (100, 25))]
	course = Course(ball, (200, 75), walls)

	golfer_drawer = GolferDrawer()
	ball_drawer = BallDrawer()
	course_drawer = CourseDrawer()
	wall_drawer = WallDrawer()

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
				golfer_controller.handle_event(event)
				
		golfer.update()
		course.update(delta_ms)

		d_surf.fill(BG_COL)
		course_drawer.draw(d_surf, course)
		for wall in walls:
			wall_drawer.draw(d_surf, wall)
		golfer_drawer.draw(d_surf, golfer)
		ball_drawer.draw(d_surf, ball)
		
		if course.is_complete():
			pygame.quit()
			sys.exit()

		pygame.display.update()
	

if __name__ == '__main__':
	main()