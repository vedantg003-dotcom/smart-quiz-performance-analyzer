# 🧠 Smart Quiz & Performance Analyzer (Python + Streamlit)

**PCU — B.Tech CSE (AI & ML) Mini Project**

A complete multiple-choice quiz web application built **only with Python 3 and Streamlit**.
There is **no Flask, no Node.js, no database, no API key and no separate backend server**.

> **Main file for Streamlit Cloud:** `streamlit_app.py`
> **Run command:** `streamlit run streamlit_app.py`

---

## ✨ Features

| # | Feature |
|---|---------|
| 1 | Attractive home page with project title, introduction and instructions |
| 2 | Category selection (Python Programming, Computer Science, General Knowledge) |
| 3 | **Start Quiz** button |
| 4 | 18 MCQs (6 per category), 4 options each, one correct answer |
| 5 | One question shown at a time inside a clean card |
| 6 | **⬅️ Previous** and **Next ➡️** navigation — answers are never lost |
| 7 | Radio-button answer selection |
| 8 | Progress bar + "Question X of Y" indicator |
| 9 | Live **Answered / Unanswered** counts and a question navigator (🟢 / ⚪) |
| 10 | **Submit Quiz** with a Yes/No confirmation step |
| 11 | Score out of total, percentage, grade (A/B/C/D) |
| 12 | Category-wise performance table + bar chart + strongest/weakest topic |
| 13 | Answer review with ✅ / ❌ / ⚪ indicators, correct answer and explanation |
| 14 | Review filter: All / Correct only / Incorrect & Unanswered only |
| 15 | Download result report as CSV |
| 16 | **Restart Quiz** and **Retry same categories** buttons |
| 17 | Responsive layout for desktop and mobile |
| 18 | Professional footer: *PCU B.Tech CSE (AI & ML) Mini Project* |

**Grading scale:** A = 80% and above · B = 60–79.99% · C = 40–59.99% · D = below 40%
**Unanswered questions always score 0 marks.**

---

## 📁 Project files (these go in the GitHub repository root)

```
smart-quiz-performance-analyzer/
├── streamlit_app.py     ← MAIN FILE (Streamlit entry point)
├── requirements.txt     ← dependencies
├── questions.json       ← optional question bank (app works without it too)
├── README.md
├── .gitignore
└── LICENSE
```

> ⚠️ If your folder still contains old Flask files (`app.py`, `Procfile`, `render.yaml`,
> `templates/`, `static/`, `index.html`), **delete them** before uploading. They are not
> used by Streamlit. Only the 6 files listed above are needed.

---

## 💻 Run on Windows (beginner-friendly, step by step)

1. **Install Python 3** from <https://www.python.org/downloads/>.
   On the first install screen, tick ✅ **"Add Python to PATH"**, then click *Install Now*.
2. Put all project files in a folder, for example `C:\Users\YourName\Desktop\smart-quiz`.
3. Open the **Command Prompt** (press `Windows key`, type `cmd`, press Enter).
4. Go into your folder:
   ```
   cd C:\Users\YourName\Desktop\smart-quiz
   ```
