#!/usr/bin/env python3
"""simular_enviar.py
Gera dados simulados de sinais vitais e envia via HTTP POST para o Node-RED.
Exemplo de uso:
  python simular_enviar.py --url http://localhost:1880/paciente --interval 1 --patients 3
"""
import time, json, argparse, random
import requests

def gerar_batch(n):
    pacientes = [f'Paciente {chr(65+i)}' for i in range(n)]
    dados = []
    for i,p in enumerate(pacientes):
        batimentos = int(round(60 + random.random()*60 + (i*3 - 3)))
        temperatura = float(round(36 + random.random()*2 + i*0.1,1))
        spo2 = int(round(92 + random.random()*8 - i))
        pa_s = int(round(110 + random.random()*20))
        pa_d = int(round(70 + random.random()*15))
        dados.append({
            'paciente': p,
            'batimentos': batimentos,
            'temperatura': temperatura,
            'spo2': spo2,
            'pa': {'sistolica': pa_s, 'diastolica': pa_d},
            'ts': int(time.time()*1000)
        })
    return dados

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='http://localhost:1880/paciente', help='URL do endpoint Node-RED (HTTP POST)')
    parser.add_argument('--interval', type=float, default=1.0, help='Intervalo em segundos entre envios')
    parser.add_argument('--patients', type=int, default=3, help='Número de pacientes simulados')
    args = parser.parse_args()

    print(f'Enviar para {args.url} cada {args.interval}s ({args.patients} pacientes)')
    while True:
        batch = gerar_batch(args.patients)
        payload = {'dados': batch}
        try:
            r = requests.post(args.url, json=payload, timeout=5)
            print(f'Enviado: {len(batch)} pacientes | status: {r.status_code}')
        except Exception as e:
            print('Erro ao enviar:', e)
        time.sleep(args.interval)

if __name__ == '__main__':
    main()
