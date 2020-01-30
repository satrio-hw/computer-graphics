import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def loadTexture() :
	textureSurface = pygame.image.load('metal.jpg')
	textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
	width = textureSurface.get_width()
	height = textureSurface.get_height()
	
	glEnable(GL_TEXTURE_2D)
	texid = glGenTextures(1)
	
	glBindTexture(GL_TEXTURE_2D, texid)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 
				0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
				
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	
	return texid

def ploting(matrix,c,l):
    
    for square in matrix: 
        glColor3f(c[0],c[1],c[2]) 
        glBegin(GL_POLYGON) 
        for point in square: 
            glVertex3f(point[0]*0.1, point[1]*0.1, point[2]*0.1) 
        glEnd() 
        glColor3f(l[0],l[1],l[2]) 
        glBegin(GL_LINE_LOOP) 
        for point in square: 
            glVertex3f(point[0]*0.1, point[1]*0.1, point[2]*0.1) 
        glEnd()

def plotwings(f1top,f1bottom,f2top,f2bottom,rudder):
    
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0, 0.0, 0.0) 
    glPointSize(1.0)

    defcolor=[0,0,0]

    color_bag1=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag1 = [ 
    [[0,0,8],[1,1,4],[-1,1,4]], #S1 = B11, B12, B16 (atas)
    [[0,0,8],[-1,1,4],[-1,-1,4]], #S2 = B11, B16, B111 (kiri)
    [[0,0,8],[1,-1,4],[1,1,4]], #S3 = B11, B112, B12 (kanan)
    [[0,0,8],[1,-1,4],[-1,-1,4]], #S4 = B11, B112, B111(bawah)
    [[-0.8,0.8,5],[-1,0.8,4],[-1,0.8,2],[-0.8,0.8,1],[0.8,0.8,1],[1,0.8,2],[1,0.8,4],[0.8,0.8,5]]
    #alas kokpit = C18, C17, C16, C15, C15a, C16a, C17a, C18a
    ]
    ploting(bag1,color_bag1,defcolor)

    color_bag2=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag2 = [ 
    [[-1,1,4],[-1,1,-3],[1,1,-3],[1,1,4]], #S1 = B16, B15, B13, B12
    [[-1,1,4],[-1,1,-3],[-1,-1,-3],[-1,-1,4]], #S2 = B16, B15, B113, B111
    [[1,1,4],[1,1,-3],[1,-1,-3],[1,-1,4]], #S3 = B12, B13, B114, B112
    [[-1,-1,4],[-1,-1,-3],[1,-1,-3],[1,-1,4]] #S4 = B111, B113, B114, B112
     
    ]
    ploting(bag2,color_bag2,defcolor)

    color_bag3=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag3 = [ 
    [[0,0,-8],[1,1,-3],[-1,1,-3]], #S1 = B14a, B13, B15 (atas)
    [[0,0,-8],[-1,1,-3],[-1,-1,-3]], #S2 = B14a, B15, B113 (kiri)
    [[0,0,-8],[1,1,-3],[1,-1,-3]], #S3 = B14a, B13, B114 (kanan)
    [[0,0,-8],[-1,-1,-3],[1,-1,-3]] #S4 = B14a, B113, B114(bawah)
    ]
    ploting(bag3,color_bag3,defcolor)

    color_bag4=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag4 = [ 
    [[-1,1,-3],[-0.2,1,-7],[0,0.6,-8],[0.2,1,-7],[1,1,-3]], #S1 = B15,B18,B14,B17,B13
    [[-1,-1,-3],[-0.2,-1,-7],[0,-0.6,-8],[0.2,-1,-7],[1,-1,-3]] #S2 = B113,B110,B19,B115,B114
     
    ]
    ploting(bag4,color_bag4,defcolor)

    color_bag5=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag5 = [ 
    [[-1,0.6,3],[-2,0.6,3],[-2,0.6,-4],[-1.4,0.6,-6],[-1.4,0.6,-8],[0,0.6,-8]],
    #S1 = B31, B32, B33, B34, B35, B14
    [[-2,0.6,3],[-2,-0.6,2],[-2,-0.6,-4],[-1.4,-0.6,-6],[-1.4,-0.6,-8],[-1.4,0.6,-8],[-1.4,0.6,-6],[-2,0.6,-4]],
    #S2 = B32, B39, B311, B310, B38, B35, B34, B33
    [[-1.4,0.6,-8],[0,0.6,-8],[0,-0.6,-8],[-1.4,-0.6,-8]], #S3 = B35, B14, B19, B38
    [[-1,-0.6,2],[-2,-0.6,2],[-2,-0.6,-4],[-1.4,-0.6,-6],[-1.4,-0.6,-8],[0,-0.6,-8]],
    #S4 = B31a, B39, B311, B310, B38, B19
    [[-1,0.6,3],[-2,0.6,3],[-2,-0.6,2],[-1,-0.6,2]] #S5 = B31, B32, B39, B31a
    ]
    ploting(bag5,color_bag5,defcolor)

    color_bag6=[0.49,0.56,0.64]
    #[X,Y,Z]
    bag6 = [ 
    [[1,0.6,3],[2,0.6,3],[2,0.6,-4],[1.4,0.6,-6],[1.4,0.6,-8],[0,0.6,-8]],
    #S1 = B21, B22, B23, B24, B25, B14
    [[2,0.6,3],[2,-0.6,2],[2,-0.6,-4],[1.4,-0.6,-6],[1.4,-0.6,-8],[1.4,0.6,-8],[1.4,0.6,-6],[2,0.6,-4]],
    #S2 = B22, B39a, B311a, B310a, B38a, B25, B24, B23
    [[1.4,0.6,-8],[0,0.6,-8],[0,-0.6,-8],[1.4,-0.6,-8]], #S3 = B25, B14, B19, B38a
    [[1,-0.6,2],[2,-0.6,2],[2,-0.6,-4],[1.4,-0.6,-6],[1.4,-0.6,-8],[0,-0.6,-8]],
    #S4 = B21a, B39a, B311a, B310a, B38a, B19
    [[1,0.6,3],[2,0.6,3],[2,-0.6,2],[1,-0.6,2]] #S5 = B21, B22, B39a, B21a
    ]
    ploting(bag6,color_bag6,defcolor)

    
    #--------------------- WING 2 START ------------------------#
    color_w2=[0.45,0.53,0.93]
    wing2 = [ 
    [[-2, 0.4,1], [-10, 0.2,-2], [-10, 0.2,-4], [-2, 0.2,-3]], #top[w21,w22,w23,w24]
    [[-2, -0.2,1], [-10, 0.0,-2], [-10, 0.0,-4], [-2, 0.0,-3]], #bottom[w210,w211,w212,w29]
    [[-2, 0.4,1], [-2, -0.2,1], [-10, 0.0,-2], [-10, 0.2,-2]], #front
    [[-2, 0.2,-3], [-2, 0.0,-3], [-10, 0.0,-4], [-10, 0.2,-4]], #back
    [[-10, 0.2,-2], [-10, 0.2,-4], [-10, 0.0,-4], [-10, 0.0,-2]], #outer side
    [[-2, 0.4,1], [-2, 0.2,-3], [-2, 0.0,-3], [-2, -0.2,1]] #inner side
    ] #tutup 
    
    ploting(wing2,color_w2,defcolor)
    #--------------------- WING 2 END ------------------------#
    
    #--------------------- FLAP 2 START ------------------------#
    color_f2=[1.0,0.0,0.0]
    #[X,Y,Z]
    flap2 = [ 
    [[-3, 0.2,-2.8], [-9, 0.2,-3.4], [-9, (f2top),-4], [-3, (f2top),-3.2]], #top[w11,w12,w13,w14]
    [[-3, 0.0,-2.8], [-9, 0.0,-3.4], [-9, (f2bottom),-4], [-3, (f2bottom),-3.2]], #bottom[w110,w111,w112,w19]
    [[-3, 0.2,-2.8], [-3, 0.0,-2.8], [-9, 0.0,-3.4], [-9, 0.2,-3.4]], #front
    [[-3, (f2top),-3.2], [-3, (f2bottom),-3.2], [-9, (f2bottom),-4], [-9, (f2top),-4]], #back
    [[-9, 0.0,-3.4], [-9, 0.2,-3.4], [-9, (f2top),-4], [-9, (f2bottom),-4]], #outer side
    [[-3, 0.2,-2.8], [-3, 0.0,-2.8], [-3, (f2bottom),-3.2], [-3, (f2top),-3.2]] #inner side
    ] #tutup 
    
    ploting(flap2,color_f2,defcolor)
    #--------------------- FLAP 2 END ------------------------#

    #--------------------- WING 1 START ------------------------#
    color_w1=[0.45,0.53,0.93]
    #[X,Y,Z]
    wing1 = [ 
    [[2, 0.4,1], [10, 0.2,-2], [10, 0.2,-4], [2, 0.2,-3]], #top[w11,w12,w13,w14]
    [[2, -0.2,1], [10, 0.0,-2], [10, 0.0,-4], [2, 0.0,-3]], #bottom[w110,w111,w112,w19]
    [[2, 0.4,1], [2, -0.2,1], [10, 0.0,-2], [10, 0.2,-2]], #front
    [[2, 0.2,-3], [2, 0.0,-3], [10, 0.0,-4], [10, 0.2,-4]], #back
    [[10, 0.2,-2], [10, 0.2,-4], [10, 0.0,-4], [10, 0.0,-2]], #outer side
    [[2, 0.4,1], [2, 0.2,-3], [2, 0.0,-3], [2, -0.2,1]] #inner side
    ] #tutup 
    
    ploting(wing1,color_w1,defcolor)
    #--------------------- WING 1 END ------------------------#

    #--------------------- FLAP 1 START ------------------------#
    color_f1=[1.0,0.0,0.0]
    #[X,Y,Z]
    flap1 = [ 
    [[3, 0.2,-2.8], [9, 0.2,-3.4], [9, (f1top),-4], [3, (f1top),-3.2]], #top[w11,w12,w13,w14]
    [[3, 0.0,-2.8], [9, 0.0,-3.4], [9, (f1bottom),-4], [3, (f1bottom),-3.2]], #bottom[w110,w111,w112,w19]
    [[3, 0.2,-2.8], [3, 0.0,-2.8], [9, 0.0,-3.4], [9, 0.2,-3.4]], #front
    [[3, (f1top),-3.2], [3, (f1bottom),-3.2], [9, (f1bottom),-4], [9, (f1top),-4]], #back
    [[9, 0.0,-3.4], [9, 0.2,-3.4], [9, (f1top),-4], [9, (f1bottom),-4]], #outer side
    [[3, 0.2,-2.8], [3, 0.0,-2.8], [3, (f1bottom),-3.2], [3, (f1top),-3.2]] #inner side
    ] #tutup  
    
    ploting(flap1,color_f1,defcolor)
    #--------------------- FLAP 1 End ------------------------#

    #--------------------- TAIL START ------------------------#
    color_t1=[0.49,0.56,0.64]
    #[X,Y,Z]
    #TAIL
    tail1 = [ 
    [[-0.2, 1,-4], [0.2, 1,-4], [0.2, 3,-5], [-0.2, 3,-5]], #top[t11,t12,t13,t16]
    [[0.2, 3,-5], [0.2, 3,-6.2], [-0.2, 3,-6.2], [-0.2, 3,-5]], #top[t13,t14,t15,t16]
    [[-0.2, 1,-4], [-0.2, 1,-6], [-0.2, 3,-6.2], [-0.2, 3,-5]], #left[t11,t17.t15,t16]
    [[-0.2, 3,-6.2], [-0.2, 1,-6], [0.2, 1,-6], [0.2, 3,-6.2]], #back
    [[-0.2, 1,-4], [0.2, 1,-4], [0.2, 1,-6], [-0.2, 1,-6]], #bottom
    [[0.2, 1,-4], [0.2, 1,-6], [0.2, 3,-6.2], [0.2, 3,-5]] #right
    ] #tutup
    ploting(tail1,color_t1,defcolor)
    #--------------------- TAIL END ------------------------#

    
    
    #--------------------- RUDDER START ------------------------#
    color_e1=[1,0,0]
    rudder1 = [ 
    [[0.2, 3,-6.2], [rudder, 3,-7], [-0.2, 3,-6.2]], #top[r11,r12,r13]
    [[-0.2, 3,-6.2], [rudder, 3,-7], [rudder, 1,-7], [-0.2, 1,-6]], #left
    [[0.2, 1,-6.2], [rudder, 1,-7], [-0.2, 1,-6.2]], #bottom
    [[0.2, 3,-6.2], [rudder, 3,-7], [rudder, 1,-7], [0.2, 1,-6]] #right
    ] #tutup
    ploting(rudder1,color_e1,defcolor)
    #--------------------- RUDDER END ------------------------#

    

    #kokpit
    color_k1=[0.94,0.97,1.0]
    #[X,Y,Z]
    k1 = [ 
    [[-0.8,0.8,5],[-0.8,1.6,4],[0.8,1.6,4],[0.8,0.8,5]],
    #S1 = C18, C111, C111a, C18a
    [[-0.8,1.6,4],[0.8,1.6,4],[0.8,1.6,2],[-0.8,1.6,2]],
    #S2 = C111, C111a, C112,C112a
    [[-0.8,1.6,2],[0.8,1.6,2],[0.8,0.8,1],[-0.8,0.8,1]],
    #S3 = C112, C112a, C15a, C15
    [[-1,0.8,4],[-1,0.8,2],[-0.8,1.6,2],[-0.8,1.6,4]],
    #S4 = C17, C16, C112, C111,
    [[1,0.8,4],[1,0.8,2],[0.8,1.6,2],[0.8,1.6,4]],
    #S5 = C17a, C16a, C112a, C111a
    [[-0.8,0.8,5],[-1,0.8,4],[-0.8,1.6,4]],
    #S6 = C18, C17, C111
    [[-0.8,0.8,1],[-1,0.8,2],[-0.8,1.6,2]],
    #S7 = C15, C16, C112
    [[0.8,0.8,1],[1,0.8,2],[0.8,1.6,2]],
    #S8 = C15a, C16a, C112a
    [[0.8,0.8,5],[1,0.8,4],[0.8,1.6,4]]
    #S19 = C18a, C16a, C111a
    
    ] 

    ploting(k1,color_k1,defcolor)

    
    
    glFlush()
