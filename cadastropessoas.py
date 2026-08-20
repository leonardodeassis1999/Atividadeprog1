from databasepessoas import session_local
from pessoas import pessoas

session = session_local()

novas_pessoas = pessoas(
    nome = "Leonardo",
    cidade = "Fraiburgo"
)

session.add(novas_pessoas)
session.commit()
print("inserido com sucesso")

session.close()