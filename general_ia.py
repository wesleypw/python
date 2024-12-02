import random

# Definição das constantes do jogo
# Estas constantes podem ser modificadas para alterar a dificuldade do jogo
MAX_DADOS = 5        # Número total de dados no jogo
LADOS_DADO = 6       # Número de lados em cada dado
MAX_TENTATIVAS = 3   # Número máximo de tentativas por rodada
MIN_DADOS_IGUAIS = 2 # Número mínimo de dados iguais necessários para vencer

class JogoDados:
    """
    Classe principal que controla toda a lógica do jogo General.
    O jogo consiste em rolar dados e tentar conseguir números iguais.
    """
    
    def __init__(self):
        """
        Método construtor da classe.
        Inicializa a lista de valores dos dados vazia e já faz primeira rolagem.
        """
        self.valores_dados = []  # Lista que armazena os valores atuais dos dados
        self.resetar_dados()     # Faz a primeira rolagem dos dados
    
    def resetar_dados(self):
        """
        Gera novos valores aleatórios para todos os dados.
        Usa list comprehension para criar uma lista com valores entre 1 e LADOS_DADO.
        """
        self.valores_dados = [random.randint(1, LADOS_DADO) for _ in range(MAX_DADOS)]
    
    def obter_valores_dados(self):
        """
        Retorna a lista atual com os valores dos dados.
        Este método é útil quando precisamos acessar os valores sem modificá-los.
        """
        return self.valores_dados
    
    def verificar_combinacao_vencedora(self, dados_selecionados):
        """
        Verifica se os dados selecionados formam uma combinação vencedora.
        
        Parâmetros:
            dados_selecionados (list): Lista com os valores dos dados escolhidos
        
        Retorna:
            bool: True se houver 2 ou mais dados iguais, False caso contrário
        """
        # Verifica se tem dados suficientes e se são todos iguais ao primeiro
        if len(dados_selecionados) >= MIN_DADOS_IGUAIS:
            return all(dado == dados_selecionados[0] for dado in dados_selecionados)
        return False

    def jogar_rodada(self):
        """
        Controla uma rodada completa do jogo.
        Uma rodada consiste em até MAX_TENTATIVAS tentativas de conseguir dados iguais.
        
        Retorna:
            bool: True se o jogador venceu, False se perdeu
        """
        # Loop principal da rodada
        for tentativa in range(MAX_TENTATIVAS):
            print(f"\n=== Tentativa {tentativa + 1} de {MAX_TENTATIVAS} ===")
            self.resetar_dados()  # Gera novos valores para os dados
            dados_selecionados = self.obter_escolhas_jogador()  # Jogador escolhe os dados
            
            # Verifica se o jogador venceu
            if self.verificar_combinacao_vencedora(dados_selecionados):
                print("\nParabéns! Você conseguiu dados iguais!")
                return True
            # Se não venceu mas ainda tem tentativas
            elif tentativa < MAX_TENTATIVAS - 1:
                print("\nTente novamente! Os dados não são iguais.")
            # Se acabaram as tentativas
            else:
                print("\nFim de Jogo! Suas tentativas acabaram.")
        return False

    def obter_escolhas_jogador(self):
        """
        Gerencia a interação com o jogador para escolher os dados.
        Permite que o jogador selecione quais dados quer manter para a próxima rodada.
        
        Retorna:
            list: Lista com os valores dos dados escolhidos pelo jogador
        """
        dados_selecionados = []  # Lista para armazenar os dados escolhidos
        # Mostra os valores atuais dos dados
        print(f"\nDados atuais: {', '.join(map(str, self.valores_dados))}")
        
        # Loop de tentativas para escolher dados
        for tentativa in range(MAX_TENTATIVAS):
            print(f"\nTentativa {tentativa + 1} de {MAX_TENTATIVAS}")
            print("Quais dados você quer guardar? (Digite os números dos dados separados por espaço)")
            print("Exemplo: Se quiser guardar o primeiro e terceiro dado, digite: 1 3")
            print("Pressione Enter para pular a tentativa")
            
            try:
                # Obtém e processa a entrada do usuário
                escolha = input("Sua escolha: ").strip()
                if not escolha:  # Se o usuário só apertar Enter, pula a tentativa
                    continue
                
                # Converte as posições escolhidas em números
                posicoes = [int(pos) for pos in escolha.split()]
                # Processa cada posição escolhida
                for pos in posicoes:
                    if 1 <= pos <= MAX_DADOS:  # Verifica se a posição é válida
                        dados_selecionados.append(self.valores_dados[pos-1])
                    else:
                        print(f"Posição {pos} inválida. Use números de 1 até {MAX_DADOS}.")
                
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números separados por espaço.")
            
            # Mostra os dados que foram guardados até agora
            if dados_selecionados:
                print(f"Dados guardados até agora: {dados_selecionados}")
        
        return dados_selecionados

def menu_principal():
    """
    Função que controla o menu principal do jogo.
    Permite que o jogador inicie um novo jogo ou saia do programa.
    """
    jogo = JogoDados()  # Cria uma nova instância do jogo
    
    # Loop principal do menu
    while True:
        print("\n=== MENU ===")
        print("Bem-vindo ao jogo do General!")
        print("1 - Jogar")
        print("2 - Sair")
        
        try:
            # Processa a escolha do usuário
            opcao = int(input("\nDigite a opção desejada: "))
            if opcao == 1:
                jogo.jogar_rodada()  # Inicia uma nova rodada
            elif opcao == 2:
                print("Obrigado por jogar!")
                break  # Sai do jogo
            else:
                print("Opção inválida! Por favor, escolha 1 para jogar ou 2 para sair.")
        except ValueError:
            print("Por favor, digite apenas números!")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()