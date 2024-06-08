import tkinter as tk
from PIL import Image, ImageTk

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

# Cria a janela principal
root = tk.Tk()
root.title("Animação com Tkinter")
root.resizable(False, False)  # Desabilita redimensionamento

# Configurações do canvas
canvas_width = 300  # Largura semelhante à de um celular
canvas_height = 600  # Altura semelhante à de um celular
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Carregar a imagem do personagem
img = Image.open("anime_character_neutral.png")
img_width, img_height = img.size
tk_img = ImageTk.PhotoImage(img)

# Definindo parâmetros da animação
x, y = (canvas_width - img_width) // 2, (canvas_height - img_height) // 2  # Centraliza a imagem no canvas
dx, dy = 5, 5

# Adiciona a imagem do personagem ao canvas
character_id = canvas.create_image(x, y, anchor=tk.NW, image=tk_img)

# Inicia a animação
move_image()

# Executa a aplicação
root.mainloop()
