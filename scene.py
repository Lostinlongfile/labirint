from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from onebox import *
import sys

class LScene:
	ex=3.0
	ey=3.0
	ez=-3.0
	sex=0.0
	sey=0.0
	sez=0.0
	stp=0.1
	def __init__(self):
		self.ob=OneBox(0,0,0)
		pass 
	def initFun(self):
		glMatrixMode   ( GL_PROJECTION )
		glClearColor(1.0,1.0,1.0,0.0)
		glColor3f(0.0,0.0, 0.0)
		glLoadIdentity()
		glOrtho(-5,5,-5,5,-5,5)
	def keyPressed(self,c,x,y):
		print (c,x,y,self.sex,self.sey,self.sez,self.ex,self.ey,self.ez)
		if c==b'w':
			self.ey+=self.stp
		elif c==b's':
			self.ey-=self.stp
		elif c==b'a':
			self.ex-=self.stp
		elif c==b'd':
			self.ex+=self.stp
		elif c==b'f':
			self.ez-=self.stp
		elif c==b'c':
			self.ez+=self.stp
		elif c==b'q':
			sys.exit()
		self.displayFun()
	def displayFun(self):
		glClear        ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
		glMatrixMode   ( GL_MODELVIEW )
		glLoadIdentity () 
		gluLookAt (self.sex, self.sey, self.sez, 
				   self.ey, self.ez, self.ex,
				   0.0, 1.0, 0.0);
		self.ob.render_for_point(point(self.ex, self.ey, self.ez));
		glFlush()
