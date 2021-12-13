import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSettings, QCoreApplication
from ui.task1_ui import Ui_MainWindow


ORGANIZATION_NAME = 'Arne E.'
ORGANIZATION_DOMAIN = 'Arne.com'
APPLICATION_NAME = 'ArneApp'
SETTINGS = 'settings/'


class Task1App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Task1App, self).__init__()
        self.n = 0
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setup_settings()
        if self.n % 5 == 0:
            self.line.setText('Позравляем, вы ' + str(self.n) + ' посетитель')

    def setup_settings(self):
        settings = QSettings()
        self.check1.setChecked(settings.value(SETTINGS + self.check1.objectName(), False, type=bool))
        self.check2.setChecked(settings.value(SETTINGS + self.check2.objectName(), False, type=bool))
        self.check3.setChecked(settings.value(SETTINGS + self.check3.objectName(), False, type=bool))
        self.text.setText(settings.value(SETTINGS + self.text.objectName(), '', type=str))
        self.n = settings.value(SETTINGS + 'n', 1, type=int)

        x = settings.value(SETTINGS + 'x', 100, type=int)
        y = settings.value(SETTINGS + 'y', 100, type=int)
        self.move(x, y)
        width = settings.value(SETTINGS + 'width', 100, type=int)
        height = settings.value(SETTINGS + 'height', 100, type=int)
        self.resize(width, height)

        settings.setValue(SETTINGS + 'n', self.n + 1)
        settings.sync()

    def save_settings(self):
        settings = QSettings()
        settings.setValue(SETTINGS + self.check1.objectName(), self.check1.isChecked())
        settings.setValue(SETTINGS + self.check2.objectName(), self.check2.isChecked())
        settings.setValue(SETTINGS + self.check3.objectName(), self.check3.isChecked())
        settings.setValue(SETTINGS + self.text.objectName(), self.text.toPlainText())

        settings.setValue(SETTINGS + 'x', self.x())
        settings.setValue(SETTINGS + 'y', self.y())
        settings.setValue(SETTINGS + 'width', self.width())
        settings.setValue(SETTINGS + 'height', self.height())
        settings.sync()

    def closeEvent(self, e):
        self.save_settings()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)
    w = Task1App()
    w.show()
    sys.exit(app.exec())
