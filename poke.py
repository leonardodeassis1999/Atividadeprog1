import requests

def pokemon_listar():

    quantidade = input("Quantos pokemons deseja listar?").strip().lower() 
    pokemons_disponiveis = "https://pokeapi.co/api/v2/pokemon?limit="+quantidade
    respostapokemons = requests.get(pokemons_disponiveis)
    dadospokemons_disponiveis = respostapokemons.json()

    for pokemon in dadospokemons_disponiveis["results"]:
        print("-",pokemon["name"])

def pokemon_buscar():

    nome = input("Qual é o pokemon?").lower().lstrip()

    url = "https://pokeapi.co/api/v2/pokemon/" + nome 

    resposta = requests.get(url)
    dados = resposta.json()

    print("status: ", resposta.status_code)
    print("--- Informações gerais---")
    print("Nome: ", dados['name'])
    print("Número: ", dados['id'])
    print("Altura: ", dados['height'])
    print("Peso: ", dados['weight'])

    print ("--- Habilidades ---")
    for item in dados["types"]:
        ("-", item["type"]["name"])

        print ("--- Stats ---")
    for stat in dados["stats"]:
        print ("-", stat["stat"]["name"],":",stat["base_stat"])

def batalha():

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


def menu():
    
    while True:
        print("\n--- MENU POKÉMON ---")
        print("1 - Listar Pokémons")
        print("2 - Buscar Pokémon")
        print("3 - Batalha")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            pokemon_listar()
        elif opcao == "2":
            pokemon_buscar()
        elif opcao == "3":
            batalha()
        elif opcao == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
#atividade fazer função para monstrar e exibir