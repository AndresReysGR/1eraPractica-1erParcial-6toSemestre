from OpenGL.GL import *
from glew_wish import *
import glfw
import random

def main():
    if not glfw.init():
        return

    #CREA LA VENTANA
    #INDEPENDIENTEMENTE DEL SO QUE USEMOS
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #CONFIGURAMOS OPENGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #VALIDAMOS QUE SE CREE LA CENTANA
    if not window:
        glfw.terminate()
        return
    #ESTABLECEMOS EL CONTEXTO
    glfw.make_context_current(window)

    #ACTIVAMOS LA VALIDACION DE FUNCIONES MODERNAS DE OPENGL
    glewExperimental = True
    
    #INICIALIZAR GLEW
    if glewInit() != GLEW_OK:
        print("NO SE PUDO INCIALIZAR GLEW")
        return
    #OBTENEMOS VERSIONES DE OPENGL Y SHADERS
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #ESABLECER COLOR DE DIBUJO
        glViewport(0,0,800,600)
        #eSTABLECER COLOR DE BORRADO

        a = random.random() 
        b = random.random()  
        c = random.random()  
        d = random.random()         

        glClearColor(a, b, c, d)
        #BORRAR EL CONTENIDO DE LA VENTANA
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #DIBUJAR

        #PREGUNTAR SI HUBO ENTRADAS DE PERIFERICOS
        #(TECLADO, MAUSE, GAMEPAD, ETC.)
        glfw.poll_events()
        #INTERCAMBIA LOS BUFFERS
        glfw.swap_buffers(window)
    #SE DESTRUYE LA VENTANA PARA LIBERAR MEMORIA
    glfw.destroy_window(window)
    #TERMINA LOS PROCESOS DE INICIO GLFW.INIT
    glfw.terminate()

if __name__ == "__main__":
    main()