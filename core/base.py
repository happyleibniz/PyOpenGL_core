import pygame,sys
from core.input import Input
class Base(object):

    def __init__(self,screenSize=[512,512]) -> None:
        pygame.init()
        display_flags=pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLEBUFFERS,
            4
        )
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLESAMPLES,
            4
        )
        #using a core
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE
        )
        #create a window
        self.screen = pygame.display.set_mode(screenSize,
                                              display_flags)
        #set the text that appears on the title bar
        pygame.display.set_caption("A window")
        
        self.running=True

        self.clock=pygame.time.Clock()

        self.input=Input()
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        ##startup##
        self.initialize()

        while self.running:
            #process input

            self.input.update()

            
            if self.input.quit:
                self.running=False

            pygame.display.flip()

            self.clock.tick(60)#float("inf")

        pygame.quit()
        sys.exit()