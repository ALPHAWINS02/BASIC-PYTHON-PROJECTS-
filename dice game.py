import tkinter
import random

root = tkinter.Tk()
root.geometry('600x500')
root.title('Rolling Dice')
label = tkinter.Label(root, text='', font=('Helvetica', 260))

def roll_dice():
 
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()
button = tkinter.Button(root, text='roll dice', foreground='red',background='yellow' ,command=roll_dice)
button.pack()
root.mainloop()
