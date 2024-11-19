import gamelib
import tetrisC

"""
X_ORIGEN = 0
Y_ORIGEN = 0
tamaño = 20
ANCHO=tetrisCC.ANCHO_JUEGO
ALTO=tetrisCC.ALTO_JUEGO
"""

X_ORIGEN = 110
Y_ORIGEN = 20
TAMAÑO = 15

def pieza(pieza, x = 0, y = 0):
    
    for x, y in pieza:
        gamelib.draw_rectangle(10+X_ORIGEN + x * TAMAÑO,#EJE X 
                               10+Y_ORIGEN + y * TAMAÑO#EJE Y 
                            , 10+X_ORIGEN + x * TAMAÑO + TAMAÑO, #X
                              10+Y_ORIGEN + y * TAMAÑO + TAMAÑO,#Y
                                fill = "red")
def prx_pieza(pieza_sig, x=0, y=0):
    X_ORIGEN_t= X_ORIGEN-30
    Y_ORIGEN_t=Y_ORIGEN+100

    gamelib.draw_text("Next piece:", X_ORIGEN_t-80, Y_ORIGEN_t-50, fill="purple", anchor='nw')
    for x, y in pieza_sig:
        gamelib.draw_rectangle(X_ORIGEN_t-x*TAMAÑO#X
                               , Y_ORIGEN_t+y*TAMAÑO#Y
                               ,X_ORIGEN_t-x*TAMAÑO+TAMAÑO#X
                               ,Y_ORIGEN_t+y*TAMAÑO+TAMAÑO#Y
                               , fill="purple"
                               )


def DrawGrill(juego):

    for y in range(tetrisC.ALTO_JUEGO):
        for x in range(tetrisC.ANCHO_JUEGO):
            # Dibujar la cuadrícula como fondo
            gamelib.draw_rectangle( X_ORIGEN + x * TAMAÑO+10, Y_ORIGEN + y * TAMAÑO+10#punto origen
                                  ,X_ORIGEN + (x + 1) * TAMAÑO+10, Y_ORIGEN + (y + 1) * TAMAÑO+10 #punto final
                                  ,outline="gray", fil="black")

    """
    for i in range (tetrisC.ANCHO_JUEGO):
        gamelib.draw_line(X_ORIGEN + i * TAMAÑO, Y_ORIGEN
                          , X_ORIGEN + i * TAMAÑO, Y_ORIGEN + TAMAÑO * tetrisC.ALTO_JUEGO)
       
    for i in range (tetrisC.ALTO_JUEGO):
        gamelib.draw_line(X_ORIGEN, Y_ORIGEN + i * TAMAÑO
                          , X_ORIGEN + TAMAÑO * tetrisC.ANCHO_JUEGO, Y_ORIGEN + i * TAMAÑO)

"""    
    for y in range(len(juego[0])):
        for x in range(len(juego[0][y])):
            if tetrisC.hay_superficie(juego, x, y):
                gamelib.draw_rectangle(10+X_ORIGEN + x * TAMAÑO, 10+Y_ORIGEN + y * TAMAÑO
                            ,10+X_ORIGEN + x * TAMAÑO + TAMAÑO,10+Y_ORIGEN + y * TAMAÑO + TAMAÑO, fill = "gray")

def drawPTS(juego):
    """    
    Verifica si las linas completadas conforman un combo para determinar 
    una cantidad de puntos que luego se añadira al contador final.

    Entrada: 
        Eliminar_pieza(juego)
    Desarrollo:
        #1 linea==100
        #2 lineas==300
        #3 lineas==500
        #4 lineas>==1000
    Retorna:
        Puntos a sumar en el contador
     """
    gamelib.draw_text(juego[2], 400, 20, fill="red", anchor='nw')
    #gamelib text format:text, x, y, font=None, size=12, bold=False, italic=False, **options
    
#    gamelib.draw_text(juego[2],tetrisC.ANCHO_JUEGO,
 #                      Y_ORIGEN, font=None, bold=False, italic=True)

    
def CountPTS():

    """
    Verifica si las linas completadas conforman un combo para determinar 
    una cantidad de puntos que luego se añadira al contador final.

    Entrada: 
        Eliminar_pieza(juego)
    Desarrollo:
        #1 linea==100
        #2 lineas==300
        #3 lineas==500
        #4 lineas>==1000
    Retorna:
        Puntos a sumar en el contador 
    """
    """
    pts=0

    while 
    
    """
    pass
    
"""
def dibujar_pieza(pieza, x=0, y=0):
    
    for x, y in pieza:
        gamelib.draw_rectangle(X_ORIGEN-tamaño + x * tamaño, Y_ORIGEN + y * tamaño, X_ORIGEN-tamaño + x * tamaño + tamaño, Y_ORIGEN + y * tamaño + tamaño, fill = "red")

"""