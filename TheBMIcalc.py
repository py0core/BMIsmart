# Vars to store user input
height, weight, age = 0, 0, 0
heightinchmeter = "none"
weightkglb = "none"
# What system user is typing
metric_sys = False
# What the job of this calculator
print("Easy to use BMI calculator in Python!")
# what system user want to work with?
sys_chosed = input("For Metric system type m, for Imperial type i: ")
# change state of metric_sys
if sys_chosed is "m":
    #print("metric it is")
    metric_sys = True
    heightinchmeter = "cm"
    weightkglb = "kg"
elif sys_chosed is "i":
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

if metric_sys:
    bmi = round((weight/height/height) * 10000, 1)
    print(f"Your BMI is: {bmi}")
elif metric_sys == False:
    bmi = round((weight/(height ** 2)) * 703, 1)
    print(f"Your BMI is: {bmi}")
else:
    print("ERROR! something is wrong...")
    exit()
