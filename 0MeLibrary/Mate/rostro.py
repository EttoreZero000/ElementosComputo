from manim import *

class FourierSeries(Scene):
    def construct(self):
        # Definir la función periódica
        def square_wave(x, n):
            return (1 / n) * np.sin(n * x * TAU)

        # Configuración de la escena
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
        )
        graph = axes.get_graph(lambda x: square_wave(x, 1), color=WHITE)
        graph_label = axes.get_graph_label(graph, label="f(x)", x_val=2, direction=UP)

        # Crear la animación
        self.play(Create(axes), Create(graph), Write(graph_label))

        # Suma de la serie de Fourier
        n_max = 10  # Número máximo de términos de la serie
        fourier_sum = graph.copy()
        for n in range(2, n_max + 1):
            term = axes.get_graph(lambda x: square_wave(x, n), color=YELLOW)
            fourier_sum = fourier_sum + term
            self.play(Transform(graph, fourier_sum))

        self.wait(2)
