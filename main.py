import pygame
from pygame.locals import *
from src.storage_funcs import get_stored_values, set_stored_values

from time import sleep

from OpenGL.GL import *
from OpenGL.GLU import *
from src.line_sequence import LineSequence



verticies, edges = get_stored_values()


def Figure(verticies, edges):
    if len(edges) == 0 or len(verticies) == 0:
        return

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def StaticFigure():

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    



def main():
    pygame.init()
    display = (800,600)
    win = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]),
0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    line_sequence = LineSequence(800, 600)

    new_sequence = True

    pygame.font.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            leftclick, middleclick, rightclick = pygame.mouse.get_pressed()

            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                vertex, lines = line_sequence.get_vals() 
                
                if(len(vertex) > 1 and len(lines) > 0):

                    salvando = pygame.font.SysFont('timesnewroman', 30).render("Salvando", False, (255, 255, 255))

                    win.blit(salvando,( 0, 0))

                    set_stored_values(vertex, lines)

                    sleep(1)



            if event.type == pygame.MOUSEBUTTONDOWN and rightclick:
                new_sequence = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN and leftclick:
                line_sequence.add(list(pygame.mouse.get_pos()), new_sequence )
                new_sequence = False

        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        vertex, lines = line_sequence.get_vals() 
        
        print(vertex, lines)
        # StaticFigure()
        Figure(vertex, lines)
        pygame.display.flip()
        pygame.time.wait(10)


main()



def main():
    pass

if __name__ == '__main__':
    main()