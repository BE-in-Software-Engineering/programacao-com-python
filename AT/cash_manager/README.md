# Cash Manager

Sistema de **gerenciamento de caixa** para supermercados, desenvolvido em Python. Este projeto permite o registro de compras, a atualização do estoque, a geração de notas fiscais por cliente, e o fechamento de caixa com relatórios detalhados.

## Estrutura de Pastas

AT/cash_manager/
│  
├── answers/ # Respostas das etapas 15 e 16 do AT  
│ └── README.md # Respostas às perguntas do projeto  
│  
├── data/ # Arquivos de dados  
│ └── products.csv # Arquivo CSV com o estoque de produtos  
│  
├── modules/ # Módulos de funcionalidades  
│ ├── common.py # Funções gerais (formatação, mensagens de erro)  
│ ├── constants.py # Índices e constantes  
│ ├── products.py # Manipulação do estoque de produtos  
│ ├── service.py # Lógica principal do gerenciamento de vendas  
│ ├── utils.py # Relatórios  
│  
├── .gitignore # Arquivos ignorados pelo Git  
├── main.py # Arquivo principal do sistema  
├── README.md # Documentação do projeto  
└── requirements.txt # Dependências do projeto

## Funcionalidades

- Registro de compras e atualização do estoque.
- Geração de nota fiscal por compra do cliente.
- Fechamento de caixa com relatórios de vendas e produtos esgotados.
- Exibição de relatórios formatados utilizando a biblioteca `tabulate`.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/BE-in-Software-Engineering/programacao-com-python.git

   ```

2. Instale a dependência:

   ```bash
   pip install tabulate
   ```

3. Execute o sistema:

   ```bash
   python main.py
   ```
