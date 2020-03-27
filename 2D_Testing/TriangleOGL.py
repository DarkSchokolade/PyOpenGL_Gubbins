import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def triangle(x):

    glBegin(GL_QUADS)
    glVertex3fv((1+x, 1, 0))
    glVertex3fv((2+x, 1, 0))
    glVertex3fv((1.5+x, 2, 0))
    glVertex3fv((1.5+x, 2, 0))
    glEnd()

def main(x, flag):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(squareX, squareY, -5)


    while True:
        # if(x > -1):
        #     x = x-0.01
        # elif(x<2):
        #     x = x+0.01
        if (flag):
            x += 0.01
            if (x > 2.0):
                flag=False

        if (not flag):
            x -= 0.01
            if (x < -1.0):
                flag = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate for some crazy stuff
        # glRotatef(1, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 3.0)
        triangle(x)

        pygame.display.flip()
        pygame.time.wait(10)

flag = True
squareX = -2.0
squareY = -1.0
x = 0
main(x, flag)
