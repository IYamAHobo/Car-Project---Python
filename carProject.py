# We'll use this as the main file we use for the program.
FILE = "Insert filepath here"
def main():

  
  print("Welcome to the car program.")
  try:
    f = open(FILE, "r")
  except:
    print("You need to make a new file. Creating...")
    f = open(FILE, "w")
  
  
  
main()
