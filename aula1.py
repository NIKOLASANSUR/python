from flask import Flask

app = Flask(__name__) 

@app.route('/')
def significado_decorator():
    return 'Em Python, um decorator (decorador) é uma função que envolve (envelopa) outra função ou método, permitindo modificar ou estender seu comportamento sem alterar o código fonte original. Eles são úteis para adicionar funcionalidades extras, como logs, controle de acesso ou cache, de forma limpa e reutilizável, utilizando a sintaxe' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/hello') 
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
