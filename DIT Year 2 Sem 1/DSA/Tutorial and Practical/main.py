def minmax(data):
    small = big = data[0] # assuming data is non-empty
    for item in data:
        if item < small:
            small = item
        elif item > big:
            big = item
    return small, big

def sum_of_squares(n):
    sum = 0
    if n > 0:
        for i in range(1, n+1):
            sum += i*i
    else:
        sum = -1
        return sum
    return sum

def sum_of_squares2(n):
    sum = 0
    if n > 0:
        for i in range(1, n+1):
            if not (i / 2 ).is_integer():
                print(i)
                sum += i*i

    return sum

def question_4():
    for i in range(50, 90 ,10):
        print(i)

    for i in range(8, -9, -2):
        print(i)


def num_vowels(text):
    NumOfVowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in text:
        if letter.lower() in vowels:
            NumOfVowels += 1
    return NumOfVowels

def question_6():
    counter = True
    user_input = []
    while counter:
        try:
            user_text = input("Enter standard input: ")
            print(user_text)
            user_input.append(user_text)
        except EOFError:
            for i in user_input:
                print(i[::-1])

            counter = False
            return "EOF Error has occurred"

def question_7():
    str = input("Enter a sequence of numbers: ")
    NumArray = []
    for number in str:
        if number not in NumArray:
            NumArray.append(number)
        else:
            print("The sequence of numbers is not distinct")
            exit(0)
    print("The sequence of numbers is distinct")

#print(sum_of_squares(3))
#print(minmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#print(sum_of_squares2(6))
#question_4()
print(num_vowels("aaaaaaaaaaa"))
#print(question_6())
#question_7()