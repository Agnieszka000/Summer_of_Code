print("What is your weight (in kilograms)?")
weight = input()

print("What is your height (in metres)?")
height = input()

BMI = int(float(weight)/float(height)**2)

print("Your BMI is " + str(BMI))
