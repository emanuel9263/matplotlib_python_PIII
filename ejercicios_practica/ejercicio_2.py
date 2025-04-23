# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

#def multi_plot(): 
    
    # Dibujar múltiples líneas en un mismo gráfico
   
    #x = list(np.linspace(start=-4, stop=4, num=20))
    
    #SE DEFINE EL RANGO DE VALORES PARA X 
    #x = list(np.linspace(-4, 4, 20))
    
    #fig = plt.figure()
    #ax = fig.add_subplot()

#    ax.plot(x, y1, color='green', marker='^', label='y1 = x**2')
 #   ax.plot(x, y2, color='red', marker='+', label='y2 = x**3')
    
#    ax.set_facecolor('whitesmoke')
#    ax.set_title("Dos funciones juntas")
#    ax.set_ylabel("Y[amplitud]")
#    ax.set_xlabel("X[rads]")
#    ax.set_xlim([-12, 4*np.pi])  # Limito el eje "Y" entre 0 y 4*pi
#    ax.set_ylim([-4, 4])       # Limito el eje "X" entre -4 y 4
#    ax.legend()
      
    # Graficar la figura con los 2 axes
 #   plt.show()

def multi_plot():

    # DefinO el rango de valores para x
    x = np.linspace(-4,4,20)
    
    # Se calculan los valores de y para las dos funciones
    y1 = x**2  # y1 = x^2
    y2 = x**3  # y2 = x^3

    # sE Crea una figura y un eje (ax) donde se graficarán las funciones
    fig = plt.figure()
    ax = fig.add_subplot()

    # Se grafica las dos funciones con diferentes colores, marcadores y etiquetas
    ax.plot(x, y1, color='blue', marker='^', label='y1 = x^2')  # Función 1: y = x^2
    ax.plot(x, y2, color='red', marker='+', label='y2 = x^3')   # Función 2: y = x^3

    # Personalización del gráfico
    ax.set_facecolor('white')  # Fondo del gráfico
    ax.set_title("Dos funciones juntas")  # Título del gráfico
    ax.set_ylabel("Y [amplitud]")  # Etiqueta del eje Y
    ax.set_xlabel("X [rads]")  # Etiqueta del eje X
    ax.set_xlim([-4, 4])  # Limitar el eje X entre -4 y 4
    ax.set_ylim([-4, 4])  # Limitar el eje Y entre -4 y 4

    ax.grid(True)

    # Añadir la leyenda con las etiquetas definidas en las líneas anteriores
    ax.legend()

     # Mostrar el gráfico
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Multi Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico 

    multi_plot()  

    print("terminamos")