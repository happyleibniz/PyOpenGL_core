from core.base import Base#importing base
from core.openGLUtils import OpenGLUTils#importing openglutilities
from core.attribute import Attribute #importing attribues
from OpenGL.GL import * #importing all the opengl

class Test(Base):
    def initialize(self):
        print("initializing programs...")
        vsCode="""
in vec3 position;//{note}This is an input variable representing the position of the vertex in 3D space.
in vec3 vertexColor;//{note}This is an input variable representing the color of the vertex.
out vec3 color;//{note}This is an output variable representing the color that will be passed to the next stage of the rendering pipeline.
void main()//{note}The main() function is the entry point for the shader. Inside the main() function, the following operations are performed:
{
    gl_Position = vec4(position.x, position.y, position.z, 1.0);//{note}This line sets the position of the vertex in homogeneous coordinates. It creates a vec4 representing the position of the vertex, with the fourth component set to 1.0 (which is the homogeneous coordinate required for 3D vertices).
    color = vertexColor; //{note}This line assigns the input vertex color to the output variable color.
}
"""
        fsCode="""
in vec3 color;
out vec4 fragColor;
void main()
{
    fragColor = vec4(color.r,color.g,color.b,1.0);
}
//{note}in vec3 color;: This is an input variable representing the color passed from the vertex shader to the fragment shader.

//{note}out vec4 fragColor;: This is an output variable representing the final color of the fragment that will be displayed on the screen.

//{note}void main() { ... }: This is the main function of the fragment shader, where the actual shader logic is implemented.

//{note}Inside the main() function, the following operation is performed:

//{note}fragColor = vec4(color.r, color.g, color.b, 1.0);: This line constructs a vec4 representing the color of the fragment, using the individual components of the input color vec3 and setting the alpha component to 1.0.
//{note}So, this fragment shader takes the input color, constructs a vec4 color with an alpha value of 1.0, and assigns it to the output variable fragColor. This means that the final color of each fragment will be the same as the input color, with full opacity.

//{note}This code is compatible with OpenGL version 3.5.

"""
        self.programRef = OpenGLUTils.initializeProgram(vsCode,fsCode)
        ##render settings##
        glPointSize(10)
        glLineWidth(4)

        ##setup vertex array oject -trangle ##
        self.vaoRef =glGenVertexArrays(1)#OpenGL generate vertex arrays
        glBindVertexArray(self.vaoRef)#Opengl binding vertex array
        positionData = [ [0.8, 0.0, 0.0], 
                        [0.4, 0.6, 0.0], 
                        [-0.4, 0.6, 0.0], 
                        [-0.8, 0.0, 0.0], 
                        [-0.4, -0.6, 0.0], 
                        [0.4, -0.6, 0.0] ]
        self.vertexCount = len(positionData)
        positionAttriube= Attribute("vec3",
                                        positionData)
        positionAttriube.associateVariable(self.programRef,"position")
        colorData=[[1.0,0.0,0.0],
                   [1.0,.05,0.0],
                   [1.0,1.0,0.0],
                   [0.0,1.0,0.0],
                   [0.0,0.0,1.0],
                   [0.5,0.0,1.0]]
        colorAttribute = Attribute("vec3", colorData) 
        colorAttribute.associateVariable( self.programRef, "vertexColor" )
        self.update()
    def update(self):
        glUseProgram( self.programRef ) 
        glDrawArrays( GL_POINTS, 0, self.vertexCount )
Test().run()