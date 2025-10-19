import requests
import time
import random
import json

# URL do Node-RED (ajusta se for outro)
NODE_RED_URL = "http://localhost:1880/paciente"

# Lista de pacientes simulados
PACIENTES = [
    {"id": 1, "nome": "Maria Silva"},
    {"id": 2, "nome": "João Pereira"},
    {"id": 3, "nome": "Rita Costa"},
    {"id": 4, "nome": "João Silva"},
]

def gerar_sinais(p):
    return {
        "paciente": p["nome"],
        "batimentos": random.randint(60, 110),
        "temperatura": round(random.uniform(36.0, 38.5), 1),
        "spo2": random.randint(90, 100),
        "pa": {
            "sistolica": random.randint(110, 130),
            "diastolica": random.randint(70, 85),
        },
        "ts": int(time.time() * 1000),
    }

def main():
    print(f"[INFO] A enviar dados simulados para {NODE_RED_URL}")
    while True:
        batch = [gerar_sinais(p) for p in PACIENTES]
        try:
            r = requests.post(NODE_RED_URL, json=batch, timeout=5)
            if r.status_code == 200:
                print(f"[OK] Enviado batch com {len(batch)} pacientes")
            else:
                print(f"[ERRO] Código HTTP {r.status_code}: {r.text}")
        except Exception as e:
            print(f"[FALHA] {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()

