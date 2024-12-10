# Importando bibliotecas necessárias
import random  # Para realizar o sorteio aleatório
import tkinter as tk  # Para criar a interface gráfica
from tkinter import messagebox  # Para exibir mensagens ao usuário

class AmigoSecreto:
    def __init__(self):
        # Inicializa as listas e dicionários para armazenar os dados
        self.participantes = []  # Lista para armazenar os nomes dos participantes
        self.sorteio = {}  # Dicionário para armazenar o resultado do sorteio
        
        # Configuração da janela principal
        self.janela = tk.Tk()
        self.janela.title("Amigo Secreto")  # Define o título da janela
        self.janela.geometry("400x500")  # Define o tamanho da janela
        
        # Criação dos elementos da interface
        tk.Label(self.janela, text="Nome do Participante:").pack(pady=5)  # Rótulo para entrada de nome
        self.entrada_nome = tk.Entry(self.janela)  # Campo para digitar o nome
        self.entrada_nome.pack(pady=5)
        
        # Botão para adicionar participante
        tk.Button(self.janela, text="Adicionar Participante", command=self.adicionar_participante).pack(pady=5)
        
        # Lista para exibir os participantes adicionados
        self.lista_participantes = tk.Listbox(self.janela, width=40, height=10)
        self.lista_participantes.pack(pady=10)
        
        # Botões para realizar sorteio e ver resultado
        tk.Button(self.janela, text="Realizar Sorteio", command=self.realizar_sorteio).pack(pady=5)
        tk.Button(self.janela, text="Ver Meu Amigo Secreto", command=self.ver_amigo_secreto).pack(pady=5)
        
    def adicionar_participante(self):
        # Obtém o nome digitado e remove espaços em branco
        nome = self.entrada_nome.get().strip()
        if nome:  # Verifica se o nome não está vazio
            if nome not in self.participantes:  # Verifica se o nome já não foi adicionado
                self.participantes.append(nome)  # Adiciona o nome à lista
                self.lista_participantes.insert(tk.END, nome)  # Adiciona o nome na lista visual
                self.entrada_nome.delete(0, tk.END)  # Limpa o campo de entrada
            else:
                messagebox.showwarning("Aviso", "Este participante já foi adicionado!")  # Avisa sobre duplicidade
        else:
            messagebox.showwarning("Aviso", "Por favor, digite um nome!")  # Avisa sobre campo vazio

    def realizar_sorteio(self):
        # Verifica se há participantes suficientes
        if len(self.participantes) < 3:
            messagebox.showwarning("Aviso", "É necessário pelo menos 3 participantes!")
            return
        
        # Cria uma cópia da lista para manipular durante o sorteio
        sorteados = self.participantes.copy()
        
        # Realiza o sorteio
        self.sorteio.clear()  # Limpa sorteios anteriores
        for participante in self.participantes:
            while True:
                sorteado = random.choice(sorteados)  # Escolhe um nome aleatório
                if sorteado != participante:  # Verifica se não tirou o próprio nome
                    self.sorteio[participante] = sorteado  # Registra o sorteio
                    sorteados.remove(sorteado)  # Remove o sorteado da lista
                    break
        
        messagebox.showinfo("Sucesso", "Sorteio realizado com sucesso!")  # Confirma o sorteio

    def ver_amigo_secreto(self):
        # Verifica se já foi realizado o sorteio
        if not self.sorteio:
            messagebox.showwarning("Aviso", "O sorteio ainda não foi realizado!")
            return
        
        # Cria uma nova janela para consulta
        janela_consulta = tk.Toplevel(self.janela)
        janela_consulta.title("Consultar Amigo Secreto")
        janela_consulta.geometry("300x150")
        
        # Elementos da janela de consulta
        tk.Label(janela_consulta, text="Digite seu nome:").pack(pady=5)
        entrada_consulta = tk.Entry(janela_consulta)
        entrada_consulta.pack(pady=5)
        
        def consultar():
            # Função interna para realizar a consulta
            nome = entrada_consulta.get().strip()
            if nome in self.sorteio:  # Verifica se o nome existe no sorteio
                messagebox.showinfo("Seu Amigo Secreto", f"Olá {nome}!\nSeu amigo secreto é: {self.sorteio[nome]}")
                ,,
                janela_consulta.destroy()  # Fecha a janela após consulta
            else:
                messagebox.showwarning("Erro", "Nome não encontrado!")
        
        tk.Button(janela_consulta, text="Consultar", command=consultar).pack(pady=10)

    def iniciar(self):
        # Inicia o loop principal da aplicação
        self.janela.mainloop()

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    app = AmigoSecreto()  # Cria uma instância da aplicação
    app.iniciar()  # Inicia a aplicação
