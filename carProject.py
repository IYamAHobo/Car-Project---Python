# Authors: Jayveon Jackson, Esteban Valero, Elliot Flores
# Project: Car Ordering Program
# Date: 11/30/2016
# Instructor: Joe Bryan

FILE = "car_file.txt"

def options(myBrand, myMake, cost, name):
    carFile = open(FILE, "w")
    
    carFile.write("Order for: ")
    carFile.write(name)
    carFile.write("\n")
    
    carFile.write(str(myBrand))
    carFile.write(" ")
    carFile.write(str(myMake))
    
    carFile.close()
     
    
    # Ask user to select car options. Use Boolean logic to confirm user selections.
    hasInvisibleHeadlights = False
    
    hasHydraulics = False
    
    hasPrescriptionWindShield = False
    
    loop = 0
    
    while(loop < 5):
     
        # should we wrap these in while loops to ensure users can't continue without making a proper choice?
        while(loop <= 0):
             
            try:
                option1 = input("\nWould you like to add Invisible Headlights to your vehicle? 'Yes' or 'No': ")
                if (option1.lower() == "yes"):
                    print("Invisible Headlights added to vehicle.")
                    hasInvisibleHeadlights = True
                    cost += 500
                    loop +=1
                    break
                elif (option1.lower() == "no"):
                    loop +=1
                    break
                else:
                    print("\nCould not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on invisible headlights
            except ValueError as e:
                print(e)

        while (loop <= 1):
            try:
                option2 = input("\nWould you like to add Hydraulics to your vehicle? 'Yes' or 'No': ")
                if (option2.lower() == "yes"):
                    print("Hydraulics added to your vehicle.")
                    hasHydraulics = True
                    cost += 1000
                    loop +=1
                    break

                elif (option2.lower() == "no"):
                    loop += 1
                    break
                else:
                    print("\nCould not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on hydraulics
            except ValueError as e:
                print(e)

        while (loop <= 2):
            try:
                option3 = input("\nWould you like to add a Prescription Wind Shield to your vehicle? 'Yes' or 'No': ")
                if (option3.lower() == "yes"):
                    print("Prescription wind shield has been added to your vehicle.")
                    hasPrescriptionWindShield = True
                    cost += 2000
                    loop += 1
                    break
                elif (option3.lower() == "no"):
                    loop +=1 
                    break

                else:
                    print("\nCould not understand your selection choice. Please try again.")
                    # add a way to force user back to top to make a choice on hydraulics
            except ValueError as e:
                print(e)
                      
        print("\nAre you satisfied with your selections?")
        if (hasInvisibleHeadlights):
            print("Invisible Headlights")
        if (hasHydraulics) :
            print("Hydraulics")
        if (hasPrescriptionWindShield) :
            print("Prescription Windshield")
         
        loop2 = 0
        while(loop2 == 0):
            try:
                satisfaction = input("\nEnter 'Yes' or 'No': ")
                if(satisfaction.lower() == "yes"):
                    loop = 6
                    break
                elif (satisfaction.lower() == "no"):
                    loop = 0
                    break
                else:
                    print("\nPlease try again.")
                    loop = 0
                    break
            except:
                print("\nPlease enter 'Yes' or 'No': ")
    
    # Be able to pass in the make and model selections for writing to file.
    carFile = open(FILE, "a+")
    carFile.write(" with ")
    carFile.write("\n")
    
    if (not hasHydraulics and not hasInvisibleHeadlights and not hasPrescriptionWindShield) :
        carFile.write("No add-ons")
    if (hasInvisibleHeadlights) :
        carFile.write("Invisible Headlights ")
    if (hasHydraulics) :
        carFile.write("Hydraulics ")
    if (hasPrescriptionWindShield) :
        carFile.write("Prescription Windshield ")
        
    carFile.write("\n")
    carFile.write("Total Cost: $")
    carFile.write(str(cost))
    
    carFile.close()
    
# End of options()

def main():
    isInProgram = True
    isPlacingOrder = False
    
    print("Welcome to the car ordering program!")
    
    while(isInProgram == True):
        #print("Welcome to the car program.")
        try:
            f = open(FILE, "r")
        except:
            print("You need to make a new file. Creating...")
            f = open(FILE, "w")
        f.close()
            
        print("\nPlease make a selection:")
        print("1) Place an order")
        print("2) See your order")
        print("3) Exit program")
        
        try:
            mainSelect = int(input("\nEnter selection choice: "))
        except:
            print("Invalid input. Please enter a number that corresponds to the related option.\n")
            
        # THE CAR SELECTION CODE STARTS HERE
        if (mainSelect == 1):
            f = open(FILE, "w+")
            if (f.readline() != None or f.readline() != ""):
                
                try:
                    overwrite= int(input("Order already exists. Overwrite file? (1. Yes, 2. No): "))
    
                except ValueError as e:
                    print("Error, invalid input was selected. Please enter a number corresponding to the option.", e)
                    
                if (overwrite == 1):
                    isPlacingOrder = True
                elif (overwrite == 2):
                    return None
            while (isPlacingOrder == True):
                # Print your options for each car here.
                # This will be where all the options, makers, and models will be chosen and displayed.
                orderName = input("\nPlease enter a name for the order: ")
                print("\n\nManufacturer brands:")
                print("1.) Chrysalis")
                print("2.) Insignia")
                print("3.) Joplin")
                
                try:
                    myBrandSelect = int(input("\nPlease select a manufacturer brand (1 - 3): "))
                except ValueError as e:
                    print("\nOops, Something Went Wrong: Select one of the myBrands (1 - 3)", e)
            
            
                if(myBrandSelect == 1):
                    print("\n")
                    myBrand = "Chrysalis"
                    print(myBrand, "has three different models:")
                    print("1.) Highwayman ($40000)")
                    print("2.) Rangemaster ($20000)")
                    print("3.) Pinto ($15000)")
              
                    try:              
                        Make = int(input("\nPlease select a vehicle model (1 - 3): "))
                    except ValueError as e:
                        print(e)
                    
                    if (Make == 1):
                        myMake = "Highwayman"
                        myCost = 40000
                        options(myBrand, myMake, myCost, orderName)
                    elif(Make == 2):
                        myMake = "RangeMaster"
                        myCost = 20000
                        options(myBrand, myMake, myCost, orderName)
                    elif(Make == 3):
                        myMake = "Pinto"
                        myCost = 15000
                        options(myBrand, myMake, myCost, orderName)
                
                    print("\nYou chose a(n)", myBrand,":", myMake)
                    break
                    #isPlacingOrder = False
                 
                elif(myBrandSelect == 2):
                    print("\n")
                    myBrand = "Insignia"
                    print(myBrand, "has three different models:")
                    print("1.) Hemoglobin ($35000)")
                    print("2.) PX4 ($65000)")
                    print("3.) Misage ($70000)")
                        
                    try:              
                        myMake = int(input("\nPlease select a vehicle model (1 - 3): "))
                    except ValueError as e:
                        print(e)
                    
                    if(myMake == 1):
                        myMake = "Hemoglobin"
                        myCost = 35000
                        options(myBrand, myMake, myCost, orderName)
                    elif(myMake == 2):
                        myMake = "PX4"
                        myCost = 65000
                        options(myBrand, myMake, myCost, orderName)
                    elif(myMake == 3):
                        myMake = "Misage"
                        myCost = 70000
                        options(myBrand, myMake, myCost, orderName)
                    print("\nYou chose a(n)", myBrand,":", myMake)
                    
                    isPlacingOrder = False
                 
                elif(myBrandSelect == 3):
                    print("\n")
                    myBrand = "Joplin"
                    print(myBrand, "has three different models:")
                    print("1.) Phenidate ($50000)")
                    print("2.) PCP GT500 XXX 30cc 12V 3rd Edition ($75000)")
                    print("3.) Muriatic - Limited Supply Drive ($80000)")
                    
                    # Add Make selections, format just like myBrandSelect 1 and 2 section
                    try:
                        myMake = int(input("\nPlease select a vehicle model (1 -3 ): "))
                    except ValueError as e:
                        print(e)
                    
                    if(myMake == 1):
                        myMake = "Phenidate"
                        myCost = 50000
                        options(myBrand, myMake, myCost, orderName)
                    elif(myMake == 2):
                        myMake = "PCP GT500 XXX 30cc 12V 3rd Edition"
                        myCost = 75000
                        options(myBrand, myMake, myCost, orderName)
                    elif(myMake == 3):
                        myMake = "Muriatic"
                        myCost = 80000
                        options(myBrand, myMake, myCost, orderName)
                    print("\nYou chose a(n)", myBrand, ":", myMake)
                    
                    isPlacingOrder = False
                
                elif(myBrandSelect < 1 or myBrandSelect > 3): 
                    print("You must select 1, 2, or 3.", ValueError)
              
        if (mainSelect == 2) :
            # Read the file in this section.
            # Print out the contents of the file, and then close the file.
            for line in open(FILE) :
                if (line == "" or line == None):
                    print("No order has been placed.")
                print(line)
          
        if (mainSelect == 3) :
            print("\nThank you for shopping with Jay & the WhiteBoyz LLC.")
            exit()
          
        elif (mainSelect > 3 or mainSelect < 1):
            print("\nInvalid input. Please enter a number that corresponds to the related option.\n")
      
main()
