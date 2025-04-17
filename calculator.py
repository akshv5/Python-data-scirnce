# Run the web application using the following command:
# streamlit run calculator.py   
    
    
    #streamlit run calculator.py

import streamlit as st

# Set the title of the web application
st.title('Calculator')

# Add a welcome message
st.markdown('Welcome to my web app')

# Create two columns for input fields
c1, c2 = st.columns(2)

# Input fields for the first and second numbers
fnum = c1.number_input('Enter first number', value=0)  # First number input
snum = c2.number_input('Enter second number', value=0)  # Second number input

# List of operations for the user to choose from
options = ['Addition', 'Subtraction', 'Multiplication', 'Division']

# Radio buttons for selecting the operation
choice = st.radio('Select operation', options)

# Button to trigger the calculation
button = st.button('Calculate')

# Initialize the result variable
result = 0

# Perform the calculation when the button is clicked
if button:
    if choice == 'Addition':
        result = fnum + snum  # Addition
    elif choice == 'Subtraction':
        result = fnum - snum  # Subtraction
    elif choice == 'Multiplication':
        result = fnum * snum  # Multiplication
    elif choice == 'Division':
        # Handle division to avoid division by zero
        if snum != 0:
            result = fnum / snum  # Division
        else:
            st.error('Division by zero is not allowed')  # Error message for division by zero
            result = None  # Set result to None if division by zero occurs

    # Display the result if it's valid
    if result is not None:
        st.success(f'The result is {result}')