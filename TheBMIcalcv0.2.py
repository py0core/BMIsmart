# Vars to store user input
height, weight, age = 0, 0, 0
heightinchmeter = "none"
weightkglb = "none"
# What system user is typing
metric_sys = False
# What the job of this calculator
print("Easy to use BMI calculator in Python!\n")#v0.2 added \n for making it look better
# what system user want to work with? #updatev0.2-select by number for easier understanding
sys_chosed = int(input("For Metric system press 1, for Imperial press 2: "))

#functions
#MetricBMIfunction
def metricBMIcalcFormula (w, h):
    bmi = round((w/h/h) * 10000, 1)
    return bmi
#ImperialBMIfunction
def imperialBMIcalcFormula (w, h):
    bmi = round((w/(h ** 2)) * 703, 1)
    return bmi

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

else:
    print("ERROR! simple instructions... try again.")
    exit()

# Ask for user input
height = int(input("Type your height in " + heightinchmeter + ": "))
weight = int(input("Type your weight in " + weightkglb + ": "))
#age = int(input ("Type your age: ")) #feature to add, give information if BMI is good or bad.

# ***No need to test if int as the input already have to be in INT and program will exit on other type.***
#if not isinstance(weight, int) and not isinstance(height,int):
#    print("Please input only numbers.")
#    exit()
if metric_sys:
    bmi = metricBMIcalcFormula(weight, height)
    print(f"Your BMI is: {bmi}")

else:
    bmi = imperialBMIcalcFormula(weight, height)
    print(f"Your BMI is: {bmi}")
