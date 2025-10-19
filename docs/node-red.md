# Node-RED Flow — ProjetoSaudeV2

## 1. Overview
The **Node-RED** environment acts as the central logic and automation layer of the system.  
It manages the complete process — simulation, data transformation, database insertion, and real-time dashboard updates — ensuring seamless integration between all components.

---

## 2. Main Functions
- **Data Simulation:** Automatically generates patient vital signs using the `simulate_data_pacient` node.  
- **Data Conversion:** The `convert_payload_to_insert_sqllite` node structures data for storage.  
- **Database Insertion:** Inserts validated readings into the local **SQLite (`db_saude`)** database.  
- **Real-Time Visualization:** The `Gerar sinais e enviar a uibuilder` node sends updates directly to **uibuilder <projetosaudev2>**.  
- **Monitoring and Debugging:** Multiple debug nodes (`debug 3`, `debug 4`, `debug 5`) allow flow verification during testing.

---

## 3. Core Nodes Utilized

| Node | Function |
|------|-----------|
| **timestamp / Start Simulation (1s)** | Triggers the data generation cycle periodically. |
| **simulate_data_pacient** | Produces random values for heart rate, temperature, SpO₂, and blood pressure. |
| **convert_payload_to_insert_sqllite** | Converts simulated data into an SQL-friendly format. |
| **db_saude (SQLite)** | Executes INSERT commands to store readings locally. |
| **Gerar sinais e enviar a uibuilder** | Forwards processed data to the dashboard for real-time updates. |
| **uibuilder <projetosaudev2>** | Displays data dynamically on the web interface. |
| **debug (3, 4, 5)** | Monitors outputs at various stages for troubleshooting. |

---

## 4. Data Flow
```
[timestamp / Start Simulation]
     ↓
[simulate_data_pacient]
     ↓
[convert_payload_to_insert_sqllite]
     ↓
[db_saude (SQLite)]
     ↓
[Gerar sinais e enviar a uibuilder]
     ↓
[uibuilder <projetosaudev2> → Real-Time Dashboard]
     ↓
[debug nodes (3, 4, 5) → Data validation and monitoring]
```

This design ensures that every data packet moves efficiently through simulation, processing, storage, and visualization.

---

## 5. Database Interaction
- Each new simulation generates an SQL `INSERT` command executed in **db_saude**.  
- Records are timestamped (`timestamp_ms`) and stored for later analysis or visualization.  
- The database operates entirely locally, without any remote or external API dependencies.

---

## 6. Flow Export
The full Node-RED flow configuration is stored in:  
`node-red/flows_ProjetoSaudeV2.json`

**Included in the export:**
- Simulation and data generation logic.  
- SQLite connection and insertion workflow.  
- Real-time dashboard configuration via uibuilder.  
- Debug nodes for runtime verification.

---

## 7. Summary
The Node-RED flow serves as the **central processing core** of *ProjetoSaudeV2*.  
It unifies simulation, local data storage, and real-time visualization in a fully offline, modular, and low-code architecture — providing both technical robustness and educational value.
