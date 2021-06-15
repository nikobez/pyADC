# This is a sample Python script.
#

from ctypes import *
from PyQt5 import QtWidgets, uic
import sys

#lib = cdll.LoadLibrary(r"C:\ICPDAS\UniDAQ\driver\DLL\x64\UniDAQ.dll")

#Public Function Ixud_GetDllVersion(ByRef dwDLLver As UInt32) As UInt16
#
#Ixud_GetDllVersion = getattr(lib2, "Ixud_GetDllVersion")
#version = Ixud_GetDllVersion()
#
#print(">>", version)

app = QtWidgets.QApplication([])
win = uic.loadUi("forms/mainform.ui")

win.show()
sys.exit(app.exec())