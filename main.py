import streamlit as st
from datetime import date
st.header("Hey testing some streamlit today")
st.subheader("First website")
st.write("WTF is this")
st.text("Nahh man this shit is easy")

test = st.selectbox("Select your favorite chatllm: ",[ "Select an option","ChatGPT", "Perplexity", "Claude", "Gemini"])

st.write(f"You chose {test}")

if(test != "Select an option") :
    st.success(f"Your option {test} was recorded")

aurlv = st.slider("**Aura level**",0,100, step=5)

st.text(f"Aura level selected: {aurlv}")

age = st.number_input("What is your age",min_value=1,max_value=120)

if age:
    st.text(f"Your age is : {age}")

name = st.text_input("What is your name ? ",placeholder="John doe")

if name:
    st.text(f"Your name is {name}")

dob = st.date_input("Select your dob",min_value=date(1900, 1, 1),  max_value=date.today() )

if dob:
    today = date.today()
    age  = today.year - dob.year - ((today.month,today.year)  < (dob.month, dob.year))
    st.write(f"Your age is {age}")
