import random
import tkinter as tk
from tkinter import messagebox

class AmigoSecreto:
    def __init__(self):
        self.participantes = []
        self.sorteio = {}
        
        # Criar janela principal
        self.janela = tk.Tk()
        self.janela.title("Amigo Secreto")
        self.janela.geometry("400x500")
        
        # Criar elementos da interface
        tk.Label(self.janela, text="Nome do Participante:").pack(pady=5)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.pack(pady=5)
        
        tk.Button(self.janela, text="Adicionar Participante", command=self.adicionar_participante).pack(pady=5)
        
        self.lista_participantes = tk.Listbox(self.janela, width=40, height=10)
        self.lista_participantes.pack(pady=10)
        
        tk.Button(self.janela, text="Realizar Sorteio", command=self.realizar_sorteio).pack(pady=5)
        tk.Button(self.janela, text="Ver Meu Amigo Secreto", command=self.ver_amigo_secreto).pack(pady=5)
        
    def adicionar_participante(self):
        nome = self.entrada_nome.get().strip()
        if nome:
            if nome not in self.participantes:
                self.participantes.append(nome)
                self.lista_participantes.insert(tk.END, nome)
                self.entrada_nome.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Este participante já foi adicionado!")
        else:
            messagebox.showwarning("Aviso", "Por favor, digite um nome!")

    def realizar_sorteio(self):
        if len(self.participantes) < 3:
            messagebox.showwarning("Aviso", "É necessário pelo menos 3 participantes!")
            return
        
        # Criar uma cópia da lista de participantes para os sorteados
        sorteados = self.participantes.copy()
        
        # Realizar o sorteio
        self.sorteio.clear()
        for participante in self.participantes:
            while True:
                sorteado = random.choice(sorteados)
                if sorteado != participante:
                    self.sorteio[participante] = sorteado
                    sorteados.remove(sorteado)
                    break
        
        messagebox.showinfo("Sucesso", "Sorteio realizado com sucesso!")

    def ver_amigo_secreto(self):
        if not self.sorteio:
            messagebox.showwarning("Aviso", "O sorteio ainda não foi realizado!")
            return
        
        # Criar uma janela para consulta
        janela_consulta = tk.Toplevel(self.janela)
        janela_consulta.title("Consultar Amigo Secreto")
        janela_consulta.geometry("300x150")
        
        tk.Label(janela_consulta, text="Digite seu nome:").pack(pady=5)
        entrada_consulta = tk.Entry(janela_consulta)
        entrada_consulta.pack(pady=5)
        
        def consultar():
            nome = entrada_consulta.get().strip()
            if nome in self.sorteio:
                messagebox.showinfo("Seu Amigo Secreto", 
                                  f"Olá {nome}!\nSeu amigo secreto é: {self.sorteio[nome]}")
                janela_consulta.destroy()
            else:
                messagebox.showwarning("Erro", "Nome não encontrado!")
        
        tk.Button(janela_consulta, text="Consultar", command=consultar).pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = AmigoSecreto()
    app.iniciar()
