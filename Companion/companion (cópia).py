import tkinter as tk
from PIL import Image, ImageTk
import os

# Função para mover a imagem
def move_image():
    global x, y, dx, dy
    x += dx
    y += dy

    # Manter a imagem dentro dos limites do canvas
    if x >= canvas_width - img_width or x <= 0:
        dx = -dx
    if y >= canvas_height - img_height or y <= 0:
        dy = -dy

    canvas.coords(character_id, x, y)
    root.after(50, move_image)

# Função para alternar a expressão facial
def toggle_expression():
    global current_image
    current_image = (current_image + 1) % 2
    canvas.itemconfig(character_id, image=tk_images[current_image])
    root.after(1000, toggle_expression)

# Função para criar um arquivo .desktop
def create_desktop_file():
    desktop_entry = f"""
    [Desktop Entry]
    Name=My Application
    Comment=Um exemplo de aplicação Python
    Exec=python3 {os.path.abspath(__file__)}
    Icon={os.path.abspath('logo.png')}
    Terminal=false
    Type=Application
    Categories=Utility;
    """
    desktop_path = os.path.join(os.path.expanduser('~'), '.local/share/applications/my_application.desktop')
    with open(desktop_path, 'w') as f:
        f.write(desktop_entry.strip())
    print(f"Arquivo .desktop criado em: {desktop_path}")

# Verifica se o arquivo .desktop existe, se não, cria
desktop_file_path = os.path.join(os.path.expanduser('~'), '.local/share/applications/my_application.desktop')
if not os.path.exists(desktop_file_path):
    create_desktop_file()

# Cria a janela principal
root = tk.Tk()
root.title("Animação com Tkinter")
root.resizable(False, False)  # Desabilita redimensionamento

# Definir o ícone da janela
icon_path = "logo.png"
if os.path.exists(icon_path):
    icon_img = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_img)
    root.tk.call('wm', 'iconphoto', root._w, icon_photo)
else:
    print(f"Arquivo de ícone não encontrado: {icon_path}")

# Configurações do canvas
canvas_width = 300  # Largura semelhante à de um celular
canvas_height = 600  # Altura semelhante à de um celular
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Carregar as duas imagens do personagem e redimensionar
img1 = Image.open("anime_character_neutral.png")
img2 = Image.open("anime_character_smile.png")
img_width, img_height = img1.size
resize_factor = 0.5  # Fator de redimensionamento (50%)
img1_resized = img1.resize((int(img_width * resize_factor), int(img_height * resize_factor)))
img2_resized = img2.resize((int(img_width * resize_factor), int(img_height * resize_factor)))
tk_img1 = ImageTk.PhotoImage(img1_resized)
tk_img2 = ImageTk.PhotoImage(img2_resized)
tk_images = [tk_img1, tk_img2]

# Definindo parâmetros da animação
x, y = (canvas_width - img1_resized.width) // 2, (canvas_height - img1_resized.height) // 2  # Centraliza a imagem no canvas
dx, dy = 5, 5

# Adiciona a imagem do personagem ao canvas
current_image = 0
character_id = canvas.create_image(x, y, anchor=tk.NW, image=tk_images[current_image])

# Inicia a animação
move_image()
toggle_expression()

# Executa a aplicação
root.mainloop()
