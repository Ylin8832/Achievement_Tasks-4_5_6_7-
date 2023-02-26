# Name:                     Task 4: Unit Converter
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             February 25, 2023
# Date Last Modified:       February 25, 2023


print("\n{0:-^64s}".format("Welcome to Unit Converter Program".upper()), "\n\n{0:^40s}{1:s}".format("1. Temperature","2. Speed"))
conversion = int(input("\nPlease Enter [1] For temperature conversion, [2] for speed conversion: "))

def tempConver(number1): # Define a function called [tempConver] that accepts on parameter called [number1].

    if number1 == 1:
        temperature = float(input("Enter the temperature: ").strip()) # Ask the user to enter the temperature (number) they want to convert. Remove whitespace.
        tempUnit = input("Enter the current temperature unit C(Celsius) or F(Fahrenheit): ") # Ask the user to enter the current unit used for the temperature.
        if tempUnit.strip().upper() == "C": # remove whitespace and ignore letter-case differences "C", "c".
            print("{0:.1f}°C = {1:.1f}°F".format(temperature , temperature * 9/5 + 32)) # Display result using substitution (format() method) for the output.
        elif tempUnit.strip().upper() == "F": # remove whitespace and ignore letter-case differences "F", "f".
            print("{0:.1f}°F = {1:.1f}°C".format(temperature , (temperature - 32) * 5/9))

def speedConver(number2): # Define a function called [speedConver] that accepts on parameter called [number2].

    if number2 == 2:
         # Ask the user to enter the speed (number) they want to convert.  
         # Add .strip() to remove whitespace, but it might not needed if already had one in the following if statement.
        speed = float(input("Enter the speed: ").strip())
        speedUnit = input("Enter the current speed unit KMH(Kilometer per hour) or MPH(Miles per hour): ") # Ask the user to enter the current unit used for the speed.
        if speedUnit.strip().upper() == "KMH": # remove whitespace and ignore letter-case differences "KMH", "kmh".
            print("{0:.2f}k/h = {1:.2f}m/h".format(speed , speed/1.609)) # Display result using substitution (format() method) for the output.
        elif speedUnit.strip().upper() == "MPH": # remove whitespace and ignore letter-case differences "MPH", "mph".
            print("{0:.2f}m/h = {1:.2f}k/h".format(speed , speed * 1.609))


tempConver(conversion) # call the function and pass the input data (argument) for the function to execute the temperature conversion. 
speedConver(conversion) # Call the function and pass the input data (argument) for the function to execute the speed conversion. 