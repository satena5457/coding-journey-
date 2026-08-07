#Definition of function for returning the total value of character in a string 

def letters_to_numbers(s): 

    Sum = 0;  #Variable for storing the total total value of the characters

    #Creating a loop to check a type of each character in the string and add its value to the Sum

    for char in s:
        if char.isupper():
            Sum += (ord(char) - 48)
        elif char.islower():
            Sum += (2*(ord(char)-64))
        elif char.isdigit():
            Sum += (ord(char)-96)
        else:
            Sum += (0*ord(char))
    return Sum
