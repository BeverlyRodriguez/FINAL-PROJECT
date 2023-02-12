#Bubble Sorting Algorithm
import time #For time in animation

def BubbleSort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ["#0000FF" if x == j or x == j+1 else "#DCDC14" for x in range(len(data))] )
                time.sleep(timeTick)
                
    drawData(data, ["#0000FF" for x in range(len(data))])