w = float(input("Weight: "))
o = input("in KG or Lbs: ")
o = o.upper()

if "K" in o: #searches string for substring
    w = w * 2.205
    print("Weight in Pounds is " + str(w))

elif "L" in o:
    w = w / 2.205
    print("Weight in Kg is " + str(w))

