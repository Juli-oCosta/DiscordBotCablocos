import json

CAMINHO_ESTADO = "json/estado.json"

def carregar_estado():
    with open(CAMINHO_ESTADO, "r") as f:
        return json.load(f)
    

def salvar_estado(dados):
    with open(CAMINHO_ESTADO, "w") as f:
        json.dump(dados, f, indent=4)