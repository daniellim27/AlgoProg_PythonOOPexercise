from FancyShoppingListJS import FancyShoppingListJS


def create_shopping_list():
    shopping_list = []
    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))

    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food = input("Enter food: ")
        amount = float(input("Enter amount of pounds: "))
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))
        shopping_list.append(FancyShoppingListJS(food, amount))

    return shopping_list


def display_shopping_list(shopping_list):
    for item in shopping_list:
        print(item)
        print()


def calculate_total_cost(shopping_list):
    total_cost = sum(item.calculate_cost() for item in shopping_list)
    return total_cost

def main():
    shopping_list = create_shopping_list()
    print("\nHere's a summary of the items purchased:")
    display_shopping_list(shopping_list)
    total_cost = calculate_total_cost(shopping_list)
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
