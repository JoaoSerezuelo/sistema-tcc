import os
import sys
from utils.gerenciador_csv import GerenciadorCSV

class InterfaceUsuario:
    """
    Classe responsável pela interface de linha de comando do sistema.
    """
    def __init__(self):
        """
        Inicializa a interface de usuário.
        """
        self.gerenciador = None
        self.arquivo_csv = None
        self.alteracoes_nao_salvas = False
    
    def iniciar(self):
        """
        Inicia a execução do sistema.
        """
        self._configurar_arquivo()
        self._exibir_menu_principal()
    
    def _configurar_arquivo(self):
        """
        Configura o arquivo CSV a ser utilizado.
        """
        # Verifica se foi fornecido um arquivo como argumento
        if len(sys.argv) > 1:
            self.arquivo_csv = sys.argv[1]
        else:
            self.arquivo_csv = input("Digite o nome do arquivo CSV (ou pressione Enter para usar 'dados.csv'): ")
            if not self.arquivo_csv:
                self.arquivo_csv = "dados.csv"
        
        self.gerenciador = GerenciadorCSV(self.arquivo_csv)
        
        # Verifica se o arquivo existe
        if not os.path.exists(self.arquivo_csv):
            print(f"O arquivo '{self.arquivo_csv}' não existe.")
            opcao = input("Deseja criar um novo arquivo vazio? (S/N): ").strip().upper()
            
            if opcao == 'S':
                if self.gerenciador.criar_arquivo_vazio():
                    print(f"Arquivo '{self.arquivo_csv}' criado com sucesso.")
                else:
                    print(f"Não foi possível criar o arquivo '{self.arquivo_csv}'.")
                    sys.exit(1)
            else:
                print("Operação cancelada.")
                sys.exit(0)
        else:
            # Pergunta se deseja carregar os dados do arquivo
            opcao = input(f"Deseja carregar os dados do arquivo '{self.arquivo_csv}'? (S/N): ").strip().upper()
            
            if opcao == 'S':
                if self.gerenciador.carregar_dados():
                    print(f"Dados do arquivo '{self.arquivo_csv}' carregados com sucesso.")
                else:
                    print(f"Não foi possível carregar os dados do arquivo '{self.arquivo_csv}'.")
                    sys.exit(1)
    
    def _exibir_menu_principal(self):
        """
        Exibe o menu principal do sistema.
        """
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE GERENCIAMENTO DE TCCs")
            print("="*50)
            print("1. Gerenciar Alunos")
            print("2. Gerenciar Professores")
            print("3. Gerenciar Coorientadores")
            print("4. Gerenciar TCCs")
            print("5. Gerenciar Bancas")
            print("6. Visualizar Dados")
            print("7. Gerar Relatórios")
            print("8. Salvar Dados")
            print("0. Sair")
            print("="*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._menu_alunos()
            elif opcao == '2':
                self._menu_professores()
            elif opcao == '3':
                self._menu_coorientadores()
            elif opcao == '4':
                self._menu_tccs()
            elif opcao == '5':
                self._menu_bancas()
            elif opcao == '6':
                self._menu_visualizacao()
            elif opcao == '7':
                self._menu_relatorios()
            elif opcao == '8':
                self._salvar_dados()
            elif opcao == '0':
                self._sair()
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_alunos(self):
        """
        Exibe o menu de gerenciamento de alunos.
        """
        while True:
            print("\n" + "-"*50)
            print("GERENCIAMENTO DE ALUNOS")
            print("-"*50)
            print("1. Cadastrar Aluno")
            print("2. Visualizar Alunos")
            print("3. Atualizar Aluno")
            print("4. Remover Aluno")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._cadastrar_aluno()
            elif opcao == '2':
                self._visualizar_alunos()
            elif opcao == '3':
                self._atualizar_aluno()
            elif opcao == '4':
                self._remover_aluno()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_professores(self):
        """
        Exibe o menu de gerenciamento de professores.
        """
        while True:
            print("\n" + "-"*50)
            print("GERENCIAMENTO DE PROFESSORES")
            print("-"*50)
            print("1. Cadastrar Professor")
            print("2. Visualizar Professores")
            print("3. Atualizar Professor")
            print("4. Remover Professor")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._cadastrar_professor()
            elif opcao == '2':
                self._visualizar_professores()
            elif opcao == '3':
                self._atualizar_professor()
            elif opcao == '4':
                self._remover_professor()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_coorientadores(self):
        """
        Exibe o menu de gerenciamento de coorientadores.
        """
        while True:
            print("\n" + "-"*50)
            print("GERENCIAMENTO DE COORIENTADORES")
            print("-"*50)
            print("1. Cadastrar Coorientador")
            print("2. Visualizar Coorientadores")
            print("3. Atualizar Coorientador")
            print("4. Remover Coorientador")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._cadastrar_coorientador()
            elif opcao == '2':
                self._visualizar_coorientadores()
            elif opcao == '3':
                self._atualizar_coorientador()
            elif opcao == '4':
                self._remover_coorientador()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_tccs(self):
        """
        Exibe o menu de gerenciamento de TCCs.
        """
        while True:
            print("\n" + "-"*50)
            print("GERENCIAMENTO DE TCCs")
            print("-"*50)
            print("1. Cadastrar TCC")
            print("2. Visualizar TCCs")
            print("3. Atualizar TCC")
            print("4. Remover TCC")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._cadastrar_tcc()
            elif opcao == '2':
                self._visualizar_tccs()
            elif opcao == '3':
                self._atualizar_tcc()
            elif opcao == '4':
                self._remover_tcc()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_bancas(self):
        """
        Exibe o menu de gerenciamento de bancas.
        """
        while True:
            print("\n" + "-"*50)
            print("GERENCIAMENTO DE BANCAS")
            print("-"*50)
            print("1. Cadastrar Banca")
            print("2. Visualizar Bancas")
            print("3. Atualizar Banca")
            print("4. Remover Banca")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._cadastrar_banca()
            elif opcao == '2':
                self._visualizar_bancas()
            elif opcao == '3':
                self._atualizar_banca()
            elif opcao == '4':
                self._remover_banca()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_visualizacao(self):
        """
        Exibe o menu de visualização de dados.
        """
        while True:
            print("\n" + "-"*50)
            print("VISUALIZAÇÃO DE DADOS")
            print("-"*50)
            print("1. Listar Alunos")
            print("2. Listar Professores")
            print("3. Listar Coorientadores")
            print("4. Listar TCCs")
            print("5. Listar Bancas")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._visualizar_alunos()
            elif opcao == '2':
                self._visualizar_professores()
            elif opcao == '3':
                self._visualizar_coorientadores()
            elif opcao == '4':
                self._visualizar_tccs()
            elif opcao == '5':
                self._visualizar_bancas()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _menu_relatorios(self):
        """
        Exibe o menu de geração de relatórios.
        """
        while True:
            print("\n" + "-"*50)
            print("GERAÇÃO DE RELATÓRIOS")
            print("-"*50)
            print("1. Gerar Relatório de TCCs")
            print("2. Gerar Relatório de Bancas")
            print("0. Voltar")
            print("-"*50)
            
            opcao = input("Digite a opção desejada: ").strip()
            
            if opcao == '1':
                self._gerar_relatorio_tccs()
            elif opcao == '2':
                self._gerar_relatorio_bancas()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def _salvar_dados(self):
        """
        Salva os dados no arquivo CSV.
        """
        if self.gerenciador.salvar_dados():
            print(f"Dados salvos com sucesso no arquivo '{self.arquivo_csv}'.")
            self.alteracoes_nao_salvas = False
        else:
            print(f"Não foi possível salvar os dados no arquivo '{self.arquivo_csv}'.")
    
    def _sair(self):
        """
        Encerra a execução do sistema.
        """
        if self.alteracoes_nao_salvas:
            opcao = input("Existem alterações não salvas. Deseja salvar antes de sair? (S/N): ").strip().upper()
            
            if opcao == 'S':
                self._salvar_dados()
        
        print("Encerrando o sistema...")
    
    # Implementação das funcionalidades de CRUD para Alunos
    def _cadastrar_aluno(self):
        """
        Cadastra um novo aluno no sistema.
        """
        from models.aluno import Aluno
        
        print("\nCADASTRO DE ALUNO")
        
        while True:
            ra = input("RA do aluno: ").strip()
            if not ra:
                print("RA não pode ser vazio.")
                continue
            
            if ra in self.gerenciador.alunos:
                print(f"Já existe um aluno com o RA '{ra}'.")
                continue
            
            break
        
        nome = input("Nome do aluno: ").strip()
        while not nome:
            print("Nome não pode ser vazio.")
            nome = input("Nome do aluno: ").strip()
        
        while True:
            tipo_tcc = input("Tipo de TCC (TCC1 ou TCC2): ").strip().upper()
            if tipo_tcc not in ["TCC1", "TCC2"]:
                print("Tipo de TCC inválido. Digite TCC1 ou TCC2.")
                continue
            
            break
        
        aluno = Aluno(ra, nome, tipo_tcc)
        self.gerenciador.alunos[ra] = aluno
        
        print(f"Aluno '{nome}' cadastrado com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _visualizar_alunos(self):
        """
        Visualiza todos os alunos cadastrados.
        """
        if not self.gerenciador.alunos:
            print("Não há alunos cadastrados.")
            return
        
        print("\nLISTA DE ALUNOS")
        print("-" * 60)
        print(f"{'RA':<10} | {'Nome':<30} | {'Tipo de TCC':<10}")
        print("-" * 60)
        
        for aluno in self.gerenciador.alunos.values():
            print(f"{aluno.ra:<10} | {aluno.nome:<30} | {aluno.tipo_tcc:<10}")
    
    def _atualizar_aluno(self):
        """
        Atualiza os dados de um aluno.
        """
        if not self.gerenciador.alunos:
            print("Não há alunos cadastrados.")
            return
        
        self._visualizar_alunos()
        
        ra = input("\nDigite o RA do aluno que deseja atualizar: ").strip()
        
        if ra not in self.gerenciador.alunos:
            print(f"Não existe aluno com o RA '{ra}'.")
            return
        
        aluno = self.gerenciador.alunos[ra]
        
        print(f"\nAtualizando dados do aluno '{aluno.nome}'")
        
        nome = input(f"Nome ({aluno.nome}): ").strip()
        if nome:
            aluno.nome = nome
        
        while True:
            tipo_tcc = input(f"Tipo de TCC ({aluno.tipo_tcc}): ").strip().upper()
            if not tipo_tcc:
                break
                
            if tipo_tcc not in ["TCC1", "TCC2"]:
                print("Tipo de TCC inválido. Digite TCC1 ou TCC2.")
                continue
            
            aluno.tipo_tcc = tipo_tcc
            break
        
        print(f"Dados do aluno '{aluno.nome}' atualizados com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _remover_aluno(self):
        """
        Remove um aluno do sistema.
        """
        if not self.gerenciador.alunos:
            print("Não há alunos cadastrados.")
            return
        
        self._visualizar_alunos()
        
        ra = input("\nDigite o RA do aluno que deseja remover: ").strip()
        
        if ra not in self.gerenciador.alunos:
            print(f"Não existe aluno com o RA '{ra}'.")
            return
        
        aluno = self.gerenciador.alunos[ra]
        
        # Verifica se o aluno está associado a algum TCC
        tccs_associados = [tcc for tcc in self.gerenciador.tccs.values() if tcc.aluno.ra == ra]
        
        if tccs_associados:
            print(f"Não é possível remover o aluno '{aluno.nome}' pois está associado a {len(tccs_associados)} TCC(s).")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover o aluno '{aluno.nome}'? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            del self.gerenciador.alunos[ra]
            print(f"Aluno '{aluno.nome}' removido com sucesso.")
            self.alteracoes_nao_salvas = True
        else:
            print("Operação cancelada.")
    
    # Implementação das funcionalidades de CRUD para Professores
    def _cadastrar_professor(self):
        """
        Cadastra um novo professor no sistema.
        """
        from models.professor import Professor
        
        print("\nCADASTRO DE PROFESSOR")
        
        nome = input("Nome do professor: ").strip()
        while not nome:
            print("Nome não pode ser vazio.")
            nome = input("Nome do professor: ").strip()
        
        if nome in self.gerenciador.professores:
            print(f"Já existe um professor com o nome '{nome}'.")
            return
        
        instituicao = input("Instituição (pressione Enter para UTFPR): ").strip()
        if not instituicao:
            instituicao = "UTFPR"
        
        professor = Professor(nome, instituicao)
        self.gerenciador.professores[nome] = professor
        
        print(f"Professor '{nome}' cadastrado com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _visualizar_professores(self):
        """
        Visualiza todos os professores cadastrados.
        """
        if not self.gerenciador.professores:
            print("Não há professores cadastrados.")
            return
        
        print("\nLISTA DE PROFESSORES")
        print("-" * 50)
        print(f"{'Nome':<30} | {'Instituição':<20}")
        print("-" * 50)
        
        for professor in self.gerenciador.professores.values():
            print(f"{professor.nome:<30} | {professor.instituicao:<20}")
    
    def _atualizar_professor(self):
        """
        Atualiza os dados de um professor.
        """
        if not self.gerenciador.professores:
            print("Não há professores cadastrados.")
            return
        
        self._visualizar_professores()
        
        nome = input("\nDigite o nome do professor que deseja atualizar: ").strip()
        
        if nome not in self.gerenciador.professores:
            print(f"Não existe professor com o nome '{nome}'.")
            return
        
        professor = self.gerenciador.professores[nome]
        
        print(f"\nAtualizando dados do professor '{professor.nome}'")
        
        novo_nome = input(f"Nome ({professor.nome}): ").strip()
        if novo_nome and novo_nome != nome:
            if novo_nome in self.gerenciador.professores:
                print(f"Já existe um professor com o nome '{novo_nome}'.")
                return
            
            # Atualiza a chave no dicionário
            self.gerenciador.professores[novo_nome] = professor
            del self.gerenciador.professores[nome]
            professor.nome = novo_nome
        
        instituicao = input(f"Instituição ({professor.instituicao}): ").strip()
        if instituicao:
            professor.instituicao = instituicao
        
        print(f"Dados do professor '{professor.nome}' atualizados com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _remover_professor(self):
        """
        Remove um professor do sistema.
        """
        if not self.gerenciador.professores:
            print("Não há professores cadastrados.")
            return
        
        self._visualizar_professores()
        
        nome = input("\nDigite o nome do professor que deseja remover: ").strip()
        
        if nome not in self.gerenciador.professores:
            print(f"Não existe professor com o nome '{nome}'.")
            return
        
        professor = self.gerenciador.professores[nome]
        
        # Verifica se o professor está associado a algum TCC como orientador
        tccs_associados = [tcc for tcc in self.gerenciador.tccs.values() if tcc.orientador.nome == nome]
        
        if tccs_associados:
            print(f"Não é possível remover o professor '{professor.nome}' pois está associado como orientador a {len(tccs_associados)} TCC(s).")
            return
        
        # Verifica se o professor está associado a alguma banca
        bancas_associadas = [banca for banca in self.gerenciador.bancas if any(membro.nome == nome for membro in banca.membros)]
        
        if bancas_associadas:
            print(f"Não é possível remover o professor '{professor.nome}' pois está associado a {len(bancas_associadas)} banca(s).")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover o professor '{professor.nome}'? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            del self.gerenciador.professores[nome]
            print(f"Professor '{professor.nome}' removido com sucesso.")
            self.alteracoes_nao_salvas = True
        else:
            print("Operação cancelada.")

    # Implementação das funcionalidades de CRUD para Coorientadores
    def _cadastrar_coorientador(self):
        """
        Cadastra um novo coorientador no sistema.
        """
        from models.coorientador import Coorientador
        
        print("\nCADASTRO DE COORIENTADOR")
        
        nome = input("Nome do coorientador: ").strip()
        while not nome:
            print("Nome não pode ser vazio.")
            nome = input("Nome do coorientador: ").strip()
        
        if nome in self.gerenciador.coorientadores:
            print(f"Já existe um coorientador com o nome '{nome}'.")
            return
        
        instituicao = input("Instituição: ").strip()
        while not instituicao:
            print("Instituição não pode ser vazia.")
            instituicao = input("Instituição: ").strip()
        
        coorientador = Coorientador(nome, instituicao)
        self.gerenciador.coorientadores[nome] = coorientador
        
        print(f"Coorientador '{nome}' cadastrado com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _visualizar_coorientadores(self):
        """
        Visualiza todos os coorientadores cadastrados.
        """
        if not self.gerenciador.coorientadores:
            print("Não há coorientadores cadastrados.")
            return
        
        print("\nLISTA DE COORIENTADORES")
        print("-" * 50)
        print(f"{'Nome':<30} | {'Instituição':<20}")
        print("-" * 50)
        
        for coorientador in self.gerenciador.coorientadores.values():
            print(f"{coorientador.nome:<30} | {coorientador.instituicao:<20}")
    
    def _atualizar_coorientador(self):
        """
        Atualiza os dados de um coorientador.
        """
        if not self.gerenciador.coorientadores:
            print("Não há coorientadores cadastrados.")
            return
        
        self._visualizar_coorientadores()
        
        nome = input("\nDigite o nome do coorientador que deseja atualizar: ").strip()
        
        if nome not in self.gerenciador.coorientadores:
            print(f"Não existe coorientador com o nome '{nome}'.")
            return
        
        coorientador = self.gerenciador.coorientadores[nome]
        
        print(f"\nAtualizando dados do coorientador '{coorientador.nome}'")
        
        novo_nome = input(f"Nome ({coorientador.nome}): ").strip()
        if novo_nome and novo_nome != nome:
            if novo_nome in self.gerenciador.coorientadores:
                print(f"Já existe um coorientador com o nome '{novo_nome}'.")
                return
            
            # Atualiza a chave no dicionário
            self.gerenciador.coorientadores[novo_nome] = coorientador
            del self.gerenciador.coorientadores[nome]
            coorientador.nome = novo_nome
        
        instituicao = input(f"Instituição ({coorientador.instituicao}): ").strip()
        if instituicao:
            coorientador.instituicao = instituicao
        
        print(f"Dados do coorientador '{coorientador.nome}' atualizados com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _remover_coorientador(self):
        """
        Remove um coorientador do sistema.
        """
        if not self.gerenciador.coorientadores:
            print("Não há coorientadores cadastrados.")
            return
        
        self._visualizar_coorientadores()
        
        nome = input("\nDigite o nome do coorientador que deseja remover: ").strip()
        
        if nome not in self.gerenciador.coorientadores:
            print(f"Não existe coorientador com o nome '{nome}'.")
            return
        
        coorientador = self.gerenciador.coorientadores[nome]
        
        # Verifica se o coorientador está associado a algum TCC
        tccs_associados = [tcc for tcc in self.gerenciador.tccs.values() if tcc.coorientador and tcc.coorientador.nome == nome]
        
        if tccs_associados:
            print(f"Não é possível remover o coorientador '{coorientador.nome}' pois está associado a {len(tccs_associados)} TCC(s).")
            return
        
        # Verifica se o coorientador está associado a alguma banca
        bancas_associadas = [banca for banca in self.gerenciador.bancas if any(membro.nome == nome for membro in banca.membros)]
        
        if bancas_associadas:
            print(f"Não é possível remover o coorientador '{coorientador.nome}' pois está associado a {len(bancas_associadas)} banca(s).")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover o coorientador '{coorientador.nome}'? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            del self.gerenciador.coorientadores[nome]
            print(f"Coorientador '{coorientador.nome}' removido com sucesso.")
            self.alteracoes_nao_salvas = True
        else:
            print("Operação cancelada.")
    
    # Implementação das funcionalidades de CRUD para TCCs
    def _cadastrar_tcc(self):
        """
        Cadastra um novo TCC no sistema.
        """
        from models.tcc import TCC
        
        print("\nCADASTRO DE TCC")
        
        if not self.gerenciador.alunos:
            print("Não há alunos cadastrados. Cadastre um aluno primeiro.")
            return
        
        if not self.gerenciador.professores:
            print("Não há professores cadastrados. Cadastre um professor primeiro.")
            return
        
        # Seleciona o tipo de TCC
        while True:
            tipo = input("Tipo de TCC (TCC1 ou TCC2): ").strip().upper()
            if tipo not in ["TCC1", "TCC2"]:
                print("Tipo de TCC inválido. Digite TCC1 ou TCC2.")
                continue
            break
        
        # Seleciona o aluno
        self._visualizar_alunos()
        
        while True:
            ra_aluno = input("\nDigite o RA do aluno: ").strip()
            
            if ra_aluno not in self.gerenciador.alunos:
                print(f"Não existe aluno com o RA '{ra_aluno}'.")
                continue
            
            aluno = self.gerenciador.alunos[ra_aluno]
            
            # Verifica se o aluno já está associado a um TCC
            tccs_aluno = [tcc for tcc in self.gerenciador.tccs.values() if tcc.aluno.ra == ra_aluno]
            
            if tccs_aluno:
                print(f"O aluno '{aluno.nome}' já está associado a um TCC.")
                continue
            
            break
        
        # Seleciona o orientador
        self._visualizar_professores()
        
        while True:
            nome_orientador = input("\nDigite o nome do professor orientador: ").strip()
            
            if nome_orientador not in self.gerenciador.professores:
                print(f"Não existe professor com o nome '{nome_orientador}'.")
                continue
            
            orientador = self.gerenciador.professores[nome_orientador]
            break
        
        # Seleciona o coorientador (opcional)
        tem_coorientador = input("\nO TCC possui coorientador? (S/N): ").strip().upper() == 'S'
        coorientador = None
        
        if tem_coorientador:
            if not self.gerenciador.coorientadores:
                print("Não há coorientadores cadastrados.")
                cadastrar_novo = input("Deseja cadastrar um novo coorientador? (S/N): ").strip().upper() == 'S'
                
                if cadastrar_novo:
                    self._cadastrar_coorientador()
                    
                    if not self.gerenciador.coorientadores:
                        print("Não foi possível cadastrar um coorientador.")
                        tem_coorientador = False
            
            if tem_coorientador and self.gerenciador.coorientadores:
                self._visualizar_coorientadores()
                
                while True:
                    nome_coorientador = input("\nDigite o nome do coorientador: ").strip()
                    
                    if nome_coorientador not in self.gerenciador.coorientadores:
                        print(f"Não existe coorientador com o nome '{nome_coorientador}'.")
                        continue
                    
                    coorientador = self.gerenciador.coorientadores[nome_coorientador]
                    break
        
        # Título do TCC
        titulo = input("\nTítulo do TCC: ").strip()
        while not titulo:
            print("Título não pode ser vazio.")
            titulo = input("Título do TCC: ").strip()
        
        # Verifica se já existe um TCC com o mesmo título para o mesmo aluno
        if (ra_aluno, titulo) in self.gerenciador.tccs:
            print(f"Já existe um TCC com o título '{titulo}' para o aluno '{aluno.nome}'.")
            return
        
        # Cria o TCC
        tcc = TCC(tipo, aluno, orientador, titulo, coorientador)
        self.gerenciador.tccs[(ra_aluno, titulo)] = tcc
        
        print(f"TCC '{titulo}' cadastrado com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _visualizar_tccs(self):
        """
        Visualiza todos os TCCs cadastrados.
        """
        if not self.gerenciador.tccs:
            print("Não há TCCs cadastrados.")
            return
        
        print("\nLISTA DE TCCs")
        print("-" * 100)
        print(f"{'Tipo':<5} | {'Aluno':<30} | {'Orientador':<20} | {'Coorientador':<20} | {'Título':<30}")
        print("-" * 100)
        
        for tcc in self.gerenciador.tccs.values():
            coorientador_nome = tcc.coorientador.nome if tcc.coorientador else "-"
            print(f"{tcc.tipo:<5} | {tcc.aluno.nome:<30} | {tcc.orientador.nome:<20} | {coorientador_nome:<20} | {tcc.titulo:<30}")
    
    def _atualizar_tcc(self):
        """
        Atualiza os dados de um TCC.
        """
        if not self.gerenciador.tccs:
            print("Não há TCCs cadastrados.")
            return
        
        self._visualizar_tccs()
        
        ra_aluno = input("\nDigite o RA do aluno do TCC que deseja atualizar: ").strip()
        
        # Filtra os TCCs pelo RA do aluno
        tccs_aluno = [tcc for tcc in self.gerenciador.tccs.values() if tcc.aluno.ra == ra_aluno]
        
        if not tccs_aluno:
            print(f"Não existe TCC para o aluno com RA '{ra_aluno}'.")
            return
        
        if len(tccs_aluno) == 1:
            tcc = tccs_aluno[0]
        else:
            print("\nTCCs encontrados para o aluno:")
            for i, tcc in enumerate(tccs_aluno):
                print(f"{i+1}. {tcc.titulo}")
            
            while True:
                try:
                    opcao = int(input("\nSelecione o TCC (número): "))
                    if 1 <= opcao <= len(tccs_aluno):
                        tcc = tccs_aluno[opcao-1]
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")
        
        print(f"\nAtualizando dados do TCC '{tcc.titulo}'")
        
        # Atualiza o tipo
        while True:
            tipo = input(f"Tipo ({tcc.tipo}): ").strip().upper()
            if not tipo:
                break
                
            if tipo not in ["TCC1", "TCC2"]:
                print("Tipo de TCC inválido. Digite TCC1 ou TCC2.")
                continue
            
            tcc.tipo = tipo
            break
        
        # Atualiza o orientador
        atualizar_orientador = input(f"Deseja atualizar o orientador (atual: {tcc.orientador.nome})? (S/N): ").strip().upper() == 'S'
        
        if atualizar_orientador:
            self._visualizar_professores()
            
            while True:
                nome_orientador = input("\nDigite o nome do novo orientador: ").strip()
                
                if nome_orientador not in self.gerenciador.professores:
                    print(f"Não existe professor com o nome '{nome_orientador}'.")
                    continue
                
                tcc.orientador = self.gerenciador.professores[nome_orientador]
                break
        
        # Atualiza o coorientador
        atualizar_coorientador = input(f"Deseja atualizar o coorientador (atual: {tcc.coorientador.nome if tcc.coorientador else 'Nenhum'})? (S/N): ").strip().upper() == 'S'
        
        if atualizar_coorientador:
            tem_coorientador = input("O TCC possui coorientador? (S/N): ").strip().upper() == 'S'
            
            if tem_coorientador:
                if not self.gerenciador.coorientadores:
                    print("Não há coorientadores cadastrados.")
                    cadastrar_novo = input("Deseja cadastrar um novo coorientador? (S/N): ").strip().upper() == 'S'
                    
                    if cadastrar_novo:
                        self._cadastrar_coorientador()
                
                if self.gerenciador.coorientadores:
                    self._visualizar_coorientadores()
                    
                    while True:
                        nome_coorientador = input("\nDigite o nome do coorientador: ").strip()
                        
                        if nome_coorientador not in self.gerenciador.coorientadores:
                            print(f"Não existe coorientador com o nome '{nome_coorientador}'.")
                            continue
                        
                        tcc.coorientador = self.gerenciador.coorientadores[nome_coorientador]
                        break
                else:
                    print("Não foi possível atualizar o coorientador.")
            else:
                tcc.coorientador = None
        
        # Atualiza o título
        novo_titulo = input(f"Título ({tcc.titulo}): ").strip()
        if novo_titulo and novo_titulo != tcc.titulo:
            # Verifica se já existe um TCC com o mesmo título para o mesmo aluno
            if (tcc.aluno.ra, novo_titulo) in self.gerenciador.tccs:
                print(f"Já existe um TCC com o título '{novo_titulo}' para o aluno '{tcc.aluno.nome}'.")
            else:
                # Remove a entrada antiga e adiciona a nova
                del self.gerenciador.tccs[(tcc.aluno.ra, tcc.titulo)]
                tcc.titulo = novo_titulo
                self.gerenciador.tccs[(tcc.aluno.ra, tcc.titulo)] = tcc
        
        print(f"Dados do TCC '{tcc.titulo}' atualizados com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _remover_tcc(self):
        """
        Remove um TCC do sistema.
        """
        if not self.gerenciador.tccs:
            print("Não há TCCs cadastrados.")
            return
        
        self._visualizar_tccs()
        
        ra_aluno = input("\nDigite o RA do aluno do TCC que deseja remover: ").strip()
        
        # Filtra os TCCs pelo RA do aluno
        tccs_aluno = [tcc for tcc in self.gerenciador.tccs.values() if tcc.aluno.ra == ra_aluno]
        
        if not tccs_aluno:
            print(f"Não existe TCC para o aluno com RA '{ra_aluno}'.")
            return
        
        if len(tccs_aluno) == 1:
            tcc = tccs_aluno[0]
        else:
            print("\nTCCs encontrados para o aluno:")
            for i, tcc in enumerate(tccs_aluno):
                print(f"{i+1}. {tcc.titulo}")
            
            while True:
                try:
                    opcao = int(input("\nSelecione o TCC (número): "))
                    if 1 <= opcao <= len(tccs_aluno):
                        tcc = tccs_aluno[opcao-1]
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")
        
        # Verifica se o TCC está associado a alguma banca
        bancas_associadas = [banca for banca in self.gerenciador.bancas if banca.tcc.aluno.ra == tcc.aluno.ra and banca.tcc.titulo == tcc.titulo]
        
        if bancas_associadas:
            print(f"Não é possível remover o TCC '{tcc.titulo}' pois está associado a {len(bancas_associadas)} banca(s).")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover o TCC '{tcc.titulo}'? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            del self.gerenciador.tccs[(tcc.aluno.ra, tcc.titulo)]
            print(f"TCC '{tcc.titulo}' removido com sucesso.")
            self.alteracoes_nao_salvas = True
        else:
            print("Operação cancelada.")
    
    # Implementação das funcionalidades de CRUD para Bancas
    def _cadastrar_banca(self):
        """
        Cadastra uma nova banca no sistema.
        """
        from models.banca import Banca
        
        print("\nCADASTRO DE BANCA")
        
        if not self.gerenciador.tccs:
            print("Não há TCCs cadastrados. Cadastre um TCC primeiro.")
            return
        
        if not self.gerenciador.professores and not self.gerenciador.coorientadores:
            print("Não há professores ou coorientadores cadastrados. Cadastre pelo menos um professor ou coorientador primeiro.")
            return
        
        # Seleciona o TCC
        self._visualizar_tccs()
        
        while True:
            ra_aluno = input("\nDigite o RA do aluno do TCC: ").strip()
            
            # Filtra os TCCs pelo RA do aluno
            tccs_aluno = [tcc for tcc in self.gerenciador.tccs.values() if tcc.aluno.ra == ra_aluno]
            
            if not tccs_aluno:
                print(f"Não existe TCC para o aluno com RA '{ra_aluno}'.")
                continue
            
            if len(tccs_aluno) == 1:
                tcc = tccs_aluno[0]
                break
            else:
                print("\nTCCs encontrados para o aluno:")
                for i, tcc in enumerate(tccs_aluno):
                    print(f"{i+1}. {tcc.titulo}")
                
                while True:
                    try:
                        opcao = int(input("\nSelecione o TCC (número): "))
                        if 1 <= opcao <= len(tccs_aluno):
                            tcc = tccs_aluno[opcao-1]
                            break
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Digite um número válido.")
                
                break
        
        # Verifica se o TCC já está associado a uma banca
        bancas_tcc = [banca for banca in self.gerenciador.bancas if banca.tcc.aluno.ra == tcc.aluno.ra and banca.tcc.titulo == tcc.titulo]
        
        if bancas_tcc:
            print(f"O TCC '{tcc.titulo}' já está associado a uma banca.")
            return
        
        # Data da banca
        data = input("\nData da banca (DD/MM/AAAA HH:MM): ").strip()
        while not data:
            print("Data não pode ser vazia.")
            data = input("Data da banca (DD/MM/AAAA HH:MM): ").strip()
        
        # Local ou link
        local_ou_link = input("\nLocal ou link para videoconferência: ").strip()
        while not local_ou_link:
            print("Local ou link não pode ser vazio.")
            local_ou_link = input("Local ou link para videoconferência: ").strip()
        
        # Membros da banca
        print("\nMembros da banca:")
        print("O orientador é automaticamente incluído como membro da banca.")
        
        # Lista de todos os possíveis membros (professores e coorientadores)
        membros_possiveis = list(self.gerenciador.professores.values()) + list(self.gerenciador.coorientadores.values())
        
        # Adiciona o orientador como primeiro membro
        membros = [tcc.orientador]
        
        # Adiciona os outros membros
        for i in range(3):  # 2 membros titulares + 1 suplente
            if i == 0:
                print("\nSelecione o primeiro membro titular:")
            elif i == 1:
                print("\nSelecione o segundo membro titular:")
            else:
                print("\nSelecione o membro suplente:")
            
            # Lista os membros possíveis (excluindo os já selecionados)
            membros_disponiveis = [m for m in membros_possiveis if m not in membros]
            
            if not membros_disponiveis:
                print("Não há mais membros disponíveis para selecionar.")
                break
            
            print("\nMembros disponíveis:")
            for j, membro in enumerate(membros_disponiveis):
                print(f"{j+1}. {membro.nome} ({membro.instituicao})")
            
            while True:
                try:
                    opcao = int(input("\nSelecione o membro (número): "))
                    if 1 <= opcao <= len(membros_disponiveis):
                        membros.append(membros_disponiveis[opcao-1])
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")
        
        # Cria a banca
        banca = Banca(tcc, data, local_ou_link, membros)
        self.gerenciador.bancas.append(banca)
        
        print(f"Banca para o TCC '{tcc.titulo}' cadastrada com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _visualizar_bancas(self):
        """
        Visualiza todas as bancas cadastradas.
        """
        if not self.gerenciador.bancas:
            print("Não há bancas cadastradas.")
            return
        
        print("\nLISTA DE BANCAS")
        print("-" * 100)
        print(f"{'Tipo':<5} | {'Aluno':<20} | {'Título':<30} | {'Data':<20} | {'Local/Link':<30}")
        print("-" * 100)
        
        for banca in self.gerenciador.bancas:
            print(f"{banca.tcc.tipo:<5} | {banca.tcc.aluno.nome:<20} | {banca.tcc.titulo:<30} | {banca.data:<20} | {banca.local_ou_link:<30}")
    
    def _atualizar_banca(self):
        """
        Atualiza os dados de uma banca.
        """
        if not self.gerenciador.bancas:
            print("Não há bancas cadastradas.")
            return
        
        self._visualizar_bancas()
        
        ra_aluno = input("\nDigite o RA do aluno da banca que deseja atualizar: ").strip()
        
        # Filtra as bancas pelo RA do aluno
        bancas_aluno = [banca for banca in self.gerenciador.bancas if banca.tcc.aluno.ra == ra_aluno]
        
        if not bancas_aluno:
            print(f"Não existe banca para o aluno com RA '{ra_aluno}'.")
            return
        
        if len(bancas_aluno) == 1:
            banca = bancas_aluno[0]
        else:
            print("\nBancas encontradas para o aluno:")
            for i, banca in enumerate(bancas_aluno):
                print(f"{i+1}. {banca.tcc.titulo} - {banca.data}")
            
            while True:
                try:
                    opcao = int(input("\nSelecione a banca (número): "))
                    if 1 <= opcao <= len(bancas_aluno):
                        banca = bancas_aluno[opcao-1]
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")
        
        print(f"\nAtualizando dados da banca para o TCC '{banca.tcc.titulo}'")
        
        # Atualiza a data
        data = input(f"Data ({banca.data}): ").strip()
        if data:
            banca.data = data
        
        # Atualiza o local ou link
        local_ou_link = input(f"Local ou link ({banca.local_ou_link}): ").strip()
        if local_ou_link:
            banca.local_ou_link = local_ou_link
        
        # Atualiza os membros
        atualizar_membros = input("Deseja atualizar os membros da banca? (S/N): ").strip().upper() == 'S'
        
        if atualizar_membros:
            print("\nMembros atuais da banca:")
            for i, membro in enumerate(banca.membros):
                if i == 0:
                    print(f"Orientador: {membro.nome} ({membro.instituicao})")
                elif i == len(banca.membros) - 1:
                    print(f"Suplente: {membro.nome} ({membro.instituicao})")
                else:
                    print(f"Membro {i}: {membro.nome} ({membro.instituicao})")
            
            # O orientador não pode ser alterado
            print("\nO orientador não pode ser alterado.")
            
            # Lista de todos os possíveis membros (professores e coorientadores)
            membros_possiveis = list(self.gerenciador.professores.values()) + list(self.gerenciador.coorientadores.values())
            
            # Mantém o orientador como primeiro membro
            novos_membros = [banca.membros[0]]
            
            # Atualiza os outros membros
            for i in range(1, len(banca.membros)):
                if i == 1:
                    print("\nSelecione o primeiro membro titular:")
                elif i == 2:
                    print("\nSelecione o segundo membro titular:")
                else:
                    print("\nSelecione o membro suplente:")
                
                # Lista os membros possíveis (excluindo os já selecionados)
                membros_disponiveis = [m for m in membros_possiveis if m not in novos_membros]
                
                if not membros_disponiveis:
                    print("Não há mais membros disponíveis para selecionar.")
                    break
                
                print("\nMembros disponíveis:")
                for j, membro in enumerate(membros_disponiveis):
                    print(f"{j+1}. {membro.nome} ({membro.instituicao})")
                
                while True:
                    try:
                        opcao = int(input("\nSelecione o membro (número): "))
                        if 1 <= opcao <= len(membros_disponiveis):
                            novos_membros.append(membros_disponiveis[opcao-1])
                            break
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Digite um número válido.")
            
            banca.membros = novos_membros
        
        print(f"Dados da banca para o TCC '{banca.tcc.titulo}' atualizados com sucesso.")
        self.alteracoes_nao_salvas = True
    
    def _remover_banca(self):
        """
        Remove uma banca do sistema.
        """
        if not self.gerenciador.bancas:
            print("Não há bancas cadastradas.")
            return
        
        self._visualizar_bancas()
        
        ra_aluno = input("\nDigite o RA do aluno da banca que deseja remover: ").strip()
        
        # Filtra as bancas pelo RA do aluno
        bancas_aluno = [banca for banca in self.gerenciador.bancas if banca.tcc.aluno.ra == ra_aluno]
        
        if not bancas_aluno:
            print(f"Não existe banca para o aluno com RA '{ra_aluno}'.")
            return
        
        if len(bancas_aluno) == 1:
            banca = bancas_aluno[0]
        else:
            print("\nBancas encontradas para o aluno:")
            for i, banca in enumerate(bancas_aluno):
                print(f"{i+1}. {banca.tcc.titulo} - {banca.data}")
            
            while True:
                try:
                    opcao = int(input("\nSelecione a banca (número): "))
                    if 1 <= opcao <= len(bancas_aluno):
                        banca = bancas_aluno[opcao-1]
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")
        
        confirmacao = input(f"Tem certeza que deseja remover a banca para o TCC '{banca.tcc.titulo}'? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            self.gerenciador.bancas.remove(banca)
            print(f"Banca para o TCC '{banca.tcc.titulo}' removida com sucesso.")
            self.alteracoes_nao_salvas = True
        else:
            print("Operação cancelada.")
    
    # Implementação das funcionalidades de geração de relatórios
    def _gerar_relatorio_tccs(self):
        """
        Gera um relatório em PDF com os dados de todos os TCCs do semestre.
        """
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
        except ImportError:
            print("Instalando dependências para geração de PDF...")
            import subprocess
            subprocess.call([sys.executable, "-m", "pip", "install", "reportlab"])
            
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
        
        if not self.gerenciador.tccs:
            print("Não há TCCs cadastrados.")
            return
        
        nome_arquivo = input("Digite o nome do arquivo PDF (sem extensão): ").strip()
        if not nome_arquivo:
            nome_arquivo = "relatorio_tccs"
        
        nome_arquivo = f"{nome_arquivo}.pdf"
        
        # Cria o documento PDF
        doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
        
        # Estilos
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Titulo', parent=styles['Heading1'], alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Subtitulo', parent=styles['Heading2'], alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Corpo', parent=styles['Normal'], alignment=TA_LEFT))
        
        # Conteúdo do documento
        conteudo = []
        
        # Título
        conteudo.append(Paragraph("Relatório de Trabalhos de Conclusão de Curso", styles['Titulo']))
        conteudo.append(Spacer(1, 20))
        
        # Separa os TCCs por tipo
        tccs_tcc1 = [tcc for tcc in self.gerenciador.tccs.values() if tcc.tipo == "TCC1"]
        tccs_tcc2 = [tcc for tcc in self.gerenciador.tccs.values() if tcc.tipo == "TCC2"]
        
        # Ordena os TCCs pelo nome do aluno
        tccs_tcc1.sort(key=lambda tcc: tcc.aluno.nome)
        tccs_tcc2.sort(key=lambda tcc: tcc.aluno.nome)
        
        # TCC1
        if tccs_tcc1:
            conteudo.append(Paragraph("Trabalhos de TCC1", styles['Subtitulo']))
            conteudo.append(Spacer(1, 10))
            
            # Cria a tabela
            dados_tabela = [["Aluno", "RA", "Orientador", "Coorientador", "Título"]]
            
            for tcc in tccs_tcc1:
                coorientador = tcc.coorientador.nome if tcc.coorientador else "-"
                dados_tabela.append([tcc.aluno.nome, tcc.aluno.ra, tcc.orientador.nome, coorientador, tcc.titulo])
            
            tabela = Table(dados_tabela, colWidths=[100, 50, 100, 100, 150])
            tabela.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
            ]))
            
            conteudo.append(tabela)
            conteudo.append(Spacer(1, 20))
        
        # TCC2
        if tccs_tcc2:
            conteudo.append(Paragraph("Trabalhos de TCC2", styles['Subtitulo']))
            conteudo.append(Spacer(1, 10))
            
            # Cria a tabela
            dados_tabela = [["Aluno", "RA", "Orientador", "Coorientador", "Título"]]
            
            for tcc in tccs_tcc2:
                coorientador = tcc.coorientador.nome if tcc.coorientador else "-"
                dados_tabela.append([tcc.aluno.nome, tcc.aluno.ra, tcc.orientador.nome, coorientador, tcc.titulo])
            
            tabela = Table(dados_tabela, colWidths=[100, 50, 100, 100, 150])
            tabela.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
            ]))
            
            conteudo.append(tabela)
        
        # Gera o PDF
        doc.build(conteudo)
        
        print(f"Relatório de TCCs gerado com sucesso: {nome_arquivo}")
    
    def _gerar_relatorio_bancas(self):
        """
        Gera um relatório em PDF com os dados de todas as bancas do semestre.
        """
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
        except ImportError:
            print("Instalando dependências para geração de PDF...")
            import subprocess
            subprocess.call([sys.executable, "-m", "pip", "install", "reportlab"])
            
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
        
        if not self.gerenciador.bancas:
            print("Não há bancas cadastradas.")
            return
        
        nome_arquivo = input("Digite o nome do arquivo PDF (sem extensão): ").strip()
        if not nome_arquivo:
            nome_arquivo = "relatorio_bancas"
        
        nome_arquivo = f"{nome_arquivo}.pdf"
        
        # Cria o documento PDF
        doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
        
        # Estilos
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Titulo', parent=styles['Heading1'], alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Subtitulo', parent=styles['Heading2'], alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Corpo', parent=styles['Normal'], alignment=TA_LEFT))
        
        # Conteúdo do documento
        conteudo = []
        
        # Título
        conteudo.append(Paragraph("Relatório de Bancas de TCC", styles['Titulo']))
        conteudo.append(Spacer(1, 20))
        
        # Separa as bancas por tipo de TCC
        bancas_tcc1 = [banca for banca in self.gerenciador.bancas if banca.tcc.tipo == "TCC1"]
        bancas_tcc2 = [banca for banca in self.gerenciador.bancas if banca.tcc.tipo == "TCC2"]
        
        # Ordena as bancas por data
        bancas_tcc1.sort(key=lambda banca: banca.data)
        bancas_tcc2.sort(key=lambda banca: banca.data)
        
        # Bancas de TCC1
        if bancas_tcc1:
            conteudo.append(Paragraph("Bancas de TCC1", styles['Subtitulo']))
            conteudo.append(Spacer(1, 10))
            
            for banca in bancas_tcc1:
                # Informações da banca
                conteudo.append(Paragraph(f"<b>Título:</b> {banca.tcc.titulo}", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Aluno:</b> {banca.tcc.aluno.nome} (RA: {banca.tcc.aluno.ra})", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Data:</b> {banca.data}", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Local/Link:</b> {banca.local_ou_link}", styles['Corpo']))
                
                # Membros da banca
                conteudo.append(Paragraph("<b>Membros da Banca:</b>", styles['Corpo']))
                for i, membro in enumerate(banca.membros):
                    if i == 0:
                        conteudo.append(Paragraph(f"- Orientador: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                    elif i == len(banca.membros) - 1:
                        conteudo.append(Paragraph(f"- Suplente: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                    else:
                        conteudo.append(Paragraph(f"- Membro: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                
                conteudo.append(Spacer(1, 10))
            
            conteudo.append(Spacer(1, 10))
        
        # Bancas de TCC2
        if bancas_tcc2:
            conteudo.append(Paragraph("Bancas de TCC2", styles['Subtitulo']))
            conteudo.append(Spacer(1, 10))
            
            for banca in bancas_tcc2:
                # Informações da banca
                conteudo.append(Paragraph(f"<b>Título:</b> {banca.tcc.titulo}", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Aluno:</b> {banca.tcc.aluno.nome} (RA: {banca.tcc.aluno.ra})", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Data:</b> {banca.data}", styles['Corpo']))
                conteudo.append(Paragraph(f"<b>Local/Link:</b> {banca.local_ou_link}", styles['Corpo']))
                
                # Membros da banca
                conteudo.append(Paragraph("<b>Membros da Banca:</b>", styles['Corpo']))
                for i, membro in enumerate(banca.membros):
                    if i == 0:
                        conteudo.append(Paragraph(f"- Orientador: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                    elif i == len(banca.membros) - 1:
                        conteudo.append(Paragraph(f"- Suplente: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                    else:
                        conteudo.append(Paragraph(f"- Membro: {membro.nome} ({membro.instituicao})", styles['Corpo']))
                
                conteudo.append(Spacer(1, 10))
        
        # Gera o PDF
        doc.build(conteudo)
        
        print(f"Relatório de bancas gerado com sucesso: {nome_arquivo}")
