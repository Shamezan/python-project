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
## A function to ask user input
## Error checking if users enter an alphabet instead of a number
def user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Please enter a number. ')

def additional():
            first_number = user_input('Enter the first number: ')
            second_number = user_input('Enter the second number: ')
            add = first_number + second_number
            print(f'The answer is: {add}')
    
def substract():
            first_number = user_input('Enter first number: ')
            second_number = user_input('Enter second number: ')
            subs = first_number - second_number
            print(f'The answer is: {subs}')
 
def multiply():
            first_number = user_input('Enter first number: ')
            second_number = user_input('Enter second number: ')
            mult = first_number * second_number
            print(f'The answer is: {mult}')


def divide():
            first_number = user_input('Enter first number: ')
            second_number = user_input('Enter second number: ')
            if second_number == 0:
                print('A number cannot divided by zero.')
            else:
                div = first_number / second_number
                print(f'The answer is: {div}')
     
def calculate(calculator):
    while True:
        try:
            task = input("Please enter an operation number or 'done' to finish: ").lower()
            if task == 'done':
                print('Goodbye!')
                break
            elif task == '1':
                additional()
            elif task == '2':
                substract()
            elif task == '3':
                multiply()
            elif task == '4':
                divide()
        except ValueError:
            print('Please insert listed operation number only. ')
    
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

if __name__ == '__main__':
    main()
