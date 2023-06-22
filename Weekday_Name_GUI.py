'''
Rayyan Jamil
Mr. Dohmen
8/27/2021
Weekday Name with GUI
'''
#import the tkinter module to make GUI
import tkinter as tk

#Making function for program
def showDay(event):
 
    numEntered = ansBox.get()
    numEntered = int(numEntered)
    if numEntered == 1:
        print("Sunday\n")
    elif numEntered == 2:
        print('Monday\n')
    elif numEntered == 3:
        print('Tuesday\n')
    elif numEntered == 4:
        print('Wednesday\n')
    elif numEntered == 5:
        print('Thursday\n')
    elif numEntered == 6:
        print('Friday\n')
    elif numEntered == 7 or numEntered == 0:
        print('Saturday\n')
    else:
        print('Your number is INVALID.\nRESTART PROGRAM')

#Creating GUI
mainWindow = tk.Tk()
mainWindow.geometry('500x500+800+100')
mainWindow.title("Weekday Name Program")

qLabel = tk.Label(mainWindow, text="Enter a number from 0-7:")
qLabel.grid(row=1, column=1, padx=10, pady=10)
ansBox = tk.Entry(mainWindow, width=20)
ansBox.grid(row=1, column=2, padx=0, pady=0)
submitBtn = tk.Button(mainWindow, text='SUBMIT')
submitBtn.grid(row=2, column=2, padx=0, pady=10)
submitBtn.bind('<ButtonPress-1>', showDay)
submitBtn.bind('<Return>', showDay)

mainWindow.mainloop()
