def question1():
    mystring = "this is python Programing."
    print(mystring.replace(" ", ""))

def question2():
    my_string = "this is python Programing"
    print(my_string[-18:-11])

def question3():
    my_list = [100, 100.5, 30, 70, 125.6, 'Python', 'Java',
               'Ruby']
    my_list.insert(4, 77)
    print(my_list)

def question4():    
    my_list = [100, 100.5, 30, 70, 125.6, 109.25, 101.01, 209.99]
    my_list.sort(reverse=True)
    desc = my_list
    print(desc)

def question5():
    my_list = [100, 100.5, 30, 70, 125.6, 'Python', 'Java',
               'Ruby']
    my_slice = my_list[:-4]
    print(my_slice)


def question6():
    programming = {1: "Java", 2: "C", 3: "C++", 4: "R", 5:
    "Python"}
    if not programming.keys().__contains__(6):
        verify = True
    else:
        verify = False

    print(verify)

def question7():
    programming = {1: "Java", 2: "C", 3: "C++", 4: "R", 5:
        "Python"}
    val = programming.values()
    print(list(val))

def question8():
    programming = {1: "Java", 2: "C#", 3: "C++", 4: "R", 5:
        "Python", 6: "Javascript"}

    minValue = "a" * 10000000
    numOfAs = 0

    for language in programming.values():
        if len(language) < len(minValue):
            #print(len(minValue))
            minValue = language
    numOfAs=programming[6].count("a")
    if numOfAs == len(minValue):
        print("True!")
    else:
        print("False!")

def question9():
    x = [2, 4, 6, 8]
    y = [5, 10, 15, 20]
    for xnumber in x:
        for ynumber in y:
            if xnumber > 5 and ynumber < 12:
                print(xnumber * ynumber)

def question10():
    var = 8

    def my_func(x):
        print(x * var)


    my_func(10)



def main():
    #question10()
    print("👨🏻‍🔧")

if __name__ == '__main__':
    main()