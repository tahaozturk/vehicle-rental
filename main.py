from rent import CarRent, MotorcycleRent, Customer

def display_menu():
    print("""
    *******************
    Vehicle Rental Shop
    A. Motorcycle Menu
    B. Car Menu
    Q. Exit
    *******************
    """)

def motorcycle_menu():
    print("""
    *******************
    MOTORCYCLE MENU
    1. Display available motorcycles
    2. Request a motorcycle on an hourly basis $ 5
    3. Request a motorcycle on a daily basis $ 84
    4. Return a motorcycle
    5. Main Menu
    6. Exit
    *******************
    """)

def car_menu():
    print("""
    *******************
    CAR MENU
    1. Display available cars
    2. Request a car on an hourly basis $ 10
    3. Request a car on a daily basis $ 192
    4. Return a car
    5. Main Menu
    6. Exit
    *******************
    """)

def get_user_choice():
    return input("Enter choice: ").upper()

def process_motorcycle_choice(choice, customer, motorcycle):
    if choice == "1":
        motorcycle.displayStock()
    elif choice == "2":
        count, rental_time = customer.requestVehicle("motorcycle")
        customer.rentalTime_m = motorcycle.rentHourly(count)
    elif choice == "3":
        count, rental_time = customer.requestVehicle("motorcycle")
        customer.rentalTime_m = motorcycle.rentDaily(count)
    elif choice == "4":
        request = customer.returnVehicle("motorcycle")
        customer.bill = motorcycle.returnVehicle(
            request, "motorcycle", MotorcycleRent.MOTORCYCLE_HOURLY_PRICE, MotorcycleRent.MOTORCYCLE_DAILY_PRICE,
            MotorcycleRent.DISCOUNT_THRESHOLD_MOTORCYCLE
        )
        customer.rentalBasis_m, customer.rentalTime_m, customer.motorcycles = 0, 0, 0
    elif choice == "5":
        pass
    elif choice == "6":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid input. Please enter a number between 1-6")

def process_car_choice(choice, customer, car):
    if choice == "1":
        car.displayStock()
    elif choice == "2":
        count, rental_time = customer.requestVehicle("car")
        customer.rentalTime_c = car.rentHourly(count)
    elif choice == "3":
        count, rental_time = customer.requestVehicle("car")
        customer.rentalTime_c = car.rentDaily(count)
    elif choice == "4":
        request = customer.returnVehicle("car")
        customer.bill = car.returnVehicle(
            request, "car", CarRent.CAR_HOURLY_PRICE, CarRent.CAR_DAILY_PRICE, CarRent.DISCOUNT_THRESHOLD_CAR
        )
        customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0, 0, 0
    elif choice == "5":
        pass
    elif choice == "6":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid input. Please enter a number between 1-6")

def main():
    motorcycle = MotorcycleRent(100)
    car = CarRent(10)
    customer = Customer()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "A":
            motorcycle_menu()
            motorcycle_choice = get_user_choice()
            process_motorcycle_choice(motorcycle_choice, customer, motorcycle)

        elif choice == "B":
            car_menu()
            car_choice = get_user_choice()
            process_car_choice(car_choice, customer, car)

        elif choice == "Q":
            print("Exiting the program.")
            break

        else:
            print("Invalid input. Please enter A, B, or Q.")

    print("Thank you for using the vehicle rental shop")

if __name__ == "__main__":
    main()
