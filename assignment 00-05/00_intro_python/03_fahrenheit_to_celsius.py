def main():
    degrees_fahrenheit = float(input('Write temperature in Fahrenheit to convert in Celsius: '))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f'Temperature: {degrees_fahrenheit}F = {degrees_celsius}C')



if __name__ == '__main__':
    main()