def main():
    lst = []
    val = input("Enter a value to add in list or press Enter to print List: ")

    while val:
        lst.append(val)
        val = input("Enter a value to add in list or press Enter to print List: ")

    print("Here's the list:", lst)



if __name__ == '__main__':
    main()