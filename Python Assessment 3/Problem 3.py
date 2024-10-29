def count(value, data):
    counting = 0
    #Checks whether each value in the data is equal to the value inputed, and adds 1 to counting for each
    #For loop for i in data allows us to handle any size set of data
    for i in data:
        if i == value:
            counting += 1
    return print(counting)

def search(value, data):
    #Checks whether the current value is equal to the inputed values, if so it is returned, if not a negative message is returned
    for i in range(len(data)):
        if data[i] == value:
            return print(i)
    return print('could not find value in data')

def sort(data):
    temp2 = data.copy()
    # use .copy()as when creating such variables it can reference where data is stored and not modify the original
    for i in range(len(temp2)):
        for j in range(1, len(temp2)-i):
            if temp2[j] < temp2[j-1]:
                temp = temp2[j]
                temp2[j] = temp2[j-1]
                temp2[j-1] = temp
    return print(temp2)

def delete(value, data):
    #here i have used list comprehension in order to efficiently and easily produce a new list where (not value in output):
    output = [i for i in data if i != value]
    return print(output)             

count(8, [5, 6, 7, 8, 9, 10, 11, 2, 3, 4, 8, 10, 12])
search(8, [5, 6, 7, 8, 9, 10, 11, 2, 3, 4, 8, 10, 12])
sort([5, 6, 7, 8, 9, 10, 11, 2, 3, 4, 8, 10, 12])
delete(8,[5, 6, 7, 8, 9, 10, 11, 2, 3, 4, 8, 10, 12])
