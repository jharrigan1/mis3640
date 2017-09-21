#Exercise 1
def calculate_BMI(weight, height):
    BMI = 703 * (weight/height**2)

    if BMI <=18.5:
        print('Your BMI is {:.1f}.'.format(BMI))
        print('Underweight')
    elif BMI >=18.5<=24.9:
        print('Your BMI is {:.1f}.'.format(BMI))
        print('Normal weight')
    elif BMI >= 25<=29.9:
        print('Your BMI is {:.1f}.'.format(BMI))
        print('Overweight')
    else:
        print('Obese')

weight = input('How much do you weigh (in pounds)? ')
weight = float(weight)
height = input('How tall are you (inches)? ')   
height = float(height)
calculate_BMI(weight, height)