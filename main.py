import pygame, sys
from golfer import Golfer
from golfer_controller import GolferController
from golfer_drawer import GolferDrawer
from course import Course
from course_drawer import CourseDrawer
from ball import Ball
from ball_drawer import BallDrawer


BG_COL = (0, 200, 100)


def main():
	pygame.init()
	size = width, height = 800, 800
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	ball = Ball((400, 400))
	golfer = Golfer(ball)
	golfer_controller = GolferController(golfer)
	course = Course(ball, (600, 600))

	golfer_drawer = GolferDrawer()
	ball_drawer = BallDrawer()
	course_drawer = CourseDrawer()

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
		golfer_drawer.draw(d_surf, golfer)
		ball_drawer.draw(d_surf, ball)

		pygame.display.update()
	

if __name__ == '__main__':
	main()