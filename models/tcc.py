class TCC:
    """
    Classe que representa um Trabalho de Conclusão de Curso.
    """
    def __init__(self, tipo, aluno, orientador, titulo, coorientador=None):
        """
        Inicializa um objeto TCC.
        
        Args:
            tipo (str): Tipo do TCC (TCC1 ou TCC2)
            aluno (Aluno): Objeto Aluno responsável pelo TCC
            orientador (Professor): Objeto Professor orientador do TCC
            titulo (str): Título do trabalho
            coorientador (Coorientador, optional): Objeto Coorientador, se houver
        """
        self.tipo = tipo
        self.aluno = aluno
        self.orientador = orientador
        self.titulo = titulo
        self.coorientador = coorientador
    
    def __str__(self):
        """
        Retorna uma representação em string do TCC.
        
        Returns:
            str: Representação em string do TCC
        """
        coorientador_info = f", Coorientador: {self.coorientador.nome}" if self.coorientador else ""
        return f"{self.tipo} - {self.titulo}\nAluno: {self.aluno.nome} (RA: {self.aluno.ra})\nOrientador: {self.orientador.nome}{coorientador_info}"
    
    def to_csv(self):
        """
        Converte o objeto para uma linha CSV.
        
        Returns:
            list: Lista com os atributos do TCC para salvar em CSV
        """
        coorientador_id = self.coorientador.nome if self.coorientador else ""
        return ["TCC", self.tipo, self.aluno.ra, self.orientador.nome, coorientador_id, self.titulo]
    
    @classmethod
    def from_csv(cls, dados, alunos, professores, coorientadores):
        """
        Cria um objeto TCC a partir de dados CSV.
        
        Args:
            dados (list): Lista com os dados do TCC [tipo_registro, tipo_tcc, ra_aluno, nome_orientador, nome_coorientador, titulo]
            alunos (dict): Dicionário de alunos indexado por RA
            professores (dict): Dicionário de professores indexado por nome
            coorientadores (dict): Dicionário de coorientadores indexado por nome
            
        Returns:
            TCC: Objeto TCC criado a partir dos dados
        """
        tipo = dados[1]
        aluno = alunos.get(dados[2])
        orientador = professores.get(dados[3])
        coorientador = coorientadores.get(dados[4]) if dados[4] else None
        titulo = dados[5]
        
        return cls(tipo, aluno, orientador, titulo, coorientador)
