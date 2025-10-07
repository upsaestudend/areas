import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

# Funciones de dibujo de miniaturas
def dibujar_minatura(figura):
    fig, ax = plt.subplots(figsize=(2, 2), dpi=100)
    ax.set_aspect('equal')
    ax.axis('off')
    if figura == "cuadrado":
        l = 1
        square = plt.Rectangle((0, 0), l, l, fill=False, edgecolor="black", linewidth=3)
        ax.add_patch(square)
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
    elif figura == "triangulo":
        tri = plt.Polygon([(0,0), (1,0), (0.5,0.866)], fill=None, edgecolor="black", linewidth=3)
        ax.add_patch(tri)
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1.0)
    elif figura == "circulo":
        circ = plt.Circle((0.5,0.5), 0.4, fill=False, edgecolor="black", linewidth=3)
        ax.add_patch(circ)
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
    return fig

# Título y secciones
st.title("Galería decorativa de figuras")

# Sección principal (sin interacción, solo entradas para cálculo si quieres)
st.write("Estas son las figuras subidas, mostradas como adorno.")
# Aquí podrías dejar el bloque para subir imágenes si quieres, o usar las ya existentes.

# Galería decorativa en la parte inferior
st.markdown("---")
st.subheader("Figuras decorativas")
cols = st.columns(3)

figuras = ["cuadrado", "triangulo", "circulo"]
for idx, figura in enumerate(figuras):
    with cols[idx]:
        fig = dibujar_minatura(figura)
        canvas = fig.canvas
        buf = canvas.tostring_rgb()
        height, width = fig.canvas.get_width_height()
        import PIL.Image as PILImage
        image = PILImage.fromarray(np.asarray(fig.canvas.buffer_rgba())[...,[0,1,2,3]])
        st.image(image, caption=figura.capitalize(), use_column_width=True)

st.markdown("---")
st.caption("Notas: estas son imágenes decorativas. Si quieres que sean interactives, dime y las convertimos en thumbnails clicables.")