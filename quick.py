#QUICK SORT ALGORITHM 
import time #For time in animation


def partition(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def QuickSort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        QuickSort(data, start, pivot_position-1, drawData, timeTick)
        QuickSort(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, ["darkseagreen1" if x >= start and x < pivot_position else "#0000FF" if x == pivot_position
                        else "darkslategray1" if x > pivot_position and x <=end else "gray10"  for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, ["#E066FF"  for x in range(len(data))])
