list1= [1, 4, 6, 8, 7]
def rotatearray(arr):
    newarr = list()
    for i in range(len(arr)):
        if i == 0:
            newarr.append(arr[-1])
        else:
            newarr.append(arr[i-1])
    return newarr

if __name__ == '__main__':
    print(rotatearray(list1))

    
