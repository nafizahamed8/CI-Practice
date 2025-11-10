import streamlit as st

#streamlit ui
st.title("power calculator")
st.write("Enter a number to calculate square,cube and fifth power")

n=st.number_input("Enter an Integer",value=1,step=1)

#calculate result
square=n**2
cube=n**3
fifth_power=n**5

#display result
st.write(f"the square of {n} is:{square}")
st.write(f"the cube of {n} is:{cube}")
st.write(f"the fifth_power of {n} is:{fifth_power}")