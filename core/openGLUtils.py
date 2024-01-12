from OpenGL.GL import *
class ShaderError(Exception):
    error=error
class ProgramError(Exception):
   pass
class OpenGLUTils(object):
    @staticmethod
    def initializeShader(shaderCode,shaderType):
        shaderCode='#version 330\n'+shaderCode

        shaderRef=glCreateShader(shaderType)
        glShaderSource(shaderRef,shaderCode)
        glCompileShader(shaderRef)

        compileSucess=glGetShaderiv(shaderRef,
                                    GL_COMPILE_STATUS)
        if not compileSucess:
            errorMessage=glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)

            errorMessage = "\n" +errorMessage.decode("utf-8")

            raise ShaderError(errorMessage)
        return shaderRef
    @staticmethod
    def initializeProgram(vertexShaderCode,
                          fragmentShaderCode):
        vertexShaderRef = OpenGLUTils.initializeShader(
            vertexShaderCode,GL_VERTEX_SHADER
        )
        fragmentShaderRef=OpenGLUTils.initializeShader(
            fragmentShaderCode,GL_FRAGMENT_SHADER
        )

        programRef = glCreateProgram()

        glAttachShader(programRef,vertexShaderRef)
        glAttachShader(programRef,fragmentShaderRef)

        glLinkProgram(programRef)

        linkSuccess = glGetProgramiv(programRef,GL_LINK_STATUS)
        if not linkSuccess:
            errormessage=glGetProgramInfoLog(programRef)
            glDeleteProgram(programRef)
            errormessage = "\n" + errormessage.decode("utf-8")
            raise ProgramError(errormessage)
        return programRef
    @staticmethod
    def printSystemInfo():
        print("Vendor: "+glGetString(GL_VENDOR).decode("utf-8"))
        print("Renderer: "+glGetString(GL_RENDERER).decode("utf-8"))
        print("OpenGL Version Supported: "+glGetString(GL_VERSION).decode("utf-8"))
        print("GLSL Version supported: "+ glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8"))
        