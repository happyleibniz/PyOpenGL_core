from core.base import Base
from core.openGLUtils import OpenGLUTils
from core.attribute import Attribute
from OpenGL.GL import *

class Test(Base):
    def initialize(self):
        print("inicializing..")
        for i in range(len([1,1,4,5,1,4])):
            print("<!>OpenGL.SECURITY.ERROR")
        vsCode="""
in vec3 position;
void main()
{
    gl_Position = vec4(
        position.x,position.y,position.z,1.0);

}
"""
        fsCode="""
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0,1.0,0.0,1.0);
}
"""
        self.programRef=OpenGLUTils.initializeProgram(vsCode,fsCode)
        glLineWidth(4)
        vaoRef=glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        positionData=[[0.8,0.0,0.0],[0.4,0.6,0.0],
                      [-0.4,0.6,0.0],[-0.8,0.0,0.0],
                      [-0.4,-0.6,0.0],[0.4,-0.6,0.0]]
        self.vertexCount = len(positionData)
        positionAttribute=Attribute("vec3",
                                    positionData)
        positionAttribute.associateVariable(self.programRef,"position")
        self.update()
    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_LINE_LOOP,0,self.vertexCount)

Test().run()