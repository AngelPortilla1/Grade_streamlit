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