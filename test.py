from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_MainWindow import Ui_MainWindow

import sys

from PySide6 import QtGui
from commdefs import *
from stackshot_controller import StackShotController

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        short = 0.1
        middle = 0.5
        long = 1.0
        # move forward
        self.gui.fwdShortPushButton.pressed.connect(lambda: self.moveStackShot(RailDir.FWD, short))
        self.gui.fwdMiddlePushButton.pressed.connect(lambda: self.moveStackShot(RailDir.FWD, middle))
        self.gui.fwdLongPushButton.pressed.connect(lambda: self.moveStackShot(RailDir.FWD, long))

        # move back
        self.gui.backShortPushButton.pressed.connect(lambda: self.moveStackShot(RailDir.BACK, short))
        self.gui.backMiddlePushButton.pressed.connect(lambda: self.moveStackShot(RailDir.BACK, middle))
        self.gui.backLongPushButton.pressed.connect(lambda: self.moveStackShot(RailDir.BACK, long))

        # when start app, connect with StackShot3X and stop all axis(prevent infinite move)
        self.controller = StackShotController()
        try:
            print('connecting to Stackshot3X...')
            self.controller.open()
            self.controller.stop(RailAxis.X)
            self.controller.stop(RailAxis.Y)
            self.controller.stop(RailAxis.Z)
        except Exception as excpt:
            print(excpt)
            exit()

    def moveStackShot(self, dir: RailDir, dist: float):
        axis = None
        if self.gui.xRadioButton.isChecked() == True:
            axis = RailAxis.X
        elif self.gui.yRadioButton.isChecked() == True:
            axis = RailAxis.Y
        elif self.gui.zRadioButton.isChecked() == True:
            axis = RailAxis.Z

        self.controller.move(axis, dir, dist)

    # when close window, this function is fired
    def closeEvent(self, event: QtGui.QCloseEvent):
        # after stop all axis, disconnect from StackShot3X
        try:
            print('discoonnecting from Stackshot3X...')
            self.controller.stop(RailAxis.X)
            self.controller.stop(RailAxis.Y)
            self.controller.stop(RailAxis.Z)
            self.controller.close()
        except Exception as excpt:
            print(excpt)
            return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
