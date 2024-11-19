import sqlite3 as sq
import gamelib as gb
def ChargePiece():

    archivo = open("piezas.txt", 'r')
    piezas = []

    for linea in archivo:
        
        linea = linea.rstrip().split()
        for _ in range(2):
            linea.pop()

        for i in range(len(linea)):
            linea[i] = linea[i].split(';')
            
            for j in range(len(linea[i])):
                linea[i][j] = linea[i][j].split(',')
                linea[i][j] = (int(linea[i][j][0]), int(linea[i][j][1]))    
            
            linea[i].sort()
        #print("La linea que se agregará es:",linea)       
        piezas.append(linea)
    archivo.close()
    #print(f"---------------------------------------\n {piezas[0][0][0]}\n--------------------------------")
    return piezas

def saveScore(ranking:list,pts : int):
    #A modo de ejemplo, se indican los valores de score y name.
    #ranking = [(str(player1), int(1000)),(str(player2, int(1))),(...)]
            # player => Iterable for the var ranking
            #player (String(playerX), Integer(Rank))
            # 
            # New_Ranked_Player => suplent from player if player <= rank #
    rankeos=[ranking[i][1] for i in range(len(ranking))]
    print(len(ranking))
    if pts in range(min(rankeos), max(rankeos)):
        if len(ranking)==12:
            ranking.pop()
        nickname = gb.input("agree your name, congratulations, you are into the top ten🥳:")
        player=(f"{nickname}", pts)
        ranking.append(player)
        ranking=_order(ranking, cont=0)

        with open("points.csv", 'w') as file:
            for usrs in ranking:
                file.write(f"{usrs[0]}|{usrs[1]} \n")
    else:
        return gb.draw_text("You are noob 🫵🏼!", 50, 50, fill="Cyan", anchor='nw')
    
    """players=[]
        for player in range(len(ranking)):
            if ranking[player][1] <= rank or len(ranking)<12:
                nickname=gb.draw_text(gb.input("agree your name, congratulations, you are into the top ten🥳:"), 50, 50, fill="blue", anchor = 'nw' )
                player = (f"{nickname}|{rank}\n")
                players.append(player)
        
    for _ in players:
        with open("points.csv", 'a') as file:
            file.write(_)
        file.close()
    """
      



    """"database = sq.connect("Scores")
    cur = database.cursor()

    cur.execute("DROP TABLE IF EXISTS points")    
    cur.execute("CREATE TABLE points(nickname, rank)")

    cur.execute(f"INSERT INTO points(nickname, points) VALUES ({nickname}, {rank})")

    res = cur.execute("SELECT nickname FROM points WHERE rank != 0")
    res.fetchall()
    database.commit()
    database.close()"""

def _order(list: list, cont):
    if cont==2:
        return list
    for _ in range(2):
        for user in range(len(list)-1):
            #print("Jugador:",list[user])
            if list[user][1] <= list[user+1][1]:
                aux=list[user]
                list[user]=list[user+1]
                list[user+1]=aux
        
    print("-----------------------------")
    return _order(list, cont+1)

def ChargeScore() -> list:
    #[(score, name),
    #(score, name)]
    
    """
    Argumento=>Null
    ----------------
    cargar data del archivo csv.
    -----------------------------------
    lista de tuplas [(name, score), ...]
    """

    file = open("points.csv", "r")

#    points={}
    points=[]
    for line in file:
        ClearLine=line.rstrip(f"\n").split("|")
        ClearLine[1]=int(ClearLine[1])
        #points.update(ClearLine[1]:ClearLine[0])
        points.append(tuple(ClearLine))

    file.close()
    #print("El ranking está así: ",points)
    #print("__________________")
    points = _order(points, cont=0) 

    #print("El ranking quedó así: ",points)

    file = open("points.csv", 'w')
    for user in points:
            file.write(f"{user[0]}|{user[1]} \n")
    file.close()

    return points
    

"""
def main():
    saveScore(score=juego[2], name=input("Ingrese un nombre: "))
    print(ChargeScore())
main()"""

        
