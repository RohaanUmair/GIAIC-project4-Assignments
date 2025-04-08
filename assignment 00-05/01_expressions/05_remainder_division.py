def main():
    dividend = int(input('Please enter an integer to be divided: '))
    divisor = int(input('Please enter an integer to divid by: '))

    quotient, remainder = divmod(dividend, divisor)

    print(f'The result of this division is {quotient} with a remainder of {remainder}')


if __name__ == '__main__':
    main()