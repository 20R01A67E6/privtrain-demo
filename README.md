# PrivaTrain — Demo Landing Page

A demo site for **PrivaTrain**, a private AI training platform that lets organisations fine-tune AI models on their own sensitive data — without sending that data to any external company or server.

Live site: [privtrain-demo.vercel.app](https://privtrain-demo.vercel.app)

---

## What This Repo Contains

```
privtrain-demo/
├── index.html        # Full frontend — landing page, contact form, interactive pipeline demo
├── server.py         # Python Flask backend — handles contact form submissions via Gmail SMTP
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend hosting | Vercel (free tier) |
| Backend hosting | Render (free tier) |
| Backend framework | Python Flask |
| Email delivery | Gmail SMTP via environment variables |
| Fonts | Google Fonts — Syne + DM Sans |

---

## Local Development

### Frontend
The frontend is a single HTML file with no build step. Open `index.html` directly in a browser to preview it.

### Backend

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root with your credentials:
```
GMAIL_USER=your@gmail.com
GMAIL_PASS=your-16-char-app-password
```

3. Run the server:
```bash
python server.py
```

The backend runs on `http://localhost:5000`. The contact form in `index.html` points to the deployed Render URL — update it to `http://localhost:5000/contact` if you want to test locally.

---

## Deployment

### Frontend — Vercel
- Connect this GitHub repo to Vercel
- Framework preset: **Other**
- Root directory: leave empty
- Build command: leave empty
- Vercel auto-deploys on every push to `main`

### Backend — Render
- Connect this GitHub repo to Render
- Language: **Python**
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn server:app`
- Add environment variables in Render dashboard:
  - `GMAIL_USER` — your Gmail address
  - `GMAIL_PASS` — your Gmail app password (not your real password — generate one at myaccount.google.com → Security → App Passwords)

---

## Environment Variables

Never commit credentials to the repo. All secrets are managed as environment variables on Render.

| Variable | Description |
|---|---|
| `GMAIL_USER` | Gmail address that sends contact form emails |
| `GMAIL_PASS` | Gmail app password (16 characters, no spaces) |

---

## Contact Form Flow

```
Visitor fills form on Vercel site
        │
        │  POST /contact  (JSON)
        ▼
Flask server on Render
        │
        │  Gmail SMTP
        ▼
abhinav.kandula.ae@gmail.com
```

---

## About PrivaTrain

PrivaTrain is a platform where any organisation can download a base AI model, fine-tune it on their own private data, and have it continuously improve itself through an agentic training pipeline — all without their data ever leaving their control.

Built for industries where cloud AI isn't a legal or practical option: healthcare (HIPAA), legal (attorney-client privilege), finance (regulatory compliance), and manufacturing (IP protection).

**Built by:** Abhinav Reddy Kandula  
**Location:** Cincinnati, Ohio  
**Email:** abhinav.kandula.ae@gmail.com  
**LinkedIn:** [linkedin.com/in/kandula-abhinav-reddy](https://www.linkedin.com/in/kandula-abhinav-reddy)  
**GitHub:** [github.com/20R01A67E6](https://github.com/20R01A67E6)
