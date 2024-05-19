import sys
from cx_Freeze import setup, Executable
import os

# Inclua os arquivos necessários no pacote
files = [
    "C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\icon.ico",
    "C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\capture.png",
    "C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\save.png",
    "C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\clear.png",
    "C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\close.png"
]

# Verifica se a plataforma é Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# Cria o executável
executables = [
    Executable(
        script="webcam2.py",
        base=base,
        icon="C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\icon.ico"
    )
]

# Setup cx_Freeze
setup(
    name="Webcam2.exe",
    version="0.0.0.2",
    description="Menu Webcam dev Joel 2024 PT",
    options={
        'build_exe': {
            'packages': ["tkinter", "cv2", "PIL"],
            'include_files': files
        }
    },
    executables=executables
)
