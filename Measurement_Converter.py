from measurement.measures import Weight, Temperature, Speed

print("Welcome!")
print("Your personal measurement calculator")
print("")
print("Example -- Convert 20 kg or Convert 50 MPH or Convert 90 F")
while True:
    usr_input = input("What would you like to convert, Please follow example: ")
    print("")


    user = usr_input.split()
    type = user[2]
    value = user[1]
    print(type, value)

    if type == "kg":
        val = Weight(kg=value)
        print(val.lb, "lb")

    if type == "lb":
        val = Weight(lb=value)
        print(val.kg, "kg")

    if type == "MPH":
        val = Speed(mile__hour=value)
        print(val.km__hr, "KPH")

    if type == "KPH":
        val = Speed(km__hr=value)
        print(val.mile__hour, "MPH")

    if type == "C":
        val = Temperature(c=value)
        print(val.f, "F")

    if type == "f":
        val = Temperature(f=value)
        print(val.c, "C")