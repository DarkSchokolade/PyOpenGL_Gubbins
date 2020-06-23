"""
Opengl project demonstrating lighting and smooth shading
Using GLU primitive shapes
written in python because C++ did not work for me

Spinning primitives
Press UP ARROW or DOWN ARROW to adjust the slices and stacks of the primitive shapes
Press and Hold (x)  to view X-Ray(Wireframe) mode

Written and modified by SUHAS.K.SHETTY
"""

import time
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# GLUT doesn't work


def draw(slices, stacks):
    t = time.time() % 1000
    angle = t*90
    quad = gluNewQuadric()

    glColor3f(0.5, 1.0, 0.4)

    glPushMatrix()
    glTranslatef(-2.4, 1.5, -6)
    glRotatef(45,1,0,0)
    glRotatef(angle,0,0,1)
    gluSphere(quad, 1, slices, stacks)  # quads, radius, slices, stacks
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 1.5, -6)
    glRotatef(-60, 1, 0.2, 0)
    glRotatef(angle, 0, 0, 1)
    gluCylinder(quad, 1.5, 0.1, 2, slices, stacks)  # quads, base, top, height, slices, stacks
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 0, 1)
    gluPartialDisk(quad, 0.5, 1, slices, stacks, 0, 270)    # quad, inner, outer, slices, loops, start angle, sweep angle
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 1, 1)
    gluDisk(quad, 0.5, 1, slices, stacks)  # quad, inner, outer, slices, loops
    glPopMatrix()



def XrayDraw(slices, stacks):
    t = time.time() % 1000
    angle = t * 90
    quad = gluNewQuadric()

    glColor3f(0.5, 1.0, 0.9)

    # Wire Frame Mode Starts From Here
    gluQuadricDrawStyle(quad, GLU_LINE)

    glPushMatrix()
    glTranslatef(-2.4, 1.5, -6)
    glRotatef(45, 1, 0, 0)
    glRotatef(angle, 0, 0, 1)
    gluSphere(quad, 1, slices, stacks)  # quads, radius, slices, stacks
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 1.5, -6)
    glRotatef(-60, 1, 0.2, 0)
    glRotatef(angle, 0, 0, 1)
    gluCylinder(quad, 1.5, 0.1, 2, slices, stacks)  # quads, base, top, height, slices, stacks
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 0, 1)
    gluPartialDisk(quad, 0.5, 1, slices, stacks, 0, 270)  # quad, inner, outer, slices, loops, start angle, sweep angle
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 1, 1)
    gluDisk(quad, 0.5, 1, slices, stacks)  # quad, inner, outer, slices, loops
    glPopMatrix()

light_ambient = [0.0, 0.0, 0.0, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [2.0, 5.0, 5.0, 0.0]

mat_ambient = [0.7, 0.7, 0.7, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
high_shininess = [100.0]


def main():
    slices = 10
    stacks = 10

    xray = False

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(-2.0, -1.0, -5)
    # glTranslatef(0,0,-5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    slices += 1
                    stacks += 1
                if event.key == pygame.K_DOWN and (slices > 3 and stacks > 3):
                    slices -= 1
                    stacks -= 1
                if event.key == pygame.K_x:
                    xray = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    xray = False


        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 3.0)

        if(xray):
            XrayDraw(slices, stacks)
        else:
            draw(slices, stacks)

        glClearColor(1,1,1,1)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)

        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

        pygame.display.flip()
        pygame.time.wait(10)

angle=0
main()