def parking(day, hour):
    if hour>=19 and hour<21:
        print("both")
    elif day%2=0:
        if hour>=21 or hour<19:
            print("left")
        else:
            print("right")
    else:
        if hour>=21 or hour<19:
            print("right")
        else:
            print("left")
        
    
