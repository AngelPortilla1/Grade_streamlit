import streamlit as st

st.set_page_config(page_title="Conversor de temperatura", page_icon="🌡️", layout="centered")
st.title("🌡️ Conversor de temperatura")
st.markdown("Convierte entre Celsius y Fahrenheit con una interfaz clara y resultados rápidos.")

modo = st.radio("Selecciona la conversión:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor", value=0.0, format="%.2f")

if modo == "Celsius a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    entrada = f"{valor} °C"
    salida = f"{round(resultado, 2)} °F"
    formula = "°F = °C × 9/5 + 32"
else:
    resultado = (valor - 32) * 5 / 9
    entrada = f"{valor} °F"
    salida = f"{round(resultado, 2)} °C"
    formula = "°C = (°F - 32) × 5/9"

col1, col2 = st.columns(2)
col1.metric("Entrada", entrada)
col2.metric("Resultado", salida)

st.write("---")
st.subheader("Detalles de la conversión")
st.write(f"**Fórmula utilizada:** {formula}")
st.write("Los valores se redondean a dos decimales para mayor claridad.")

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
>>>>>>> feature/kelvin
