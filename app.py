import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", [
    "Celsius a Fahrenheit",
    "Fahrenheit a Celsius",
    "Celsius a Kelvin",
    "Kelvin a Celsius",
])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.success(f"**{round(resultado, 2)} °F**")
    st.caption(f"{valor} °C son {round(resultado, 2)} °F")
elif modo == "Fahrenheit a Celsius":
    resultado = (valor - 32) * 5 / 9
    st.success(f"**{round(resultado, 2)} °C**")
    st.caption(f"{valor} °F son {round(resultado, 2)} °C")
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.success(f"**{round(resultado, 2)} °K**")
    st.caption(f"{valor} °C son {round(resultado, 2)} K")
else:
    resultado = valor - 273.15
    st.success(f"**{round(resultado, 2)} °C**")
    st.caption(f"{valor} K son {round(resultado, 2)} °C")
