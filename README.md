# ElderGuard AI 🛡️
> **AI-Powered IoT-Based Elderly Care, Remote Caregiver Alerting & Clinical Emergency Assistance System**  
> *Developed for IoTrix 2.0 | Team KingTech | Sabaragamuwa University of Sri Lanka*

---

## 📌 1. Project Overview
**ElderGuard AI** is a smart IoT healthcare monitoring and emergency assistance system designed for elderly people living independently.

Traditional elderly care faces two major challenges:
1. **At Home:** Falls and abnormal vital signs often go unnoticed when an elderly person is alone, delaying life-saving help.
2. **At Clinics / Hospitals:** When an elderly patient arrives at a clinic, doctors and nurses do not have immediate access to their recent vital history, past incidents, or medication adherence.

**ElderGuard AI solves both issues:**
* An **ESP32 wearable device** continuously tracks heart rate, blood oxygen ($SpO_2$), body temperature, and body movement (fall detection).
* The wearable sends data via **Bluetooth Low Energy (BLE)** to the patient's smartphone.
* A **dual-mode Flutter mobile application** provides local medication and meal reminders for the elderly user, while sending instant emergency push alerts to linked family caregivers during critical events.
* When visiting a clinic, the elderly app displays a **unique Patient QR Code**. Hospital staff can scan the QR code to open a zero-login **Hospital Web Dashboard** and immediately print a 1-page health summary (`Ctrl + P`) for the consulting physician.

---

## 👥 2. Team KingTech & Module Responsibilities
* **V. Kathirsan** — *IoT Wearable & BLE Integration* (ESP32 firmware, sensor data acquisition, fall-detection logic, BLE communication).
* **S. Abisegan** — *Backend API, Risk Engine & Database* (FastAPI backend, MySQL schema, multi-tier risk evaluation, push alert services).
* **M. Pavithar** — *Dual-Mode Mobile Application* (Flutter UI/UX, Elderly Mode vitals display, Caregiver Mode monitoring, QR code generator).
* **T. Saruhasan** — *Hospital Web Dashboard & System Documentation* (Clinical summary web portal, print-optimized CSS, pitch presentation).

---

## 🏗️ 3. System Architecture & End-to-End Workflow
[ ESP32 Wearable Device ]
• MAX30102 (Heart Rate & SpO2)
• DS18B20 (Body Temperature)
• MPU6050 (6-Axis Accelerometer for Fall Detection)
│
▼  Bluetooth Low Energy (BLE)
[ Flutter Mobile Application (Gateway) ]
• Elderly Mode: Large vitals display, medicine/food pop-ups, patient QR code
│
▼  HTTPS / REST API
[ FastAPI Backend + MySQL Database ]
• Evaluates risk levels: NORMAL | WARNING | CRITICAL
│
├──► Push Notifications ──► [ Caregiver Mode App ]
│    (Instant alerts for falls or abnormal vitals)
│
└──► Tokenized Patient URL ──► [ Hospital Web Dashboard ]
(Nurses scan QR code ➔ View vitals ➔ Press Ctrl+P for Doctor)

---

## ⚙️ 4. Technology Stack

| Layer | Component / Technology | Purpose |
| :--- | :--- | :--- |
| **Edge Hardware** | ESP32 Microcontroller | Wearable processing and BLE transmission |
| **Sensors** | MAX30102, DS18B20, MPU6050 | Heart rate, $SpO_2$, temperature, and fall detection |
| **Edge Protocol** | Bluetooth Low Energy (BLE GATT) | Low-power wearable-to-mobile data streaming |
| **Mobile App** | Flutter & Dart | Cross-platform dual-mode mobile application |
| **Cloud Protocol** | HTTPS / REST APIs | Secure mobile-to-cloud data communication |
| **Backend** | Python & FastAPI | Asynchronous telemetry processing and risk engine |
| **Database** | MySQL | Relational storage for vitals, logs, and users |
| **Clinical Web Portal** | HTML5, Tailwind CSS, JavaScript | Zero-login QR scanner viewer with `@media print` CSS |
| **Design & Simulation** | Figma, Wokwi, Postman | UI/UX design, virtual ESP32 testing, and API verification |

---

## 🚀 5. Key System Features

### A. Dual-Mode Mobile Application
* **Elderly Mode:**
  * Simple, high-contrast, large-font interface for seniors.
  * Real-time vitals display (Heart Rate, $SpO_2$, Temp).
  * Medication and meal reminders.
  * Generates a persistent, encrypted **Patient QR Code**.
  * 30-second cancellation countdown for accidental fall triggers to prevent false alarms.
* **Caregiver Mode:**
  * Links directly to the elderly account via Patient ID.
  * Displays live vital graphs and daily health trends.
  * Receives high-priority push alerts for falls and critical vitals.

### B. Intelligent Risk Engine
Incoming health and motion readings are evaluated into three defined tiers:
* **Normal:** All vitals within healthy ranges; normal movement detected.
* **Warning:** Mild deviations (e.g., slight fever, elevated heart rate); logs status and updates trends.
* **Critical:** Fall detected ($\text{SVM} > 2.5g$ followed by inactivity) or severe vital abnormalities; triggers immediate caregiver alert.

### C. Zero-Login Hospital Clinical Web Dashboard
* No account or app installation required for hospital staff.
* Clinic receptionists or nurses simply scan the patient's QR code.
* Displays the patient's last 24 hours of vitals, active medications, and recorded incidents.
* **1-Click Print Summary (`Ctrl + P`):** Formatted with print-ready CSS to produce a clean physical 1-page report for the doctor.



## 📁 6. Repository Directory Structure

```text
ElderGuard-AI/
├── README.md                          # Project documentation and guide
├── docs/                              # Architecture diagrams, proposal, and progress sheet
│   ├── ElderGuard_Proposal.pdf
│   └── ElderGuard_Technical_Progress_Sheet.pdf
├── mobile_app/                        # Flutter mobile application
│   ├── lib/
│   │   ├── screens/
│   │   │   ├── elderly/               # Vitals, QR code, and reminders
│   │   │   └── caregiver/             # Caregiver charts and alert history
│   │   └── services/                  # BLE connection and API client
├── backend/                           # FastAPI backend
│   ├── main.py                        # API routes and entry point
│   ├── requirements.txt               # Python dependencies
│   └── routers/                       # Telemetry ingestion and risk engine
├── firmware/                          # ESP32 sensor reading and BLE code
│   └── esp32_firmware.ino
└── web-dashboard/                     # Hospital QR web portal
    ├── index.html                     # Patient summary page
    └── print-style.css                # CSS for clean Ctrl+P printing

```
7. How to Run Locally
1. Run the FastAPI Backend
Bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
Interactive API documentation will be available at: http://localhost:8000/docs

2. Run the Hospital Web Dashboard
Open web-dashboard/index.html in any modern web browser.

Use Ctrl + P (or Cmd + P on Mac) to view the formatted 1-page clinical print preview.

8. Grand Finale Roadmap (Target: October 17)
[ ] Complete physical soldering and assembly of ESP32, MAX30102, and MPU6050 in a wrist wearable enclosure.

[ ] Establish active BLE GATT bonding with the Flutter mobile application.

[ ] Deploy the FastAPI backend and Hospital Web Dashboard to cloud hosting (AWS / Render).

[ ] Conduct live physical drop tests and vital monitoring during the finale presentation.

 9. Disclaimer
ElderGuard AI is an academic prototype developed for the IoTrix 2.0 competition. It is designed for monitoring assistance and clinical decision support, and is not certified as a medical diagnostic device.
