import tkinter as tk
from PIL import Image, ImageTk
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Rota para servir arquivos estáticos (imagens)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Função para mover a imagem
def move_image(canvas, character_id, x, y, dx, dy):
    x += dx
    y += dy

    # Manter a imagem dentro dos limites do canvas
    if x >= canvas.winfo_width() - img_width or x <= 0:
        dx = -dx
    if y >= canvas.winfo_height() - img_height or y <= 0:
        dy = -dy

    canvas.coords(character_id, x, y)

    return x, y, dx, dy

# Função para criar a animação Tkinter
def create_animation(root, canvas, img_path):
    img = Image.open(img_path)
    img_width, img_height = img.size
    tk_img = ImageTk.PhotoImage(img)

    x, y = (canvas.winfo_width() - img_width) // 2, (canvas.winfo_height() - img_height) // 2
    dx, dy = 5, 5

    character_id = canvas.create_image(x, y, anchor=tk.NW, image=tk_img)

    def animate():
        nonlocal x, y, dx, dy
        x, y, dx, dy = move_image(canvas, character_id, x, y, dx, dy)
        root.after(50, animate)

    animate()

# Rota para a animação Tkinter
@app.route('/animation')
def animation():
    root = tk.Tk()
    root.title("Animação com Tkinter")
    root.resizable(False, False)

    canvas_width = 300
    canvas_height = 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    create_animation(root, canvas, "static/anime_character_neutral.png")

    root.mainloop()

    return ''

# Rota padrão para renderizar o template HTML original
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
