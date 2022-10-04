import unittest

from wind_chill import *


class MyFirstTests(unittest.TestCase):

    def test_wind_chill_index(self):
        self.assertEqual(wind_chill_index(10,15), -6.5895344209562525)


def wind_chill_index(air_temp,air_speed):
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return wind_chill

def outputs():
    print(f"When temp is 10 and speed is 15, wind chill is: {wind_chill_index(10,15)}")
    print(f"When temp is 0 and speed is 25, wind chill is: {wind_chill_index(0,25)}")
    print(f"When temp is -10 and speed is 35, wind chill is: {wind_chill_index(-10,35)}")

def inputs():
    temp = float(input("enter air temp: "))
    speed = float(input("enter air speed: "))
    print(f"Windchill: {wind_chill_index(temp,speed)}")


if __name__ == '__main__':    
    inputs()
    outputs()
    unittest.main()
