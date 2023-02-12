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


# Making a window using the Tk widget
window = tk.Tk()
window.title('SORTING ALGORITHM VISUALIZER')
window.geometry('895x720')
Title = Label(window, text="SORTING ALGORITHM VISUALIZER", bg="#FAFAEB", font=("georgia",22))
Title.grid(row=0, column=0, padx=10, pady=5)
Name = Label(window, text="Programmed By: Beverly Ann L. Rodriguez", bg="#FAFAEB", font=("roboto",10))
Name.grid(row=1, column=0, padx=10, pady=0)


# Generatorating Function
Algorithm = StringVar()
ForSpeed = StringVar()
ForSize = StringVar()
data = []
Speed = ['FAST', 'MEDIUM', 'SLOW']
Size = ['20','40','60','80','100']
SortingList = ['SELECTION SORT',  
               'BUBBLE SORT', 
               'INSERTION SORT', 
               'MERGE SORT', 
               'QUICK SORT']

canvas = Canvas(window, width=872, height=460, bg="#FAFAEB")
canvas.grid(row=2, column=0, padx=10, pady=10)

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 872
    canvas_height = 455
    x_width = canvas_width / (len(data) + 1)
    offset = 3
    spacing = 3
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 445
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def generate():
    global data

    data = []
    size = int(SizeMenu.get())
    minVal = int(MinimumData.get())
    maxVal = int(MaximumData.get())
    
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

def SizeSetter():
    if SizeMenu.get() == '20':
        return 20
    elif SizeMenu.get() == '40':
        return 40
    elif SizeMenu.get() == '60':
        return 60
    elif SizeMenu.get() == '80':
        return 80
    

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



FirstFrame = Frame(window, width= 1050, height=300, bg="#FAFAEB")
FirstFrame.grid(row=11, column=0, padx=8, pady=10)

#ComboBox
FirstLabel = Label(FirstFrame, text="ALGORITHM: ", bg="#FAFAEB")
FirstLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
SortMenu = ttk.Combobox(FirstFrame, textvariable=Algorithm, values=SortingList, width=10)
SortMenu.grid(row=1, column=1, padx=5, pady=5)
SortMenu.current(0)

SecondLabel = Label(FirstFrame, text="SPEED: ", bg="#FAFAEB")
SecondLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)
SpeedMenu = ttk.Combobox(FirstFrame, textvariable=ForSpeed, values=Speed, width=8)
SpeedMenu.grid(row=1, column=3, padx=5, pady=5)
SpeedMenu.current(0)

ThirdLabel = Label(FirstFrame, text="DATA SIZE: ", bg="#FAFAEB")
ThirdLabel.grid(row=1, column=4, padx=10, pady=5, sticky=W)
SizeMenu = ttk.Combobox(FirstFrame, textvariable=ForSize, values=Size, width=5)
SizeMenu.grid(row=1, column=5, padx=5, pady=5)
SizeMenu.current(0)

#Buttons
SortingButton = Button(FirstFrame, text="SORT", command=sort, bg="#CDCDC0", width=8, height=3)
SortingButton.grid(column=8, row=3, padx=5, pady=5)

ShuffleButton = Button(FirstFrame, text="SHUFFLE", command=generate, bg = "red", fg = "white", width=8, height=3)
ShuffleButton.grid(column=8, row=1, padx=5, pady=5)

#Scale
MinimumData = Scale(FirstFrame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value",bg='white')
MinimumData.grid(row=3, column=1, padx=5, pady=5)

MaximumData = Scale(FirstFrame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value",bg='white')
MaximumData.grid(row=3, column=3, padx=5, pady=5)

window.mainloop()
