import tkinter as tk
import random


class CampoMinado:
    def __init__(self, root, tamanho, num_minas):
        self.tamanho = tamanho
        self.num_minas = num_minas
        self.tabuleiro = []
        self.revelado = []
        self.botoes = []
        self.minas = set()
        self.jogo_terminado = False
        
        # Configuração da janela
        self.root = root
        self.root.title("Campo Minado")
        
        # Criar o tabuleiro e configurar o jogo
        self.criar_tabuleiro()
        self.colocar_minas()
        self.calcular_numeros()
        self.criar_botoes()

    def criar_tabuleiro(self):
        """Inicializa o tabuleiro e a matriz de células reveladas."""
        self.tabuleiro = [[' ' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.revelado = [[False for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def colocar_minas(self):
        """Coloca minas em posições aleatórias no tabuleiro."""
        while len(self.minas) < self.num_minas:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)
            self.minas.add((linha, coluna))
        for (linha, coluna) in self.minas:
            self.tabuleiro[linha][coluna] = 'M'

    def calcular_numeros(self):
        """Calcula os números ao redor das minas."""
        direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for linha in range(self.tamanho):
            for coluna in range(self.tamanho):
                if self.tabuleiro[linha][coluna] == 'M':
                    continue
                contador = 0
                for d_linha, d_coluna in direcoes:
                    nova_linha, nova_coluna = linha + d_linha, coluna + d_coluna
                    if (
                        0 <= nova_linha < self.tamanho
                        and 0 <= nova_coluna < self.tamanho
                        and self.tabuleiro[nova_linha][nova_coluna] == 'M'
                    ):
                        contador += 1
                self.tabuleiro[linha][coluna] = str(contador) if contador > 0 else ' '

    def criar_botoes(self):
        """Cria os botões na interface para o jogador interagir."""
        for i in range(self.tamanho):
            linha_botoes = []
            for j in range(self.tamanho):
                botao = tk.Button(
                    self.root, 
                    text='', 
                    width=3, 
                    height=1, 
                    command=lambda i=i, j=j: self.revelar_celula(i, j)
                )
                botao.bind("<Button-3>", lambda event, i=i, j=j: self.marcar_mina(i, j))
                botao.grid(row=i, column=j)
                linha_botoes.append(botao)
            self.botoes.append(linha_botoes)

    def revelar_celula(self, linha, coluna):
        """Revela uma célula no tabuleiro."""
        if self.jogo_terminado or self.revelado[linha][coluna]:
            return

        self.revelado[linha][coluna] = True
        self.botoes[linha][coluna].config(text=self.tabuleiro[linha][coluna], state="disabled")

        if self.tabuleiro[linha][coluna] == 'M':
            self.botoes[linha][coluna].config(bg='red')
            self.fim_de_jogo(False)
        elif self.tabuleiro[linha][coluna] == ' ':
            self.botoes[linha][coluna].config(bg='light grey')
            # Revela células adjacentes se for um espaço vazio
            direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for d_linha, d_coluna in direcoes:
                nova_linha, nova_coluna = linha + d_linha, coluna + d_coluna
                if 0 <= nova_linha < self.tamanho and 0 <= nova_coluna < self.tamanho:
                    self.revelar_celula(nova_linha, nova_coluna)

        # Verifica vitória
        if all(
            (self.revelado[i][j] or (i, j) in self.minas)
            for i in range(self.tamanho)
            for j in range(self.tamanho)
        ):
            self.fim_de_jogo(True)

    def marcar_mina(self, linha, coluna):
        """Marca ou desmarca uma célula como mina (botão direito)."""
        if not self.revelado[linha][coluna]:
            botao = self.botoes[linha][coluna]
            if botao["text"] == '':
                botao.config(text='🚩', fg='orange')
            else:
                botao.config(text='')

    def fim_de_jogo(self, venceu):
        """Finaliza o jogo e exibe uma mensagem."""
        self.jogo_terminado = True
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) in self.minas:
                    self.botoes[i][j].config(text='M', bg='red')
                self.botoes[i][j].config(state="disabled")
        if venceu:
            tk.messagebox.showinfo("Campo Minado", "Parabéns! Você venceu! 🎉")
        else:
            tk.messagebox.showinfo("Campo Minado", "Você perdeu! 💥")

# Função para iniciar o jogo
def iniciar_jogo():
    root = tk.Tk()
    tamanho = 9  # Tamanho do tabuleiro (ex.: 9x9)
    num_minas = 10  # Número de minas
    CampoMinado(root, tamanho, num_minas)
    root.mainloop()

# Iniciar o jogo
iniciar_jogo()