def main(): 
    pygame.init() 
    display = (800,800) 
    pygame.display.set_caption('Function Plot') 
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) 
    glTranslatef(0.0,0.0,-5) 
    glClearColor(1.0, 1.0, 1.0, 1.0)

    pygame.mixer.init(22100, -16, 2, 4)

    loadTexture()
    
    rotate_angle = 0.0 
    x_rotate = 0
    y_rotate = 0
    z_rotate = 0

    movement=0.0

    #init flap
    f1top=0.2
    f1bottom=0.0
    f2bottom=f1bottom
    f2top=f1top
    rudder=0
    transr=0

    transf1=0
    transf2=transf1
    normf1=0
    normf2=normf1

    flag=0

    glRotatef(180, 0,1,0)
    glRotatef(-45, 1,0,0)
    pygame.mixer.music.load('avion.mp3')
    pygame.mixer.music.play(-1)

    speed=0.1
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
        glRotatef(rotate_angle, x_rotate, y_rotate, z_rotate)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        if(f1top >=-0.3 and f1top <=0.5):
            f1top+=transf1
            f1bottom+=transf1

            f2top+=transf2
            f2bottom+=transf2

            oldflag=flag
        #elif(f1top <=-0.3 or f1top >=0.5):
         #   f1top+=normf1
          #  f1bottom+=normf1

           # f2top+=normf2
            #f2bottom+=normf2

        if(f2top >=-0.3 and f2top <=0.5):
            f1top+=transf1
            f1bottom+=transf1

            f2top+=transf2
            f2bottom+=transf2

            oldflag=flag
        #elif(f2top <=-0.3 or f2top >=0.5):
         #   f1top+=normf1
          #  f1bottom+=normf1

           # f2top+=normf2
            #f2bottom+=normf2

        if(rudder >=-0.3 and rudder <=0.3):
            rudder+=transr
        elif(rudder <=-0.3 or rudder >=0.3):
            rudder+=normf1
            
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_DOWN:
                
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0):
                    f1top=0.2
                    f1bottom=0.0
                    f2bottom=f1bottom
                    f2top=f1top
                    
                transf1=-0.01
                transf2=-0.01
                flag=1

                rotate_angle = -speed
                x_rotate = 1
                y_rotate = 0
                z_rotate = 0
                
            if(event.key == pygame.K_UP):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0):
                    f1top=0.2
                    f1bottom=0.0
                    f2bottom=f1bottom
                    f2top=f1top
                    
                transf1=+0.01
                transf2=+0.01
                flag=2

                rotate_angle = speed
                x_rotate = 1
                y_rotate = 0
                z_rotate = 0
                
            if(event.key == pygame.K_LEFT):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0):
                    f1top=0.2
                    f1bottom=0.0
                    f2bottom=f1bottom
                    f2top=f1top
                    
                transf1=+0.01
                transf2=-0.01
                flag=3

                rotate_angle = -speed 
                x_rotate = 0
                y_rotate = 0
                z_rotate = 1
                
            if(event.key == pygame.K_RIGHT):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0):
                    f1top=0.2
                    f1bottom=0.0
                    f2bottom=f1bottom
                    f2top=f1top
                    
                transf1=-0.01
                transf2=+0.01
                flag=4

                rotate_angle = +speed 
                x_rotate = 0
                y_rotate = 0
                z_rotate = 1
                
            # RUDDER START
            if(event.key == pygame.K_a):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0 or rudder!= 0.0):
                    rudder= 0.0
                    
                transr=+0.01
                flag=5

                rotate_angle = +speed 
                x_rotate = 0
                y_rotate = 1
                z_rotate = 0

            if(event.key == pygame.K_d):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0 or rudder!= 0.0):       
                    rudder= 0.0
                    
                transr=-0.01
                flag=6

                rotate_angle = -speed
                x_rotate = 0
                y_rotate = 1
                z_rotate = 0
            # RUDDER END

            if(event.key == pygame.K_w):
                if speed == 0.1:
                    speed=0.8
                    
            if(event.key == pygame.K_s):
                if speed == 0.8:
                    speed=0.1
            
            if(event.key == pygame.K_SPACE):
                if(f1top!=0.2 or f1bottom!=0.0 or f2top!=0.2 or f2bottom!=0.0 or rudder!= 0.0):
                    f1top=0.2
                    f1bottom=0.0
                    
                    f2bottom=f1bottom
                    f2top=f1top
                    rudder= 0.0
                    
                transf1=0
                transf2=0
                transr=0
                flag=0

                rotate_angle = 0
                x_rotate = 0
                y_rotate = 0
                z_rotate = 0
                speed=0.1
                
        plotwings(f1top,f1bottom,f2top,f2bottom,rudder)
            
        pygame.display.flip()
        pygame.time.wait(10) 
main() 
