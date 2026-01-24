def check_number(numbers) :
    pairs = []
    odd = []
    for number in numbers :
        if number % 2 == 0 :
            pairs.append(number)
        else : 
            odd.append(number)
    return pairs, odd

print(check_number([1, 2, 4, 6, 5, 7, 11, 20]))