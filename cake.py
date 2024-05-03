class CakeFlavor:
    """
    Subsystem for handling cake flavors.
    """
    FLAVORS = ["coconut", "vanilla", "lemon", "chocolate", "red velvet", "funfetti", "carrot"]

    def choose_flavor(self, flavor: str) -> str:
        if flavor.lower() in self.FLAVORS:
            return f"Chosen cake flavor: {flavor}"
        else:
            return "Invalid flavor selection."

class CakeLayers:
    """
    Subsystem for handling number of cake layers.
    """
    def choose_layers(self, layers: int) -> str:
        return f"Chosen number of layers: {layers}"
    
class CakeFillings:
    """
    Subsystem for handling cake fillings.
    """
    FILLINGS = ["chocolate mousse", "raspberry", "peach", "buttercream", "nutella buttercream", "whipped cream"]

    def choose_fillings(self, fillings: list, layers: int) -> str:
        if layers == 1 and len(fillings) == 1:
            return f"Chosen fillings: {', '.join(fillings)}"
        elif layers > 1 and len(fillings) > 1:
            return f"Chosen fillings: {', '.join(fillings)}"
        else:
            return "Invalid filling selection based on layers."

class CakeOptions:
    """
    Subsystem for handling additional cake options.
    """
    def choose_hidden_ring(self, option: bool) -> str:
        return f"Hidden ring option: {'Yes' if option else 'No'}"

    def choose_vegan_option(self, option: bool) -> str:
        return f"Vegan option: {'Yes' if option else 'No'}"

class CakeOrder_Customizer:
    """
    Facade class which simplifies the cake order customization process.
    """
    def __init__(self):
        self.cake_flavor = CakeFlavor()
        self.cake_layers = CakeLayers()
        self.cake_fillings = CakeFillings()
        self.cake_options = CakeOptions()

    def customize_cake_order(self) -> dict:
        flavor = input("Choose cake flavor (coconut, vanilla, lemon, chocolate, red velvet, funfetti, carrot): ")
        layers = int(input("Choose number of cake layers (1-3): "))
        fillings = []
        for i in range(layers):
            filling = input(f"Choose filling for layer {i+1} ({', '.join(CakeFillings.FILLINGS)}): ")
            fillings.append(filling)
        
        hidden_ring = input("Do you want a hidden ring (Yes/No)? ")
        vegan_option = input("Do you want a vegan cake (Yes/No)? ")

        results = {}
        results["flavor_result"] = self.cake_flavor.choose_flavor(flavor)
        results["layers_result"] = self.cake_layers.choose_layers(layers)
        results["fillings_result"] = self.cake_fillings.choose_fillings(fillings, layers)
        
        hidden_ring_bool = hidden_ring.lower() == 'yes'
        vegan_option_bool = vegan_option.lower() == 'yes'
        
        results["hidden_ring_result"] = self.cake_options.choose_hidden_ring(hidden_ring_bool)
        results["vegan_option_result"] = self.cake_options.choose_vegan_option(vegan_option_bool)
        
        return results

def client_code(cake_order_customizer: CakeOrder_Customizer) -> None:
    """
    The client code that uses the facade to simplify the process of customizing a cake order.
    :param cake_order_customizer:
    :return:
    """
    cake_order_details = cake_order_customizer.customize_cake_order()
    print("Cake Order Details:")
    print(cake_order_details["flavor_result"])
    print(cake_order_details["layers_result"])
    print(cake_order_details["fillings_result"])
    print(cake_order_details["hidden_ring_result"])
    print(cake_order_details["vegan_option_result"])

if __name__ == "__main__":
    cake_order_customizer = CakeOrder_Customizer()
    client_code(cake_order_customizer)
