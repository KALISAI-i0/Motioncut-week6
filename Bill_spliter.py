import time

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Number must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_names(n):
    names = []
    for i in range(n):
        name = input(f"Enter name for person {i+1}: ")
        if name.strip() == "":
            name = f"Person {i+1}"
        names.append(name)
    return names


def split_evenly(total, names):
    n = len(names)
    share = round(total / n, 2)

    print("\n--- Even Split ---")
    for name in names:
        print(f"{name} pays: ₹{share}")

    return {name: share for name in names}


def split_by_percentage(total, names):
    percentages = []
    total_percent = 0

    print("\nEnter percentages for each person:")

    for name in names:
        while True:
            try:
                percent = float(input(f"{name}: "))
                if percent < 0:
                    print("Percentage cannot be negative.")
                else:
                    percentages.append(percent)
                    total_percent += percent
                    break
            except ValueError:
                print("Invalid input.")

    if round(total_percent, 2) != 100:
        print("\nError: Total percentage must equal 100%.")
        return None

    print("\n--- Uneven Split ---")
    result = {}
    for i in range(len(names)):
        amount = round((percentages[i] / 100) * total, 2)
        print(f"{names[i]} pays: ₹{amount}")
        result[names[i]] = amount

    return result


def save_to_file(data):
    choice = input("\nDo you want to save results to a file? (y/n): ").lower()
    if choice == 'y':
        filename = "bill_split.txt"
        with open(filename, "a") as f:
            f.write("\n--- Bill Split Result ---\n")
            for name, amount in data.items():
                f.write(f"{name}: ₹{amount}\n")
        print(f"Saved to {filename}")


def main():
    print("💰 Welcome to Bill Splitter!")

    while True:
        total = get_float_input("\nEnter total bill amount: ₹")
        num_people = get_int_input("Enter number of people: ")

        names = get_names(num_people)

        print("\nChoose split method:")
        print("1. Even Split")
        print("2. Uneven Split (Percentage)")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            result = split_evenly(total, names)

        elif choice == "2":
            result = split_by_percentage(total, names)
            if result is None:
                continue

        else:
            print("Invalid choice.")
            continue

        save_to_file(result)

        again = input("\nDo another split? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for using Bill Splitter! 👋")
            break

        time.sleep(1)


if __name__ == "__main__":
    main()
