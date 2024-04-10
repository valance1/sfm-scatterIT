import random, math

import sfm, sfmApp, sfmConsole
import PySide
from PySide import QtCore, QtGui, shiboken
from PySide.QtGui import *
from PySide.QtCore import *

class scatterUI(QtGui.QWidget):
    def __init__(self):
        super(scatterUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 280, 352)
        self.setMinimumSize(280, 352)
        self.gridLayout = QtGui.QGridLayout(self)
        self.setupUI()

    def setupUI(self):
        self.setMinimumSize(280, 352)
        #Components related to RotationBox
        self.RotationBox = QtGui.QGroupBox("Rotation")
        self.GridRotBox = QtGui.QGridLayout(self.RotationBox)
        self.RandomizeRotCheckbox = QtGui.QCheckBox("Randomize Rotation")
        self.RandomizeRotCheckbox.stateChanged.connect(self.switchRotState)
        self.GridRotBox.addWidget(self.RandomizeRotCheckbox, 0, 0, 1, 2)

        self.MinRot = QtGui.QLabel("Min:")
        self.GridRotBox.addWidget(self.MinRot, 1, 0, 1, 1)
        self.MaxRot = QtGui.QLabel("Max:")
        self.GridRotBox.addWidget(self.MaxRot, 2, 0, 1, 1)
        self.MinXRot = QtGui.QLabel("X")
        self.GridRotBox.addWidget(self.MinXRot, 1, 1, 1, 1)
        self.MinXRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MinXRotInput, 1, 2, 1, 1)
        self.MinYRot = QtGui.QLabel("Y")
        self.GridRotBox.addWidget(self.MinYRot, 1, 3, 1, 1)
        self.MinYRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MinYRotInput, 1, 4, 1, 1)
        self.MinZRot = QtGui.QLabel("Z")
        self.GridRotBox.addWidget(self.MinZRot, 1, 5, 1, 1)
        self.MinZRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MinZRotInput, 1, 6, 1, 1)
        self.MaxXRot = QtGui.QLabel("X")
        self.GridRotBox.addWidget(self.MaxXRot, 2, 1, 1, 1)
        self.MaxXRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MaxXRotInput, 2, 2, 1, 1)
        self.MaxYRot = QtGui.QLabel("Y")
        self.GridRotBox.addWidget(self.MaxYRot, 2, 3, 1, 1)
        self.MaxYRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MaxYRotInput, 2, 4, 1, 1)
        self.MaxZRot = QtGui.QLabel("Z")
        self.GridRotBox.addWidget(self.MaxZRot, 2, 5, 1, 1)
        self.MaxZRotInput = QtGui.QLineEdit()
        self.GridRotBox.addWidget(self.MaxZRotInput, 2, 6, 1, 1)

        # Components related to CloneBox
        self.CloneBox = QtGui.QGroupBox("Clone selected")
        self.GridCloneBox = QtGui.QGridLayout(self.CloneBox)
        self.CopyCheckbox = QtGui.QCheckBox("Create copies of the selected models")
        self.CopyCheckbox.stateChanged.connect(self.switchQuantityState)
        self.GridCloneBox.addWidget(self.CopyCheckbox, 0, 0, 1, 2)

        self.Quantity = QtGui.QLabel("Quantity:")
        self.GridCloneBox.addWidget(self.Quantity, 1, 0, 1, 1)
        self.QuantityInput = QtGui.QLineEdit()
        self.QuantityInput.setEnabled(False)
        self.GridCloneBox.addWidget(self.QuantityInput, 1, 1, 1, 1)

        # Components related to PositionBox
        self.PositionBox = QtGui.QGroupBox("Position")
        self.GridPosBox = QtGui.QGridLayout(self.PositionBox)
        self.RandomizePosCheckbox = QtGui.QCheckBox("Randomize Position")
        self.RandomizePosCheckbox.stateChanged.connect(self.switchPosState)
        self.GridPosBox.addWidget(self.RandomizePosCheckbox, 0, 0, 1, 2)

        self.MinPos = QtGui.QLabel("Min:")
        self.GridPosBox.addWidget(self.MinPos, 1, 0, 1, 1)
        self.MaxPos = QtGui.QLabel("Max:")
        self.GridPosBox.addWidget(self.MaxPos, 2, 0, 1, 1)
        self.MinXPos = QtGui.QLabel("X")
        self.GridPosBox.addWidget(self.MinXPos, 1, 1, 1, 1)
        self.MinXPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MinXPosInput, 1, 2, 1, 1)
        self.MinYPos = QtGui.QLabel("Y")
        self.GridPosBox.addWidget(self.MinYPos, 1, 3, 1, 1)
        self.MinYPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MinYPosInput, 1, 4, 1, 1)
        self.MinZPos = QtGui.QLabel("Z")
        self.GridPosBox.addWidget(self.MinZPos, 1, 5, 1, 1)
        self.MinZPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MinZPosInput, 1, 6, 1, 1)
        self.MaxXPos = QtGui.QLabel("X")
        self.GridPosBox.addWidget(self.MaxXPos, 2, 1, 1, 1)
        self.MaxXPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MaxXPosInput, 2, 2, 1, 1)
        self.MaxYPos = QtGui.QLabel("Y")
        self.GridPosBox.addWidget(self.MaxYPos, 2, 3, 1, 1)
        self.MaxYPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MaxYPosInput, 2, 4, 1, 1)
        self.MaxZPos = QtGui.QLabel("Z")
        self.GridPosBox.addWidget(self.MaxZPos, 2, 5, 1, 1)
        self.MaxZPosInput = QtGui.QLineEdit()
        self.GridPosBox.addWidget(self.MaxZPosInput, 2, 6, 1, 1)
        
        self.MinXRotInput.setEnabled(False)
        self.MinYRotInput.setEnabled(False)
        self.MinZRotInput.setEnabled(False)
        self.MaxXRotInput.setEnabled(False)
        self.MaxYRotInput.setEnabled(False)
        self.MaxZRotInput.setEnabled(False)
        self.MinXPosInput.setEnabled(False)
        self.MinYPosInput.setEnabled(False)
        self.MinZPosInput.setEnabled(False)
        self.MaxXPosInput.setEnabled(False)
        self.MaxYPosInput.setEnabled(False)
        self.MaxZPosInput.setEnabled(False)


        # Add widgets to the main grid layout
        self.gridLayout.addWidget(self.PositionBox, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.CloneBox, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.RotationBox, 1, 0, 1, 2)
        self.scatterButton = QtGui.QPushButton("Scatter")
        self.scatterButton.setEnabled(True)
        self.scatterButton.clicked.connect(self.scatterIT)
        self.scatterButton.setMinimumSize(QtCore.QSize(0, 30))
        self.gridLayout.addWidget(self.scatterButton, 4, 0, 1, 2)

    def switchPosState(self):
        self.MinXPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
        self.MinYPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
        self.MinZPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
        self.MaxXPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
        self.MaxYPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
        self.MaxZPosInput.setEnabled(self.RandomizePosCheckbox.isChecked())
    
    def switchRotState(self):
        self.MinXRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())
        self.MinYRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())
        self.MinZRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())
        self.MaxXRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())
        self.MaxYRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())
        self.MaxZRotInput.setEnabled(self.RandomizeRotCheckbox.isChecked())

    def switchQuantityState(self):
        self.QuantityInput.setEnabled(self.CopyCheckbox.isChecked())

    def messageBox(self, message):
        mensagem = QtGui.QMessageBox()
        mensagem.setText(message)
        mensagem.exec_()

    def randomize_position(min_x, max_x, min_y, max_y, min_z, max_z):
        # Generate random coordinates for x, y, and z within the given range
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        z = random.uniform(min_z, max_z)
        return x, y, z

    def randomize_rotation(min_x, max_x, min_y, max_y, min_z, max_z):
        # Generate random rotations for x, y, and z within the given range
        x_rot = random.uniform(min_x, max_x)
        y_rot = random.uniform(min_y, max_y)
        z_rot = random.uniform(min_z, max_z)
        return x_rot, y_rot, z_rot

    def scatterIT(self):
        if(self.RandomizePosCheckbox.isChecked() == False and self.RandomizeRotCheckbox.isChecked() == False):
            self.messageBox("You did not allow the scattering of objects via position or rotation, no changes were made")


janela = scatterUI()
sfmApp.RegisterTabWindow( "scatterUI", "scatterIT", shiboken.getCppPointer(janela)[0] )
sfmApp.ShowTabWindow("scatterUI")
