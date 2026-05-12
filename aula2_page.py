from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Nikolas Ansur</title>
            <style>
                /* General Styles */
                body {
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(135deg, #007BFF, #6C63FF);
                    color: #333;
                    overflow-x: hidden;
                }
                nav {
                    background: #007BFF;
                    color: #fff;
                    padding: 15px 0;
                    position: sticky;
                    top: 0;
                    z-index: 1000;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                nav ul {
                    list-style: none;
                    display: flex;
                    justify-content: center;
                    margin: 0;
                    padding: 0;
                }
                nav ul li {
                    margin: 0 15px;
                }
                nav ul li a {
                    color: #fff;
                    text-decoration: none;
                    font-weight: bold;
                    transition: color 0.3s ease;
                }
                nav ul li a:hover {
                    color: #FFD700;
                }
                header {
                    text-align: center;
                    padding: 50px 20px;
                    color: #fff;
                }
                header h1 {
                    font-size: 3rem;
                    margin: 0;
                    animation: fadeIn 1.5s ease-in-out;
                }
                header p {
                    font-size: 1.2rem;
                    margin-top: 10px;
                }
                .container {
                    width: 90%;
                    max-width: 1200px;
                    margin: 30px auto;
                    background: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    animation: slideIn 1s ease-in-out;
                }
                h2 {
                    color: #007BFF;
                    border-bottom: 2px solid #007BFF;
                    padding-bottom: 5px;
                    margin-bottom: 20px;
                    font-size: 1.8rem;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
                ul li {
                    margin: 10px 0;
                    font-size: 1.1rem;
                }
                ul li strong {
                    color: #007BFF;
                }
                .btn {
                    display: inline-block;
                    background: #007BFF;
                    color: #fff;
                    padding: 10px 20px;
                    border-radius: 5px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: background 0.3s ease;
                }
                .btn:hover {
                    background: #0056b3;
                }
                footer {
                    text-align: center;
                    padding: 20px;
                    background: #007BFF;
                    color: #fff;
                    margin-top: 30px;
                }
                footer a {
                    color: #FFD700;
                    text-decoration: none;
                    font-weight: bold;
                }
                footer a:hover {
                    color: #fff;
                }

                /* Animations */
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                    }
                    to {
                        opacity: 1;
                    }
                }
                @keyframes slideIn {
                    from {
                        transform: translateY(50px);
                        opacity: 0;
                    }
                    to {
                        transform: translateY(0);
                        opacity: 1;
                    }
                }
            </style>
        </head>
        <body>
            <nav>
                <ul>
                    <li><a href="#info">Informações Pessoais</a></li>
                    <li><a href="#objetivo">Objetivo</a></li>
                    <li><a href="#formacao">Formação Acadêmica</a></li>
                    <li><a href="#conhecimentos">Conhecimentos Técnicos</a></li>
                    <li><a href="#idiomas">Idiomas</a></li>
                    <li><a href="#competencias">Competências</a></li>
                </ul>
            </nav>
            <header>
                <h1>Currículo</h1>
                <p>Bem-vindo ao currículo de Nikolas Ansur</p>
            </header>
            <div class="container" id="info">
                <h2>Informações Pessoais</h2>
                <ul>
                    <li><strong>Nome:</strong> Nikolas Ansur Proti Soares</li>
                    <li><strong>Endereço:</strong> Rua Luiz Peçanha, 214 – Apto 201 – Santa Cruz - Belo Horizonte, MG</li>
                    <li><strong>Telefone:</strong> (31) 97179.7786</li>
                    <li><strong>Email:</strong> nikolas.ansur@gmail.com</li>
                </ul>
            </div>
            <div class="container" id="objetivo">
                <h2>Objetivo</h2>
                <p>Buscando uma oportunidade como Jovem Aprendiz ou Estagiário de TI, com foco em desenvolvimento de habilidades técnicas e práticas no ambiente corporativo. Estudante dedicado e entusiasta por tecnologia, com vontade de aprender e crescer na área.</p>
            </div>
            <div class="container" id="formacao">
                <h2>Formação Acadêmica</h2>
                <ul>
                    <li><strong>Instituição:</strong> Cotemig — Colégio e Faculdade de Tecnologia</li>
                    <li><strong>Curso:</strong> Técnico em Informática (Em andamento – 3º Ano)</li>
                    <li><strong>Previsão de conclusão:</strong> 2026</li>
                </ul>
            </div>
            <div class="container" id="conhecimentos">
                <h2>Conhecimentos Técnicos</h2>
                <ul>
                    <li>Python (estrutura de dados, automação, scripts)</li>
                    <li>C# e Front-end intermediário</li>
                    <li>MySQL (consultas avançadas, modelagem, procedures e views)</li>
                    <li>Redes de computadores (IP, protocolos, DNS, DHCP)</li>
                    <li>Lógica de Programação</li>
                    <li>Pacote Office (Word, Excel, PowerPoint)</li>
                </ul>
            </div>
            <div class="container" id="idiomas">
                <h2>Idiomas</h2>
                <ul>
                    <li>Espanhol: Intermediário</li>
                    <li>Inglês: Básico</li>
                </ul>
            </div>
            <div class="container" id="competencias">
                <h2>Competências Comportamentais</h2>
                <ul>
                    <li>Facilidade para aprender</li>
                    <li>Boa comunicação</li>
                    <li>Trabalho em equipe</li>
                    <li>Proatividade e responsabilidade</li>
                </ul>
            </div>
            <footer>
                <p>Desenvolvido por <a href="mailto:nikolas.ansur@gmail.com">Nikolas Ansur</a></p>
            </footer>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)