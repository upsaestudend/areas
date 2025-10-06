import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def dibujar_figura(figura, valores):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    if figura == "cuadrado":
        l = valores["lado"]
        square = plt.Rectangle((0, 0), l, l, fill=False, edgecolor="k", linewidth=2)
        ax.add_patch(square)
        ax.set_xlim(-1, max(l, 1)+1)
        ax.set_ylim(-1, max(l, 1)+1)
    elif figura == "triangulo":
        b = valores["base"]
        h = valores["altura"]
        coords = [(0,0), (b,0), (0,h)]
        triangle = plt.Polygon(coords, fill=None, edgecolor="k", linewidth=2)
        ax.add_patch(triangle)
        ax.set_xlim(-1, b+1)
        ax.set_ylim(-1, h+1)
    elif figura == "rectangulo":
        b = valores["base"]
        h = valores["altura"]
        rect = plt.Rectangle((0,0), b, h, fill=None, edgecolor="k", linewidth=2)
        ax.add_patch(rect)
        ax.set_xlim(-1, b+1)
        ax.set_ylim(-1, h+1)
    elif figura == "circulo":
        r = valores["radio"]
        circle = plt.Circle((0,0), r, fill=False, edgecolor="k", linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-r-1, r+1)
        ax.set_ylim(-r-1, r+1)
    
    st.pyplot(fig)
