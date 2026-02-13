def meters_to_km(meters):
    return meters / 1000

def km_to_meters(km):
    return km * 1000

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60


def main():
    print("====== Simple Unit Converter ======")
    print("1. Meters → Kilometers")
    print("2. Kilometers → Meters")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Kilograms → Pounds")
    print("6. Pounds → Kilograms")
    print("7. Hours → Minutes")
    print("8. Minutes → Hours")


    choice = input("Choose an option (1–8): ")

    if choice == "1":
        val = float(input("Enter meters: "))
        print(f"{val} m = {meters_to_km(val)} km")

    elif choice == "2":
        val = float(input("Enter kilometers: "))
        print(f"{val} km = {km_to_meters(val)} m")

    elif choice == "3":
        val = float(input("Enter Celsius: "))
        print(f"{val} °C = {c_to_f(val)} °F")

    elif choice == "4":
        val = float(input("Enter Fahrenheit: "))
        print(f"{val} °F = {f_to_c(val)} °C")

    elif choice == "5":
        val = float(input("Enter kilograms: "))
        print(f"{val} kg = {kg_to_lb(val)} lb")

    elif choice == "6":
        val = float(input("Enter pounds: "))
        print(f"{val} lb = {lb_to_kg(val)} kg")
    
    elif choice == "7":
        val = float(input("Enter hours: "))
        print(f"{val} hours = {hours_to_minutes(val)} minutes")

    elif choice == "8":
        val = float(input("Enter minutes: "))
        print(f"{val} minutes = {minutes_to_hours(val)} hours")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
