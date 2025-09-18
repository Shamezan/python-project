## Hi! I created a simple calculator project
## Only involved basic arithmetic like addition, subtraction, multiplication, and division
## Next time, I may create an advanced calculator
## That can do complex maths like differential equations

## A function to display the operations menu
def display_calc(calculator):
    print('\n--- Calculator ---')
    for operation_number, operation_name in calculator.items():
        print(f'{operation_number}. {operation_name['operation']}')
    print('------------------')
## addition operation
def additional():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    add = int(first_number) + int(second_number)
    print('The answer is: ' + str(add))
## subtract operation
def substract():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    if second_number > first_number:
        subs = second_number - first_number
        print('-' + subs)
    elif second_number < first_number:
        subs = first_number + second_number
        print('The answer is: ' + str(subs))
    else:
        print('error')
 ## multiply operation
def multiply():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    mult = first_number * second_number
    print('The answer is: ' + str(mult))
## division operation
def divide():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    if second_number == 0:
        print('A number cannot divided by zero.')
    else:
        div = first_number / second_number
        print('The answer is: ' + str(div))
## ask user which operation they want
def calculate(calculator):
    while True:
        task = input("Please enter an operation number or 'done' to finish: ").lower()
        if task == 'done':
            break
        elif task == '1':
            additional()
        elif task == '2':
            substract()
        elif task == '3':
            multiply()
        elif task == '4':
            divide()
        else:
            print('Error')
## The main function
def main():
    """Main function for calculator"""
    calculator = {
        1: {'operation': 'addition'},
        2: {'operation': 'substraction'},
        3: {'operation': 'multiplication'},
        4: {'operation': 'division'}
    }
    print('\nCalculate simple arithmetic')
    display_calc(calculator)
    user_task = calculate(calculator)
## Only run the main function
if __name__ == '__main__':
    main()
    
    
    
     

