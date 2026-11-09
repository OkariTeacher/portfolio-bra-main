# ============================================================
# main.py - o "cérebro" do site de portfólio
#
# Aqui ficam as ROTAS: cada rota é um endereço do site
# e a função que roda quando alguém acessa esse endereço.
#
#   "/"          (GET)  -> mostra a página inicial
#   "/"          (POST) -> o visitante clicou em "VER PROJETO"
#   "/feedback"  (POST) -> o visitante enviou o formulário de feedback
# ============================================================

# Importar
# Flask         -> cria o site
# render_template -> abre um arquivo HTML da pasta "templates"
# request       -> permite ler o que o visitante enviou pelo formulário
from flask import Flask, render_template, request

# Cria o aplicativo. O __name__ ajuda o Flask a achar sozinho
# as pastas "templates" (HTML) e "static" (CSS e imagens).
app = Flask(__name__)


# ------------------------------------------------------------
# PÁGINA INICIAL
# Roda quando o visitante digita o endereço do site (método GET).
# ------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------------------------------------
# HABILIDADES DINÂMICAS
# Roda quando o visitante clica num botão "VER PROJETO" (método POST).
#
# Como funciona:
#   1. Cada botão do HTML tem um "name" (button_python, button_discord...)
#   2. Só o botão que foi clicado chega aqui com um valor.
#   3. Mandamos esse valor para o HTML, e lá o Jinja decide
#      se mostra ou não o projeto ({% if button_python %}).
# ------------------------------------------------------------
@app.route('/', methods=['POST'])
def process_form():
    # request.form.get('nome') devolve o valor do campo com esse "name".
    # Se o botão NÃO foi clicado, devolve None (que conta como "falso").
    button_python = request.form.get('button_python')

    # (Sprint 2): faça o mesmo para as outras habilidades!
    # Dica: copie a linha de cima e troque o nome. Exemplo:
    # button_discord = request.form.get('button_discord')
    # button_html = request.form.get('button_html')
    # button_db = request.form.get('button_db')

    # Envia as variáveis para o HTML. O nome do lado esquerdo (button_python=)
    # é o nome que você vai usar dentro do index.html.
    # (Sprint 2): lembre de adicionar aqui as variáveis novas também!
    return render_template(
        'index.html',
        button_python=button_python,
    )


# ------------------------------------------------------------
# FORMULÁRIO DE FEEDBACK
# Roda quando o visitante clica em "ENVIAR" no formulário de feedback.
# ------------------------------------------------------------
@app.route('/feedback', methods=['POST'])
def feedback():
    # Aqui o nome entre aspas é o "name" do campo no HTML:
    # <input name="email"> e <textarea name="text">
    email = request.form.get('email')
    text = request.form.get('text')

    # Por enquanto o feedback só aparece no TERMINAL onde o site está rodando.
    print(f'Novo feedback de {email}: {text}')

    # (desafio): salvar o feedback em um arquivo ou em um banco de dados.
    # Veja as dicas no README.

    # feedback_sent=True faz o HTML mostrar a mensagem de agradecimento.
    return render_template('index.html', feedback_sent=True, email=email)


# Só liga o site quando você roda ESTE arquivo (python main.py).
# debug=True reinicia o site sozinho quando você salva o código
# e mostra os erros na tela. Use só enquanto estiver desenvolvendo!
if __name__ == "__main__":
    app.run(debug=True)