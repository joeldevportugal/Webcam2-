# importar as bibliotecas a usar -------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from tkinter import PhotoImage
#--------------------------------------------------------------------------------------------------
# Função para atualizar a imagem da webcam --------------------------------------------------------
def update_webcam():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        label_foto.imgtk = frame
        label_foto.configure(image=frame)
        label_foto.after(10, update_webcam)
#--------------------------------------------------------------------------------------------------
# Função para capturar a imagem -------------------------------------------------------------------
def capturar_imagem():
    global frame_capturado
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        label_copia.imgtk = frame
        label_copia.configure(image=frame)
        messagebox.showinfo("imagem"," captura de imagem com sucesso!")
    else:
        messagebox.showerror("Erro","Erro ao capturar imagem!")
#--------------------------------------------------------------------------------------------------
# Função para selecionar a webcam -----------------------------------------------------------------
def Selecionar(event):
    global cap
    if cmb_device.get() == 'Webcam':
        cap = cv2.VideoCapture(0)
        update_webcam()
    else:
        cap.release()
#--------------------------------------------------------------------------------------------------
# Função para guardar a imagem capturada ----------------------------------------------------------
def Guardar():
    # Captura o frame atual da webcam
    ret, frame = cap.read()
    if ret:
        # Abre o diálogo de salvamento de arquivo
        file_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("BMP files", "*.bmp"), ("All Files", "*.*")])
        if file_path:
            # Salva a imagem no formato especificado pelo usuário
            cv2.imwrite(file_path, frame)
            messagebox.showinfo("Guardar", "Imagem salva com sucesso em: " + file_path)
    else:
        messagebox.showinfo("Erro", "Erro ao capturar imagem!")
#--------------------------------------------------------------------------------------------------
# função para Limpar a copia ----------------------------------------------------------------------
def Limpar():
    # Remove a imagem do label
    label_copia.imgtk = None
    label_copia.configure(image=None)
    messagebox.showinfo('Limpeza','Sua Copia Limpa com Sucesso !....')  
#---------------------------------------------------------------------------------------------------
# função para Sair ---------------------------------------------------------------------------------
def Sair():
    # Perguntar ao usuário se deseja sair
    resposta = messagebox.askyesno("Sair", "Deseja realmente sair? sim / nao")
    
    if resposta:  # Se o usuário escolher "Sim"
        Janela.destroy()  # Destruir a janela principal, encerrando o programa      
#---------------------------------------------------------------------------------------------------
# defnir as cores a Usar ---------------------------------------------------------------------------
co0 = '#FFFFFF'  # cor branco
co1 = '#F4F2F4'  # cor Cinza Botões
co2 = '#F6FFFF'  # cor Azul Claro Para O estido Combobox
#---------------------------------------------------------------------------------------------------
# configurar a Nossa janela ------------------------------------------------------------------------
Janela = Tk()
Janela.geometry('618x390+100+100')
Janela.resizable(0, 0)
Janela.title('Menu Webcam dev Joel 2024 PT 0.0.0.2 ©')
Janela.configure(bg=co0)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\icon.ico')
#---------------------------------------------------------------------------------------------------
# Criar um estilo ----------------------------------------------------------------------------------
style = ttk.Style()
#---------------------------------------------------------------------------------------------------
# Frame para a foto---------------------------------------------------------------------------------
frame_foto = Frame(Janela, width=300, height=300, bg='white')
frame_foto.place(x=10, y=35)
#---------------------------------------------------------------------------------------------------
# Frame para a cópia da foto -----------------------------------------------------------------------
frame_copia = Frame(Janela, width=300, height=300, bg='white')
frame_copia.place(x=320, y=35)
#--------------------------------------------------------------------------------------------------
# Criar combobox ----------------------------------------------------------------------------------
cmb_device = ttk.Combobox(Janela, width=40, style='Custom.TCombobox')
cmb_device.place(x=10, y=5)
cmb_device.set('Selecione a sua Webcam')
cmb_device.bind("<<ComboboxSelected>>", Selecionar)
cmb_device['values'] = ['Webcam']
#--------------------------------------------------------------------------------------------------
# Label para a foto -------------------------------------------------------------------------------
label_foto = Label(frame_foto, bg='white')
label_foto.pack(fill=BOTH, expand=YES)
label_foto.configure(width=295, height=290)  # Redimensiona o Label
#--------------------------------------------------------------------------------------------------
# Label para a cópia da foto ----------------------------------------------------------------------
label_copia = Label(frame_copia, bg='white')
label_copia.pack(fill=BOTH, expand=YES)
label_copia.configure(width=275, height=290)  # Redimensiona o Label
#--------------------------------------------------------------------------------------------------
# Carregar a imagem -------------------------------------------------------------------------------
image1 = PhotoImage(file="C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\capture.png")
image2 = PhotoImage(file="C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\save.png")
image3 = PhotoImage(file="C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\clear.png")
image4 = PhotoImage(file="C:\\Users\\HP\\Desktop\\Python tkinter\\Menu Webcam Versões\\Menu Webcam 2\\imagens\\close.png")
#--------------------------------------------------------------------------------------------------
# criar Os botões ---------------------------------------------------------------------------------
BtnCapturar = Button(Janela, image=image1, width=48, relief=RAISED, overrelief=RIDGE, bg=co1,command=capturar_imagem)
BtnCapturar.place(x=10, y=340)
BtnGuardar = Button(Janela, image=image2, width=48, relief=RAISED, overrelief=RIDGE, bg=co1,command=Guardar)
BtnGuardar.place(x=70, y=340)
BtnLimpar = Button(Janela, image=image3, width=48, relief=RAISED, overrelief=RIDGE, bg=co1,command=Limpar)
BtnLimpar.place(x=130, y=340)
BtnSair = Button(Janela, image=image4, width=48, relief=RAISED, overrelief=RIDGE, bg=co1,command=Sair)
BtnSair.place(x=190, y=340)
#---------------------------------------------------------------------------------------------------
# iniciar a Nossa Janela ---------------------------------------------------------------------------
Janela.mainloop()
#---------------------------------------------------------------------------------------------------