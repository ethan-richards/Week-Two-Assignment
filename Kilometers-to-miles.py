__author__ = 'Ethan Richards'

# CIS 125
#Kilometers to Miles
# Converts Kilometers to Miles and reports the results.
def main():
    K = eval(input("Enter a distance in Kilometers."))
    M = (K * 0.621371) 
    print(K,"Kilometers is",M,"Miles.")
    
main()