class CakeFrosting:
    """
    Subsystem for handling cake frosting details.
    """
    FROSTING_FLAVORS = ["Vanilla", "Chocolate", "Strawberry", "Lemon", "Cream Cheese"]

    def choose_frosting_flavor(self, flavor: str) -> str:
        if flavor.lower() in self.FROSTING_FLAVORS:
            return f"Chosen frosting flavor: {flavor}"
        else:
            return "Invalid frosting flavor."

class CakeDesign:
    """
    Subsystem for handling cake design details.
    """
    COLORS = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "White", "Black"]

    def choose_colors(self, colors: list) -> str:
        if all(color.lower() in self.COLORS for color in colors):
            return f"Chosen frosting colors: {', '.join(colors)}"
        else:
            return "Invalid color selection."

    def choose_decorations(self, decorations: list) -> str:
        valid_decorations = ["Flowers", "Balloons", "Swirls"]
        if all(decoration.lower() in valid_decorations for decoration in decorations):
            return f"Chosen decorations: {', '.join(decorations)}"
        else:
            return "Invalid decoration selection."

class CakeDesign_Customizer:
    """
    Facade class which simplifies the cake design customization process.
    """
    def __init__(self):
        self.cake_frosting = CakeFrosting()
        self.cake_design = CakeDesign()

    def customize_cake_design(self, request_form: dict) -> dict:
        frosting_flavor = request_form.get('frosting_flavor', 'No flavor selected')  # Use get() with a default value
        
        base_color = request_form.get('base_color', 'No base color selected')  # Use get() with a default value

        num_decorations = int(request_form.get('num_decorations', 0))  # Use get() with a default value and convert to int
        decorations = []
        for i in range(1, num_decorations + 1):
            if f'decoration{i}' in request_form:  # Check if key exists before accessing getlist()
                decoration = request_form.getlist('decoration' + str(i))
                decoration_color = request_form.getlist('decoration_color' + str(i))
                decorations.extend([f"{decoration[i]} ({decoration_color[i]})" for i in range(len(decoration))])

        results = {}
        results["frosting_flavor_result"] = self.cake_frosting.choose_frosting_flavor(frosting_flavor)
        results["base_color_result"] = f"Chosen base frosting color: {base_color}"
        
        if decorations:
            results["decorations_result"] = self.cake_design.choose_decorations(decorations)
        
        return results

def client_code(cake_design_customizer: CakeDesign_Customizer, request_form: dict) -> None:
    """
    The client code that uses the facade to simplify the process of customizing a cake design.
    :param cake_design_customizer:
    :param request_form: Form data from the HTML request
    :return:
    """
    cake_design_details = cake_design_customizer.customize_cake_design(request_form)
    print("Cake Design Details:")
    for key, value in cake_design_details.items():
        print(f"{key}: {value}")
