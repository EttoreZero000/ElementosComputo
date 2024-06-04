from manim import *

class Face(Scene):
    def construct(self):
        # Coordenadas de los círculos que formarán la cara
        circle_coords = [
            (0, 0),     # Centro de la cara
            (-1, 1),    # Ojo izquierdo
            (1, 1),     # Ojo derecho
            (0, -1),    # Boca
            (-1.5, 0),  # Nariz izquierda
            (1.5, 0)    # Nariz derecha
        ]

        # Radio de los círculos
        circle_radius = [1, 0.2, 0.2, 0.5, 0.1, 0.1]

        # Colores de los círculos
        circle_colors = [WHITE, BLUE, BLUE, RED, BLACK, BLACK]

        # Crear círculos y agregarlos a la escena
        for coord, radius, color in zip(circle_coords, circle_radius, circle_colors):
            circle = Circle(radius=radius, color=color).shift(coord)
            self.add(circle)
