def findMaxStep(dataList, step=1):
    max_start_index = 0
    max_len = 1
    start_index = 0
    count = 1
    for i in range(1, len(dataList)):
        if dataList[i] - dataList[i - 1] == step:
            count = count + 1
        else:
            if count > max_len:
                max_len = count
                max_start_index = start_index
            start_index = i
            count = 1
    return dataList[max_start_index : max_start_index + max_len]


answer = findMaxStep([3, 2 , 4 , 5 ,  6,  1, 9])
print(answer)

answer = findMaxStep([3, 2 , 4 , 5 ,  6,  1,2,3,4, 9])
print(answer)
