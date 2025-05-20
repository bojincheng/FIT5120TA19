```markdown
# Water Wise Family 
An interactive web platform promoting water safety awareness for Australian families, especially those from immigrant backgrounds. Built as part of the FIT5120 project, this system empowers users to assess beach, pool, and river risks in real-time through AI detection, live data, and educational simulations.

---

## Features

- Real-time beach conditions with rip current detection
- Pool safety regulation checker by postcode
- River safety awareness through interactive content
- Upload or capture images to detect rip currents using AI (Roboflow)
- Historical drowning data search and comparison
- Multilingual and mobile-friendly UI

---

## Tech Stack

- **Frontend**: Vue.js 3 + Netlify
- **Backend**: Flask (Python) + Render
- **Database**: PostgreSQL (Google Cloud SQL)
- **AI Integration**: Roboflow (Rip Current Detection API)
- **Version Control**: Git + GitHub

---

````

---

## Getting Started

### Frontend (Vue)

```bash
npm install
npm run dev
````

### Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Database (PostgreSQL)

* Use pgAdmin / Google Cloud SQL
* Configure credentials in `.env`
* Run connection test: `http://localhost:5000/test-db-connection`

---

## AI Rip Current Detection

* Upload or capture images to detect rip currents via Roboflow
* Adjustable confidence & overlap thresholds
* Endpoint: `https://detect.roboflow.com/rip-currents/3`

---

## Hosting Setup

| Component | Service          |
| --------- | ---------------- |
| Frontend  | Netlify          |
| Backend   | Render           |
| DB        | Google Cloud SQL |

---

## 🛠 Troubleshooting

*  *Vue module error?* Add `netlify.toml` to root
*  *PostgreSQL connection issue?* Check user role & credentials
*  *Page not found?* Ensure build settings + retry deploy on Netlify

---

## Security Notes

* Roboflow API key stored in `.env` (never exposed to frontend)
* Image uploads sanitized and limited to 50MB
* CORS enabled for frontend-backend communication

---

## Future Enhancements

* Offline AI support
* Historical safety heatmaps by location
* Model comparison & user feedback system

---

## License

MIT License | Developed for Monash FIT5120 IE Project

---
