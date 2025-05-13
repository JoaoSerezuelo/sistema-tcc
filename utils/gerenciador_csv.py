import csv
import os
from models.aluno import Aluno
from models.professor import Professor
from models.coorientador import Coorientador
from models.tcc import TCC
from models.banca import Banca

class GerenciadorCSV:
    """
    Classe responsável pelo gerenciamento de dados em CSV.
    """
    def __init__(self, nome_arquivo="dados.csv"):
        """
        Inicializa o gerenciador CSV.
        
        Args:
            nome_arquivo (str, optional): Nome do arquivo CSV. Padrão é "dados.csv".
        """
        self.nome_arquivo = nome_arquivo
        self.alunos = {}  # Dicionário de alunos indexado por RA
        self.professores = {}  # Dicionário de professores indexado por nome
        self.coorientadores = {}  # Dicionário de coorientadores indexado por nome
        self.tccs = {}  # Dicionário de TCCs indexado por (ra_aluno, titulo)
        self.bancas = []  # Lista de bancas
        
    def carregar_dados(self):
        """
        Carrega os dados do arquivo CSV.
        
        Returns:
            bool: True se o arquivo foi carregado com sucesso, False caso contrário
        """
        if not os.path.exists(self.nome_arquivo):
            return False
            
        try:
            with open(self.nome_arquivo, 'r', encoding='utf-8', newline='') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    if not linha:  # Ignora linhas vazias
                        continue
                        
                    tipo_registro = linha[0]
                    
                    if tipo_registro == "ALUNO":
                        aluno = Aluno.from_csv(linha)
                        self.alunos[aluno.ra] = aluno
                        
                    elif tipo_registro == "PROFESSOR":
                        professor = Professor.from_csv(linha)
                        self.professores[professor.nome] = professor
                        
                    elif tipo_registro == "COORIENTADOR":
                        coorientador = Coorientador.from_csv(linha)
                        self.coorientadores[coorientador.nome] = coorientador
                        
                    elif tipo_registro == "TCC":
                        tcc = TCC.from_csv(linha, self.alunos, self.professores, self.coorientadores)
                        self.tccs[(tcc.aluno.ra, tcc.titulo)] = tcc
                        
                    elif tipo_registro == "BANCA":
                        banca = Banca.from_csv(linha, self.tccs, self.professores, self.coorientadores)
                        self.bancas.append(banca)
            
            return True
            
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
            return False
    
    def salvar_dados(self):
        """
        Salva os dados no arquivo CSV.
        
        Returns:
            bool: True se os dados foram salvos com sucesso, False caso contrário
        """
        try:
            with open(self.nome_arquivo, 'w', encoding='utf-8', newline='') as arquivo:
                escritor = csv.writer(arquivo)
                
                # Salva os alunos
                for aluno in self.alunos.values():
                    escritor.writerow(aluno.to_csv())
                
                # Salva os professores
                for professor in self.professores.values():
                    escritor.writerow(professor.to_csv())
                
                # Salva os coorientadores
                for coorientador in self.coorientadores.values():
                    escritor.writerow(coorientador.to_csv())
                
                # Salva os TCCs
                for tcc in self.tccs.values():
                    escritor.writerow(tcc.to_csv())
                
                # Salva as bancas
                for banca in self.bancas:
                    escritor.writerow(banca.to_csv())
            
            return True
            
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
            return False
    
    def criar_arquivo_vazio(self):
        """
        Cria um arquivo CSV vazio.
        
        Returns:
            bool: True se o arquivo foi criado com sucesso, False caso contrário
        """
        try:
            with open(self.nome_arquivo, 'w', encoding='utf-8', newline='') as arquivo:
                pass  # Apenas cria o arquivo vazio
            return True
        except Exception as e:
            print(f"Erro ao criar o arquivo: {e}")
            return False
