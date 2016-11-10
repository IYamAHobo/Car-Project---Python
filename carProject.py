# We'll use this as the main file we use for the program.
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
    isPlacingOrder = True
    while (isPlacingOrder == True) :
      # Print your options for each car here.
      # This will be where all the options, makers, and models will be chosen and displayed.
      
  if (mainSelect == 2) :
      # Read the file in this section.
      # Print out the contents of the file, and then close the file.
      
  if (mainSelect == 3) :
    exit()
      
  else :
    print("Invalid input. Please enter a number that corresponds to the related option.\n")
  
main()
