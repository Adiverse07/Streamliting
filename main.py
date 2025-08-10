import streamlit as st

st.header("Hey testing some streamlit today")
st.subheader("First website")
st.write("WTF is this")
st.text("Nahh man this shit is easy")

test = st.selectbox("Select your favorite chatllm: ",["ChatGPT", "Perplexity", "Claude", "Gemini"])

st.write(f"You chose {test}")