# We'll use this as the main file we use for the program.
FILE = "Insert filepath here"
def main():

  
  print("Welcome to the car program.")
  try:
    f = open(FILE, "r")
  except:
    print("You need to make a new file. Creating...")
    f = open(FILE, "r+")
  
  print("Please select your option:")
  print("1) Place an order")
  print("2) See your order")
  print("3) Exit program")
  
main()
