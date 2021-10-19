print(30 * "-")
print("Hello, Welcome to The Quarentine shop, Whe are here to help!")
print(30 * "-")
print("What are you looking for today?")
print(30 * "-")
print("  Items  ")
print(30 * '-')
print(" 1 - Masks -")
print(" 2 - Toilet Paper -")
print(" 3 - Hand Sanitizer -")
print(" 4 - Twinkies -")
print(30 * "-")



selection = input('Enter your choice [1-4] : ')

selection = int(selection)

if selection == 1:
    print()
    print ("Best way to Keep Yourself safe from Coronavirus!")
    print()
    print("Thats going to be $250")
    print()
x = input("yes or no?")
if x == 'yes':
    print("Thank you for your purchase")
          
elif selection == 2:
    print ("So Youre the one thats been hording all the toilet paper")
    print("you cant find this anywhere so $50 a roll")
elif selection == 3:
    print ("Dont sell this on ebay")
    print("these are $10")
elif selection == 4:
    print("Gotta have the twinkies when theres a global emergency!")
    print("Thats going to be $100 a box")
    
else:    
    print ("Im sorry but thats all we have at the moment")
        
