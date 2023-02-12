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

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position-1, drawData, timeTick)
        quick_sort(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, ["#9A9A32" if x >= start and x < pivot_position else "#0000FF" if x == pivot_position
                        else "#8F8FBC" if x > pivot_position and x <=end else "#DCDC14"  for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, ["#DCDC14"  for x in range(len(data))])
