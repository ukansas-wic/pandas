from flask import Flask, request, render_template
#import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # add Pandas code below this line
    # 1. Load the CSV file into a Pandas DataFrame
    

    # 2. Display the first few rows of the DataFrame as an HTML table
    

    # 3. Optionally, filter specific columns (e.g., select only 'Product' and 'Price')
    

    # Render the template and pass the tables for full and filtered data
    

if __name__ == '__main__':
    app.run(debug=True)
