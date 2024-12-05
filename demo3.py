import streamlit as st

st.set_page_config(page_title="Allocation",
                   layout="centered")

st.title("Workshop 1")

gold = st.number_input('Percentage in Gold',
                       min_value=0.0,
                       max_value=100.0,
                       value=20.0,
                       step=1.0)
bitcoin = st.number_input('Percentage in Bitcoin',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=1.0)
reits = st.number_input('Percentage in REITs',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=1.0)
stock = st.number_input('Percentage in Stock',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=1.0)
bond = st.number_input('Percentage in Bond',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=1.0)

data = {
    'Asset': ['Gold', 'Bitcoin', 'REITs', 'Stock','Bond'],
    'Values': [gold, bitcoin, reits, stock, bond]
    }

button = st.button('Calculate')

if button:
    total_return = ((gold*29.52)+(bitcoin*143.95)+(reits*12.34)+(stock*22.08)+(bond*4.45))*0.01
    st.write("YTD Return: ", total_return, "%")

    volatility = ((gold*15)+(bitcoin*72.9)+(reits*22.7)+(stock*19.6)+(bond*6.4))*0.01
    st.write("1-Year Volatility: ", volatility, "%")
