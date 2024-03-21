def bubble_sort(elements):
    for i in range(len(elements)-1):
        swapped = False
        for j in range(len(elements)-1-i):
            if elements[j] > elements [j+1]:
                temp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = temp
                swapped = True
        if not swapped:
            break
    return elements

if __name__ == '__main__':
    elements = [10,9,11,15,8,5,20,25,1]
    string_elements = [
        "bASOPDMA", 
        "Caspdmkakdsmsc", 
        "aaASKDMa", 
        "Bapsodmkakda"]


    print(bubble_sort(elements))
    print(bubble_sort(string_elements))
