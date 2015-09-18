# Default shell for a Python 3.x program
# Copy this and rename it to write your own code
#
__author__ = 'Ethan Richards'
# CIS 125
# Fahrenheit-to-Celcius
# Converts a number from Fahrenheit to Celcius.
def main(): 
    F = eval(input("Input a temperature in Fahrenheit:"))
    C = (F-32) * (5/9)
    print("{} in Fahrenheit is {:.1f} in Celcius.".format(F,C))
main()