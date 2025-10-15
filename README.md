# Projeto: Sistema de Monitorização de Pacientes (Node-RED + uibuilder + Python)

Este projeto é um demo educativo que combina **Node-RED + uibuilder** com um script em **Python** para simular e enviar sinais vitais em tempo real.

## O que está incluído
- `flows/monitoracao-pacientes.flows.json` — Flow para importar no Node-RED (contém: HTTP In -> Function -> uibuilder out + inject de simulação)
- `uibuilder/index.html`, `uibuilder/client.js`, `uibuilder/style.css` — Frontend servido pelo nó uibuilder
- `python/simular_enviar.py` — Script Python que gera dados simulados e envia via HTTP POST para o Node-RED
- `python/requirements.txt` — Dependências Python (requests)
- `LICENSE` — Licença MIT (demo)
- `README.md` — este ficheiro

## Instruções rápidas
1. Instalar Node-RED: https://nodered.org
2. Instalar o nó `node-red-contrib-uibuilder` via Palette Manager.
3. Importar o ficheiro `flows/monitoracao-pacientes.flows.json` no Node-RED (menu → Import → clipboard).
4. Confirmar que o nó `uibuilder` tem o `url` definido como `uibuilder` (ou ajustar conforme o flow).
5. Deploy no Node-RED.
6. Executar o script Python para começar a enviar dados:
   ```bash
   cd python
   python3 -m venv venv
   source venv/bin/activate   # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   python simular_enviar.py --url http://localhost:1880/paciente --interval 1
   ```
7. Abrir a UI: `http://localhost:1880/uibuilder` (ou o caminho indicado pelo nó uibuilder).

## Notas
- O script Python usa HTTP POST para enviar JSON para o Node-RED (nó HTTP In no flow escuta `/paciente`). Se preferires, podes alterar para MQTT ou WebSocket.
- O frontend é simples (cartões + possibilidade de ligar Chart.js). Podes expandir para históricos, alertas e persistência (InfluxDB/SQLite).
