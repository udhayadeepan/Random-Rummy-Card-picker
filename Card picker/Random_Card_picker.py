# import required module
import os
from tkinter import *
import random
win=Tk()
win.geometry('210x300')
win.resizable(0,0)
win.title("Rummy Card Picker")
win.configure(bg="yellow")
Label(win,text="Random Rummy Card Picker",bg="light blue").place(x=30,y=15)
cards_file_name=['10_of_clubs.png', '10_of_diamonds.png', '10_of_hearts.png', '10_of_spades.png', '2_of_clubs.png', '2_of_diamonds.png', '2_of_hearts.png', '2_of_spades.png', '3_of_clubs.png', '3_of_diamonds.png', '3_of_hearts.png', '3_of_spades.png', '4_of_clubs.png', '4_of_diamonds.png', '4_of_hearts.png', '4_of_spades.png', '5_of_clubs.png', '5_of_diamonds.png', '5_of_hearts.png', '5_of_spades.png', '6_of_clubs.png', '6_of_diamonds.png', '6_of_hearts.png', '6_of_spades.png', '7_of_clubs.png', '7_of_diamonds.png', '7_of_hearts.png', '7_of_spades.png', '8_of_clubs.png', '8_of_diamonds.png', '8_of_hearts.png', '8_of_spades.png', '9_of_clubs.png', '9_of_diamonds.png', '9_of_hearts.png', '9_of_spades.png', 'ace_of_clubs.png', 'ace_of_diamonds.png', 'ace_of_hearts.png', 'ace_of_spades.png', 'ace_of_spades2.png', 'black_joker.png', 'jack_of_clubs.png', 'jack_of_clubs2.png', 'jack_of_diamonds.png', 'jack_of_diamonds2.png', 'jack_of_hearts.png', 'jack_of_hearts2.png', 'jack_of_spades.png', 'jack_of_spades2.png', 'king_of_clubs.png', 'king_of_clubs2.png', 'king_of_diamonds.png', 'king_of_diamonds2.png', 'king_of_hearts.png', 'king_of_hearts2.png', 'king_of_spades.png', 'king_of_spades2.png', 'queen_of_clubs.png', 'queen_of_clubs2.png' ]
win1=Frame(win,bg="yellow")
win1.place(x=40,y=100)
slash='\\'
card=[]
for i in cards_file_name:
      image_path=str(os.getcwd())+"\card"+slash+i
      card.append(PhotoImage(file=image_path))
view=Label(win1)
view.pack()
def pick():
      view.configure(image=card[random.randint(0,60)])
b1=Button(win,text="Pick",command=pick,width=10)
b1.place(x=60,y=60)

