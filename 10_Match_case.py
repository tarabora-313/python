x = int(input(" Enter the value of x: "))

match x:

    case 0:
        print("x is 0")

    case 4:
        print("case is 4")    

    case _ if x != 90:
        print(x, "is not 90")    

    case _ if x != 70:
        print(x, "is not 70")    

    case _ :
        print(x)    


