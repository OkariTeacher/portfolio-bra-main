# 🌐 Meu Site de Portfólio com Flask

Neste projeto você vai criar o **seu próprio site de portfólio** com **Flask**: uma página com a sua apresentação, as suas habilidades, uma **demonstração dinâmica dos seus projetos** e um **formulário de feedback**. No final, você vai publicar tudo no **GitHub** como um projeto **open source**. 🚀

Vamos trabalhar como em uma equipe de verdade: em **sprints** (método SCRUM), com tempo certo para cada etapa e uma **retrospectiva** depois de cada uma.

---

## 📚 O que você vai aprender

- ✅ Revisar os **elementos dinâmicos do Jinja** (`if`, `for`, variáveis)
- ✅ Criar e **processar formulários** no Flask
- ✅ Escolher uma **paleta de cores** e decidir o que mostrar sobre você
- ✅ Montar o **seu portfólio** do zero ao final
- ✅ Publicar o projeto no **GitHub**

---

## 📁 Estrutura do projeto

```
📦 meu-portfolio
 ┣ 📜 main.py                  # O "cérebro": rotas e lógica do Flask
 ┣ 📂 templates
 ┃ ┗ 📄 index.html             # A página (HTML + Jinja)
 ┗ 📂 static
   ┣ 📂 css
   ┃ ┗ 🎨 style.css            # A aparência (cores, fontes, layout)
   ┗ 📂 img                    # Suas imagens
     ┣ 🖼️ profile.png          # Sua foto
     ┣ 🖼️ python.png          # Ícones das habilidades
     ┣ 🖼️ discord.png
     ┣ 🖼️ html.png
     ┣ 🖼️ db.webp
     ┗ 🖼️ python-project.png  # Print do seu projeto de Python
```

| Arquivo | Para que serve |
|---|---|
| `main.py` | Define o que acontece quando alguém acessa o site ou clica num botão |
| `templates/index.html` | O que aparece na tela. Tem trechos em **Jinja** que mudam conforme as variáveis do Flask |
| `static/css/style.css` | Cores, fontes e posição dos elementos |
| `static/img/` | Todas as imagens do site |

> ⚠️ O Flask é exigente com os nomes: as pastas **precisam** se chamar `templates` e `static`, exatamente assim.

---

## ⚙️ Passo 0: Preparando o ambiente

### 1. Instale e ative o ambiente virtual

> ❗ Sempre use o ambiente virtual para não misturar as bibliotecas do projeto com as do computador.

1. Abra a pasta do projeto no VS Code e abra o terminal (`Ctrl + '`)
2. Instale o pipenv:
   ```bash
   pip install pipenv
   ```
3. Instale o Flask no projeto:
   ```bash
   pipenv install flask
   ```
   > 💡 Se o projeto já veio com um arquivo `Pipfile`, basta rodar `pipenv install` sem nome nenhum: ele instala tudo que o projeto precisa.
4. Ative o ambiente virtual:
   ```bash
   pipenv shell
   ```
5. Escolha o interpretador correto na IDE:
   - Pressione `Ctrl + Shift + P`
   - Digite **Python: Select Interpreter** e pressione `Enter`
   - Escolha o interpretador que tem **Pipenv** no nome

### 2. Rode o site

```bash
python main.py
```

Abra no navegador: **http://127.0.0.1:5000** 🎉

- Para **parar** o site: `Ctrl + C` no terminal
- Como o `debug=True` está ligado, o site **reinicia sozinho** quando você salva um arquivo `.py`. Para ver mudanças no HTML ou no CSS, basta **atualizar a página** (`F5`, ou `Ctrl + F5` se o CSS não mudar)

---

## 🧠 Como o site funciona

### Mostrando uma página

```
Navegador pede "/"  →  Flask (main.py)  →  render_template('index.html')
                                         →  Jinja preenche as variáveis
                                         →  HTML pronto volta para o navegador
```

### O botão "VER PROJETO" (apresentação dinâmica)

```
1. Visitante clica em "VER PROJETO" do Python
2. O formulário envia  button_python="VER PROJETO"  para a rota "/" (POST)
3. No main.py, request.form.get('button_python') lê esse valor
4. render_template(..., button_python=button_python) manda para o HTML
5. No HTML, {% if button_python %} decide: mostra o projeto ou não
```

> 💡 Se o botão **não** foi clicado, `request.form.get(...)` devolve `None`, que o Jinja trata como "falso". Por isso o bloco do projeto fica escondido.

