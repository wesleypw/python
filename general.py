import tkinter as tk
from tkinter import messagebox
import random

class JogoDeDados:
    def __init__(self, master):
        self.master = master
        master.title("Jogo de Dados")
        master.geometry("500x600")
        master.configure(bg='#f0f0f0')

        self.tentativas_restantes = 3
        self.dados_atuais = []
        self.dados_guardados = []

        self.criar_interface()

    def criar_interface(self):
        # Título
        self.titulo = tk.Label(self.master, text="Jogo de Dados", 
                               font=("Arial", 20, "bold"), 
                               bg='#f0f0f0', fg='#333')
        self.titulo.pack(pady=20)

        # Frame para os dados
        self.frame_dados = tk.Frame(self.master, bg='#f0f0f0')
        self.frame_dados.pack(pady=20)

        self.labels_dados = []
        for i in range(5):
            label = tk.Label(self.frame_dados, text="?", 
                             font=("Arial", 16), 
                             width=4, relief=tk.RAISED, 
                             bg='white', fg='#333')
            label.grid(row=0, column=i, padx=5)
            self.labels_dados.append(label)

        # Botões de seleção de dados
        self.frame_botoes = tk.Frame(self.master, bg='#f0f0f0')
        self.frame_botoes.pack(pady=20)

        self.botoes_selecao = []
        for i in range(5):
            btn = tk.Button(self.frame_botoes, text=f"Dado {i+1}", 
                            command=lambda idx=i: self.selecionar_dado(idx),
                            bg='#4CAF50', fg='white')
            btn.grid(row=0, column=i, padx=5)
            self.botoes_selecao.append(btn)

        # Botão de jogar
        self.btn_jogar = tk.Button(self.master, text="Jogar Dados", 
                                   command=self.jogar_dados,
                                   bg='#2196F3', fg='white', 
                                   font=("Arial", 12, "bold"))
        self.btn_jogar.pack(pady=20)

        # Área de status
        self.label_status = tk.Label(self.master, text="Bem-vindo ao Jogo de Dados!", 
                                     bg='#f0f0f0', fg='#333', 
                                     font=("Arial", 10))
        self.label_status.pack(pady=10)

        # Frame para dados guardados
        self.frame_guardados = tk.Frame(self.master, bg='#f0f0f0')
        self.frame_guardados.pack(pady=10)

        self.label_guardados = tk.Label(self.frame_guardados, text="Dados Guardados: ", 
                                        bg='#f0f0f0', fg='#333')
        self.label_guardados.pack()

    def jogar_dados(self):
        if self.tentativas_restantes > 0:
            # Gerar novos dados
            self.dados_atuais = [random.randint(1, 6) for _ in range(5)]
            
            # Atualizar labels dos dados
            for i, valor in enumerate(self.dados_atuais):
                self.labels_dados[i].config(text=str(valor))
            
            self.tentativas_restantes -= 1
            
            # Verificar se há dados iguais guardados
            if len(self.dados_guardados) >= 3 and all(d == self.dados_guardados[0] for d in self.dados_guardados):
                messagebox.showinfo("Parabéns!", "Você conseguiu 3 ou mais dados iguais!")
                self.reiniciar_jogo()
            else:
                self.label_status.config(text=f"Tentativas restantes: {self.tentativas_restantes}")
                
                if self.tentativas_restantes == 0:
                    messagebox.showinfo("Game Over", "Suas tentativas acabaram!")
                    self.reiniciar_jogo()

    def selecionar_dado(self, indice):
        valor = self.dados_atuais[indice]
        if valor not in self.dados_guardados:
            self.dados_guardados.append(valor)
            self.botoes_selecao[indice].config(state=tk.DISABLED, bg='gray')
            
            # Atualizar label de dados guardados
            guardados_str = ", ".join(map(str, self.dados_guardados))
            self.label_guardados.config(text=f"Dados Guardados: {guardados_str}")
            
            # Verificar se já tem 3 ou mais dados iguais
            if len(self.dados_guardados) >= 3 and all(d == self.dados_guardados[0] for d in self.dados_guardados):
                messagebox.showinfo("Parabéns!", "Você conseguiu 3 ou mais dados iguais!")
                self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.tentativas_restantes = 3
        self.dados_atuais = []
        self.dados_guardados = []
        
        # Resetar labels dos dados
        for label in self.labels_dados:
            label.config(text="?")
        
        # Reativar botões
        for btn in self.botoes_selecao:
            btn.config(state=tk.NORMAL, bg='#4CAF50')
        
        # Limpar label de dados guardados
        self.label_guardados.config(text="Dados Guardados: ")
        
        self.label_status.config(text="Bem-vindo ao Jogo de Dados!")

def main():
    root = tk.Tk()
    jogo = JogoDeDados(root)
    root.mainloop()

if __name__ == "__main__":
    main()