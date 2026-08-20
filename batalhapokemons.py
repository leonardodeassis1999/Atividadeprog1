import requests

def Batalha():

    def pokemon01():

        global pokemon01,dados01
        pokemon01 = input("Qual o pokemon você deseja escolher para batalha?").strip().lower()
        dadosPokemonURL = "https://pokeapi.co/api/v2/pokemon/"+pokemon01
        reposta = requests.get(dadosPokemonURL)
        dados01 = resposta.json()

        def status_pokemon01():
            global conta_pokemon01
            print("status do",pokemon01)
            conta_pokemon01 = 0
            for i in dados01["stats"]
                valor = i["base_stat"]
                conta_pokemon01 += valor
                print(i["stat"]["name"],i["base_stat"])

            print("poder",conta_pokemon01)
        status_pokemon01()

    def pokemon02():

        global pokemon02,dados02
        pokemon02 = input("Qual o pokemon você deseja escolher para batalha?").strip().lower()
        dadosPokemonURL = "https://pokeapi.co/api/v2/pokemon/"+pokemon02
        reposta = requests.get(dadosPokemonURL)
        dados02 = resposta.json()

        def status_pokemon02():
            global conta_pokemon02
            print("status do",pokemon02)
            conta_pokemon02 = 0
            for i in dados02["stats"]
                valor = i["base_stat"]
                conta_pokemon02 += valor
                print(i["stat"]["name"],i["base_stat"])

            print("poder",conta_pokemon02)
        status_pokemon02()

    if conta_pokemon01 < conta_pokemon02:
        print("")
        print("Pokemon02 ganhou!")

    elif conta_pokemon01 == conta_pokemon02:
        print("Ambos tem o mesmo poder")

    else:
        print("")
        print("Pokemon01 ganhou!")