### 📝 Cola do Jinja

| O que você quer | Como escrever |
|---|---|
| Mostrar uma variável | `{{ variavel }}` |
| Mostrar só se existir / for verdadeira | `{% if variavel %} ... {% endif %}` |
| Escolher entre opções | `{% if x == 'a' %} ... {% elif x == 'b' %} ... {% else %} ... {% endif %}` |
| Repetir para cada item de uma lista | `{% for item in lista %} ... {% endfor %}` |
| Comentário que não aparece no site | `{# comentário #}` |
| Caminho de arquivo da pasta static | `{{ url_for('static', filename='img/foto.png') }}` |

---

## 🗓️ Como a aula funciona (SCRUM)

**SCRUM** é um método para equipes trabalharem de forma mais eficiente. O projeto é dividido em pequenas etapas chamadas **sprints**, e depois de cada uma a equipe para para refletir sobre o que funcionou e o que pode melhorar.

| Etapa | O que fazemos |
|---|---|---|
| 🧭 Planejamento | Entender o quadro de sprint e as regras |
| 🏃 **Sprint #1** | Preparar os materiais |
| 🔄 Retrospectiva | Refletir e planejar o próximo sprint |
| 🏃 **Sprint #2** | Desenvolver o site |
| 🔄 Retrospectiva | Refletir e planejar o próximo sprint |
| 🏃 **Sprint #3** | Testar e publicar no GitHub |

> ⏱️ **Atenção ao tempo!** Cada sprint tem um limite. Se o tempo acabar, pare, faça a retrospectiva e anote o que ficou faltando.

---

## 🏃 Sprint #1: Preparando os materiais 

**Objetivos:** baixar o template, preparar todos os materiais do portfólio e registrar tudo no diário.

### Tarefas

1. **Baixe o template do repositório** e rode localmente (veja o Passo 0)
2. **Abra o diário** na plataforma
3. **Crie uma entrada** com todos os seus materiais (modelo abaixo)
4. **Escolha uma paleta de cores**
5. **Escolha as imagens**
6. **Escolha os textos**

### 🎨 4. Escolhendo a paleta de cores

Use de **3 a 5 cores** no máximo

Para aplicar, abra `static/css/style.css` e troque os códigos das cores dos arquivos

### 🖼️ 5. Escolhendo as imagens

Coloque os arquivos dentro de `static/img/`. **O nome do arquivo precisa ser igual ao que está no HTML**, ou troque o nome no HTML.

| Imagem | Nome no template | 
|---|---|---|
| Sua foto | `profile.png` |
| Ícone do Python | `python.png` | 
| Ícone do Discord | `discord.png` |
| Ícone do HTML | `html.png` | 
| Ícone do banco de dados | `db.webp` | 
| Print do projeto de Python | `python-project.png` | 

> 💡 Para o print do projeto, use a ferramenta de captura do seu computador (`Win + Shift + S` no Windows). Se você escolher uma imagem de outro formato (por exemplo `.jpg`), **troque também a extensão no HTML**.

### ✍️ 6. Escolhendo os textos

Prepare:
- **Seu nome** e uma frase de apresentação (ex: *"Estudante de Python apaixonado por bots"*)
- **Sobre mim:** 3 ou 4 frases. Quem é você? O que gosta de programar? O que já aprendeu?
- **Uma frase para cada habilidade** (Python, Discord, HTML, Banco de dados)
- **O link do GitHub** de cada projeto que você vai mostrar

## 🔄 Retrospectiva #1 

1. O que você conseguiu fazer? Teve tempo suficiente para concluir tudo?
2. Qual etapa foi a mais difícil?
3. Como você melhoraria este sprint?

Depois, **planeje o próximo sprint**: o que você precisa fazer primeiro?

---

## 🏃 Sprint #2: Desenvolvimento

**Objetivos:** adicionar todos os materiais ao site, desenvolver a apresentação dinâmica dos projetos e processar um formulário.

### ✅ Tarefa 1: Adicionar os materiais ao site

Procure os comentários **`EDITE AQUI`** no `index.html`. Eles mostram tudo que você deve personalizar:

- [ ] Cores no `style.css`
- [ ] Título da aba (`<title>`)
- [ ] Nome e frase no começo da página
- [ ] Texto e foto da seção "Sobre mim"
- [ ] Texto e imagem de cada habilidade
- [ ] Link do GitHub em "Abrir no GitHub"
- [ ] Redes sociais no rodapé

