# Create a program that allows users to convert between different units. The user will:
# Select a category (e.g., length, weight, temperature).
# Input a value and select the units to convert from and to. See the converted value displayed.
# Categories will include length, weight, and temperature, with conversions made between imperial & metric

# Length: 1 meter = 39.37 inches | 1 cm = 0.3937 inches
# Weight: 1 gram = 0.035 oz | 1 kg = 2.2 lbs
# Temperature: Celsius -> Farenheit is Celsius * 9, divided by 5, then add 32

# Program is broken into user input, GUI menu, conversion calc
# Next progression is to provide user with ability to bulk upload via xlsx conversions to be calculated. Program will then return an xlsx including the finished calcs

conversionDict = {''}

lengthList = ["Millimeter", "Centimeter", "Meter", "Inches", "Feet", "Yard", "Mile"]
widthList = ["Gram", "Kilogram", "Tonne", "Ounce", "Pound"]
TempList = ["Celsius", "Farenheit"]

metricLength = []
metricWeight = []
metricTemp = []

imperialLength = []
imperialWeight = []
imperialTemp = []


def userInput():
    
    # User input for category type conversion
    try:
        userCategoryStart = input("Which category of unit conversion would you like? Eg. Feet, Pounds, or Farenheit\n")
        print(f"Your user category is {userCategoryStart}")
    except ValueError:
        print("That is not an available category type. Please select from length, weight, or temperature to convert :)\n")
        return None
    
    # User input for metric vs imperial measurement conversion
    try:
        userCategoryEnd = input("Which measurement would you like to convert to?\n")
        print(f"Your user system is {userCategoryEnd}")
    except ValueError:
        print("That is not an available category type. Please select from length, weight, or temperature to convert :)\n")
        return None
    
    # User input for value conversion
    try:
        userValue = float(input(f"What value do you want to convert from {userCategoryEnd} to?"))
        print(f"Your user value is {userValue}")
    except ValueError:
        print("Wrong type of input dummy. Jk you are good. But you do need to input a numeral figure. Don't get it wrong!\n")
        return None
    
    return userCategoryStart, userCategoryEnd, userValue



def conversionCalc(userCatStart, userCatEnd, userVal):
    if userCatStart and userCatEnd in 


while True:


