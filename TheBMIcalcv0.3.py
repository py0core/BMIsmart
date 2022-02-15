# Vars to store user input
from tkinter import NONE


height, weight, age = 0, 0, 0
heightinchmeter = "none"
weightkglb = "none"
# What system user is typing
metric_sys = False
sys_chosed = "none"

#functions
#MetricBMIfunction
def metricBMIcalcFormula (w, h):
    bmi = round((int(w)/int(h)/int(h)) * 10000, 1)
    return bmi
#ImperialBMIfunction
def imperialBMIcalcFormula (w, h):
    bmi = round((int(w)/(int(h) ** 2)) * 703, 1)
    return bmi
# check if input is in correct type
def checkit(x, y):
    try:
        int(x)
        int(y)
        #print("all good")#DEBUGGING
    except ValueError:
        print("Please input only numbers.")
        return False
        #exit()
# check if right input on system 1 or 2.
def checksystemchoose(x):
    if x is not 1 and x is not 2:
        print("Please input only 1 or 2.")
        #exit()
    else:
        pass
# What the job of this calculator
print("Easy to use BMI calculator in Python!\n")#v0.2 added \n for making it look better
# what system user want to work with? #updatev0.2-select by number for easier understanding
# entering a loop to prevent exit of the program on wrong answer
while sys_chosed != 1 and sys_chosed != 2:
    sys_chosed = input("For Metric system press 1, for Imperial press 2: ")
    #check is the inuput only numbers
    #if not continue the loop until user got it right
    if checkit(sys_chosed, sys_chosed) == False:
        continue
    else:
        #cast to int for calculation
        sys_chosed = int(sys_chosed)
        #check if right input on system, numbers 1 or 2
        checksystemchoose(sys_chosed)
        # if everything right continue with the program



# change state of metric_sys
if sys_chosed == 1:
    #print("metric it is")
    metric_sys = True
    heightinchmeter = "cm"
    weightkglb = "kg"

elif sys_chosed == 2:
    #print("imperial it is")
    metric_sys = False
    heightinchmeter = "inches"
    weightkglb = "lbs"

# Ask for user input
height = input("Type your height in " + heightinchmeter + ": ")
weight = input("Type your weight in " + weightkglb + ": ")
#age = int(input ("Type your age: ")) #feature to add, give information if BMI is good or bad.

# ***No need to test if int as the input already have to be in INT and program will exit on other type.***
#if not isinstance(weight, int) and not isinstance(height,int):
#   print("Please input only numbers.")
#   exit()

checkit(height, weight)

if metric_sys:
    bmi = metricBMIcalcFormula(weight, height)
    print(f"Your BMI is: {bmi}")

else:
    bmi = imperialBMIcalcFormula(weight, height)
    print(f"Your BMI is: {bmi}")
