def dayReturn(day, dayIncrement):
    days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    counter = 0
    #Ensures value is in the dictionary
    if day in days:
        counter = days[day]
        #Adds to a counter for each day in input value
        if dayIncrement >= 0 and dayIncrement <= 500:
            for value in range(0,dayIncrement):
                counter += 1
                #Resets the week
                if counter == 7:
                    counter = 0
        else: 
            return "Invalid entry"
    else:
        return "Invalid day entered"

    #Matches and locates the value to print
    for number in days:
        if counter == days[number]:
            return (number)