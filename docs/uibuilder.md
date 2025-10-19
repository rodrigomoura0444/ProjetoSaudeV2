# UI Builder — ProjetoSaudeV2

## 1. Overview
The **uibuilder** component provides the visual interface of the **ProjetoSaudeV2** system.  
It allows users to monitor simulated patient data in real time through a responsive, modern, and intuitive dashboard fully integrated with **Node-RED**.

---

## 2. Purpose
The interface displays real-time vital sign data for one or more patients, including:  
- **Heart Rate (BPM)**  
- **Temperature (°C)**  
- **Blood Pressure (mmHg)**  
- **Oxygen Saturation (SpO₂)**

Each patient is represented by an individual **information card**, which updates automatically with each new simulation cycle.

---

## 3. Files Used

| File | Description |
|------|--------------|
| **index.html** | Defines the structure of the dashboard (HTML). |
| **index.css** | Controls layout, color scheme, and component design (CSS). |
| **index.js** | Manages real-time data updates received from Node-RED (JavaScript). |

These files are located in the directory:  
`ProjetoSaudeV2/uibuilder/projetosaudev2/`

---

## 4. Example Layout

```
+----------------------------------------------------+
| ProjetoSaudeV2 — Real-Time Patient Monitoring      |
|----------------------------------------------------|
| [ Patient A ] [ Patient B ] [ Patient C ] [ ... ]  |
| Heart Rate: 78 bpm  | Temp: 36.6°C | SpO₂: 97%     |
| Blood Pressure: 120 / 80 mmHg                      |
+----------------------------------------------------+
```

The interface employs **soft colors**, **rounded borders**, and **modern typography**, following a layout optimized for medical and educational purposes.

---

## 5. Real-Time Connection
- The dashboard communicates directly with **Node-RED** via the uibuilder socket connection.  
- When the flow triggers a new simulation (`simulate_data_pacient`), the results are automatically pushed to the interface.  
- The browser updates instantly — no manual refresh is required.  
- The **Gerar sinais e enviar a uibuilder** node ensures smooth and synchronous updates between backend and frontend.

---

## 6. Customization
The frontend can be easily customized and extended by editing the following files:

- **index.css** — Adjust the visual theme, colors, and layout.  
- **index.js** — Implement custom alerts or new logic (e.g., warn if heart rate > 120 BPM).  
- **index.html** — Add new visual components such as charts, patient cards, or summary panels.

---

## 7. Summary
The **uibuilder dashboard** is the visualization core of *ProjetoSaudeV2*.  
It translates backend data into a **real-time, interactive, and user-friendly web interface**, bridging automation and human interpretation.  
This makes it an ideal solution for both **academic demonstrations** and **prototype healthcare systems**.
