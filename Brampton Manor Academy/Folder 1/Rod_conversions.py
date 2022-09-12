def rod_conversion():
    rods = float(input("Enter amount of rods: "))
    print("You have entered",rods, "rods")
    return rods

def meters_conversion(rods):
    meters = rods * 5.0292
    return meters

def conversion_miles(meters):
    miles = meters / 1609.34
    return miles


def conversion_furlongs(rods):
    furlongs = rods / 40
    return furlongs


def conversion_feet(meters):
    feet = meters / 0.3048
    return feet

def conversion_walking_speed(miles):
    walking_speed = miles/3.1
    return walking_speed

def main():
    rods = rod_conversion()
    meters = meters_conversion(rods)
    miles = conversion_miles(meters)
    furlongs = conversion_furlongs(rods)
    feet = conversion_feet(meters)
    walking_speed = conversion_walking_speed(miles)
    
    print("Conversions:")
    print(f"Meters: {meters}")
    print(f"Feet: {feet}")
    print(f"Miles: {miles}")
    print(f"Furlongs: {furlongs}")
    print(f"Minutes to walk: {walking_speed*60}")

if __name__ == '__main__':
    main()
