class DeliveryDetails:
    """
    Subsystem for handling delivery details.
    """
    def __init__(self, date_time: str):
        self.date_time = date_time

    def get_delivery_date_time(self) -> str:
        return self.date_time

class PickupLocation:
    """
    Subsystem for handling pickup locations.
    """
    def __init__(self, location: str):
        self.location = location

    def get_pickup_location(self) -> str:
        return self.location

class CustomerDetails:
    """
    Subsystem for handling customer details.
    """
    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address

    def get_customer_info(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address
        }

class Order_Customizer:
    """
    Facade class which simplifies the order customization process.
    """
    def __init__(self):
        self.delivery_details = DeliveryDetails
        self.pickup_location = PickupLocation
        self.customer_details = CustomerDetails

    def customize_order(self) -> dict:
        date_time = input("Enter delivery date and time (YYYY-MM-DD HH:MM): ")
        location = input("Enter pickup location: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your delivery address: ")

        delivery = self.delivery_details(date_time).get_delivery_date_time()
        pickup = self.pickup_location(location).get_pickup_location()
        customer = self.customer_details(name, email, address).get_customer_info()

        return {
            "delivery_details": delivery,
            "pickup_location": pickup,
            "customer_details": customer
        }

def client_code(order_customizer: Order_Customizer) -> None:
    """
    The client code that uses the facade to simplify the process of customizing an order.
    :param order_customizer:
    :return:
    """
    order_details = order_customizer.customize_order()
    print("Order Details:")
    print(f"Delivery Date and Time: {order_details['delivery_details']}")
    print(f"Pickup Location: {order_details['pickup_location']}")
    print(f"Customer Name: {order_details['customer_details']['name']}")
    print(f"Customer Email: {order_details['customer_details']['email']}")
    print(f"Customer Address: {order_details['customer_details']['address']}")

if __name__ == "__main__":
    order_customizer = Order_Customizer()
    client_code(order_customizer)
