from PyQt5.QtWidgets import QMainWindow, QFileDialog
from mainwindow import *
from aboutprog import *
import os


class ApproximateView(QMainWindow):
    """
       Класс отвечающий за визуальное представление ApproximateModel.
    """

    def __init__(self, inController, inModel, parent=None):
        super(ApproximateView, self).__init__(parent)
        """
            Конструктор принимает ссылку на модель.
            Конструктор создаёт и отображает представление.
        """
        self.mController = inController
        self.mModel = inModel
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.SetupGraphicsSettings()
        self.options = ('Get File Name', 'Get File Names', 'Get Folder Dir', 'Save File Name')
        self.ui.AboutProg.triggered.connect(self.ProgInformation)
        self.ui.LoadDataSet.triggered.connect(self.LoadData)
        self.ui.PrepareData.triggered.connect(self.PrepareData)

    # НАСТРОЙКА ПОЛЯ ГРАФИКОВ
    def SetupGraphicsSettings(self):
        self.ui.graphics.setBackground('w') # Цвет фона
        self.ui.graphics.setTitle("График зависимости F(x)", color="black", size="14pt") # Название графика
        self.ui.graphics.setLabel("left", "y, усл. ед.") # Подпись сбоку
        self.ui.graphics.setLabel("bottom", "x, усл. ед.") # Подпись внизу
        self.ui.graphics.addLegend() # Добавление легенды, её можно двигать на графике

    def ProgInformation(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def LoadCSV(self):
        option = self.options.index('Get File Name')

        if option == 0:
            response = self.getFileName()
        elif option == 1:
            response = self.getFileNames()
        elif option == 2:
            response = self.getDirectory()
        elif option == 3:
            response = self.getSaveFileName()
        else:
            print('Got Nothing')
        return response

    def getFileName(self):
        file_filter = 'Файлы данных (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Выберите файл',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Файлы данных (*.txt)'
        )
        print(response)
        return response[0]

    def getFileNames(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )
        return response[0]

    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        return response

    def getSaveFileName(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            directory='Data File.dat',
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )
        print(response)
        return response[0]

    # ПОСТРОЕНИЕ ГРАФИКОВ
    def DrawGraphics(self, X, Y, F):
        self.ui.graphics.plot(X, Y, pen='b', symbol='o', symbolPen='b', symbolSize=1)
        self.ui.graphics.plot(X, F(X), pen='r', symbol='o', symbolPen='r', symbolSize=1)


    def LoadData(self):
        response = self.LoadCSV()
        X, Y, F = self.mController.LoadDataSet(response)
        self.DrawGraphics(X, Y, F)

    def PrepareData(self):
        response = self.LoadCSV()
        self.mController.DotReplace(response)


