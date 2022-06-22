def method1():
    print("First method")
    i = 0
    while i < 15:
        print(i)
        i += 1
    return i


def method2():
    print("Second method")
    k = 0
    while k < 3:
        print("Hi")
        k = 1 + k


if __name__ == '__main__':
    method1()
    method2()
    print("For loop")
    j = 1
    while j < 5:
        print(j)
        if j == 3:
            print("j is 3")
        else:
            print("j is smaller than 5")
        j += 1
    waitForInput = ""
    waitForInput = input()
