# bot_lowest_price
### O "bot_lowest_price" é um projeto desenvolvido em Python com a biblioteca Selenium. Ele recebe o nome de um produto, pesquisa nos sites Kabum, Amazon e Pichau, filtra pelo menor preço e retorna um print do produto encontrado e um objeto com o link do produto.

# Pré-requisitos
### Python 3 instalado
### Pip (gerenciador de pacotes do Python) instalado

# Passo a passo

### 1 - Clone o repositório em sua máquina local: git clone https://github.com/seu-usuario/seu-repositorio.git

### 2 - Navegue até o diretório do projeto: cd seu-repositorio

### 3 - Crie um ambiente virtual para o projeto: python -m venv venv

### 4 - Ative o ambiente virtual: 

### No Windows: .\venv\Scripts\activate

### No Linux ou MacOS: source venv/bin/activate

### 5 - Instale as dependências do projeto: pip install -r requirements.txt

### 6 - Defina o nome do produto que deseja buscar:

### Abra o arquivo app.py;

### Na linha: application = LowestPrice("Kingston"), substitua exemplo_produto pelo nome do produto que deseja buscar.

### 7 - Execute o bot no terminal: python app.py

### OBS: O bot irá buscar o produto especificado nos sites de compras cadastrados e retornará o preço mais baixo encontrado. Caso ocorra algum erro durante a execução, será exibida uma mensagem de erro no terminal.
