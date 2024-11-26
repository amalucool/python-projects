try:
  x = open("demofile.txt")
  try:
    x.write("Amal Dcruz")
  except:
    print("Something went wrong when writing to the file")
  finally:
    x.close()
except:
  print("FileNotFoundError, the file you have given is refusing to open")