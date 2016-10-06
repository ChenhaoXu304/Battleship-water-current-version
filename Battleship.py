#Name: Chenhao Xu
#Program: Battleship: water current version

import layout


filename=input("Enter an existing Battleship file, or 'none': ")
#If no save file is read, make an empty board
if filename=='none':
    board=[]
    for _ in range(layout.rows):
        col=[]
        for _a in range(layout.columns):
            col.append(layout.marker.water)
        board.append(col)
    #Putting the ships according to arrangements iin the layoutf file
    for co1,co2 in layout.ships:
        x1=co1[0]
        y1=co1[1]
        x2=co2[0]
        y2=co2[1]
        if y1==y2:
            if x1<=x2:
                for i in range(x1,x2+1):
                    board[i][y1]=layout.marker.ship
            else:
                for i in range(x2,x1+1):
                    board[i][y1]=layout.marker.ship
        #Case 2: same y coordinate
        elif x1==x2:
            row=board[x1]
            if y1<=y2:
                for i in range(y1,y2+1):
                    row[i]=layout.marker.ship
            else:
                for i in range(y2,y1+1):
                    row[i]=layout.marker.ship
    rows=layout.rows
    columns=layout.columns
    #if an existing filename is entered, read the save file
else:


    fp=open(filename)
    board=[]
            
    for line in fp:
        row=line.strip("\n")
        
        L=[]
        for i in row:
            L.append(i)
        board.append(L)
    
    fp.close()

    row=len(board)
    columns=len(board[0])




#Initialization
hits=0
misses=0
guesses=0
#Count ships for later use:
shipCount=0
for row in board:
    for marker in row:
        if marker==layout.marker.ship:
            shipCount+=1

#the game loop
#first take and transform user input

while True:
    user_input=input("Enter the guess, or quit to save and exit: ")
    if user_input=="quit":
        
        save=input("Do you want to save the board? If yes, press y; if no, press any button")
        save=(save=='y')
        if save:
            save_file=input("Type in the filename of your save file: ")
        break
    
    user_guess=list(map(int,user_input.split(',')))
    x=user_guess[0]
    y=user_guess[1]
    guesses+=1
    #Document hits and misses
    if board[x][y]==layout.marker.ship:
        board[x][y]=layout.marker.hit
        hits+=1
        shipCount-=1
        
    else:
        board[x][y]=layout.marker.miss
        misses+=1
    #Print the board and interactions
    for row in board:
        print(decor)
        row_display=''
        for marker in row:
            if marker==layout.marker.ship and layout.competition:
                row_display+=(layout.board.side+layout.marker.water)
            else:
                row_display+=(layout.board.side+marker)
        row_display+=layout.board.side
        print(row_display)
    print(decor)
    feedback="Hits: "+str(hits)+", Misses: "+str(misses)+", Guesses: "+str(guesses)
    print(feedback)
    #check if game's over; if it is, break out of the game
    if not shipCount:
        break
    movement=layout.current()
    
    row_m=movement[0]
    col_m=movement[1]
    replica=board[:]

    for r in range(layout.rows):
        
        board[r]=replica[(r-row_m)%layout.rows]
        
    for row in board:
        replica=row[:]
        for c in range(layout.columns):
            row[c]=replica[(c-col_m)%layout.columns]
if save:
    fp=open(save_file,"w")
    for row in board:
        s=""
        for char in row:
            s+=char
        fp.write(s+'\n')
    fp
    fp.close()

#Final feedback when game's over
if guesses>0:
    hit_rate=hits/guesses
    print("Final score:",hit_rate)



