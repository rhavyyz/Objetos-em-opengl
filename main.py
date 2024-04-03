import pygame
from pygame.locals import *
from src.storage_funcs import get_stored_values, set_stored_values, get_n_on_storage

from OpenGL.GL import *
from OpenGL.GLU import *
from src.line_sequence import LineSequence



verticies, edges = get_stored_values("data")


def Figure(verticies, edges):
    if len(edges) == 0 or len(verticies) == 0:
        return

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            # print("\n\n\n", vertex,"\n\n" ,edge, verticies)
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
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

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

            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                line_sequence = LineSequence(800, 600)
            elif event.type == pygame.KEYDOWN and event.key == K_z:
                line_sequence.remove_last()


            leftclick, middleclick, rightclick = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN and middleclick:
                vertex, lines = line_sequence.get_vals() 
                if(len(vertex) > 1 and len(lines) > 0):
                    set_stored_values(vertex, lines, str(get_n_on_storage()))

                    line_sequence = LineSequence(800, 600)


            elif event.type == pygame.MOUSEBUTTONDOWN and rightclick:
                new_sequence = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN and leftclick:
                line_sequence.add(list(pygame.mouse.get_pos()), new_sequence )
                new_sequence = False

        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        vertex, lines = line_sequence.get_vals() 
        
        # print(vertex, lines)
        # StaticFigure()
        Figure(vertex, lines)
        pygame.display.flip()
        pygame.time.wait(10)


main()



def main():
    pass

if __name__ == '__main__':
    main()