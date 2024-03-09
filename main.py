import tkinter as tk 
from better_profanity import profanity

# Top level window 
frame = tk.Tk() 
frame.title("TextBox Input") 
frame.geometry('400x200') 

# Function for getting Input from textbox and printing the censored text at label widget 
def censor_txt(input_txt):
	profanity.load_censor_words()
	return profanity.censor(input_txt)

def printInput(): 
	inp = inputtxt.get(1.0, "end-1c") 
	inp = censor_txt(inp)
	lbl.config(text = "Provided Input: \n"+inp) 

# TextBox Creation 
inputtxt = tk.Text(frame, height = 5, width = 20) 
inputtxt.pack() 

# Button Creation 
printButton = tk.Button(frame, text = "Print", command = printInput) 
printButton.pack() 

# Label Creation 
lbl = tk.Label(frame, text = "") 
lbl.pack() 
frame.mainloop()