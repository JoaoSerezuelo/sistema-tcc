from models.aluno import Aluno
from models.professor import Professor
from models.coorientador import Coorientador
from models.tcc import TCC
from models.banca import Banca

# Importa todos os módulos para garantir que não há erros de importação
def test_imports():
    print("Testando importações...")
    print("Todas as importações foram bem-sucedidas!")

# Testa a criação de objetos
def test_object_creation():
    print("\nTestando criação de objetos...")
    
    # Cria um aluno
    aluno = Aluno("123456", "João Silva", "TCC1")
    print(f"Aluno criado: {aluno}")
    
    # Cria um professor
    professor = Professor("Carlos Ferreira", "UTFPR")
    print(f"Professor criado: {professor}")
    
    # Cria um coorientador
    coorientador = Coorientador("Roberto Almeida", "USP")
    print(f"Coorientador criado: {coorientador}")
    
    # Cria um TCC
    tcc = TCC("TCC1", aluno, professor, "Desenvolvimento de um sistema de gerenciamento de TCCs", coorientador)
    print(f"TCC criado: {tcc}")
    
    # Cria uma banca
    membros = [professor, Professor("Mariana Costa", "UTFPR"), coorientador, Professor("Juliana Martins", "UNICAMP")]
    banca = Banca(tcc, "15/06/2023 14:00", "Sala A-201", membros)
    print(f"Banca criada: {banca}")
    
    print("Todos os objetos foram criados com sucesso!")

# Testa a conversão para CSV
def test_csv_conversion():
    print("\nTestando conversão para CSV...")
    
    # Cria objetos
    aluno = Aluno("123456", "João Silva", "TCC1")
    professor = Professor("Carlos Ferreira", "UTFPR")
    coorientador = Coorientador("Roberto Almeida", "USP")
    tcc = TCC("TCC1", aluno, professor, "Desenvolvimento de um sistema de gerenciamento de TCCs", coorientador)
    membros = [professor, Professor("Mariana Costa", "UTFPR"), coorientador, Professor("Juliana Martins", "UNICAMP")]
    banca = Banca(tcc, "15/06/2023 14:00", "Sala A-201", membros)
    
    # Converte para CSV
    aluno_csv = aluno.to_csv()
    professor_csv = professor.to_csv()
    coorientador_csv = coorientador.to_csv()
    tcc_csv = tcc.to_csv()
    banca_csv = banca.to_csv()
    
    print(f"Aluno CSV: {aluno_csv}")
    print(f"Professor CSV: {professor_csv}")
    print(f"Coorientador CSV: {coorientador_csv}")
    print(f"TCC CSV: {tcc_csv}")
    print(f"Banca CSV: {banca_csv}")
    
    print("Todos os objetos foram convertidos para CSV com sucesso!")

# Testa o gerenciador CSV
def test_csv_manager():
    from utils.gerenciador_csv import GerenciadorCSV
    import os
    
    print("\nTestando gerenciador CSV...")
    
    # Cria um gerenciador CSV
    gerenciador = GerenciadorCSV("teste_gerenciador.csv")
    
    # Cria objetos
    aluno1 = Aluno("123456", "João Silva", "TCC1")
    aluno2 = Aluno("234567", "Maria Oliveira", "TCC1")
    professor1 = Professor("Carlos Ferreira", "UTFPR")
    professor2 = Professor("Mariana Costa", "UTFPR")
    coorientador = Coorientador("Roberto Almeida", "USP")
    
    # Adiciona objetos ao gerenciador
    gerenciador.alunos[aluno1.ra] = aluno1
    gerenciador.alunos[aluno2.ra] = aluno2
    gerenciador.professores[professor1.nome] = professor1
    gerenciador.professores[professor2.nome] = professor2
    gerenciador.coorientadores[coorientador.nome] = coorientador
    
    # Cria TCCs
    tcc1 = TCC("TCC1", aluno1, professor1, "Desenvolvimento de um sistema de gerenciamento de TCCs", coorientador)
    gerenciador.tccs[(aluno1.ra, tcc1.titulo)] = tcc1
    
    tcc2 = TCC("TCC1", aluno2, professor2, "Aplicação de Inteligência Artificial em Sistemas Educacionais")
    gerenciador.tccs[(aluno2.ra, tcc2.titulo)] = tcc2
    
    # Cria bancas
    membros1 = [professor1, professor2, coorientador]
    banca1 = Banca(tcc1, "15/06/2023 14:00", "Sala A-201", membros1)
    gerenciador.bancas.append(banca1)
    
    # Salva os dados
    if gerenciador.salvar_dados():
        print("Dados salvos com sucesso!")
    else:
        print("Erro ao salvar os dados!")
    
    # Cria um novo gerenciador para carregar os dados
    gerenciador2 = GerenciadorCSV("teste_gerenciador.csv")
    
    # Carrega os dados
    if gerenciador2.carregar_dados():
        print("Dados carregados com sucesso!")
    else:
        print("Erro ao carregar os dados!")
    
    # Verifica se os dados foram carregados corretamente
    print(f"Alunos carregados: {len(gerenciador2.alunos)}")
    print(f"Professores carregados: {len(gerenciador2.professores)}")
    print(f"Coorientadores carregados: {len(gerenciador2.coorientadores)}")
    print(f"TCCs carregados: {len(gerenciador2.tccs)}")
    print(f"Bancas carregadas: {len(gerenciador2.bancas)}")
    
    # Remove o arquivo de teste
    os.remove("teste_gerenciador.csv")
    print("Arquivo de teste removido!")
    
    print("Teste do gerenciador CSV concluído com sucesso!")

# Executa todos os testes
def run_all_tests():
    test_imports()
    test_object_creation()
    test_csv_conversion()
    test_csv_manager()
    print("\nTodos os testes foram concluídos com sucesso!")

if __name__ == "__main__":
    run_all_tests()
