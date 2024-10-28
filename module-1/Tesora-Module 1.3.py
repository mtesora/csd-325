# Function to manage the countdown
def countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print(
                f"{bottles} bottle of beer on the wall, {bottles} bottle of beer."
            )
            print(
                "Take it down, pass it around, no more bottles of beer on the wall.\n"
            )
        else:
            print(
                f"{bottles} bottles of beer on the wall, {bottles} bottles of beer."
            )
            print(
                f"Take one down, pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n"
            )
        bottles -= 1  # Decrement the bottle count


# Main program
def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles < 1:
            print("Please enter a positive number.")
        else:
            countdown(bottles)
            print("Time to buy more bottles of beer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Run the program
if __name__ == "__main__":
    main()
