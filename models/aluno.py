class Aluno:
    """
    Classe que representa um aluno de TCC.
    """
    def __init__(self, ra, nome, tipo_tcc):
        """
        Inicializa um objeto Aluno.
        
        Args:
            ra (str): Registro Acadêmico do aluno
            nome (str): Nome completo do aluno
            tipo_tcc (str): Tipo de TCC (TCC1 ou TCC2)
        """
        self.ra = ra
        self.nome = nome
        self.tipo_tcc = tipo_tcc
    
    def __str__(self):
        """
        Retorna uma representação em string do aluno.
        
        Returns:
            str: Representação em string do aluno
        """
        return f"Aluno: {self.nome} (RA: {self.ra}) - {self.tipo_tcc}"
    
    def to_csv(self):
        """
        Converte o objeto para uma linha CSV.
        
        Returns:
            list: Lista com os atributos do aluno para salvar em CSV
        """
        return ["ALUNO", self.ra, self.nome, self.tipo_tcc]
    
    @classmethod
    def from_csv(cls, dados):
        """
        Cria um objeto Aluno a partir de dados CSV.
        
        Args:
            dados (list): Lista com os dados do aluno [tipo, ra, nome, tipo_tcc]
            
        Returns:
            Aluno: Objeto Aluno criado a partir dos dados
        """
        return cls(dados[1], dados[2], dados[3])