5. (Recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
6. Install the packages:
   ```
   pip install -r requirements.txt
   ```
7. Start the app:
   ```
   streamlit run streamlit_app.py
   ```
8. Your browser opens automatically at **http://localhost:8501**.
   If it does not open, copy that address into Chrome.
9. To stop the app, click on the Command Prompt window and press `Ctrl + C`.

---

## 🐙 Step-by-step: upload to GitHub

1. Download and extract the project folder.
2. Go to <https://github.com> and sign in (create a free account if needed).
3. Click **+** (top right) → **New repository**.
4. Repository name: **`smart-quiz-performance-analyzer`**
5. Select **Public**. Do **not** tick "Add a README file" (you already have one).
6. Click **Create repository**.
7. On the next page click **uploading an existing file**.
8. Drag and drop these files: `streamlit_app.py`, `requirements.txt`, `questions.json`,
   `README.md`, `.gitignore`, `LICENSE`.
   👉 Drop the **files themselves**, not the outer folder, so they sit at the repo root.
9. Type a commit message such as `Smart Quiz Streamlit mini project` and click **Commit changes**.
10. Check the repository home page — you must **see `streamlit_app.py` and `requirements.txt`
    in the file list at the root**. If they are inside a sub-folder, the deployment will fail.

**Optional (using Git commands instead):**
```bash
git init
git add .
git commit -m "Smart Quiz & Performance Analyzer - Streamlit"
git branch -M main
git remote add origin https://github.com/<your-username>/smart-quiz-performance-analyzer.git
git push -u origin main
```

---

## ☁️ Step-by-step: deploy on Streamlit Community Cloud

1. Download and extract the generated project folder.
2. Create a public GitHub repository named **`smart-quiz-performance-analyzer`**.
3. Upload the contents of the project folder to the repository **root**.
4. Confirm that **`streamlit_app.py`** and **`requirements.txt`** are visible at the root
   of the GitHub repository.
5. Visit <https://share.streamlit.io/>
6. Sign in using **GitHub** and authorise Streamlit to read your repositories.
7. Click **“Create app”** (choose *“Deploy a public app from GitHub”* if asked).
8. In **Repository**, select `your-username/smart-quiz-performance-analyzer`.
9. In **Branch**, select **`main`**.
10. In **Main file path**, enter exactly: **`streamlit_app.py`**
11. Click **“Deploy”**.
12. Wait 1–3 minutes while it installs the packages, then copy the generated public URL
    (it looks like `https://smart-quiz-performance-analyzer-xxxxx.streamlit.app`).

Every time you push a change to `main`, Streamlit Cloud redeploys automatically.

### 📌 Which file is the "main file"?
**`streamlit_app.py`** — nothing else. It must be typed exactly, lower-case, with the
`.py` extension, and it must be at the repository root (no folder name in front of it).

---

## 🛠️ Troubleshooting

**“This file does not exist” / “Main module not found”**
- The main file path is wrong. It must be `streamlit_app.py`, not `/streamlit_app.py`,
  not `app.py`, not `src/streamlit_app.py`.
- Open your GitHub repo and check the file is really at the root and spelled correctly
  (GitHub is case-sensitive: `Streamlit_App.py` ≠ `streamlit_app.py`).
- Click **Manage app → Settings → Main file path**, fix it, then **Reboot app**.

**Missing Python packages (`ModuleNotFoundError: No module named 'pandas'`)**
- `requirements.txt` is missing, misspelled (`requirement.txt` is wrong) or not at the root.
- Add the missing package name on its own line, commit, then **Reboot app**.
- Do not add `flask` or `gunicorn` — they are not needed.

**Syntax errors (`SyntaxError`, `IndentationError`)**
- The log shows the file name and line number. Open that line on GitHub and fix the
  indentation/bracket, commit, and the app redeploys.
- Test locally first with: `python -m py_compile streamlit_app.py` (no output = no syntax error).

**Incorrect repository or branch**
- If your repo's default branch is `master`, choose `master` instead of `main`.
- The repository must be **public**, or you must grant Streamlit private-repo access.

**App startup failures / “Oh no. Error running app.”**
- Click **Manage app** (bottom-right) and read the red error in the log.
- Common causes: wrong file path, missing package, or a typo in the code.
- Try **Reboot app** from the app menu (⋮ → Reboot).

**Reading Streamlit Cloud logs**
- Open your app → bottom-right **Manage app** → the terminal panel shows the full
  build and runtime log. Scroll to the first red line — that is the real error.

**App is "sleeping"**
- Free apps sleep after inactivity. Just open the URL and click **“Yes, get this app back up!”**.

---

## ✅ Testing checklist

Tick each item after you run the app:

- [ ] Home page opens with title, metrics and instructions
- [ ] All three category checkboxes work; unticking all shows an error and disables Start
- [ ] **Start Quiz** opens Question 1 of N
- [ ] Each question shows exactly 4 radio options (A–D)
- [ ] Selecting an option shows “✔️ Answer saved.”
- [ ] **Next ➡️** moves forward; **⬅️ Previous** moves back and the earlier answer is still selected
- [ ] Previous is disabled on the first question; Next is disabled on the last question
- [ ] Answered / Unanswered counters update correctly
- [ ] Question navigator jumps to any question (🟢 = answered, ⚪ = unanswered)
- [ ] **Submit Quiz** asks for confirmation; “No” returns to the quiz
- [ ] Score equals the number of correct answers; skipped questions give 0
- [ ] Percentage = score ÷ total × 100 (e.g. 12/18 → 66.67%)
- [ ] Grade boundaries: 80%→A, 60%→B, 40%→C, 39%→D
- [ ] Category table and bar chart show correct per-category percentages
- [ ] Review shows ✅ / ❌ / ⚪, your answer, correct answer and explanation
- [ ] Review filter (All / Correct / Incorrect) works
- [ ] CSV report downloads
- [ ] **Restart Quiz** clears everything and returns to the home page
- [ ] Works on a mobile screen (narrow browser window)

---

## 🧰 Technology used

- Python 3.11+
- Streamlit (UI, routing, `st.session_state`, charts)
- Pandas (results table + CSV report)
- No Flask · No Gunicorn · No database · No API keys

## 👤 Author
`<Your Name>` — B.Tech CSE (AI & ML), Pimpri Chinchwad University (PCU)

## 📄 License
MIT — see `LICENSE`.
