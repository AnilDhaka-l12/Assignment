def main():
    products = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0
    print("Supermarket\n===========")
    while True:
        try:
            selection = int(input("Please select product (1-10) 0 to Quit: ").strip())

            if selection == 0:
                break
            elif 1 <= selection <= 10:
                price = products[selection - 1]
                total_sum += price
                print(f"Product: {selection} Price: {price}")
            else:
                print("Invalid selection. Please choose a number between 1 and 10, or 0 to quit.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Total: {total_sum}")

    try:
        payment = float(input("Payment: ").strip())
        if payment >= total_sum:
            change = payment - total_sum
            print(f"Change: {change}")
        else:
            print("Insufficient payment. Please try again.")
    except ValueError:
        print("Invalid payment amount.")

if __name__ == "__main__":
    main()