### ✅ Tarefa 2: Apresentação dinâmica dos projetos

Hoje só o botão do **Python** mostra o projeto. Faça os outros três funcionarem! São 3 passos:

**Passo 1: no `main.py`, leia os outros botões**

```python
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')


    return render_template(
        'index.html',
        button_python=button_python,

    )
```

**Passo 2: no `index.html`, copie o bloco do projeto** (o que está dentro de `{% if button_python %}`) e cole logo abaixo, uma vez para cada habilidade, trocando o nome da variável, a imagem e o link:

```html
{% if button_discord %}
<div class="skills__project project" id="project">
  <img
    class="project__img"
    src="{{ url_for('static', filename='img/discord-project.png') }}"
    alt="projeto de discord"
    width="500"
  />
  <a class="project__link" href="https://github.com/SEU_USUARIO/SEU_BOT" target="_blank">Abrir no GitHub</a>
</div>
{% endif %}
```

**Passo 3: teste!** Clique em cada botão e veja se o projeto certo aparece.

### ✅ Tarefa 3: Processar o formulário de feedback

O formulário do final da página já está ligado à rota `/feedback` do `main.py`. Veja como ele funciona:

```python
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')   # <input name="email">
    text = request.form.get('text')     # <textarea name="text">
    print(f'Novo feedback de {email}: {text}')
    return render_template('index.html', feedback_sent=True, email=email)
```

**Teste:** preencha o formulário, clique em **ENVIAR** e olhe o **terminal**: o feedback aparece lá! 🎉 Na página, aparece a mensagem de agradecimento (que só existe porque o HTML tem `{% if feedback_sent %}`).

> 💡 **Regra de ouro:** o `name=""` do campo no HTML e o nome dentro de `request.form.get('...')` precisam ser **exatamente iguais**.

#### 🌟 Se sobrar tempo: guarde os feedbacks

**Opção A: em um arquivo de texto**

```python
with open('feedback.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{email}: {text}\n')
```

Coloque essas linhas dentro da função `feedback()`, antes do `return`. O `'a'` significa *append*: adiciona ao final sem apagar o que já tinha.

**Opção B: em um banco de dados** (com Flask-SQLAlchemy)

```bash
pipenv install flask-sqlalchemy
```

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

# Cada classe que herda de db.Model vira uma TABELA no banco
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Cria as tabelas (rode uma vez, antes do app.run)
with app.app_context():
    db.create_all()
```

E dentro da função `feedback()`:

```python
db.session.add(Feedback(email=email, text=text))
db.session.commit()
```

> ⚠️ **Cuidado:** `feedback.txt` e `feedback.db` guardam **e-mails de pessoas**. Não envie esses arquivos para o GitHub! Adicione-os ao `.gitignore` (veja o Sprint #3).

#### ⭐ Mais ideias para quem terminar cedo

- Adicionar links das redes sociais no rodapé (`<footer>`)
- Criar uma quinta habilidade
- Testar o site no celular (aperte `F12` e clique no ícone de celular)
- Trocar a fonte no `--font-main` do CSS

---

## 🔄 Retrospectiva #2 

1. O que deu certo neste sprint? E o que deu errado?
2. Terminou todas as tarefas? Se não, o que falta?
3. O que você faria diferente?

Planeje o último sprint: **testar e publicar**.

---

## 🏃 Sprint #3: Testando e publicando no GitHub 

**Objetivos:** testar o site e enviá-lo para um repositório público.

### 🧪 1. Teste o site

Use esta lista antes de publicar:

| Teste | ✅ |
|---|---|
| O site abre em `http://127.0.0.1:5000` sem erros | ☐ |
| Os 4 links do menu levam às seções certas | ☐ |
| Todas as imagens aparecem (nenhuma "quebrada") | ☐ |
| Cada botão **VER PROJETO** mostra o projeto certo | ☐ |
| Cada link **Abrir no GitHub** abre a página certa | ☐ |
| O formulário de feedback envia e mostra o agradecimento | ☐ |
| O texto está fácil de ler com as cores escolhidas | ☐ |
| Não sobrou nenhum "Informações sobre mim" ou "NOME SOBRENOME" 😅 | ☐ |


### 📤 3. Envie para o GitHub

#### Pelo VS Code (interface gráfica)

