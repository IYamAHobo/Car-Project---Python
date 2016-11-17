# We'll use this as the main file we use for the program.
# import os
# You can use os.system("clear") to clear the screen on the program.
FILE = "Insert filepath here"
def main():

  isInProgam = True
  isPlacingOrder = False
  
  while(isInProgram == True) :
  print("Welcome to the car program.")
  try:
    f = open(FILE, "r")
    f.readline()
  except:
    print("You need to make a new file. Creating...")
    f = open(FILE, "r+")
  
  print("Please select your option:")
  print("1) Place an order")
  print("2) See your order")
  print("3) Exit program")

  
  try:
    mainSelect = int(input())
  except:
    print("Invalid input. Please enter a number that corresponds to the related option.\n")
    
  # THE CAR SELECTION CODE STARTS HERE
  if (mainSelect == 1) :
    if (f.readline() != null or f.readline() != ""):
      try: 
        overwrite= int(input("Order already exists. Overwrite file? (1. Yes, 2. No)\n")
      except TypeError :
        print("Error, invalid input was selected. Please enter a number corresponding to the option.")
      if (overwrite == 1):
        isPlacingOrder = True
      elif (overwrite == 2):
        return null
      else :
        print("Invalid input. Please enter a number corresponding to the option.")
    while (isPlacingOrder == True) :
      # Print your options for each car here.
      # This will be where all the options, makers, and models will be chosen and displayed.
        print("Brands")
        print(''' 
        1.) Chrysalis
        2.) Insignia
        3.) Joplin''')
        try:
          myBrand = int(input("Please select a Brand. (1-3)"))
        except Value Error as e:
          print("Oops, Something Went Wrong: Select one of the Brands (1-3)", e)
        
        
        if(myBrand == 1):
          brand = "Chrysalis"
          print(brand, " has three different makes select one.")
          print("1.)Highwayman ($40000) It's a two-door muscle car evocative of a 50s design.")
          print("2.)Rangemaster ($20000) An old, beat-down pickup.")
          print("3.)Pinto ($15000) You know what this is.")
      
          try:              
            myMake = int(input("Please select a make. (1-3)"))
          except ValueError as e:
            print(e)
            
          if (myMake == 1):
            myMake = "Highwayman"
          elif(myMake == 2):
            myMake = "RangeMaster"
          elif(myMake == 3):
            myMake = "Pinto"
          print(" You chose a(n)", Chrysalis,":", myMake)
         
         elif(myBrand == 2):
          brand = "Insignia"
          print(brand, " has three different makes select one.")
          print("1.)Hemoglobin ($35000) You can have your Hemoglobin in any color you want, so long as that color is red.")
          print("2.)PX4 ($65000)")
          print("3.)Misage ($70000) A sporty coup.")
                
           try:              
            myMake = int(input("Please select a make. (1-3)"))
          except ValueError as e:
            print(e)
            
          if (myMake == 1):
            myMake = "Hemoglobin"
          elif(myMake == 2):
            myMake = "PX4"
          elif(myMake == 3):
            myMake = "Misage"
          print(" You chose a(n)", brand,":", myMake)
         
        elif(myBrand == 3):
          brand = "Joplin"
          print(brand, " has three different makes select one.")
          print("1.)Phenidate ($50000) This totally isn't a drug reference.")
          print("PCP GT500 XXX 30cc 12V 3rd Edition ($75000)")
          print("Muriatic - Limited Supply Drive ($80000)")
          
        elif(myBrand < 1 or myBrand > 3):
            raise ValueError = ("Your option have to be 1,2, or 3.")
          
 if (mainSelect == 2) :
      # Read the file in this section.
      # Print out the contents of the file, and then close the file.
      f = open(FILE, r)
      if (f.readline() == "" or f.readline() == null) :
        print("No order has been placed.")
      else: 
        print(f.read())
      f.close()
      
  if (mainSelect == 3) :
    print("Thank you for shopping with Jay & the WhiteBoyz LLC.")
    exit()
      
  else :
    print("Invalid input. Please enter a number that corresponds to the related option.\n")
  
main()
