import datetime

# parent class
class VehicleRent:
    DISCOUNT_RATE = 0.2

    def __init__(self, stock):
        self.stock = stock

    def displayStock(self):
        print("{} vehicles available to rent".format(self.stock))
        return self.stock

    def rentHourly(self, n, vehicle_type, h_price):
        return self._rentVehicle(n, vehicle_type, h_price, "hourly")

    def rentDaily(self, n, vehicle_type, d_price):
        return self._rentVehicle(n, vehicle_type, d_price, "daily")

    def _rentVehicle(self, n, vehicle_type, price, rental_type):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicles available to rent".format(self.stock))
            return None
        else:
            self.stock -= n
            now = datetime.datetime.now()
            print("Rented {} {} for {} at {} hours".format(n, vehicle_type, rental_type, now.hour))
            return now

    def returnVehicle(self, request, brand, h_price, d_price, discount_threshold):
        rental_time, rental_basis, num_of_vehicle = request
        bill = 0

        if brand in ["car", "motorcycle"]:
            if all([rental_time, rental_basis, num_of_vehicle > 0]):
                self.stock += num_of_vehicle
                now = datetime.datetime.now()
                rental_period_hours = (now - rental_time).total_seconds() / 3600

                price_per_unit = h_price if rental_basis == "hourly" else d_price
                bill = self._calculateBill(rental_period_hours, price_per_unit, num_of_vehicle)

                if num_of_vehicle >= discount_threshold:
                    print("You have an extra 20% discount")
                    bill = self._applyDiscount(bill)

                print("Thank you for returning your {}".format(brand))
                print("Price: $ {}".format(bill))
                return bill
            else:
                print("Invalid return request")
        else:
            print("Invalid vehicle brand")
        return None

    def _calculateBill(self, rental_period, price_per_unit, num_of_vehicle):
        return rental_period * price_per_unit * num_of_vehicle

    def _applyDiscount(self, bill):
        discounted_bill = bill - (bill * self.DISCOUNT_RATE)
        return discounted_bill

# child class
class CarRent(VehicleRent):
    DISCOUNT_THRESHOLD_CAR = 2
    CAR_HOURLY_PRICE = 10
    CAR_DAILY_PRICE = CAR_HOURLY_PRICE * 0.8 * 24

    def __init__(self, stock):
        super().__init__(stock)

    def rentHourly(self, n):
        return super().rentHourly(n, "car", self.CAR_HOURLY_PRICE)

    def rentDaily(self, n):
        return super().rentDaily(n, "car", self.CAR_DAILY_PRICE)

# child class 2
class MotorcycleRent(VehicleRent):
    DISCOUNT_THRESHOLD_MOTORCYCLE = 4
    MOTORCYCLE_HOURLY_PRICE = 5
    MOTORCYCLE_DAILY_PRICE = MOTORCYCLE_HOURLY_PRICE * 0.8 * 24

    def __init__(self, stock):
        super().__init__(stock)

    def rentHourly(self, n):
        return super().rentHourly(n, "motorcycle", self.MOTORCYCLE_HOURLY_PRICE)

    def rentDaily(self, n):
        return super().rentDaily(n, "motorcycle", self.MOTORCYCLE_DAILY_PRICE)

class Customer:
    def __init__(self):
        self.vehicles = {'car': {'count': 0, 'rentalBasis': 0, 'rentalTime': 0},
                         'motorcycle': {'count': 0, 'rentalBasis': 0, 'rentalTime': 0}}

    def requestVehicle(self, brand):
        count_key = 'count'
        rental_basis_key = 'rentalBasis'
        rental_time_key = 'rentalTime'

        if brand == "motorcycle" or brand == "car":
            count = input(f"How many {brand}s would you like to rent?: ")

            try:
                count = int(count)
            except ValueError:
                print("Number should be a number")
                return -1

            if count < 1:
                print(f"Number of {brand}s should be greater than zero")
                return -1

            self.vehicles[brand][count_key] = count
            self.vehicles[brand][rental_basis_key] = 1  # Default to hourly basis
            self.vehicles[brand][rental_time_key] = datetime.datetime.now()

            return count, self.vehicles[brand][rental_time_key]
        else:
            print("Invalid vehicle brand")
            return -1

    def returnVehicle(self, brand):
        count_key = 'count'
        rental_basis_key = 'rentalBasis'
        rental_time_key = 'rentalTime'

        if brand == "motorcycle" or brand == "car":
            if all([self.vehicles[brand][rental_time_key], self.vehicles[brand][count_key] > 0]):
                return (
                    self.vehicles[brand][rental_time_key],
                    self.vehicles[brand][rental_basis_key],
                    self.vehicles[brand][count_key]
                )
            else:
                print(f"You have not rented any {brand}s.")
        else:
            print("Invalid vehicle brand for return")
        return 0, 0, 0
