# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from ctypes import *

lib = cdll.LoadLibrary(r"C:\Windows\System32\msvcrt.dll")
lib2 = cdll.LoadLibrary(r"C:\ICPDAS\UniDAQ\driver\DLL\x64\UniDAQ.dll")

var_c = 51
print_from_C = getattr(lib, "printf")  # да, тут можно вписать даже "??2@YAPAXI@Z"
print_from_C(b"Print int_c = %d\n", var_c)

#Public Function Ixud_GetDllVersion(ByRef dwDLLver As UInt32) As UInt16

Ixud_GetDllVersion = getattr(lib2, "Ixud_GetDllVersion")
version = Ixud_GetDllVersion()

print(">>", version)