from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Biblioteca</title>
            <style>
                body { background-color: white; margin: 20px; padding: 5px; font-family: Arial; }
                .Main { margin: 0 auto; padding: 10px; text-align: center; font-weight: bold; }
                #titulo { color: green; font-size: 40px; font-family: Helvetica; }
                p { font-size: 30px; }
                nav { text-align: right; margin-bottom: 20px; }
                nav a { padding: 5px; margin-right: 2px; }
            </style>
        </head>
        <body>
            <nav>
                <a href="/">Inicio</a>
                <a href="/livros">Livros</a>
                <a href="/carrinho">Carrinho</a>
                <a href="/sobre">Sobre</a>
            </nav>
            
            <div class="Main">
                <h1 id="titulo">Biblioteca Virtual</h1>
                <p>Explore a nossa coleção de livros</p>
            </div>
        </body>
    </html>
    '''

@app.route("/livros")
def livros():
    livros = [
        {"id": 1, "titulo": "1984", "ano": 1949, "autor": "George Orwell"},
        {"id": 2, "titulo": "O Senhor dos Anéis", "ano": 1954, "autor": "JRR Tolkien"},
        {"id": 3, "titulo": "Dom Casmurro", "ano": 1899, "autor": "Machado de Assis"},
        {"id": 4, "titulo": "O Príncipe", "ano": 1532, "autor": "Nicolau Maquíavel"},
        ]
        
    livros_html = "<h2>Lista de Livros</h2> <hr> <ul>"
    
    for livro in livros:
        livros_html += f'''
        <li>
            <strong>{livro['titulo']}</strong> - {livro['autor']} ({livro['ano']})
        </li>
        '''
    
    livros_html += "</ul>"
        
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Lista de Livros</title>
            <style>
                body {{ background-color: white; margin: 20px; padding: 5px; font-family: Arial; }}
                .Main {{ padding: 10px 0px 10px 0px}}
                nav {{ text-align: right; margin-bottom: 20px; }}
                nav a {{ padding: 5px; margin-right: 2px; }}
                ul {{ font-size: 25px; }}
                h2{{ text-align: center; font-weight: bold; font-size: 35px; font-family: Helvetica; }}
        </style>
        </head>
        <body>
            <nav>
                <a href="/">Inicio</a>
                <a href="/livros">Livros</a>
                <a href="/carrinho">Carrinho</a>
                <a href="/sobre">Sobre</a>
            </nav>
                
            <div class="Main">            
                {livros_html}
            </div>
        </body>
    </html>
    '''
    
@app.route("/carrinho")
def carrinho():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Carrinho</title>
            <style>
                body { background-color: white; font-family: Arial; margin: 20px; padding: 5px; }
                .Main { margin: 0 auto; padding: 10px; font-weight: bold; font-size: 30px; text-align: center; }
                button { background-color: green; color: black; padding: 15px 24px; border-radius: 4px; }
                nav { text-align: right; margin-bottom: 20px; }
                nav a { padding: 5px; margin-right: 2px; }
                .form { font-size: 25px; text-align: left; padding: 20px 0px; }
            </style>
        </head>
        <body>
            <nav>
                <a href="/">Inicio</a>
                <a href="/livros">Livros</a>
                <a href="/carrinho">Carrinho</a>
                <a href="/sobre">Sobre</a>
            </nav>
            
            <div class="Main">
                <h1>Carrinho</h1>
                <hr>
                <form class="form">
                    <span>1984</span>
                    <input type="checkbox" name="livros" id="1984">
                    <span>O Senhor dos Anéis</span>
                    <input type="checkbox" name="livros" id="O Senhor dos Anéis">
                    <span>Dom Casmurro</span>
                    <input type="checkbox" name="livros" id="Dom Casmurro">
                    <span>O Príncipe</span>
                    <input type="checkbox" name="livros" id="O Príncipe">
                    <br>
                    
                    <p>Deseja alugar ou comprar: </p>
                        <select>
                            <option value="comprar">Comprar</option>
                            <option value="alugar">Alugar</option>
                        </select>
                    <br>
                    
                    <button type="submit">Finalizar</button>
                </form>
            </div>
        </body>
    </html>
    '''
    
@app.route("/sobre")
def sobre():
    return '''
    <!DOCTYPE html> 
    <html>
        <head>
            <title>Sobre</title>            
            <style>
                body { background-color: ; font-family: Arial; margin: 20px; padding: 5px; }
                .Main { margin: 0 auto; padding: 10px; }
            </style>
        </head>
        <body>
            <nav>
                <a href="/">Inicio</a>
                <a href="/livros">Livros</a>
                <a href="/carrinho">Carrinho</a>
                <a href="/sobre">Sobre</a>
            </nav>
            
            <div class="Main">
                <h2>Sobre</h2>
                <h3>Biblioteca Virtual</h3>
                <h3>Desenvolvido por: Sérgio</h3>
                <h4>IFBA - 2025</h4>
            </div>
        </body>
    </html>
    '''
    
if __name__ == "__main__":
    app.run(debug=True)
