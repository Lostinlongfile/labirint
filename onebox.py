from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def place(self):
        glVertex3f(self.x,self.y,self.z)
class side:
    typ=True
    def __init__(self,p1,p2,p3,p4):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
    def render(self):
        if self.typ:
            glBegin(GL_LINE_LOOP)
        else:
            glBegin(GL_POLYGONE)
            
        self.p1.place()
        self.p2.place()
        self.p3.place()
        self.p4.place()
        glEnd();

class OneBox:
    x=0
    y=0
    z=0
    sx=1
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.p1=point(self.x,         self.y,self.         z)
        self.p2=point(self.x,         self.y+self.sx, self.z)
        self.p3=point(self.x+self.sx, self.y+self.sx, self.z)
        self.p4=point(self.x+self.sx, self.y,         self.z)
        self.p5=point(self.x,         self.y,         self.z+self.sx)
        self.p6=point(self.x,         self.y+self.sx, self.z+self.sx)
        self.p7=point(self.x+self.sx, self.y+self.sx, self.z+self.sx)
        self.p8=point(self.x+self.sx, self.y,         self.z+self.sx)
        self.frontside=side(self.p1,self.p2,self.p3,self.p4)
        self.downside=side(self.p1,self.p2,self.p6,self.p5)
        self.backside=side(self.p8,self.p7,self.p6,self.p5)
        self.leftside=side(self.p1,self.p4,self.p8,self.p5)
        self.rightside=side(self.p2,self.p3,self.p7,self.p6)
        self.upside=side(self.p4,self.p3,self.p7,self.p8)
    def render(self):
        self.upside.render()
        self.downside.render()
        self.backside.render()
        self.leftside.render()
        self.rightside.render()
        self.frontside.render()
