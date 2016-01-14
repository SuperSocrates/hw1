def convert():
    fah = eval(input("What is the temperature in Fahrenheit? "))
    celsius = (fah - 32) * 5/9
    print("The temperature is " + celsius + " degrees Celsius.")

    convert()
