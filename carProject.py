# We'll use this as the main file we use for the program.
# import os
# You can use os.system("clear") to clear the screen on the program.

FILE = "car_file.txt"

def options(myBrand, myMake):
    carFile = open(FILE, "w")
    uselessString = "Selected myBrand:", str(myBrand), "\n"
    carFile.write(str(uselessString))
    uselessString = "Selected make:", str(myMake), "\n"
    carFile.write(str(uselessString))
    carFile.write("Selected options:\n")
    carFile.close()
     
    
    # Ask user to select car options. Use Boolean logic to confirm user selections.
    invisibleHeadlights = ""
    
    hydraulics = ""
    
    prescriptionWindShield = ""
    
    loop = 0
    
    while(loop < 5):
     
        # should we wrap these in while loops to ensure users can't continue without making a proper choice?
        while(invisibleHeadlights == ""):
             
            try:
                option1 = input("Would you like to add Invisible Headlights to your vehicle? 'Yes' or 'No': ")
                if (option1.lower() == "yes"):
                    print("Invisible Headlights added to vehicle.")
                    selection1 = "Invisible Headlights"
                    loop +=1
                    break
                elif (option1.lower() == "no"):
                    selection1 = ("Invisible Head lights")
                    loop +=1
                    break
                else:
                    print("Could not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on invisible headlights
            except ValueError as e:
                print(e)

        while (hydraulics == ""):
            try:
                option2 = input("Would you like to add Hydraulics to your vehicle? 'Yes' or 'No': ")
                if (option2.lower() == "yes"):
                    print("Hydraulics added to your vehicle.")
                    selection2 = "Hydraulics"
                    loop +=1
                    break

                elif (option2.lower() == "no"):
                    selection2 = ("Hydraulics")
                    loop += 1
                    break
                else:
                    print("Could not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on hydraulics
            except ValueError as e:
                print(e)

        while (prescriptionWindShield == ""):
            try:
                option3 = input("Would you like to add a Prescription Wind Shield to your vehicle? 'Yes' or 'No': ")
                if (option3.lower() == "yes"):
                    print("Prescription wind shield has been added to your vehicle.")
                    selection3 = "Prescription wind shield"
                    loop += 1
                    break
                elif (option3.lower() == "no"):
                    selection3 = ("Prescription Wind Shield")
                    loop +=1 
                    break

                else:
                    print("Could not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on hydraulics
            except ValueError as e:
                print(e)
                      
        print("Are you satisfied with your selections:")
        print(selection2, option2)
        print(selection3, option3)
        print(selection1, option1)
        
        loop2 = 0
        while(loop2 == 0):
            try:
                satisfaction = input("yes or no")
                if(satisfaction.lower() == "yes"):
                    loop = 6
                    break
                elif (satisfaction.lower() == "no"):
                    loop = 3
                    break
                else:
                    print("Try again")
                    loop = 0
                    break
            except:
                print("I'm sorry enter yes or no")
    
    # Be able to pass in the make and model selections for writing to file.
    optionSelections = [selection1, "\n",
                        selection2, "\n",
                        selection3, "\n"]
    carFile = open(FILE, "a+")    
    carFile.write(str(optionSelections))
    carFile.close()
    
# End of options()

def main():
    isInProgram = True
    isPlacingOrder = False
    
    while(isInProgram == True):
        print("Welcome to the car program.")
        try:
            f = open(FILE, "r")
        except:
            print("You need to make a new file. Creating...")
            f = open(FILE, "r+")
        f.close()
            
        print("Please select your option:")
        print("1) Place an order")
        print("2) See your order")
        print("3) Exit program")
        
        try:
            mainSelect = int(input("Enter selection choice: "))
        except:
            print("Invalid input. Please enter a number that corresponds to the related option.\n")
            
        # THE CAR SELECTION CODE STARTS HERE
        if (mainSelect == 1):
            f = open(FILE, "w+")
            if (f.readline() != None or f.readline() != ""):
                
                try:
                    overwrite= int(input("Order already exists. Overwrite file? (1. Yes, 2. No)\n"))
    
                except ValueError as e:
                    print("Error, invalid input was selected. Please enter a number corresponding to the option.", e)
                    
                if (overwrite == 1):
                    isPlacingOrder = True
                elif (overwrite == 2):
                    return None
            while (isPlacingOrder == True):
                # Print your options for each car here.
                # This will be where all the options, makers, and models will be chosen and displayed.
                print("myBrands")
                print(''' 
                1.) Chrysalis
                2.) Insignia
                3.) Joplin''')
                try:
                    myBrandSelect = int(input("Please select a myBrand. (1-3)"))
                except ValueError as e:
                    print("Oops, Something Went Wrong: Select one of the myBrands (1-3)", e)
            
            
                if(myBrandSelect == 1):
                    myBrand = "Chrysalis"
                    print(myBrand, " has three different makes select one.")
                    print("1.)Highwayman ($40000) It's a two-door muscle car evocative of a 50s design.")
                    print("2.)Rangemaster ($20000) An old, beat-down pickup.")
                    print("3.)Pinto ($15000) You know what this is.")
              
                    try:              
                        Make = int(input("Please select a make. (1-3)"))
                    except ValueError as e:
                        print(e)
                    
                    if (Make == 1):
                        myMake = "Highwayman"
                        options(myBrandSelect, myMake)
                    elif(Make == 2):
                        myMake = "RangeMaster"
                        options(myBrandSelect, myMake)
                    elif(Make == 3):
                        myMake = "Pinto"
                        options(myBrandSelect, myMake)
                
                    print(" You chose a(n)", myBrand,":", myMake)
                    break
                    #isPlacingOrder = False
                 
                elif(myBrandSelect == 2):
                    myBrand = "Insignia"
                    print(myBrand, " has three different makes select one.")
                    print("1.)Hemoglobin ($35000) You can have your Hemoglobin in any color you want, so long as that color is red.")
                    print("2.)PX4 ($65000)")
                    print("3.)Misage ($70000) A sporty coup.")
                        
                    try:              
                        myMake = int(input("Please select a make. (1-3)"))
                    except ValueError as e:
                        print(e)
                    
                    if(myMake == 1):
                        myMake = "Hemoglobin"
                        options(myBrandSelect, myMake)
                    elif(myMake == 2):
                        myMake = "PX4"
                        options(myBrandSelect, myMake)
                    elif(myMake == 3):
                        myMake = "Misage"
                        options(myBrandSelect, myMake)
                    print("You chose a(n)", myBrand,":", myMake)
                    
                    isPlacingOrder = False
                 
                elif(myBrandSelect == 3):
                    myBrand = "Joplin"
                    print(myBrand, " has three different makes select one.")
                    print("1.) Phenidate ($50000) This totally isn't a drug reference.")
                    print("2.) PCP GT500 XXX 30cc 12V 3rd Edition ($75000)")
                    print("3.) Muriatic - Limited Supply Drive ($80000)")
                    
                    # Add Make selections, format just like myBrandSelect 1 and 2 section
                    try:
                        myMake = int(input("Please select a make. (1-3)"))
                    except ValueError as e:
                        print(e)
                    
                    if(myMake == 1):
                        myMake = "Phenidate"
                        options(myBrandSelect, myMake)
                    elif(myMake == 2):
                        myMake = "PCP GT500 XXX 30cc 12V 3rd Edition"
                        options(myBrandSelect, myMake)
                    elif(myMake == 3):
                        myMake = "Muriatic"
                        options(myBrandSelect, myMake)
                    print("You chose a(n)", myBrand, ":", myMake)
                    
                    isPlacingOrder = False
                
                elif(myBrandSelect < 1 or myBrandSelect > 3): 
                    print("Your option have to be 1,2, or 3.", ValueError)
              
        if (mainSelect == 2) :
            # Read the file in this section.
            # Print out the contents of the file, and then close the file.
            f = open(FILE, "r")
            if (f.readline() == "" or f.readline() == None) :
                print("No order has been placed.")
            else: 
                print(f.read())
            f.close()
          
        if (mainSelect == 3) :
            print("Thank you for shopping with Jay & the WhiteBoyz LLC.")
            exit()
          
        elif (mainSelect > 3 or mainSelect < 1):
            print("Invalid input. Please enter a number that corresponds to the related option.\n")
      
main()
