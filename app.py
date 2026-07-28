import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Kelvin a Celsius", "Celsius a Kelvin"])
valor = st.number_input("Valor")
mostrar_clasificacion = st.checkbox("Mostrar clasificación de temperatura")

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

if mostrar_clasificacion:
    if modo == "Celsius a Fahrenheit" or modo == "Celsius a Kelvin":
        celsius = valor
    elif modo == "Fahrenheit a Celsius":
        celsius = (valor - 32) * 5 / 9
    else:
        celsius = valor - 273.15

    if celsius <= 0:
        clasificacion = "Muy frío / bajo cero"
    elif celsius <= 20:
        clasificacion = "Frío / templado"
    elif celsius <= 35:
        clasificacion = "Cálido"
    else:
        clasificacion = "Muy caliente"

    st.write(f"Clasificación: {clasificacion} ({round(celsius, 2)} °C)")