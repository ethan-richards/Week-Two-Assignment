
__author__ = 'Ethan Richards'

# CIS 125
# Celcius-to-Fahrenheit       
# Creates a table for Celcius to Fahrenheit conversion.
def main():
    for C in range(0,101,10):
        f = (C*(9/5) + 32)
        print(C,f)
        
main()
