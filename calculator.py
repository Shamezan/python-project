
def display_calc(calculator):
    print('\n--- Calculator ---')
    for operation_number, operation_name in calculator.items():
        print(f'{operation_number}. {operation_name['operation']}')
    print('------------------')

def additional():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    add = int(first_number) + int(second_number)
    print('The answer is: ' + str(add))

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
 
def multiply():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    mult = first_number * second_number
    print('The answer is: ' + str(mult))

def divide():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    if second_number == 0:
        print('A number cannot divided by zero.')
    else:
        div = first_number / second_number
        print('The answer is: ' + str(div))


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
    
    
    
     
