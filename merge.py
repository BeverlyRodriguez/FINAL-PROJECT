# MERGE SORTING ALGORITHM
import time #For time in animation


def Mergesort(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def MergeSort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        MergeSort(data, start, mid, drawData, timeTick)
        MergeSort(data, mid+1, end, drawData, timeTick)

        Mergesort(data, start, mid, end, drawData, timeTick)

        drawData(data, ["darkseagreen1" if x >= start and x < mid else "#E066FF" if x == mid 
                        else "darkslategray1" if x > mid and x <=end else "gray10" for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, ["#E066FF" for x in range(len(data))])
