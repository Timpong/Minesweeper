from random import randint
from tkinter import *
from functools import partial
fönster =Tk()
fönster.title('Minröjning')
fönster['bg']='white'
fönster.geometry("600x400+400+50")
knappar = []

def välkomstGIU():
    fönster =Tk()
    fönster.title('Minröjning')
    fönster['bg']='white'
    fönster.geometry("600x400+400+50")
    textVälkommen = Label(fönster, text = 'Välkommen!', width= '22', font= ('Courirer', '40', 'bold'))
    textVälkommen.grid(row = 0, column = 0)
    Label(fönster, text = 'Detta är Tims version av Minesweeper',  height='2', font= ('Courirer', '28')).grid(row= 1, column = 0)
    Button(fönster, text = 'Tyck för att komma igång', height = '7', command = måttangivelseGIU).grid(row = 2, column = 0)
    Label(fönster, text = 'Enjoy :)', height = '3', font= ('Courirer', '28', 'italic')).grid( row = 3, column = 0)  
    
    return (fönster, textVälkommen)

    
def måttangivelseGIU():
    textVälkommen.destroy()
    Label(fönster, text = 'Välkommen',          anchor = W, fg = 'blue'     ).grid( row = 0 , column = 0)
    Label(fönster, text = 'Ange egna mått:',    anchor = W, bg = 'lightgrey').grid( row = 1 , column = 0)
    Label(fönster, text = 'Ange Rader       :', anchor = W, bg = 'lightgrey').grid( row = 2 , column = 0)
    Label(fönster, text = 'Ange Kolumner :',    anchor = W, bg = 'lightgrey').grid( row = 3 , column = 0)
    Label(fönster, text = 'Ange Minor       :', anchor = W, bg = 'lightgrey').grid( row = 4 , column = 0)
    

def minfältet (rader, kolumner, minor):
    minfält = [ [0 for i in range(kolumner)] for j in range (rader)]                            #skapar ett minfält med 

    for mina in minor:
        (x, y) = mina
        minfält[x][y] = 'X'                                                                     #ger minans koordinat värdet X i minfältet
    
        # närliggande celler (nl)
        nl_rader    = range(x - 1, x + 2)                                                           # från rutan till vänster(x-1) till rutan till höger (x+1) då range inte har med (x+2)
        nl_kolumner = range(y - 1, y + 2)

        for i in nl_rader:                                                                      # jobbar igenom minorna och söker av de närligggande raderna och kolumnerna
            for j in nl_kolumner:
                if 0 <= i < rader and 0 <= j < kolumner and minfält[i][j] != 'X':               # alla celler/rutor måste vara i minfältet och inte vara en mina
                    minfält[i][j] += 1                                                          # adderar närliggande bomber med 1
    return(minfält)       

def angivna_värden():
    print('Hur stort ska minfältet vara? ')
    while True:
        try:
            kolumner = int(input('Ange bredd: '))
            if not 0 < kolumner:
                print('Antal kolumner måste vara fler än 0.')
                #kolumner = int(input('Ange bredd: '))
            elif not kolumner <= 40:
                print('Antal kolumner får inte överstiga 64.')
                #kolumner = int(input('Ange bredd: '))
            else:
                break
        except ValueError:
            print('Går endast att ange positiva heltal upp till och med 64. \n')

    while True:
        try:
            rader = int(input('Ange höjd: '))
            if not 0 < kolumner:
                print('Antal rader måste vara fler än 0.')
            elif not kolumner <= 40:
                print('Antal rader får inte överstiga 64.')
            else:
                break
        except ValueError:
            print('Går endast att ange positiva heltal upp till och med 64. \n')
    
    return (rader, kolumner)

def placeraMinor(rader,kolumner):
    minor= []
    while True:
        try:
            antalMinor = int(input('Antal minor: '))
            if antalMinor <= (rader*kolumner) and antalMinor >= 1:                          #begränsar antal minor
                for i in range (antalMinor):
                    koordinat_mina = [ randint(0,rader-1) , randint(0,kolumner-1)]
                    while koordinat_mina in minor:                                          #ser till så att flera minor inte får samma koordinater                               
                        koordinat_mina = [ randint(0,rader-1) , randint(0,kolumner-1)]
                    minor.append(koordinat_mina)
                break
            else:
                print('Accepteras Ej. Antalet minor får inte överstiga antalet rutor i fältet eller vara mindre än 1 \n')
        except ValueError:                                                                  # Om man anger annat än heltal
            print('Går endast att ange positivt heltal. \n')
    return(minor)

def skapa_knappar (rader, kolumner):
    knappar = []
    visad_knapp = []
    knappar = [[Button(fönster,width= '2', height='1', fg= 'darkgrey', bg='grey') for i in range(kolumner)] for j in range (rader)]
    visad_knapp = [[0 for i in range(kolumner)] for j in range (rader)]
    return(knappar,visad_knapp)

def press_knapp(x,y):                   #ha den i separat fil???
    if minfält[x][y] == 0:          
        for a in range(-1,2):
            for b in range(-1,2):
                if (0 <= x+a < rader) and (0 <= y+b < kolumner) and (x+a,y+b)!=(x,y) and visad_knapp[x+a][y+b] != 1:
                    visad_knapp[x][y]= 1 
                    press_knapp(x+a,y+b)
    if minfält[x][y] == 1:
        knappar[x][y].configure(text = '1', fg= 'darkblue', bg='grey')
    if minfält[x][y] == 2:
        knappar[x][y].configure(text = '2', fg= 'lightgreen')
    if minfält[x][y] == 3:
        knappar[x][y].configure(text = '3', fg= 'red')
    if minfält[x][y] == 4:
        knappar[x][y].configure(text = '4', fg= 'purple')
    if minfält[x][y] == 5:
        knappar[x][y].configure(text = '5', fg= 'brown')
    if minfält[x][y] == 6:
        knappar[x][y].configure(text = '6', fg= 'lightblue')
    if minfält[x][y] == 7:
        knappar[x][y].configure(text = '7', fg= 'black')
    if minfält[x][y] == 8:
        knappar[x][y].configure(text = '8', fg= 'lightgrey')
    if minfält[x][y] == 'X':
        knappar[x][y].configure(text = '*', bg='black')
    visad_knapp[x][y]= 1

def placera_knapp(rader,kolumner):
    for x in range(rader):
        for y in range(kolumner):
            trycka = partial(press_knapp, x, y)
            knappar[x][y] = Button(fönster, width= '3', height ='2', command = trycka, bg='black',)
            knappar[x][y].grid(row = x, column = y)
    
    return (knappar)

#fönster,textVälkommen=välkomstGIU()
(rader, kolumner)=angivna_värden()


minfält = minfältet(rader, kolumner,placeraMinor(rader, kolumner) )
(knappar,visad_knapp) = skapa_knappar(rader,kolumner)
placera_knapp(rader,kolumner)


