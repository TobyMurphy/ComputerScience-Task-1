from curses import window
from curses.textpad import Textbox
from distutils.log import WARN
from tkinter import *
counter = 0
valuesall =[]
counter2 = 0 
print("HELP MODE: IN CASE THAT IT DOES NOT OPEN OR YOU REQUIRE HELP PLEASE LOOK BELOW \n SIMPLY ENTER THE NAME, DETAILS AND DATA FOR EACH TEAM YOU WISH TO ADD. \n AFTER YOU HAVE DONE THIS, YOU CAN PRESS THE 'ADD TEAM' BUTTON WITHIN. AFTER ADDING MULTIPLE TEAMS, TO SUIT YOUR NEEDS PRESS THE 'FINISH' BUTTON AND THE PROGRAM WILL PRINT A TABLE.")


def mainmode():

        #The click funtion
        def click():
                global values
                global valuessorted
                global counter
                Tn = TeamName.get() #Grabs the team name
                TnU=Tn.upper()
                Abriv = TnU[0]+TnU[-1]##Creates the abbrivation

                W = GamesWon.get() #Obtains more values that are needed for the table.
                D = GamesDraw.get()
                Score = GoalScore.get()
                Concede = GoalConc.get()
                GP = GamesPlay.get()

                VicRoy=int(W)#Converting 
                AntiVicRoy=int(D)
                Attempts=int(GP)
                S=int(Score)
                C=int(Concede)

                points = VicRoy*3 + AntiVicRoy

                GD = S-C
                L = Attempts-VicRoy-AntiVicRoy

                values = [Abriv, W, D, S, C, GD, points, L, counter] #Creating Lists.

                valuesall.append(values)
                valuessorted = sorted(valuesall, key=lambda x: x[6], reverse=True)

                TeamName.delete(0, END)
                GamesPlay.delete(0, END)
                GamesDraw.delete(0, END)
                GamesWon.delete(0, END)
                GoalConc.delete(0, END)
                GoalScore.delete(0, END)

                counter=counter+1
        ################################################################################ SELECTED AREA OF REPORT FOR PSUEDO CODE
        def finished():
                global counter2
                placemaker = 3
                
                Label (window, text="Name", font="none 12 bold"  ) .grid (row = 1, column = 1,)
                Label (window, text="Points", font="none 12 bold"  ) .grid (row = 1, column = 2,)    
                Label (window, text="Won", font="none 12 bold"  ) .grid (row = 1, column = 3,)  #Prints the headers of the columns for the table 
                Label (window, text="Draw", font="none 12 bold"  ) .grid (row = 1, column = 4,)
                Label (window, text="GD", font="none 12 bold"  ) .grid (row = 1, column = 5,)
                Label (window, text="-"*40, font="none 12 bold"  ) .grid (row = 2, column=1, columnspan= 10)
                
                while counter > counter2:
                        Label (text=valuessorted[counter2][0]).grid(row = placemaker, column = 1,) #Prints the names and the data of the table
                        Label (text=valuessorted[counter2][6]).grid(row = placemaker, column = 2,)
                        Label (text=valuessorted[counter2][1]).grid(row = placemaker, column = 3,)
                        Label (text=valuessorted[counter2][2]).grid(row = placemaker, column = 4,)
                        Label (text=valuessorted[counter2][5]).grid(row = placemaker, column = 5,)
                        counter2=counter2+1
                        placemaker=placemaker+1

        ####################################################################################
                

        
        global TeamName
        global GamesDraw
        global GamesPlay
        global GamesWon
        global GoalConc
        global GoalScore

        window = Tk() #Creates a window and gives it a name.
        window.title("Ladder Maker")
        Label (window, text="Welcome to the Window Maker!"  ) .grid (row = 0, column = 0, sticky = W)
        Label (window, text="Enter the Details of the first team you wish to add below:", font="none 12 bold"  ) .grid (row = 1, column = 0, sticky = W)

        #The below code will obtain the values require for creating a leauge table.
        Label (window, text="Team Name:", font="none 12 bold"  ) .grid (row = 2, column = 0, sticky = W)
        TeamName = Entry(window, width =20)
        TeamName.grid (row=2, column = 0, sticky=E)

        Label (window, text="Games Played:", font="none 12 bold"  ) .grid (row = 3, column = 0, sticky = W)
        GamesPlay = Entry(window, width =20)
        GamesPlay.grid (row=3, column = 0, sticky=E)


        Label (window, text="Games Won:", font="none 12 bold"  ) .grid (row = 4, column = 0, sticky = W)
        GamesWon = Entry(window, width =20)
        GamesWon.grid (row=4, column = 0, sticky=E)

        Label (window, text="Games Drawn:", font="none 12 bold"  ) .grid (row = 5, column = 0, sticky = W)
        GamesDraw = Entry(window, width =20)
        GamesDraw.grid (row=5, column = 0, sticky=E)

        Label (window, text="Goals Scored:", font="none 12 bold"  ) .grid (row = 6, column = 0, sticky = W)
        GoalScore = Entry(window, width =20)
        GoalScore.grid (row=6, column = 0, sticky=E)

        Label (window, text="Goals Conceded:", font="none 12 bold"  ) .grid (row = 7, column = 0, sticky = W)
        GoalConc = Entry(window, width =20)
        GoalConc.grid (row=7, column = 0, sticky=E)

        #Buttons for the program 
        Button(window, text="ADD TEAM", width=6, command=click) .grid(row=10, column=0, sticky=W)
        Button(window, text="PRINT TABLE", width=6, command=finished) .grid(row = 10, column=0, sticky=E)


        ##Main body of code

        window.mainloop()

mainmode()

def killer():
        global killswitch
        killswitch=int(input("Press 1 to exit the program"))
killer()
if killswitch == 1:
        exit()
else:
        killer()