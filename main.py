import tkinter as tk
import random
from tkinter import *
from tkinter import ttk



# Importing Sorting Algorithms
from bubble import BubbleSort
from insertion import InsertionSort
from selection import SelectionSort
from merge import MergeSort
from quick import QuickSort


#Making a window using the Tk widget
window = tk.Tk()
window.title('SORTING ALGORITHM VISUALIZER')
window.geometry('850x530')


# Generatorating Function
Algorithm = StringVar()
ForSpeed = StringVar()
data = []
Speed = ['FAST', 'MEDIUM', 'SLOW']
SortingList = ['SELECTION SORT',  
               'BUBBLE SORT', 
               'INSERTION SORT', 
               'MERGE SORT', 
               'QUICK SORT']

canvas = Canvas(window, width=822, height=400, bg="#FAFAEB")
canvas.grid(row=1, column=0, padx=10, pady=5)
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 822
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 5
    spacing = 3
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def generate():
    global data

    data = []
    size = int(sizeEntry.get())
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    
    for _ in range(size):
        data.append(random.randrange(minVal+1, maxVal+1))

    drawData(data, ["#DCDC14" for x in range(len(data))])


def SpeedSetter():
    if SpeedMenu.get() == 'SLOW':
        return 0.4
    elif SpeedMenu.get() == 'MEDIUM':
        return 0.2
    else:
        return 0.001


def sort():
    global data
    timeTick = SpeedSetter()

    if SortMenu.get() == 'SELECTION SORT':
        SelectionSort(data, drawData, timeTick)
    elif SortMenu.get() == 'BUBBLE SORT':
        BubbleSort(data, drawData, timeTick)
    elif SortMenu.get() == 'INSERTION SORT':
        InsertionSort(data, drawData, timeTick)
    elif SortMenu.get() == 'MERGE SORT':
        MergeSort(data, 0, len(data)-1, drawData, timeTick)
    elif SortMenu.get() == 'QUICK SORT':
        QuickSort(data, 0, len(data)-1, drawData, timeTick)



FirstFrame = Frame(window, width= 900, height=300, bg="#FAFAEB")
FirstFrame.grid(row=10, column=0, padx=10, pady=5)

FirstLabel = Label(FirstFrame, text="Algorithm: ", bg="#FAFAEB")
FirstLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)
SortMenu = ttk.Combobox(FirstFrame, textvariable=Algorithm, values=SortingList)
SortMenu.grid(row=0, column=1, padx=5, pady=5)
SortMenu.current(0)

SecondLabel = Label(FirstFrame, text="SPEED: ", bg="#FAFAEB")
SecondLabel.grid(row=0, column=5, padx=10, pady=5, sticky=W)
SpeedMenu = ttk.Combobox(FirstFrame, textvariable=ForSpeed, values=Speed)
SpeedMenu.grid(row=0, column=6, padx=5, pady=5)
SpeedMenu.current(0)

sizeEntry = Scale(FirstFrame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='white',label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)
#Buttons
SortingButton = Button(FirstFrame, text="SORT", command=sort, bg="#CDCDC0")
SortingButton.grid(column=3, row=2, padx=5, pady=5)

ShuffleButton = Button(FirstFrame, text="SHUFFLE", command=generate, bg = "red", fg = "white")
ShuffleButton.grid(column=2, row=2, padx=5, pady=5)


minEntry = Scale(FirstFrame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value",bg='white')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(FirstFrame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value",bg='white')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

sizeEntry = Scale(FirstFrame, from_=10, to=100, resolution=1, orient=HORIZONTAL, bg='white',label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)
window.mainloop()
