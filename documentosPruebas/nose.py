import sys
import random
import matplotlib
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QToolBar, QStatusBar, QMenuBar
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use("QtAgg")

# Clase para el lienzo de Matplotlib
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

# Clase para la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar ventana principal
        self.setWindowTitle("Aplicación PySide6 con Barra de Herramientas")
        self.setGeometry(100, 100, 800, 600)

        # Agregar un widget central con diseño
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Layout principal
        layout = QVBoxLayout(self.central_widget)

        # Crear un lienzo de Matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        # Layout para controles
        controls_layout = QHBoxLayout()
        
        # Botón para actualizar gráfico
        self.button = QPushButton("Actualizar gráfico", self)
        self.button.clicked.connect(self.update_plot)
        controls_layout.addWidget(self.button)

        # Etiqueta de estado
        self.status_label = QLabel("Listo", self)
        controls_layout.addWidget(self.status_label)

        layout.addLayout(controls_layout)

        # Barra de estado
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Timer para actualizar el gráfico
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Actualiza cada 1 segundo
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        # Crear menú
        self.create_menu()

        # Crear barra de herramientas
        self.create_toolbar()

        # Iniciar datos
        self.xdata = list(range(50))
        self.ydata = [random.randint(0, 10) for _ in range(50)]
        self.update_plot()

    def update_plot(self):
        """ Actualiza el gráfico de matplotlib con nuevos datos """
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]  # Añadir un nuevo dato
        self.canvas.axes.cla()  # Limpiar el lienzo
        self.canvas.axes.plot(self.xdata, self.ydata, "r")
        self.canvas.draw()
        self.status_label.setText(f"Datos actualizados: {self.ydata[-1]}")

    def create_menu(self):
        """ Crea el menú de la aplicación """
        menubar = self.menuBar()
        
        # Menú archivo
        file_menu = menubar.addMenu("Archivo")
        exit_action = QAction(QIcon(), "Salir", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def create_toolbar(self):
        """ Crea la barra de herramientas """
        toolbar = self.addToolBar("Toolbar")

        # Botón de actualizar gráfico
        refresh_action = QAction(QIcon(), "Actualizar gráfico", self)
        refresh_action.triggered.connect(self.update_plot)
        toolbar.addAction(refresh_action)

        # Botón de cambiar color a azul
        blue_action = QAction(QIcon(), "Cambiar color a azul", self)
        blue_action.triggered.connect(self.change_to_blue)
        toolbar.addAction(blue_action)

        # Botón de cambiar color a verde
        green_action = QAction(QIcon(), "Cambiar color a verde", self)
        green_action.triggered.connect(self.change_to_green)
        toolbar.addAction(green_action)

        # Botón de mostrar mensaje de estado
        show_message_action = QAction(QIcon(), "Mostrar mensaje de estado", self)
        show_message_action.triggered.connect(self.show_status_message)
        toolbar.addAction(show_message_action)

    def change_to_blue(self):
        """ Cambia el color de la línea del gráfico a azul """
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, color="blue")
        self.canvas.draw()
        self.status_label.setText("Color del gráfico cambiado a azul")

    def change_to_green(self):
        """ Cambia el color de la línea del gráfico a verde """
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, color="green")
        self.canvas.draw()
        self.status_label.setText("Color del gráfico cambiado a verde")

    def show_status_message(self):
        """ Muestra un mensaje en la barra de estado """
        self.statusBar.showMessage("Este es un mensaje de estado")

# Crear la aplicación y la ventana
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
