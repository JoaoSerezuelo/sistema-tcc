class Banca:
    """
    Classe que representa uma banca de defesa de TCC.
    """
    def __init__(self, tcc, data, local_ou_link, membros):
        """
        Inicializa um objeto Banca.
        
        Args:
            tcc (TCC): Objeto TCC associado à banca
            data (str): Data e hora da defesa (formato: DD/MM/AAAA HH:MM)
            local_ou_link (str): Local físico ou link para videoconferência
            membros (list): Lista de objetos Professor/Coorientador que compõem a banca
                           [orientador, membro1, membro2, suplente]
        """
        self.tcc = tcc
        self.data = data
        self.local_ou_link = local_ou_link
        self.membros = membros  # [orientador, membro1, membro2, suplente]
    
    def __str__(self):
        """
        Retorna uma representação em string da banca.
        
        Returns:
            str: Representação em string da banca
        """
        membros_str = "\n".join([f"- {membro.nome} ({membro.instituicao})" for membro in self.membros])
        return (f"Banca de {self.tcc.tipo} - {self.tcc.titulo}\n"
                f"Aluno: {self.tcc.aluno.nome} (RA: {self.tcc.aluno.ra})\n"
                f"Data: {self.data}\n"
                f"Local/Link: {self.local_ou_link}\n"
                f"Membros da banca:\n{membros_str}")
    
    def to_csv(self):
        """
        Converte o objeto para uma linha CSV.
        
        Returns:
            list: Lista com os atributos da banca para salvar em CSV
        """
        # Identificamos o TCC pelo RA do aluno e título
        membros_nomes = [membro.nome for membro in self.membros]
        return ["BANCA", self.tcc.aluno.ra, self.tcc.titulo, self.data, 
                self.local_ou_link, *membros_nomes]
    
    @classmethod
    def from_csv(cls, dados, tccs, professores, coorientadores):
        """
        Cria um objeto Banca a partir de dados CSV.
        
        Args:
            dados (list): Lista com os dados da banca 
                         [tipo_registro, ra_aluno, titulo_tcc, data, local_ou_link, orientador, membro1, membro2, suplente]
            tccs (dict): Dicionário de TCCs indexado por (ra_aluno, titulo)
            professores (dict): Dicionário de professores indexado por nome
            coorientadores (dict): Dicionário de coorientadores indexado por nome
            
        Returns:
            Banca: Objeto Banca criado a partir dos dados
        """
        ra_aluno = dados[1]
        titulo_tcc = dados[2]
        tcc = tccs.get((ra_aluno, titulo_tcc))
        data = dados[3]
        local_ou_link = dados[4]
        
        # Recupera os membros da banca (podem ser professores ou coorientadores)
        membros = []
        for i in range(5, len(dados)):
            membro_nome = dados[i]
            if not membro_nome:
                continue
                
            membro = professores.get(membro_nome)
            if not membro:
                membro = coorientadores.get(membro_nome)
            
            if membro:
                membros.append(membro)
        
        return cls(tcc, data, local_ou_link, membros)
