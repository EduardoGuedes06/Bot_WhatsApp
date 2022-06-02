import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys", "gzip","tkinter", "xlrd", "urllib", "selenium"], "includes": ["tkinter", "xlrd", "urllib", "time", "selenium"]}

base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "BOT_WHATSAPP",
    version = "0.1",
    description = "BOT_WHATSAPP",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)])

#Comando para compilar o codigo
#"c:\Users\CDHU Agentes\AppData\Local\Programs\Python\Python37-32\python.exe" setup.py build