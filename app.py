from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from conexao import conectar

app = FastAPI()



class Pessoa(BaseModel):
    nome: str
    cidade: str



@app.get("/pessoas")
def listar_pessoas():

    banco = conectar()
    cursor = banco.cursor(dictionary=True)

    cursor.execute("SELECT * FROM pessoas ORDER BY id")

    pessoas = cursor.fetchall()

    cursor.close()
    banco.close()

    return pessoas



@app.post("/pessoas")
def cadastrar_pessoa(pessoa: Pessoa):

    banco = conectar()
    cursor = banco.cursor()

    sql = "INSERT INTO pessoas (nome, cidade) VALUES (%s, %s)"

    cursor.execute(
        sql,
        (pessoa.nome, pessoa.cidade)
    )

    banco.commit()

    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa cadastrada com sucesso"}



@app.put("/pessoas/{id}")
def atualizar_pessoa(id: int, pessoa: Pessoa):

    banco = conectar()
    cursor = banco.cursor()

    sql = """
        UPDATE pessoas
        SET nome = %s, cidade = %s
        WHERE id = %s
    """

    cursor.execute(
        sql,
        (pessoa.nome, pessoa.cidade, id)
    )

    banco.commit()

    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa atualizada com sucesso"}


@app.delete("/pessoas/{id}")
def excluir_pessoa(id: int):

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(
        "DELETE FROM pessoas WHERE id = %s",
        (id,)
    )

    banco.commit()

    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa excluída com sucesso"}


# chama o html   >> criem uma pasta static e adicionem dentro dela no projeto, se trocar o noem ajustar abaixo em directory
app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)