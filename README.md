# Flask and Pandas CSV Upload Project

## Overview
This project shows you how to use Flask for web app development and Pandas for data handling. You can upload a CSV file, view the full data, and use Pandas to filter specific columns.

## Getting Started

1. **Fork the Repository**:
   - Go to the repository on GitHub.
   - Click the "Fork" button in the top-right corner to create a copy of the repository under your own GitHub account.
  
2. **Clone Your Forked Repository**:
   - Copy the URL of your forked repository (it will look like `https://github.com/your-username/repo-name.git`).
   - In your terminal, run the following commands:
      - git clone 'your-forked-repo-url'
      - cd 'your-repo-name'

3. **Create and Activate a Virtual Environment**
   - A virtual environment keeps your project’s dependencies isolated from other projects.
   - Run the following commands to create and activate the virtual environment:
   **On macOS/Linux**:
   python3 -m venv venv  # Creates a virtual environment in a folder named 'venv'
   source venv/bin/activate  # Activates the virtual environment
   **On Windows**:
   python -m venv venv  # Creates a virtual environment in a folder named 'venv'
   venv\Scripts\activate  # Activates the virtual environment

4. **Install Dependencies**
**On macOS/Linux:**
pip3 install -r requirements.txt
**On Windows:**
pip install -r requirements.txt

5. **Add Pandas Code on app.py**
# Importing Pandas
- import pandas as pd
# Load the CSV file into a Pandas DataFrame
- df = pd.read_csv(file)

# Display the first few rows of the DataFrame as an HTML table
- full_table = df.to_html()

# Optionally, filter specific columns (e.g., select only 'Product' and 'Price')
- filtered_df = df[df['Price'] < 0.80][['Product', 'Price', 'Quantity']]
- filtered_table = filtered_df.to_html()

# Render the template and pass the tables for full and filtered data
- return render_template('index.html', tables=full_table, filtered_tables=filtered_table)

3. **Run the App**:
**On macOS/Linux:**
python3 app.py
**On Windows:**
python app.py

4. **Open in Browser**:
- Go to `http://127.0.0.1:5000` and upload a CSV file.

## Sample CSV File

A sample CSV file (`samples.csv`) is included. This file contains data can be used to test the app.

### To Use the Sample File:
- Run the app by following the instructions above.
- Go to the web page and upload `samples.csv`.
