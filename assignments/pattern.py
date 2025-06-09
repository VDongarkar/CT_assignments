def pyramid(n):
    for i in range(1 , n + 1):
        for j in range(n - i):
            print(" ",end = "")
        for k in range(1,2*i):
            print("*",end="")
        print()



def lower_traingle(n):
    print("lower pattern")
    print("===========================================================")
    for i in range(n):
        for j in range (i + 1):
            print("*",end = " ")
        print()

def upper_triangle(n):
    print("upper pattern")
    print("===========================================================")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")



if __name__ == "__main__":
    n = 4
    pyramid(n)
    lower_traingle(n)
    upper_triangle(n)