---

# 🚀 AI Career Coach: Personalized Career and Skills Advisor

<p align="center">
  <strong>Stop guessing. Start building. AI-powered career roadmaps that turn your ambition into achievement.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Live-brightgreen.svg"/>
  <img src="https://img.shields.io/badge/AI-Google%20Gemini%202.5-4285F4.svg"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688.svg"/>
  <img src="https://img.shields.io/badge/Frontend-Vanilla%20JS-F7DF1E.svg"/>
  <img src="https://img.shields.io/badge/Database-Firebase-FFCA28.svg"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</p>

---
## 🌐 Live Demo

> 🚀 **[https://ai-career-coach-hackwins.vercel.app](https://ai-career-coach-hackwins.vercel.app)**
> *(Backend runs on Render free tier — first request may take ~30s)*

> ## 🎥 Demo Video
> 👉 https://drive.google.com/file/d/1uynJ8xppnPfLWKQBMB2Qij0BaHKSGLz-/view?usp=sharing

---

## ► The Problem: The Career Maze

Students and professionals struggle with generic career advice, static roadmaps, unclear interview feedback, and portfolios that fail to communicate real capability. Most tools do not adapt as the user grows, leading to wasted effort and slow progress.

---

## ► Our Solution: An Adaptive AI Career System

**AI Career Coach** is an end-to-end AI-driven platform that continuously adapts to the user’s progress. It combines **dynamic career planning, resume optimization, interview intelligence, portfolio evaluation, and job matching** into a single evolving system.

---

## ✨ Key Capabilities

### 🗺️ Dynamic & Personalized Career Roadmap

* Generates **3 / 6 / 12-month roadmaps**
* Tailored to:

  * Target role
  * Current skill level
  * Experience
  * Time availability
* **Dynamically adapts** based on:

  * Task completion
  * Skill assessment results
  * Interview performance
  * Resume and portfolio quality
* Roadmap updates automatically as the user progresses
  *(Not a static plan — it evolves with the user)*

---

### 📄 Resume & LinkedIn Optimization

* ATS compatibility scoring
* Role-specific keyword optimization
* Bullet point rewriting with quantified impact

---

### 🧩 Skill Gap Analysis

* Compares current skills with real job requirements
* Identifies exact missing competencies
* Injects missing skills directly into the roadmap

---

### 💼 Intelligent Job Matching

* Powered by **Adzuna Jobs API**
* Matches top **7 relevant job openings**
* Based on skills, experience, role fit, and location

---

### 🎙️ AI Mock Interviews

* Domain-specific interview questions
* Video response recording
* Instant AI feedback and follow-up questions
* Performance analysis (clarity, confidence, depth)

---

### 📧 Email-Based Interview Feedback & Smart Scheduling

* Post-interview **detailed feedback emails**
* Highlights strengths, weak areas, and improvement steps
* Personalized preparation suggestions for upcoming interviews
* Acts as a continuous post-interview mentor
* Automatically pushes:
  * Follow-ups to **Google Tasks**
  * Interview prep & reminders to **Google Calendar**
* Ensures no missed deadlines or interview steps

---

### 🤖 24/7 AI Career Mentor

* Always-available AI assistant
* “I’m stuck” support for roadmap, skills, and decisions
* Context-aware and goal-driven guidance

---

### 📊 AI Portfolio Rater (Google Vision)

* Upload portfolio screenshots or website links
* Uses **Google Vision AI** to analyze:

  * Visual layout and hierarchy
  * UI consistency and clarity
  * Professional presentation quality
* Combines visual analysis with **technical project depth**
---

### 🛠️ AI Portfolio Generator (Auto-Deployed)

* Generates:

  * Portfolio structure
  * Project descriptions
  * Tech stack sections
  * About and achievements
* Automatically deploys to **GitHub Pages**

---
### 📈 Market Trend & Skill Demand Analysis

* Uses **Google Trends API** and **BigQuery**
* Analyzes long-term market demand for skills and roles
* Identifies:
  * Rising skills
  * Declining / saturated skills
* Injects trending skills directly into:
  * Career roadmap
  * Skill gap analysis
  * Resume and portfolio recommendations

## 🛠️ Tech Stack

| Layer          | Technology                     |
| -------------- | ------------------------------ |
| AI / LLM       | Google Gemini 2.5 Flash        |
| Vision AI      | Google Vision API              |
| Backend        | Python, FastAPI                |
| Frontend       | HTML, CSS, Vanilla JS          |
| Database       | Firebase Firestore             |
| Authentication | Google OAuth 2.0               |
| Jobs API       | Adzuna                         |
| Email          | Email APIs                     |
|Trends          | Google Trends API, BigQuery    |
|Automation      |Google Tasks and Google Calender|
| Deployment     | Render (Backend), Vercel       |

---

## 🧱 System Architecture

```
User
 ↓
Frontend (HTML / CSS / JS + OAuth)
 ↓
FastAPI Backend
 ├── Gemini AI (Roadmaps, Resume, Interviews)
 ├── Dynamic Roadmap Engine (Progress-aware)
 ├── Portfolio Analysis (Google Vision)
 ├── Email Feedback + Tasks & Calendar Sync
 ├── Market Trend Analyzer (BigQuery + Trends)
 ├── Job Matching (Adzuna)
 └── Firebase Firestore

```
---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/GenAI_hack.git
cd GenAI_hack
```

### Backend

```bash
cd Backend
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd Frontend
python -m http.server 8080
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

