import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Kelvin a Celsius", "Celsius a Kelvin"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.write(f"{valor} °C son {round(resultado, 2)} °F")
elif modo == "Fahrenheit a Celsius":
    resultado = (valor - 32) * 5 / 9
    st.write(f"{valor} °F son {round(resultado, 2)} °C")
elif modo == "Kelvin a Celsius":
    resultado = valor - 273.15
    st.write(f"{valor} K son {round(resultado, 2)} °C")
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.write(f"{valor} °C son {round(resultado, 2)} K")