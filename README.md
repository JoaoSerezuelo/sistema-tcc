# Sistema de Gerenciamento de TCCs

Este sistema foi desenvolvido para auxiliar o Professor Responsável pelas Atividades de TCC (PRATCC) no controle da execução e das entregas dos Trabalhos de Conclusão de Curso.

## Descrição

O sistema permite o gerenciamento completo de TCCs, incluindo:

- Cadastro de alunos de TCC1 e TCC2
- Cadastro de professores orientadores
- Cadastro de coorientadores (internos ou externos)
- Cadastro de trabalhos de TCC
- Cadastro de bancas de defesa
- Visualização de listas de TCCs e bancas
- Geração de relatórios em PDF

## Estrutura do Projeto

```
sistema_tcc/
├── models/              # Classes de modelo
│   ├── aluno.py         # Classe Aluno
│   ├── professor.py     # Classe Professor
│   ├── coorientador.py  # Classe Coorientador
│   ├── tcc.py           # Classe TCC
│   └── banca.py         # Classe Banca
├── views/               # Interfaces de usuário
│   └── interface_usuario.py  # Interface de linha de comando
├── utils/               # Utilitários
│   └── gerenciador_csv.py    # Gerenciador de dados em CSV
├── main.py              # Arquivo principal
└── tests.py             # Testes do sistema
```

## Requisitos

- Python 3.6 ou superior
- Biblioteca ReportLab (instalada automaticamente pelo sistema quando necessário)

## Como Executar

1. Clone o repositório ou extraia os arquivos para uma pasta
2. Navegue até a pasta do projeto
3. Execute o arquivo principal:

```bash
python main.py [nome_arquivo.csv]
ou
python main.py
```

Onde `[nome_arquivo.csv]` é opcional. Se não for fornecido, o sistema perguntará o nome do arquivo ao iniciar. (OBS.: arquivo para teste dados_teste.csv)

## Funcionalidades

### Gerenciamento de Alunos

- Cadastrar alunos com RA, nome e tipo de TCC (TCC1 ou TCC2)
- Visualizar lista de alunos
- Atualizar dados de alunos
- Remover alunos (se não estiverem associados a TCCs)

### Gerenciamento de Professores

- Cadastrar professores com nome e instituição
- Visualizar lista de professores
- Atualizar dados de professores
- Remover professores (se não estiverem associados a TCCs ou bancas)

### Gerenciamento de Coorientadores

- Cadastrar coorientadores com nome e instituição
- Visualizar lista de coorientadores
- Atualizar dados de coorientadores
- Remover coorientadores (se não estiverem associados a TCCs ou bancas)

### Gerenciamento de TCCs

- Cadastrar TCCs com tipo, aluno, orientador, coorientador (opcional) e título
- Visualizar lista de TCCs
- Atualizar dados de TCCs
- Remover TCCs (se não estiverem associados a bancas)

### Gerenciamento de Bancas

- Cadastrar bancas com TCC, data, local/link e membros
- Visualizar lista de bancas
- Atualizar dados de bancas
- Remover bancas

### Geração de Relatórios

- Gerar relatório de TCCs em PDF, separados por TCC1 e TCC2, ordenados por nome do aluno
- Gerar relatório de bancas em PDF, separadas por TCC1 e TCC2, ordenadas por data

## Armazenamento de Dados

Os dados são armazenados em um arquivo CSV com o seguinte formato:

- Alunos: `ALUNO,ra,nome,tipo_tcc`
- Professores: `PROFESSOR,nome,instituicao`
- Coorientadores: `COORIENTADOR,nome,instituicao`
- TCCs: `TCC,tipo,ra_aluno,nome_orientador,nome_coorientador,titulo`
- Bancas: `BANCA,ra_aluno,titulo_tcc,data,local_ou_link,orientador,membro1,membro2,suplente`

## Arquivo de Teste

O sistema inclui um arquivo CSV de teste (`dados_teste.csv`) com dados de exemplo para facilitar os testes. Para utilizá-lo, basta informar o caminho para este arquivo ao iniciar o sistema.

## Tratamento de Erros

O sistema foi desenvolvido para tratar erros de entrada do usuário, exibindo mensagens de erro apropriadas e solicitando novamente os dados quando necessário. Além disso, o sistema verifica dependências entre entidades antes de permitir a remoção de registros.

## Salvamento de Dados

O sistema permite salvar os dados a qualquer momento através da opção no menu principal. Além disso, ao encerrar o sistema, ele pergunta se o usuário deseja salvar as alterações não salvas.

## Autor

Este sistema foi desenvolvido como um projeto de exemplo para demonstrar o uso de orientação a objetos em Python.
