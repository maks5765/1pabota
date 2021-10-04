# check the main triangle property
def checkTriangle(subAr):
    subAr.sort()
    return subAr[2] < (subAr[1] + subAr[0])


# find max S
def task(ar):
    ar.sort()
    for i in range(-1, -len(ar) + 1, -1):
        subString = ar[-2 + i: len(ar) + 1 + i]
        if checkTriangle(subString):
            print(subString)
            p = (ar[-2 + i] + ar[-1 + i] + ar[i]) / 2
            print((p * (p - ar[-2 + i]) * (p - ar[-1 + i]) * (p - ar[i])) ** 0.5)
            break
        else:
            print(subString, "no")


# check for wrong data
def checkCorrectness(ar):
    for i in ar:
        if i <= 0:
            return False
    return True


# get data from console
def accept():
    return [int(i) for i in input().split(" ")]


if __name__ == '__main__':

    array = accept()

    if checkCorrectness(array):
        task(array)
    else:
        print("wrong data accepted, you can't use negative numbers and null")
