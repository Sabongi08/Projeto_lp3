from flask import Flask, render_template, request
from validate_docbr import CNPJ, CPF 

lista_produtos = [ # cada produto é um dicionário
        { "nome": "Coca-cola", "descricao" : "mata a sede","imagem": "https://choppmaisfacil.com.br/image/cache/catalog/produtos/Refrigerantes/1648036735_1SZ-1000x1000.jpg"}, 
        { "nome": "Doritos", "descricao" : "Suja a mão", "imagem": "https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
        {  "nome": "Chocolate", "descricao" : "bom","imagem": "https://cdn.awsli.com.br/800x800/1957/1957771/produto/10935798577112288ec.jpg" }
    ]

app = Flask("Minha App")

# rota + função

# Definição de rota
# / - home page  

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/contato")
def Contato():
    return render_template("contato.html")

# /produtos - pagina produtos 

@app.route("/produtos")
def produtos():
    lista_produtos = [ 
        { "nome": "Coca-cola", "descricao" : "mata a sede","imagem": "https://choppmaisfacil.com.br/image/cache/catalog/produtos/Refrigerantes/1648036735_1SZ-1000x1000.jpg"}, 
        { "nome": "Doritos", "descricao" : "Suja a mão", "imagem": "https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
        {  "nome": "Chocolate", "descricao" : "bom","imagem": "https://cdn.awsli.com.br/800x800/1957/1957771/produto/10935798577112288ec.jpg" }
    ]

    return render_template("produtos.html", produtos=lista_produtos) 

# criar uma página /servicos retornar "nossos serviços" (colar oq ja tem)
# página /gerar-cpf retornar cpf aleatório (usar a biblioteca do cpf que instalamos)
# página /gerar cnpj e retornar Cnpj aleatório (usar a mesma biblioteca de cima) 

@app.route("/servicos")
def servicos():
    return "<h1> Nossos serviços <h1>"

@app.route("/termos-de-uso")
def termos():
    return render_template("termos.html")

@app.route("/politicas-de-privacidade")
def politica():
    return render_template("politicas.html")


@app.route("/como-utilizar")
def utilizar():
    return render_template("utilizar.html")

@app.route("/cpf")
def gerarCpf():
    cpf = CPF() 
    return cpf.generate(True)

@app.route("/cnpj")
def gerarCnpj():
    cnpj = CNPJ() 
    return cnpj.generate(True)

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form["nome"] 
    descricao = request.form["descricao"]

    produto = {"nome": nome, "descricao": descricao,"imagem":""}

    lista_produtos.append(produto)

    return render_template("produtos.html", produtos=lista_produtos)
    
app.run()




