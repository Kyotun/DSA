def bubble_sort(elements, key=None):
    for i in range(len(elements)-1):
        swapped = False
        for j in range(len(elements)-1-i):
            if key:
                if elements[j][key] > elements [j+1][key]:
                    temp = elements[j+1]
                    elements[j+1] = elements[j]
                    elements[j] = temp
                    swapped = True
            else:
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
    elements_3 = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    print(bubble_sort(elements_3, key="transaction_amount"))
    print(bubble_sort(elements))
