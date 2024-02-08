from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load data from CSV file
def load_data():
    data = {}
    with open('truck_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            location = row['LOCATION']
            data[location] = row
    return data

# Search for trucks based on location
@app.route('/search', methods=['GET'])
def search_trucks():
    location = request.args.get('location')
    truck_data = load_data()
    
    # Assuming truck_data is a dictionary where keys are locations and values are truck data
    data = truck_data.get(location)
    
    return render_template('search.html', data=data)


@app.route('/')
def home():
    # Pass the truck data to the template
    data = load_data()
    return render_template('crop.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
