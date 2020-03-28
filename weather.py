def weather_conditions(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

user_input = float(input("enter temperature:"))
print(weather_conditions(user_input))

f_temperature = user_input*9 / 5 + 32
print("Temperature in ferenheit is...")
print(f_temperature)