1. Abra a aba **Source Control** (ícone de ramificação) na barra lateral
2. Clique em **PUBLISH**
3. Confira os arquivos listados 
4. Escreva uma mensagem de commit (ex: `Primeira versão do meu portfólio`) e clique em **Commit**
5. Clique em **Publish Branch** e escolha criar o repositório **público** na sua conta do GitHub

#### Pelo navegador (alternativa)

1. Acesse [github.com](https://github.com) e entre na sua conta
2. Clique no **+** no canto superior direito e escolha **New repository**
3. Dê um nome ao repositório (ex: `meu-portfolio`), escolha **Public** e clique em **Create repository**
4. Na página do repositório novo, clique em **uploading an existing file**
5. Abra a pasta do projeto no seu computador e **arraste os arquivos** para a página do GitHub:
   - ✅ Envie: `main.py`, as pastas `templates` e `static`, o `Pipfile`, o `Pipfile.lock` e o `.gitignore`
   - ❌ **Não envie:** `feedback.txt`, arquivos `.db` e a pasta `__pycache__`
6. Escreva uma mensagem no campo **Commit changes** (ex: `Primeira versão do meu portfólio`)
7. Clique no botão verde **Commit changes**

### 🌍 4. O que é "open source"?

Ao deixar o repositório **público**, qualquer pessoa pode ver, aprender e até sugerir melhorias no seu código. Isso é **open source**. Por isso vale caprichar:

- 📝 Adicione um **README.md** explicando o que é o projeto, como instalar e como rodar
- 📸 Coloque um **print** do seu site funcionando
- 📄 Adicione uma **licença** (no GitHub: **Add file → Create new file**, nome `LICENSE`, e clique em **Choose a license template**. A **MIT License** é a mais comum para projetos de estudo)

---

## 🎓 Fim do Módulo 2: Flask

Parabéns! Você concluiu o módulo 2 e já está **50% do caminho** neste curso. 🎉

Com Flask você aprendeu a criar rotas, usar templates com Jinja, processar formulários e guardar dados. Essas habilidades já servem para criar sites de verdade. 💪

> 💬 **Reflexão:** o que você gostaria de fazer com essas habilidades no futuro?

---

## 🏠 Lição de casa: Aprimorando o Portfólio

Revise o seu projeto em casa. Na plataforma, você vai encontrar um **questionário** que ajuda a avaliar o seu próprio trabalho e a receber **recomendações de melhoria**. A pontuação máxima é **50 pontos**.

Ideias para deixar o portfólio mais completo:

- 🧩 Mais habilidades e projetos
- 💾 Salvar os feedbacks em um banco de dados
- 📱 Ajustar o visual para o celular
- 🎨 Animações e detalhes no CSS
- 📖 Um README caprichado no GitHub

---

## 🆘 Problemas comuns

| Problema | Provável causa e solução |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | O ambiente virtual não está ativo. Rode `pipenv shell` e confira o interpretador (`Ctrl + Shift + P`) |
| `TemplateNotFound: index.html` | A pasta precisa se chamar **`templates`** e o arquivo `index.html` precisa estar dentro dela |
| O CSS não carrega ou não muda | A pasta precisa se chamar **`static`**. Atualize com `Ctrl + F5` para limpar o cache |
| Imagem aparece "quebrada" | O nome do arquivo no HTML é diferente do arquivo em `static/img/` (cuidado com maiúsculas e com `.png` vs `.jpg`) |
| Clico em **VER PROJETO** e nada aparece | Faltou ler o botão no `main.py` **ou** esqueceu de enviar a variável no `render_template` **ou** o nome da variável no `{% if %}` está diferente |
| `405 Method Not Allowed` | A rota não tem `methods=['POST']`, ou o `action` do formulário aponta para a rota errada |
| `jinja2.exceptions.TemplateSyntaxError` | Faltou fechar um bloco: todo `{% if %}` precisa de `{% endif %}` e todo `{% for %}` de `{% endfor %}` |
| `Address already in use` | O site já está rodando em outro terminal. Feche-o com `Ctrl + C` |
| O formulário envia, mas nada acontece | Confira o terminal: o `print` do feedback aparece lá. E confira se o `name` do campo é igual ao do `request.form.get(...)` |

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)
- HTML e CSS

---

## 🚀 Próximos passos

Na próxima aula vamos aprender sobre **Inteligência Artificial** e criar um **notebook interativo**! 🧠✨

Não precisa esperar a aula para discutir as tarefas: use o grupo de chat para trocar ideias com os colegas.
