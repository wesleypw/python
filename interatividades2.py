import tkinter as tk

root = tk.Tk()
root.title("Eventos e Interatividade 🎯")
root.geometry("400x300")
root.configure(bg="white")

label = tk.Label(root, text="Bem-vindo ao Tkinter!", font=("Arial", 16), bg="white", fg="blue")
label.pack(pady=20)  # Exibindo o rótulo com espaçamento vertical

label_resultado = tk.Label(root, text="Aguardando tecla...", font=("Arial", 12), bg="lightgray", fg="white")
label_resultado.pack(pady=10)

def atualizar_label(event):
	label_resultado.config(text=f"Tecla pressionada: {event.char}")

label_instrucao = tk.Label(root, text="Pressione uma tecla ou clique no botão!", font=("Arial", 14), bg="white")
label_instrucao.pack(pady=10)
def botao_clicado():
	print("Botão clicado! 🎉")
botao_interativo = tk.Button(root, text="Clique Aqui", font=("Arial", 14), bg="blue", fg="white", command=botao_clicado)
botao_interativo.pack(pady=10)

root.bind("<Key>", atualizar_label)


root.mainloop()

