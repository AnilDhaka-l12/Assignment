def tester(givenstring="Too short"):
    if len(givenstring) >= 10:
        print(givenstring)
    else:
        print("Too short")
def main():
    while True:
        user_input = input("Write something (quit ends): ")
        if user_input.lower() == "quit":
            break
        tester(user_input)
if __name__ == "__main__":
    main()
