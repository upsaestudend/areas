import streamlit as st  
import math  
import matplotlib.pyplot as plt  

def calcular_area(figura, valores):  
    if figura == "cuadrado":  
        l = valores.get("lado", 0)  
        return l ** 2  
    elif figura == "triangulo":  
        b = valores.get("base", 0)  
        h = valores.get("altura", 0)  
        return (b * h) / 2  
    elif figura == "rectangulo":  
        b = valores.get("base", 0)  
        h = valores.get("altura", 0)  
        return b * h  
    elif figura == "circulo":  
        r = valores.get("radio", 0)  
        return math.pi * (r ** 2)  
    else:  
        raise ValueError("Figura no válida")  

def dibujar_figura(figura, valores):  
    fig, ax = plt.subplots()  
    ax.set_aspect('equal')  
    ax.axis('off')  
    
    if figura == "cuadrado":  
        l = valores.get("lado", 0)  
        if l > 0:  
            square = plt.Rectangle((0, 0), l, l, fill=False, edgecolor="k", linewidth=2)  
            ax.add_patch(square)  
            ax.set_xlim(-1, max(l, 1) + 1)  
            ax.set_ylim(-1, max(l, 1) + 1)  
    elif figura == "triangulo":  
        b = valores.get("base", 0)  
        h = valores.get("altura", 0)  
        if b > 0 and h > 0:  
            coords = [(0,0), (b,0), (0,h)]  
            triangle = plt.Polygon(coords, fill=None, edgecolor="k", linewidth=2)  
            ax.add_patch(triangle)  
            ax.set_xlim(-1, b + 1)  
            ax.set_ylim(-1, h + 1)  
    elif figura == "rectangulo":  
        b = valores.get("base", 0)  
        h = valores.get("altura", 0)  
        if b > 0 and h > 0:  
            rect = plt.Rectangle((0,0), b, h, fill=None, edgecolor="k", linewidth=2)  
            ax.add_patch(rect)  
            ax.set_xlim(-1, b + 1)  
            ax.set_ylim(-1, h + 1)  
    elif figura == "circulo":  
        r = valores.get("radio", 0)  
        if r > 0:  
            circle = plt.Circle((0,0), r, fill=False, edgecolor="k", linewidth=2)  
            ax.add_patch(circle)  
            ax.set_xlim(-r - 1, r + 1)  
            ax.set_ylim(-r - 1, r + 1)  
    return fig  

def main():  
    st.title("Calculadora de áreas con visualización")  

    figura_opciones = {  
        "Cuadrado": "cuadrado",  
        "Triángulo": "triangulo",  
        "Rectángulo": "rectangulo",  
        "Círculo": "circulo"  
    }  

    eleccion = st.selectbox("Elige la figura", list(figura_opciones.keys()))  
    valores = {}  

    # Entradas dinámicas según la figura  
    if eleccion == "Cuadrado":  
        lado = st.number_input("Longitud del lado (cm)", min_value=0.0, value=5.0, step=0.5)  
        valores["lado"] = lado  
        figura = "cuadrado"  
    elif eleccion == "Triángulo":  
        base = st.number_input("Base (cm)", min_value=0.0, value=4.0, step=0.5)  
        altura = st.number_input("Altura (cm)", min_value=0.0, value=3.0, step=0.5)  
        valores["base"] = base  
       