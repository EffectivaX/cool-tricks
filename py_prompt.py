name = input("What is your name? ")

print(f"Hello {name}, welcome to Adonai Security!")
print("How may we help you? Choose from the options below:")

choice = [
    "1. What is Adonai Security?",
    "2. What are your services?",
    "3. Why choose Adonai Security?",
    "4. Key Trade References", 
    "5. Adonai Security Contact details"
]

while True: # Creating a loop for continuous interaction
    for option in choice:
        print(option)

    # Get user input as a number with error handling
    while True:
        try:
            user_choice = int(input("Enter your choice (1, 2, 3, 4 or 5): "))
            break # Exit the inner loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Displaying information based on user choice
    if user_choice == 1:
        about_adonai = [
            "Adonai Security is an acclaimed firm of security agents with a reputation for both effective security solutions and the use of innovative technology in the pretection of life and property. ",
        ]
        for line in about_adonai:
            print(line)

    elif user_choice == 2:
        services = [
            "1. RISK ASSESSMENT AND NEEDS ANALYSIS",
            "2. UNIFORMED SECURITY GUARDS",
            "3. ELECTRONIC SECURITY SYSTEMS (CCTV)",
            "4. SPY GADGETS",
            "5. CAR ALARMING",
            "6. VEHICLE TRACKING SYSTEM",
            "7. CRIME AWARENESS TRAINING"
        ]
        for service in services:
            print(service)

    
    elif user_choice == 3:
        Why_choose_Adonai_security = [
            "1. REDUCED VULNERABILITY",
            "2. CUSTOMER CENTRICISM",
            "3. LOWERED COSTS",
            "4. INCREASED FLEXIBILITY",
        ]
        for advantage in Why_choose_Adonai_security:
            print(advantage)
    
    elif user_choice == 4:
        references = [
            "1. Zimbabwe Red Cross Society", 
            "2. Zimbabwe Ezekiel Guti University", 
            "3. Musa Commercial Farm"
        ]   
        for reference in references:
            print(reference) 
            

    elif user_choice == 5:
        contact_details = [
            "PHYSICAL ADDRESS :", 
            "6 Hampshire Drive, Eastlea, Harare", 
            "10117 Mineral Road Extension, Industrial Road", 
            
            "DIGITAL ADDRESS:", 
            "EMAIL : admin@adonaisecurity.co.zw / adonaisec@gmail.com", 
            "FACEBOOK : Adonai Security Services",
            "WEBSITE : www.adonaisecurity.co.zw", 
            
            "LANDLINE : +263 242 746089", 
            "CELL NUMBERS : +263 779713614 / +263 777735409"
        ]
        
        for contact in contact_details:
            print(contact )

    # Ask if the user wants to continue
    while True:
        continue_choice = input("Would you like to choose another option? (yes/no): ")
        if continue_choice.lower() == 'yes':
            break
        elif continue_choice.lower() == 'no':
            print("Thank you for contacting Adonai Security. Have a great day!")
            exit() # Exit the program
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")