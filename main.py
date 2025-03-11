import streamlit as st
import random
import time
import requests

st.title("Welcome To Money Making Machine")

# Generate a random number between 1 and 100
def generate_money():
    return random.randint(1, 100)

# Display the money-making machine
st.subheader("Instant Cash Machine")
if st.button ("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(3)
    money = generate_money()
    st.success(f"Congratulations! You Have Generated ${money}")
    st.balloons()


# function to add side hustle to the game
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")
    except:
        return ("Error fetching data. Please try again later!")
    

# Display the side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):  # When user clicks button
    idea = fetch_side_hustle()  # Get a hustle idea
    st.success(idea)  # Show the idea


# function to add money quotes to the game
def money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            qoutes = response.json()
            return qoutes["money_quote"]
        else:
            return ("Money is everything")
        
    except:
        return ("Error fetching data. Please try again later!")
    

# Display the money quotes
st.subheader("Money Quotes")
if st.button("Get Money Quotes"):
    quote = money_quotes()
    st.success(quote)