
def kiloToMile(myKilo):
    myKilo = myKilo * 0.62137
    return myKilo
myKiloPromt = input("Enter Kilometers: ")
answer = float(myKiloPromt.replace("Enter Kilometers: ", ""))

print("Miles: " + str(kiloToMile(answer)))


def celsiusToFahrenheit(myCelsius):
    myFahrenheit = myCelsius * 1.8 + 32
    return myFahrenheit
myCelsiusPrompt = input("Enter Celsius value: ")
answer = float(myCelsiusPrompt.replace("Enter Celsius value: ", ""))

print("Fahrenheit : " + str(celsiusToFahrenheit(answer)))

def binaryToDecimal(myBinary):
    convertVariable = int(myBinary,2)
    return convertVariable
binaryNumber = input("Enter Binary Number: ")
binaryNumber = binaryNumber.replace("Enter Binary Number: ", "")

print("Decimal Binary Number: " + str(binaryToDecimal(binaryNumber)))
