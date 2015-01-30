# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from scene import *


if __name__ == '__main__':
	wind=LScene()
	glutInit()
	glutInitWindowSize(640,480)
	glutCreateWindow(b'lab')
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutDisplayFunc(wind.displayFun)
	glutKeyboardFunc(wind.keyPressed)
	wind.initFun()
	glutMainLoop()
