#INSERTION SORTING ALGORITHM
import time #For time in animation


def InsertionSort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drawData(data, ["#0000FF" if x == k or x == i else "#DCDC14" for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, ["#DCDC14" for x in range(len(data))])
