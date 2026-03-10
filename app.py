from flask import Flask, render_template

app = Flask(__name__)

# Banco de dados fake ATUALIZADO com o caminho da imagem
filmes = {
    "matrix": {
        "titulo": "Matrix",
        "categoria": "Ficção Científica",
        "descricao": "Um hacker descobre a verdadeira realidade do mundo.",
        "imagem": "matrix.jpg" # Nome do arquivo na pasta static/images/
    },
    "vingadores": {
        "titulo": "Vingadores",
        "categoria": "Ação",
        "descricao": "Heróis se unem para salvar a Terra.",
        "imagem": "vingadores.jpg"
    },
    "titanic": {
        "titulo": "Titanic",
        "categoria": "Romance",
        "descricao": "Uma história de amor no navio mais famoso do mundo.",
        "imagem": "titanic.jpg"
    },
    "avatar": {
        "titulo": "Avatar",
        "categoria": "Ficção Científica",
        "descricao": "Em um mundo exuberante, um ex-fuzileiro embarca em uma jornada de redenção.",
        "imagem": "avatar.jpg"
    },
    "interstellar": {
        "titulo": "Interestelar",
        "categoria": "Ficção Científica",
        "descricao": "Uma equipe de exploradores viaja através de um buraco de minhoca no espaço.",
        "imagem": "interestelar.jpg"
    },
    "batman": {
        "titulo": "Batman",
        "categoria": "Ação",
        "descricao": "O justiceiro de Gotham enfrenta o caos provocado pelo Coringa.",
        "imagem": "batman.jpg"
    },
    "shrek": {
        "titulo": "Shrek",
        "categoria": "Animação",
        "descricao": "Um ogro tem sua paz invadida por personagens de contos de fadas.",
        "imagem": "shrek.webp"
    },
    "gladiador": {
        "titulo": "Gladiador",
        "categoria": "Ação",
        "descricao": "Um general romano busca vingança contra o imperador corrupto.",
        "imagem": "gladiador.jpg"
    },
    "toy-story": {
        "titulo": "Toy Story",
        "categoria": "Animação",
        "descricao": "Brinquedos ganham vida quando seus donos não estão por perto.",
        "imagem": "toy-story.jpg"
    },
    "como-eu-era-antes-de-voce": {
        "titulo": "Como Eu Era Antes de Você",
        "categoria": "Romance",
        "descricao": "Uma jovem do interior é contratada para cuidar de um tetraplégico rico e mal-humorado, mudando a vida de ambos para sempre.",
        "imagem": "como_eu_era_antes_de_voce.jpg"
    }
}


@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)


@app.route('/filme/<nome>')
def filme(nome):
    filme = filmes.get(nome)

    if filme:
        return render_template('filme.html', filme=filme)
    else:
        return "<h1>Filme não encontrado</h1>", 404


@app.route('/categorias')
def categorias():
    # Uma forma mais dinâmica de pegar as categorias
    lista_categorias = sorted(list(set(f['categoria'] for f in filmes.values())))
    return render_template('categorias.html', categorias=lista_categorias)


if __name__ == '__main__':
    app.run(debug=True)