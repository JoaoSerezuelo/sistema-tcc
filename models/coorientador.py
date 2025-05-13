class Coorientador:
    """
    Classe que representa um coorientador de TCC.
    """
    def __init__(self, nome, instituicao):
        """
        Inicializa um objeto Coorientador.
        
        Args:
            nome (str): Nome completo do coorientador
            instituicao (str): Instituição do coorientador
        """
        self.nome = nome
        self.instituicao = instituicao
    
    def __str__(self):
        """
        Retorna uma representação em string do coorientador.
        
        Returns:
            str: Representação em string do coorientador
        """
        return f"Coorientador: {self.nome} ({self.instituicao})"
    
    def to_csv(self):
        """
        Converte o objeto para uma linha CSV.
        
        Returns:
            list: Lista com os atributos do coorientador para salvar em CSV
        """
        return ["COORIENTADOR", self.nome, self.instituicao]
    
    @classmethod
    def from_csv(cls, dados):
        """
        Cria um objeto Coorientador a partir de dados CSV.
        
        Args:
            dados (list): Lista com os dados do coorientador [tipo, nome, instituicao]
            
        Returns:
            Coorientador: Objeto Coorientador criado a partir dos dados
        """
        return cls(dados[1], dados[2])
