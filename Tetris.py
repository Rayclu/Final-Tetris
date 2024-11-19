import html
import gamelib 
import tetrisC 
import dibujar
import persistencia
ESPERAR_DESCENDER = 20

screen=gamelib.resize(450, 500)



def pause(juego : list , end : bool):
    input=gamelib.input("Press 'q' to quit the game, 'r' to reset or 'p' to go back the game")
    if input=='r':
               paused=False
               end= False
               return main(), end
    elif input=='p':
               paused=False
               end= False
               return juego
    elif input=='q':
               
               end = True
               return juego, end
    """paused=True
    
    gamelib.draw_text("Press 'q' to quit game,\n 'r' to reset or \n'p' to go back the game", 10, 300, fill="Cyan", anchor='nw')
   
    while paused:
        for event in gamelib.get_events():
        #Cerrar el juego:
            if event.type == gamelib.EventType.KeyPress and event.key=='q':
               
               return juego, end==True
        #Reiniciar el juego:
            if event.type==gamelib.EventType.KeyPress and event.key=='r':
                
                return main()
        #Volver de la pausa
            if event.type==gamelib.EventType.KeyPress and event.key=='p':
                paused=False          
                return juego"""

def retry()->bool:
    paused=True
    input = gamelib.input("Press 'q' to quit the game or 'r' to retry")


    for event in gamelib.get_events():
        if input=='r':
            paused=False
            end= False
            return main(), end

        elif input=='q':
            paused=False
            end = True
            return end
        elif event.type == gamelib.EventType.KeyPress and event.key=='q':
            return
        elif event.type == gamelib.EventType.KeyPress and event.key=='r':
            return main()

def main(): 
    # Inicializar el estado del juego
    juego = tetrisC.crear_juego(pieza_inicial=tetrisC.generar_pieza())
    pieza_sig = tetrisC.generar_pieza()
    cambiar_pieza = False 
    timer = 0
    pts=juego[2]
    
    #--------------------------------------------------
    ranking = persistencia.ChargeScore()
    rank = []
    #----------------------------------------------------------------------------------------------
    end = False #bandera
    #-----------------------------------------------------------------------------------
#Union de las funciones del juego:    
    

    while gamelib.loop(200) and end!=True:
        
        # Dibujar la pantalla con el estado del juego
        gamelib.draw_begin()
        
        gamelib.draw_image("background_resized.gif",-40,-70)
        #gamelib.draw_text(pts, 10, 10, fill="Cyan", anchor='nw')        
        dibujar.drawPTS(juego)
        dibujar.DrawGrill(juego)
        dibujar.pieza(tetrisC.pieza_actual(juego))
        dibujar.prx_pieza(pieza_sig)
        gamelib.draw_text("Press:\n \t-'a' to turn left.\n\t-'d' to right\n\t-'s' to down piece", 10, 400, fill="Black", anchor='nw')
        gamelib.draw_end()
       
        #Pausar:

        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress and event.key == 'p':
                juego = pause(juego, end)
                if end==True:
                    return
 # Actualizar el estado del juego segun corresponda:

        #Izuierda:

            if event.type == gamelib.EventType.KeyPress and event.key=='q':
                 return end==True
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'a':
                juego = tetrisC.mover(juego, tetrisC.IZQUIERDA)
        #Derecha:
            if event.type == gamelib.EventType.KeyPress and event.key == 'd':
                juego = tetrisC.mover(juego, tetrisC.DERECHA)
        #Empujar pieza hacia abajo:
            if event.type == gamelib.EventType.KeyPress and event.key == 's':
                juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
                pts+=15
                
                if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()
        #Rotación:
            if event.type == gamelib.EventType.KeyPress and event.key == 'w':
                juego = (juego[0], tetrisC.RotPiece(juego), pts)

        # Descenso de la pieza automatica
        timer += 1
        if timer == ESPERAR_DESCENDER:
            juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
            
            if cambiar_pieza:
                pts=juego[2]
            timer = 0
            

        if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()


        if tetrisC.terminado(juego):
           
            gamelib.draw_text(f"The final points are: {pts}", 10, 10, fill="Cyan", anchor='nw') 
            persistencia.saveScore(ranking, pts)
        
            return retry()
        
        


gamelib.init(main)







































































































"""

espera=20
#screen = pygame.display.set_mode((1280, 720))


def main():  
    #inicializa el estado del juego
    # 
    #  
    gamelib.resize(180,360)

    juego = tetrisCC.crear_juego(tetrisC.generar_pieza())
    pieza_sig=tetrisC.generar_pieza()
    change=False
    tick=0

    while gamelib.loop(60):
      #dibujar pantalla con estado del juego
        
        gamelib.draw_begin()
        
        
        dibujar.DrawGrill(ANCHO=tetrisC.ANCHO_JUEGO, ALTO=tetrisC.ALTO_JUEGO, TAMAÑO=dibujar.TAMAÑO)
        
        dibujar.pieza(tetrisC.pieza_actual(juego), 20, 400)
        
        gamelib.draw_end()

        for event in gamelib.get_events():
#            if event.type==gamelib.EventType.KeyPress and:
        
            if event.type == gamelib.EventType.KeyPress and event.key == 'q':
            
                return   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'a':
            
                juego=tetrisC.mover(juego, tetrisC.IZQUIERDA)   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'd':
            
                juego=tetrisC.mover(juego, tetrisC.DERECHA)   
            
            if event.type == gamelib.EventType.KeyPress and event.key == 's':
            
                juego, change=tetrisC.avanzar(juego, pieza_sig)


            #Descenso de la pieza automatica
        tick+=1
        if tick == espera:
            tetrisC.avanzar(juego, pieza_sig)
            tick=0
        if change:  
    
            pieza_sig=tetrisC.generar_pieza()

gamelib.init(main)"""
"""
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


dimensiones=list(pygame.display.get_window_size())


x_org=dimensiones[0]//3
y_org=dimensiones[1]//3
"""
"""
print(f"Origen x: {x_org}")


print(f"Origen y: {y_org}")
running=True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")
""""""
def main():
    gamelib.resize(300, 300)

    while gamelib.loop(fps=1):
        for event in gamelib.get_events():
            if event.type==gamelib.EventType.KeyPress and event.key=="q":
                juego=tetrisC.mover(juego)
            
        pieza_cubo=tetrisC.generar_pieza()

        gamelib.draw_begin()

        dibujar.dibujar_pieza(pieza_cubo)

        gamelib.draw_end()

gamelib.init(main)"""


#def main():
#    x_org=
#    y_org=


 
#gamelib.init(draw_grill(ANCHO,ALTO, TAMAÑO))
