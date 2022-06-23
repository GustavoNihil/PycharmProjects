from flask import Flask, render_template

app = Flask(__name__)

#Criar a 1° página do site
## route -> link da página - Caminho depois do domínio
## função -> O que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")


#Pagina secundária


@app.route("/evolucaocomopatologia")
def evolucaocomopatologia():
    return render_template("evolucaocomopatologia.html")


#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku


# Notas:

# Forçar push: "git push --force heroku master"

