#A function that returns a string that reproduces berlin clock from the given 24hr time format(hh:mm:)

def berlin_clock(time):
    
    #extract hours, minutes and seconds from the time string
    
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:])
    HC = hours//5
    hc = hours%5
    MC = minutes//5
    MCR = minutes//15
    mc = minutes%5
    
    #first row: five hours per colour
    
    F_R = ""
    F_R += HC*"R" + (4-HC) * "O"
    
    #second row: an hour per colour
    S_R = ""
    S_R += hc*"R" + (4-hc)* "O"
    
    #third row: five minutes block
    T_R = ""
    for i in range(MC):
        if (i == 2 or i == 5 or i == 8):
            T_C += "R"
            continue
        T_R += "Y"
    T_R += (11-MC)*"O"
    
    #fourth row: one minutes block
    Fr_R = ""
    Fr_R += mc*"Y" + (4-mc)*"O" 
    if seconds%2 == 0:
        O = "Y"
    else:
        O = "O"
    
    #combine all rows
    full_show = O + "\n" + F_R + "\n" + S_R + "\n" + T_R + "\n" + Fr_R
    return full_show
