import tkinter as tk

root = tk.Tk()
root.title("minha janela interativa")
root.geometry("800x600")

root.configure(bg="white")

label = tk.Label(root, text="bem-vindo ao tkinter", font=("Arial", 16), bg="white", fg="blue")
label.pack(pady=20)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=60)

def exibir_texto():
    texto = entrada.get()
    print(f"Você digitou: {texto}")

botao_exibir = tk.Button(root, text="Exibir Texto", font=("Arial", 14),fg="white",bg="blue", command=exibir_texto)
botao_exibir.pack(pady=10)

root.mainloop()

