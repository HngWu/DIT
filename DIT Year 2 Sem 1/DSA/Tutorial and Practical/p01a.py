numbers = "0123456789"
def ProbabilitySetON():
    hint1 = int(input("Enter the number of odd number(s) : "))
    hint2 = int(input("Enter any one of the digits : "))
    if hint1 ==0:
        probability1 = (5/10) ** 3
        if hint2 % 2 == 0:
            probability2 = (((1/10) * (9/10) * (9/10)) * 3) + (((1/10) * (1/10) * (9/10)) * 3) + ((1/10) * (1/10) * (1/10))
            #probability2 = (1/5 * 4/5 * 4/5) * 3 + (1/5 * 4/5 * 4/5) * 3 + (1/5)**3
            #probability2 = (12 * 9 + 100)/ 1000
            print(probability2)
        else:
            probability2 = 0
    elif (hint1 == 1):
        probability1 = ((5/10) * 5 * 5) * 3
        if hint2 % 2 == 1:
            probability2 = 5/10 * (1/3)
        else:
            probability2 = 5/10 * (2/3)
    elif hint1 == 2:
        probability1 = ((5/10) * 5 * 5) * 3
        if hint2 % 2 == 0:
            probability2 = 5/10 * (1/3)
        else:
            probability2 = 5/10 * (2/3)
    elif hint1 == 3:
        probability1 = (5 / 10) ** 3
        if hint2 % 2 == 1:
            probability2 = 5/10
        else:
            probability2 = 0
    print(probability1)
    print(probability2)
    print(probability1 * probability2)


def floyd_triangle():
    last_row_numbers = ["1","2","5","6","9","0"]
    output = ""
    row_number = input("Enter the number of rows : ")
    first_number = 1
    total = 0

    if row_number[-1] in last_row_numbers:
        is_starting_number = True
    else:
        is_starting_number = False
    for i in range(int(row_number)):
        first_number += i

    for i in range(int(row_number)):
        if int(row_number) % 2 == first_number % 2:

                output += str(first_number ** 2)
                total += first_number ** 2

        else:

                output += " * "


        first_number += 1
    print(output)
    print(f"The sum of row {first_number} is {total}")


def ProbabilitySetON2():
    hint1 = int(input("(Hint1) Enter the number of odd number(s) : "))
    hint2 = int(input("(Hint2) Enter any one of the digits : "))

    totalNo = 0
    odd = 0
    countNo = 0

    for i in range(10):
        for k in range(10):
            for j in range(10):
                totalNo += 1
                if (i % 2) + (j % 2) + (k % 2) == hint1 :
                    odd += 1
                    if i == hint2 or k == hint2 or j == hint2:
                        countNo += 1

    print(f"Probability of number(s) satisfying hint1 {odd/totalNo*100.:0.2f}")
    print(f"Probability of number(s) satisfying both hints {countNo/totalNo*100.:0.2f}")

ProbabilitySetON2()
#floyd_triangle()