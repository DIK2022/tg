import sys
from PyQt6.QtWidgets import QApplication

from model.model import Model
from view.view_graph import Window
from controller.ctr_graph import Controller


def main():
    app = QApplication(sys.argv)

    # создаём Model и Window
    model = Model()
    view = Window()
    #создаём controller
    controller = Controller(model, view)
    #выводим на экран view
    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
