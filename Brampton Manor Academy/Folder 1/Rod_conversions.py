def rod_conversion():
    rods = float(input("Enter amount of rods: "))
    print("You have entered",rods, "rods")
    return rods

rods = rod_conversion()

def meters_conversion(rods):
    meters = rods * 5.0292
    return meters

meters = meters_conversion(rods)
def conversion_miles(meters):
    miles = meters / 1609.34
    return miles

miles = conversion_miles(meters)

def conversion_furlongs(rods):
    furlongs = rods / 40
    return furlongs

furlongs = conversion_furlongs(rods)

def conversion_feet(meters):
    feet = meters / 0.3048
    return feet

feet = conversion_feet(meters)

def conversion_walking_speed(miles):
    walking_speed = miles/3.1
    return walking_speed

walking_speed = conversion_walking_speed(miles)

def main():
    print("Conversions:")
    print("Meters:",meters)
    print("Feet:",feet)
    print("Miles:",miles)
    print("Furlongs:",furlongs)
    print("Minutes to walk:",walking_speed*60)

main()
