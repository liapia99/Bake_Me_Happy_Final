from flask import Flask, render_template, request, redirect, url_for
import json

from start_order import DeliveryDetails, CustomerDetails, Order_Customizer
from design import CakeDesign_Customizer
from cake import CakeOrder_Customizer

app = Flask(__name__, static_folder='static')

# Instantiate CakeDesign_Customizer
cake_design_customizer = CakeDesign_Customizer()

# Instantiate CakeOrder_Customizer
cake_order_customizer = CakeOrder_Customizer()

# Global variable to store order details
order_details = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Retrieve form data
        delivery_date_time = request.form['delivery_date_time']
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']

        # Create a dictionary with the form data
        order_data = {
            "delivery_date_time": delivery_date_time,
            "name": name,
            "email": email,
            "address": address
        }

        # Write the data to a JSON file
        with open('order_data.json', 'w') as json_file:
            json.dump(order_data, json_file)

        # Redirect to the next step
        return redirect(url_for('customize_cake'))

    return render_template('order.html')

@app.route('/customize_cake', methods=['GET', 'POST'])
def customize_cake():
    if request.method == 'POST':
        # Retrieve form data
        flavor = request.form['flavor']
        layers = int(request.form['layers'])
        fillings = []

        # Retrieve fillings for each layer
        for i in range(1, layers + 1):
            filling_key = f'filling{i}'
            if filling_key in request.form:
                fillings.append(request.form[filling_key])

        hidden_ring = request.form['hidden_ring']
        vegan_option = request.form['vegan_option']

        # Create dictionary with form data
        data = {
            'flavor': flavor,
            'layers': layers,
            'fillings': fillings,
            'hidden_ring': hidden_ring,
            'vegan_option': vegan_option
        }

        # Write dictionary to JSON file
        with open('cake_data.json', 'w') as f:
            json.dump(data, f)

        # Redirect to design.html
        return redirect(url_for('design'))

    # Render customize_cake.html if not a POST request
    return render_template('customize_cake.html')



@app.route('/design', methods=['GET', 'POST'])
def design():
    if request.method == 'POST':
        # Retrieve form data
        frosting_flavor = request.form['frosting_flavor']
        base_color = request.form['base_color']
        num_decorations = int(request.form['num_decorations'])

        # Prepare data for decorations
        decorations = []
        for i in range(1, num_decorations + 1):
            decoration_name = request.form.get('decoration' + str(i))
            decoration_color = request.form.get('decoration_color' + str(i))
            decorations.append({'name': decoration_name, 'color': decoration_color})

        # Create dictionary with form data
        data = {
            'frosting_flavor': frosting_flavor,
            'base_color': base_color,
            'num_decorations': num_decorations,
            'decorations': decorations
        }

        # Write dictionary to JSON file
        with open('design_data.json', 'w') as f:
            json.dump(data, f)

        # Redirect to confirmation page
        return redirect('/confirm_order')

    # Render cake_design.html if not a POST request
    return render_template('design.html')


@app.route('/confirm_order', methods=['GET'])
def confirm_order():
    # Load data from JSON files
    with open('order_data.json', 'r') as order_file:
        order_details = json.load(order_file)
    
    with open('cake_data.json', 'r') as cake_file:
        cake_details = json.load(cake_file)
    
    with open('design_data.json', 'r') as design_file:
        design_details = json.load(design_file)

    return render_template('confirm_order.html', order_details=order_details, cake_details=cake_details, design_details=design_details)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Process order submission logic here
    # For example, send confirmation email, update database, etc.
    # Then redirect to thank_you page
    return redirect(url_for('thank_you'))

@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
