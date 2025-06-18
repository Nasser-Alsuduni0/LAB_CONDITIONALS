weight = float(input("Enter your Weight in kilograms :"))
height = float(input("Enter your height in Meters :"))
square_height = height * height
BMI = weight / square_height
if BMI < 18.5 :
    print("Underweight")
elif BMI <= 24.9 :
    print("Normal weight")
elif BMI <= 29.9 :
    print("Overweight") 
else :
    print("Obese")
