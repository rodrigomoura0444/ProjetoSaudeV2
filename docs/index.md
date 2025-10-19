# ProjetoSaudeV2

## 1. Introduction
**ProjetoSaudeV2** is an educational and technical initiative designed to demonstrate how **automation**, **data processing**, and **web visualization** can be integrated into a unified, real-time healthcare monitoring system.  
The project uses **Node-RED**, **SQLite**, and **uibuilder** to create a fully local and modular architecture for patient data simulation and visualization.

---

## 2. Overview
The main objective of this project is to simulate and monitor **vital signs** such as heart rate, temperature, oxygen saturation (SpO₂), and blood pressure using a local, scalable, and open-source framework.

**Core Components:**
- **Node-RED:** Manages data flow, automation, and simulation logic.  
- **SQLite (`db_saude`):** Provides local and persistent data storage.  
- **uibuilder (HTML/CSS/JS):** Displays real-time information through an interactive dashboard.  
- **Python (optional):** Can be used to extend simulation or integrate real sensors.  
- **MkDocs:** Generates professional and structured project documentation.

---

## 3. Key Features
- Real-time simulation and visualization of patient vital signs.  
- Local database for data storage without external dependencies.  
- Responsive and modern web interface for data monitoring.  
- Fully modular and low-code structure, suitable for education and IoT integration.  
- Scalable architecture adaptable to real-world medical applications.

---

## 4. System Architecture
The system operates entirely locally, with **Node-RED** coordinating data simulation, processing, storage, and visualization.  
Each component communicates internally, ensuring low latency and high stability.

```
[ Start Simulation ] → [ simulate_data_pacient ] → [ convert_payload_to_insert_sqllite ]
       ↓
[ db_saude (SQLite) ] → [ uibuilder <projetosaudev2> → Real-Time Dashboard ]
```

This structure provides reliability, modularity, and independence from remote services.

---

## 5. Quick Start Guide
```bash
# 1. Start Node-RED
node-red

# 2. Open the dashboard in your browser
http://localhost:1880/uibuilder/ProjetoSaudeV2
```

The simulation runs automatically through the **timestamp** or **Start Simulation** node in Node-RED.

---

## 6. About
This project was developed by **Rodrigo Moura** as part of an academic initiative focused on **automation, data systems, and health monitoring**.  
It showcases how open-source tools can be used to build efficient and intelligent systems for real-time healthcare management.

> Demonstrating the integration of simulation, automation, and visualization in a unified, low-code environment.
