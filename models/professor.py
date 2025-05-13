class Professor:
    """
    Classe que representa um professor orientador de TCC.
    """
    def __init__(self, nome, instituicao="UTFPR"):
        """
        Inicializa um objeto Professor.
        
        Args:
            nome (str): Nome completo do professor
            instituicao (str, optional): Instituição do professor. Padrão é "UTFPR"
        """
        self.nome = nome
        self.instituicao = instituicao
    
    def __str__(self):
        """
        Retorna uma representação em string do professor.
        
        Returns:
            str: Representação em string do professor
        """
        return f"Professor: {self.nome} ({self.instituicao})"
    
    def to_csv(self):
        """
        Converte o objeto para uma linha CSV.
        
        Returns:
            list: Lista com os atributos do professor para salvar em CSV
        """
        return ["PROFESSOR", self.nome, self.instituicao]
    
    @classmethod
    def from_csv(cls, dados):
        """
        Cria um objeto Professor a partir de dados CSV.
        
        Args:
            dados (list): Lista com os dados do professor [tipo, nome, instituicao]
            
        Returns:
            Professor: Objeto Professor criado a partir dos dados
        """
        return cls(dados[1], dados[2])
