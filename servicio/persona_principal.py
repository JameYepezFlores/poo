from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow

from Dominio.Docente import Docente
from Dominio.Estudiante import Estudiante
from UI.vtn_principal import Ui_vtn_principal


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

    def grabar(self):
        tipo_persona = self.ui.cb_tipo.currentText()
        if tipo_persona == 'Docente':
            persona = Docente()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
            persona.cedula = self.ui.txt_cedula.text()
            persona.email = self.ui.txt_email.text()
        else:
            persona = Estudiante()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
            persona.cedula = self.ui.txt_cedula.text()
            persona.email = self.ui.txt_email.text()

        try:
            with open('archivo.txt', mode='a') as archivo:
                archivo.write(persona.__str__())
                archivo.write('\n')
        except FileNotFoundError:
            print('Archivo no encontrado.')
        except Exception as e:
            print('No se pudo grabar:', e)

        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_email.setText('')
        self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)
