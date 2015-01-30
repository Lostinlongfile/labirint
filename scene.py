from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class LScene:
	ex=3
	ey=3
	ez=3
	sex=0
	sey=0
	sez=0
	def __init__(self):
		pass
	def initFun():
		glClearColor(1.0,1.0,1.0,0.0)
		glColor3f(0.0,0.0, 0.0)
		gluLookAt (0.0, 0.0, 0.0, 
				   3.0, 3.0, 3.0,
				   0.0, 1.0, 0.0);
		glLoadIdentity()
   

	def displayFun():
		glClear(GL_COLOR_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW); 
		gluLookAt (0.0, 0.0, 0.0, 
				   3.0, 3.0, 3.0,
				   0.0, 1.0, 0.0);
		glLoadIdentity();
		glBegin(GL_POLYGON);
		glVertex2f(0.0, 0.0);
		glVertex2f(0.0, 3.0);
		glVertex2f(4.0, 3.0);
		glVertex2f(6.0, 1.5);
		glVertex2f(4.0, 0.0);
		glEnd()
		

		glFlush()
