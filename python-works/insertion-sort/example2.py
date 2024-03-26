def insertion_sort(elements, high_end):
    for i in range(1, high_end):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

def calculate_median(elements, length):
    if length == 0:
        return
    elif length == 1:
        return elements[0]
    elif length % 2 == 0:
        left_element = elements[int(length/2)]
        right_element = elements[int((length/2))-1]
        return (left_element+right_element)/2
    return elements[int(length/2)]

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    for i in range(1,len(elements)+1):
        insertion_sort(elements=elements, high_end=i)
        print(calculate_median(elements=elements, length=i))
