# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    # WRITE YOUR CODE HERE
    ######################    
    miles = kilometers * 0.6214
    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    kilometers = float(input("Enter distance in kilometers: "))
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    miles = kilometer_conversion(kilometers)
    # Display the miles
    print(f"{kilometers} kilometers is equal to {miles} miles.")
