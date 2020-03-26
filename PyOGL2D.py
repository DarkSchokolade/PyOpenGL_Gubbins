import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def square():
    glBegin(GL_QUADS)
    glVertex3fv((1, 1,0))
    glVertex3fv((2, 1,0))
    glVertex3fv((2, 2,0))
    glVertex3fv((1, 2,0))
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)


    glTranslatef(-2.0,-1.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 3.0)
        square()
        pygame.display.flip()
        pygame.time.wait(10)


main()