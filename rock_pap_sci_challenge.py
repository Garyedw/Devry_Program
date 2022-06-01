# Purpose: Rock Paper Scissors Game
#
# Name: Garfield Edwards
#
# Start Date: 05/18/2022
# Completion Date: 05/29/2022
#
# See https://www.geeksforgeeks.org/python-random-module/ for details on random package used
# See https://www.geeksforgeeks.org/progressbar-widget-in-tkinter-python/ for details on Tkinter
#     https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
#     https://www.journaldev.com/48165/tkinter-working-with-classes
#
##############################################################################

import random
from tkinter import *
from tkinter import Tk
import tkinter.messagebox


# Initialize a Label to display the User Input


def display_text(root, title, geometry, message):
    global ilabel  # Made these labels global in an attempt to overwrite the results when player makes another selection
    global jlabel  # ^^
    global klabel  # ^^
    ilabel = Label(root)  # Initialized labels here
    ilabel.pack()
    jlabel = Label(root)  # ^^
    jlabel.pack()
    klabel = Label(root)  #
    klabel.pack()
    c = [1, 2, 3]  # Options list to be used to make Rock, Paper, Scissors choice

    #    root = Tk()  # Tkinter tag for window parameters
    root.title(title)  # GUI Tittle
    root.geometry(geometry)  # GUI SIze
    my_menu = Menu(root)  # GUI menu for future use, not used in this code
    #   config(root, menu=my_menu)
    slabel = Label(root, text=message,
                   font="Courier 22 bold")  # GUI Banner to appear permanently while loaded
    slabel.pack()
    label = Label(root, text="", font="Courier 22 bold")
    label.pack()

    submit = Button(root, text="Rock", font="Courier 14 bold",
                    command=lambda: c == resbutton(root, c[0]))  # Rock Scissors Selection buttons
    submit1 = Button(root, text="Paper", font="Courier 14 bold",
                     command=lambda: c == resbutton(root, c[1]))  # Paper Scissors Selection buttons
    submit2 = Button(root, text="Scissors", font="Courier 14 bold",
                     command=lambda: c == resbutton(root, c[2]))  # Scissors Selection buttons
    submit.pack(pady=20)
    submit1.pack(pady=20)
    submit2.pack(pady=20)
    delbutton = Button(root, text="Delete", font="Courier 14 bold",
                       command=lambda: c == delwidget())  # Delete button to delete previous results(Not quite working)
    delbutton.pack(pady=20)
    exit_button = Button(root, text="Exit", command=root.destroy)  # Exit program to exit the GUI
    exit_button.pack(pady=20)
    root.mainloop()
    return None


def resbutton(root, choice):
    global ilabel  # Made these labels global in an attempt to overwrite the results when player makes another selection
    global jlabel  # ^^
    global klabel  # ^^
    root.results = game_compare(choice)
    print(root.results)
    tkinter.messagebox.showinfo(title="Results", message=(root.results[0], root.results[1]))

    delwidget()
    ilabel = Label(root, text=root.results[0],
                   font="Courier 12 bold")  # Results message printed out to the GUI
    ilabel.pack()
    jlabel = Label(root, text=root.results[1],
                   font="Courier 12 bold")  # Results message printed out to the GUI
    jlabel.pack()
    klabel = Label(root, text=root.results[2],
                   font="Courier 12 bold")  # Results message printed out to the GUI
    klabel.pack()


def delwidget():  # Potential results message delete function
    ilabel.destroy()  # Delete first message label
    jlabel.destroy()  # Delete second message label
    klabel.destroy()  # Delete  third message label
    return None


def game_compare(choice):
    # User selection of Rock Paper or Scissors ####
    rock_pap_sciss = choice
    # Validate User Selection is a valid choice ###
    global a  # Global results message variable
    global b  # Global results message variable
    global c  # Global results message variable
    i = 0  # set variable for infinite loop prevention
    # This is to prevent the code from entering an endless while loop.
    print("before while loop", rock_pap_sciss, i)
    while (rock_pap_sciss == 1) or (rock_pap_sciss == 2) or (
            rock_pap_sciss == 3 or (i <= 0)):  # Compare the selected value sent from the GUI to the acceptable choices
        i += 1

        x = ["Rock", "Paper", "Scissors"]  # Random variable with list of choices

        # Python random choice selector
        ran_var = (random.choice(x))  # Run the list against the python random selector
        print(ran_var, rock_pap_sciss)  # Print the random selection vs player choice
        if rock_pap_sciss == 1:  # Compare Player choice versus random selection
            if ran_var == "Rock":
                print("Rock = Rock, No winner Try again")
                print(" TIE GAME")
                a = "Rock = Rock"
                b = " TIE GAME"
            elif ran_var == "Paper":
                print("Paper covers Rock, Sorry you lose")
                print("LOSER!")
                a = "Paper covers Rock"
                b = "LOSER!"
            elif ran_var == "Scissors":
                print("Rock Breaks Scissors, Winner winner ")
                print("WINNER chicken DINNER!!")
                a = "Rock Breaks Scissors"
                b = "WINNER chicken DINNER!!"
        elif rock_pap_sciss == 2:  # Compare Player choice versus random selection
            print("Test Paper ")
            if ran_var == "Rock":
                print("Paper covers Rock, Winner winner ")
                print("WINNER chicken DINNER!!")
                a = "Paper covers Rock"
                b = "WINNER chicken DINNER!!"
            elif ran_var == "Paper":
                print("Paper = Paper, No winner Try again")
                print("TIE GAME")
                a = "Paper = Paper"
                b = "TIE GAME"
            elif ran_var == "Scissors":
                print("Scissors cuts Paper, Sorry you lose ")
                print("LOSER!!")
                a = "Scissors cuts Paper"
                b = "LOSER!!"
        elif rock_pap_sciss == 3:  # Compare Player choice versus random selection
            print("Test Scissors ")
            if ran_var == "Rock":
                print("Rock breaks Scissors, Sorry you lose" "\n")
                print("LOSER!!")
                a = "Rock breaks Scissors"
                b = "LOSER!!"
            elif ran_var == "Paper":
                print("Scissors cuts Paper, Winner winner", "\n")
                print("WINNER chicken DINNER!!")
                a = "Scissors cuts Paper"
                b = "WINNER chicken DINNER!!"
            elif ran_var == "Scissors":
                print("Scissors = Scissors, No winner Try again " "\n")
                print("TIE GAME!")
                a = "Scissors = Scissors"
                b = "TIE GAME!"
        elif rock_pap_sciss >= 4 or rock_pap_sciss <= 0:  # Safe exit in case selection is corrupted
            print("Invalid Selection")
            a = "Selection was invalid"
            b = "please try again"
        print('\n', "Press Exit to End Game or Make another selection to play again?")
        c = "Press Exit to End Game or play again"
        rock_pap_sciss = 0  # After all options are checked created exit to prevent infinite loop
    return a, b, c,


def main():
    root = Tk()  # Create an instance of Tkinter frame
    title = 'CEIS110 May2022 Garfield Edwards'  # Create the title to be passed to the Game function
    geo = "950x650"  # Set the geometry of Tkinter frame
    message = "Rock_Paper_Scissors_Game"  # Create a message for the rock paper scissors game

    display_text(root, title, geo, message)  # Call the game function from the class
    return None


global a
global b
global c
main()  # Entry point into the Program
exit(0)  # Exit Program
