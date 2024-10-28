# Ask user for their first, middle, and last names
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

# Display the full name
full_name = first_name + ' ' + middle_name + ' ' + last_name
print("Full Name:", full_name)

# Display their initials
initials = '. '.join([
    first_name[0].upper(), middle_name[0].upper(), last_name[0].upper()
]) + '.'
print("Initials:", initials)
