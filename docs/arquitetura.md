# ProjetoSaudeV2 — System Architecture

## 1. Overview
**ProjetoSaudeV2** is built on a modular and fully local architecture that integrates simulation, data processing, database storage, and real-time web visualization using **Node-RED**, **SQLite**, and **uibuilder**.

```
[ Timestamp / Start Simulation ]
        │
        ▼
[ simulate_data_pacient ]
        │
        ▼
[ convert_payload_to_insert_sqllite ]
        │
        ▼
[ db_saude (SQLite) ]
        │
        └──► [ uibuilder <projetosaudev2> → Real-Time Dashboard ]
```

- **Node-RED (Simulation & Logic):** Generates, processes, and routes data across all layers.  
- **SQLite (`db_saude`):** Stores patient data persistently on the local environment.  
- **uibuilder:** Provides a responsive web dashboard for real-time visualization.  
- **Python (Optional):** Can be used for extended simulations or data sources.

---

## 2. Components and Roles

### 2.1 Node-RED
- **`timestamp` / `Start Simulation (1s)`** — Initiates data generation automatically or manually.  
- **`simulate_data_pacient`** — Generates random vital sign data (heart rate, temperature, SpO₂, and blood pressure).  
- **`convert_payload_to_insert_sqllite`** — Formats and structures the payload for SQLite insertion.  
- **`db_saude (SQLite)`** — Inserts validated records into the local database.  
- **`Gerar sinais e enviar a uibuilder`** — Transmits real-time updates to the dashboard.  
- **`uibuilder <projetosaudev2>`** — Displays incoming data dynamically through the web interface.  
- **`debug` nodes** — Used for monitoring and validation during development.

### 2.2 SQLite
- Stores all patient and vital sign records locally.  
- Ensures persistence and fast access without remote dependencies.  
- Database file: `db_saude`.

### 2.3 uibuilder
- Displays patient information in real time through a browser-based dashboard.  
- Uses **HTML**, **CSS**, and **JavaScript** for responsive visualization.  
- Updates automatically with every new data packet sent by Node-RED.

---

## 3. Data Flow

### A) Simulation and Storage
1. A simulation cycle is triggered by a timestamp or timed event.  
2. The `simulate_data_pacient` function generates random patient vital signs.  
3. The data is processed and converted into SQL format by `convert_payload_to_insert_sqllite`.  
4. The processed data is stored in **db_saude (SQLite)**.  
5. The same data is simultaneously transmitted to the **uibuilder** dashboard.

### B) Visualization
1. The dashboard receives new data directly from Node-RED.  
2. All displayed values (heart rate, temperature, blood pressure, and SpO₂) are refreshed in real time.

---

## 4. Database Model (SQLite)
```sql
CREATE TABLE vitals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp_ms INTEGER NOT NULL,
  heart_rate INTEGER,
  temperature REAL,
  spo2 INTEGER,
  systolic INTEGER,
  diastolic INTEGER
);

CREATE INDEX idx_vitals_timestamp ON vitals(timestamp_ms DESC);
```

The table stores continuous measurements, maintaining chronological order for efficient retrieval and visualization.

---

## 5. Node-RED Flow Design
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
```

**Parallel Path:**
```
[debug nodes 3, 4, 5] → Validation of intermediate outputs
```

---

## 6. Summary
The architecture of **ProjetoSaudeV2** is fully local, modular, and low-code.  
It integrates **Node-RED**, **SQLite**, and **uibuilder** into a cohesive ecosystem capable of generating, storing, and displaying real-time health data.  
This structure offers a reliable foundation for academic research, prototype development, and health data visualization.
