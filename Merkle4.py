import streamlit as st

st.set_page_config(page_title="Allocation",
                   layout="centered",
                   theme={"primaryColor": "#FFFFFF"})

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://moneyexpo.net/wp-content/uploads/2024/04/Merkel.jpg", use_column_width=True)


gold = st.number_input('Gold',
                       min_value=0.0,
                       max_value=100.0,
                       value=25.0,
                       step=1.0)
bitcoin = st.number_input('Bitcoin',
                        min_value=0.0,
                        max_value=100.0,
                        value=25.0,
                        step=1.0)
reits = st.number_input('REIT',
                        min_value=0.0,
                        max_value=100.0,
                        value=25.0,
                        step=1.0)
stock = st.number_input('Stocks',
                        min_value=0.0,
                        max_value=100.0,
                        value=25.0,
                        step=1.0)
data = {
    'Asset': ['Gold', 'Bitcoin', 'REITs', 'Stock'],
    'Values': [gold, bitcoin, reits, stock]
    }

button = st.button('Calculate')

if button:
    total_return = ((gold*10)+(bitcoin*20)+(reits*5)+(stock*2))*0.01
    st.write("Total Return:", total_return, "%")
