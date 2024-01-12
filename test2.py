from core.base import Base
from core.openGLUtils import OpenGLUTils
from OpenGL.GL import *

class Test(Base):
    def initialize(self):
        print("initializing program....")
        print("loading....")
        OpenGLUTils.printSystemInfo()
        ##inicialize program ##
        #vertex shader code
        #GLSL shading language
        vsCode="""
void main()
{
    gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
}

        """

        #fragment shader code
        fsCode="""
out vec4 fragColor; 
void main() 
{
    fragColor = vec4(1.0, 1.0, 0.0, 1.0); 
}
"""
        self.programRef = OpenGLUTils.initializeProgram(
            vsCode,fsCode
        )
        ###set up vertex array object###
        vaoRef=glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ###render settings (optional)###
        #set point width and height
        glPointSize(10)
        self.update()

    def update(self):
        print("huh")
        glUseProgram( self.programRef )
        glDrawArrays( GL_POINTS, 0, 1 )
Test().run()        
