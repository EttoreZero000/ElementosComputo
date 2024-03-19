import numpy as np
import matplotlib.pyplot as plt
from svgwrite import Drawing
def generar_vectores(n_circulos):
  # Ángulos y radios
  angulos = np.linspace(0, 2*np.pi, n_circulos)
  radios = np.random.rand(n_circulos)

  # Vectores
  vectores = np.zeros((n_circulos, 2), dtype=complex)
  for i in range(n_circulos):
    vectores[i] = radios[i] * np.exp(1j * angulos[i])

  return vectores
def calcular_series_fourier(vectores):
  n_puntos = len(vectores)
  coefs_fourier = np.fft.fft(vectores)

  # Frecuencias
  frecuencias = np.fft.fftfreq(n_puntos)

  return coefs_fourier, frecuencias
def dibujar_svg(vectores, coefs_fourier, frecuencias, n_circulos):
  # Crear el dibujo SVG
  dwg = Drawing()

  # Dibujar los círculos
  for i in range(n_circulos):
    angulo = np.angle(vectores[i])
    radio = np.abs(vectores[i])
    dwg.add(dwg.circle((0, 0), radio, fill='red', stroke='black'))

  # Dibujar las series de Fourier
  for i in range(len(coefs_fourier)):
    if i == 0:
      continue
    x = frecuencias[i] * np.linspace(-1, 1, 100)
    y = np.abs(coefs_fourier[i]) * np.cos(2 * np.pi * frecuencias[i] * x)
    dwg.add(dwg.polyline([(x, y) for x, y in zip(x, y)], stroke='blue'))

  # Guardar el SVG
  dwg.saveas('fourier.svg')
n_circulos = 10

vectores = generar_vectores(n_circulos)
coefs_fourier, frecuencias = calcular_series_fourier(vectores)
dibujar_svg(vectores, coefs_fourier, frecuencias, n_circulos)
