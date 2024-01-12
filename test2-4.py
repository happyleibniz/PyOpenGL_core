from core.base import Base#importing base
from core.openGLUtils import OpenGLUTils#importing openglutilities
from core.attribute import Attribute #importing attribues
from OpenGL.GL import * #importing all the opengl

class Test(Base):
    def initialize(self):
        print("initializing programs...")
        vsCode="""
in vec3 position;
void main()
{
    gl_Position = vec4(position.x, position.y, position.z, 1.0);
    
}
"""
        fsCode="""
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0,1.0,0.0,1.0);
}
"""
        self.programRef = OpenGLUTils.initializeProgram(vsCode,fsCode)
        ##render settings##
        glLineWidth(4)

        ##setup vertex array oject -trangle ##
        self.vaoTri =glGenVertexArrays(1)#OpenGL generate vertex arrays
        glBindVertexArray(self.vaoTri)#Opengl binding vertex array
        positionDataTri=[[-0.5,0.8,0.0],
                         [-0.2,0.2,0.0],
                         [-0.8,0.2,0.0]]
        self.vertexCountTri = len(positionDataTri)
        positionAttriubeTri = Attribute("vec3",
                                        positionDataTri)
        positionAttriubeTri.associateVariable(self.programRef,"position")
        ##set up vertex array oject --sqare ###
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare=[[0.8,0.8,0.0],
                            [0.8,0.2,0.0],
                            [0.2,0.2,0.0],
                            [0.2,0.8,0.0]]
        self.vertexCountSquare = len(positionDataSquare)
        positionAttriubeSquare = Attribute("vec3",positionDataSquare)
        positionAttriubeSquare.associateVariable(self.programRef,"position")
        self.update()
    def update(self):
        #using the same program to render both shapes
        glUseProgram(self.programRef)

        #draw the triangle
        glBindVertexArray(self.vaoTri)
        #drawing arrays for the triangle
        glDrawArrays(GL_LINE_LOOP,0,self.vertexCountTri)
        #draw the square
        glBindVertexArray(self.vaoSquare)
        #drawing arrays for the square
        glDrawArrays(GL_LINE_LOOP,0,self.vertexCountSquare)
Test().run()