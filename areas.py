import streamlit as st
import math

def calcular_area(figura, valores):
    """
    figura: str - 'cuadrado', 'triangulo', 'rectangulo', 'circulo'
    valores: dict - entradas necesarias según la figura
    Devuelve el área como float.
    """
    if figura == "cuadrado":
        lado = valores["lado"]
        return lado ** 2
    elif figura == "triangulo":
        base = valores["base"]
        altura = valores["altura"]
        return (base * altura) / 2
    elif figura == "rectangulo":
        base = valores["base"]
        altura = valores["altura"]
        return base * altura
    elif figura == "circulo":
        radio = valores["radio"]
        return math.pi * (radio ** 2)
    else:
        raise ValueError("Figura no válida")

def main():
    st.title("Calculadora de área de figuras geométricas")

    st.sidebar.header("Selección de figura")
    figura_opciones = {
        "Cuadrado": "cuadrado",
        "Triángulo": "triangulo",
        "Rectángulo": "rectangulo",
        "Círculo": "circulo"
    }
    eleccion = st.sidebar.selectbox("Elige la figura", list(figura_opciones.keys()))
    figura = figura_opciones[eleccion]

    st.sidebar.markdown("---")
    st.sidebar.write("Ajusta las dimensiones en la sección principal.")

    valores = {}

    # Entradas dinámicas según la figura
    if figura == "cuadrado":
        valores["lado"] = st.number_input("Lado del cuadrado (cm)", min_value=0.0, value=5.0, step=0.1)

    elif figura == "triangulo":
        valores["base"] = st.number_input("Base del triángulo (cm)", min_value=0.0, value=5.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=4.0, step=0.1)

    elif figura == "rectangulo":
        valores["base"] = st.number_input("Base del rectángulo (cm)", min_value=0.0, value=6.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=3.0, step=0.1)

    elif figura == "circulo":
        valores["radio"] = st.number_input("Radio del círculo (cm)", min_value=0.0, value=3.0, step=0.1)

    # Botón para calcular
    if st.button("Calcular área"):
        try:
            area = calcular_area(figura, valores)
            st.success(f"Área de la {eleccion.lower()}: {area:.3f} cm²")
        except Exception as e:
            st.error(f"Error al calcular: {e}")

    st.markdown("---")
    st.caption("Notas:\n- Las unidades están en centímetros (cm).\n- Esta app es de ejemplo y asume entradas numéricas válidas.")

if __name__ == "__main__":
    main()