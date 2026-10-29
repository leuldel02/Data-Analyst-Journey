def main():
    x= int(input("What's X? "))
    if is_even(x):
         print ("Your number is Even.")
    else:
        print("Your number is Odd.")

def is_even(n):
    return True if n%2==0 else False

main()
