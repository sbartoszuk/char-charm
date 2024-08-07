#!/usr/bin/env python

import ctypes

STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * 32)]

def change_font_size(height, width = None):
    kernel32 = ctypes.WinDLL("Kernel32.dll")

    GetStdHandle = kernel32.GetStdHandle

    SetCurrentConsoleFontEx = kernel32.SetCurrentConsoleFontEx

    stdout = GetStdHandle(STD_OUTPUT_HANDLE)
    if not stdout:
        return 1

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)

    if width == None:
        width = height
    else:
        width = height//2

    font.dwFontSize.X = width
    font.dwFontSize.Y = height

    res = SetCurrentConsoleFontEx(stdout, False, ctypes.byref(font))