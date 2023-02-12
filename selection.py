# SELECTION SORTING ALGORITHM
import time #For time in animation


def SelectionSort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, ["#E066FF" if x == minimum or x == i else "gray10" for x in range(len(data))] )
        time.sleep(timeTick)
        
    drawData(data, ["#E066FF" for x in range(len(data))])
    