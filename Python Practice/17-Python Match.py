day = 8
match day:
    case 1:
        print("Monday") 
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4: 
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")   
    case 7:
        print("Sunday")
    case 8|9|10:
            print("This match canceled")
    case _:
        print("Waiting for a valid day")
        
        

