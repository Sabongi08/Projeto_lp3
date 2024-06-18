from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask("Minha aplicação")


#  rota + função 

# / -home page 
# @app.route("/")
# def home ():
#    return "<h1>Home Page </h1>"

# / -contato  page 
@app.route("/contato")
def contato ():
    return render_template ("contato.html")

@app.route("/produtos")
def produtos ():
    lista_produtos = [
        {"nome": "coca-cola", "descricao": "Mata a sede "},
        {"nome": "doritos", "descricao":"seja a tua mao "},
        {"nome": "chocolate", "descricao":"bonzao "},
    ]
    
    return render_template ("produtos.html", produtos =lista_produtos)


@app.route("/home")
def home ():
    return render_template ("home.html")

# /contato - pg de contato 
# @app.route("/contato")
# def contato():
#     return "<h1>Contato</h1>"

# /produtos - pg produtos 
# @app.route("/produtos")
# def produtos ():
#     return "<h1>Produtos</h1>"

# pagina /servicos retornar "Nossos serviços"
@app.route("/servicos")
def servicos ():
    return "<h1>Nossos serviços</h1>"

# pagina /gerar-cpf retornar Cpf aleatorio
@app.route("/cpf")
def cpf ():
        cpf = CPF()
        return f"<h1> CPF: (cpf.generate (True))</h1>"

# pagina /gerar-cpf retornar Cnpj aleatorio 
@app.route("/cnpj")
def cnpj ():
     return f"<h1> CNPJ: (cpf.generate (True))</h1>"
app.run()




