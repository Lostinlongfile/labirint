from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def place(self):
        glVertex3f(self.x,self.y,self.z)
    def __mul__(self,y):
        return point(self.x*y,self.y*y,self.z*y)
    def __add__(self,y):
        return point(self.x+y.x,self.y+y.y,self.z+y.z)
    def __sub__(self,y):
        return point(self.x-y.x,self.y-y.y,self.z-y.z)
    def __call__(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def rast(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)
    def __repr__(self):
        return str(self)
class side:
    typ=True
    def __init__(self,p1,p2,p3,p4,name='no'):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.name=name
    def render(self):
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        self.p1.place()
        self.p2.place()
        self.p3.place()
        self.p4.place()
        glEnd();
        
        glColor3f(0,0,0)
        if self.typ:
            glBegin(GL_LINE_LOOP)
        else:
            glBegin(GL_POLYGON)
            
        self.p1.place()
        self.p2.place()
        self.p3.place()
        self.p4.place()
        glEnd();
    def get_center(self):
        return self.p1+(self.p3-self.p1)*0.5
    def __str__(self):
        return "side ({4}) {0} - {1} - {2} - {3} ".format(str(self.p1),str(self.p2),str(self.p3),str(self.p4),self.name)
    def __repr__(self):
        return str(self)

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
        self.frontside=side(self.p1,self.p2,self.p3,self.p4,name='frontside')
        self.downside=side(self.p1,self.p2,self.p6,self.p5,name='downside')
        self.backside=side(self.p8,self.p7,self.p6,self.p5,name='backside')
        self.leftside=side(self.p1,self.p4,self.p8,self.p5,name='leftside')
        self.rightside=side(self.p2,self.p3,self.p7,self.p6,name='rightside')
        self.upside=side(self.p4,self.p3,self.p7,self.p8,name='upside')
        self.lst=[self.frontside,self.downside,self.backside,
                    self.leftside, self.rightside,self.upside]
    def render(self):
        self.upside.render()
        self.downside.render()
        self.backside.render()
        self.leftside.render()
        self.rightside.render()
        self.frontside.render()
        self.render_for_point(point(0,0,0))
    def render_for_point(self,p):
        s=sorted(self.lst,key=lambda so:((so.get_center()-p).rast()),reverse=True)
        for i in s:
            i.render();
            print(i,i.get_center(),((i.get_center()-p).rast()))
        print("\n");
