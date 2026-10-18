"""
Smart Quiz & Performance Analyzer
PCU B.Tech CSE (AI & ML) Mini Project

Technology : Python 3 + Streamlit (NO Flask, NO backend server, NO database)
Run locally: streamlit run streamlit_app.py
"""

import json
import os
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# 1. PAGE CONFIGURATION  (must be the first Streamlit command)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Smart Quiz & Performance Analyzer",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# 2. QUESTION BANK
#    Loaded from questions.json if that file exists, otherwise the built-in
#    list below is used. This way the app works even without questions.json.
# ---------------------------------------------------------------------------
FALLBACK_QUESTIONS = [
    # ------------------------- PYTHON PROGRAMMING -------------------------
    {"id": 1, "category": "Python Programming",
     "question": "Which keyword is used to define a function in Python?",
     "options": ["function", "def", "fun", "define"], "answer": 1,
     "explanation": "A function in Python is created with the 'def' keyword, e.g. def add(a, b):"},
    {"id": 2, "category": "Python Programming",
     "question": "What is the output of print(type([]))?",
     "options": ["<class 'tuple'>", "<class 'dict'>", "<class 'list'>", "<class 'set'>"], "answer": 2,
     "explanation": "[] creates an empty list, so type([]) is <class 'list'>."},
    {"id": 3, "category": "Python Programming",
     "question": "Which of these data types is immutable in Python?",
     "options": ["list", "dict", "set", "tuple"], "answer": 3,
     "explanation": "A tuple cannot be changed after it is created, so it is immutable."},
    {"id": 4, "category": "Python Programming",
     "question": "What does len('Streamlit') return?",
     "options": ["8", "9", "10", "Error"], "answer": 1,
     "explanation": "'Streamlit' contains 9 characters, so len() returns 9."},
    {"id": 5, "category": "Python Programming",
     "question": "Which module of the standard library is used to work with JSON data?",
     "options": ["json", "jsonify", "pyjson", "simplejson"], "answer": 0,
     "explanation": "The built-in 'json' module encodes and decodes JSON data."},
    {"id": 6, "category": "Python Programming",
     "question": "What is the result of 7 // 2 in Python 3?",
     "options": ["3.5", "3", "4", "3.0"], "answer": 1,
     "explanation": "// is floor division, so 7 // 2 gives the integer 3."},

    # --------------------------- COMPUTER SCIENCE ---------------------------
    {"id": 7, "category": "Computer Science",
     "question": "What is the time complexity of binary search on a sorted array?",
     "options": ["O(n)", "O(n log n)", "O(log n)", "O(1)"], "answer": 2,
     "explanation": "Binary search halves the search space every step, giving O(log n)."},
    {"id": 8, "category": "Computer Science",
     "question": "Which data structure follows the FIFO principle?",
     "options": ["Stack", "Queue", "Tree", "Graph"], "answer": 1,
     "explanation": "A Queue is First In First Out (FIFO); a Stack is LIFO."},
    {"id": 9, "category": "Computer Science",
     "question": "RAM is an example of which type of memory?",
     "options": ["Secondary storage", "Volatile primary memory", "Optical storage", "Read only memory"], "answer": 1,
     "explanation": "RAM is volatile primary memory - its contents are lost when power is off."},
    {"id": 10, "category": "Computer Science",
     "question": "Which protocol transfers web pages securely over the internet?",
     "options": ["FTP", "SMTP", "HTTPS", "TELNET"], "answer": 2,
     "explanation": "HTTPS is HTTP secured with TLS/SSL encryption."},
    {"id": 11, "category": "Computer Science",
     "question": "In machine learning, supervised learning is trained using what kind of data?",
     "options": ["Unlabelled data", "Labelled data", "No data at all", "Only image data"], "answer": 1,
     "explanation": "Supervised learning uses labelled input-output pairs to learn a mapping."},
    {"id": 12, "category": "Computer Science",
     "question": "Which of these is NOT an operating system?",
     "options": ["Linux", "Windows", "Oracle", "macOS"], "answer": 2,
     "explanation": "Oracle is a database company/product, not an operating system."},

    # -------------------------- GENERAL KNOWLEDGE --------------------------
    {"id": 13, "category": "General Knowledge",
     "question": "Who is known as the 'Missile Man of India'?",
     "options": ["Dr. A.P.J. Abdul Kalam", "C.V. Raman", "Homi Bhabha", "Vikram Sarabhai"], "answer": 0,
     "explanation": "Dr. A.P.J. Abdul Kalam earned this title for his work on India's missile programme."},
    {"id": 14, "category": "General Knowledge",
     "question": "Which planet is known as the Red Planet?",
     "options": ["Venus", "Jupiter", "Mars", "Mercury"], "answer": 2,
     "explanation": "Mars looks red because of iron oxide (rust) on its surface."},
    {"id": 15, "category": "General Knowledge",
     "question": "What is the capital city of Australia?",
     "options": ["Sydney", "Melbourne", "Perth", "Canberra"], "answer": 3,
     "explanation": "Canberra is the capital of Australia, not Sydney."},
    {"id": 16, "category": "General Knowledge",
     "question": "The city of Pune is located in which Indian state?",
     "options": ["Gujarat", "Maharashtra", "Karnataka", "Goa"], "answer": 1,
     "explanation": "Pune is a major educational city in the state of Maharashtra."},
    {"id": 17, "category": "General Knowledge",
     "question": "How many continents are there on Earth?",
     "options": ["5", "6", "7", "8"], "answer": 2,
     "explanation": "There are 7 continents on Earth."},
    {"id": 18, "category": "General Knowledge",
     "question": "Which gas do plants mainly absorb during photosynthesis?",
     "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": 2,
     "explanation": "Plants absorb carbon dioxide and release oxygen during photosynthesis."},
]


@st.cache_data
def load_questions():
    """Load questions.json if available, else use the built-in question bank."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.json")
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                return data
    except Exception:
        # If the JSON file is broken we quietly fall back to the built-in list.
        pass
    return FALLBACK_QUESTIONS


ALL_QUESTIONS = load_questions()
CATEGORIES = ["Python Programming", "Computer Science", "General Knowledge"]
OPTION_KEYS = ["A", "B", "C", "D"]

# ---------------------------------------------------------------------------
# 3. CUSTOM CSS (keeps the app readable on mobile and desktop)
# ---------------------------------------------------------------------------
st.markdown("""
<style>
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 860px; }
.hero {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #0891b2 100%);
    color: #ffffff; padding: 28px 26px; border-radius: 18px; margin-bottom: 18px;
}
.hero h1 { color: #ffffff; margin: 6px 0 8px 0; font-size: 2rem; line-height: 1.2; }
.hero p  { color: #e9e9ff; margin: 0; font-size: 0.98rem; }
.tagpill {
    display: inline-block; background: rgba(255,255,255,.18); color: #fff;
    padding: 4px 12px; border-radius: 999px; font-size: 12px; font-weight: 600;
}
.qcard {
    background: #ffffff; border: 1px solid #e5e7eb; border-left: 6px solid #4f46e5;
    border-radius: 14px; padding: 18px 20px; margin-bottom: 10px;
    box-shadow: 0 2px 10px rgba(15,23,42,.06);
}
.qcard h3 { margin: 0; font-size: 1.15rem; color: #111827; line-height: 1.5; }
.catlabel { font-size: 12px; font-weight: 700; color: #4f46e5; letter-spacing: .4px; text-transform: uppercase; }
.rev-ok  { background:#f0fdf4; border-left:6px solid #16a34a; padding:14px 16px; border-radius:12px; margin-bottom:10px; }
.rev-bad { background:#fef2f2; border-left:6px solid #dc2626; padding:14px 16px; border-radius:12px; margin-bottom:10px; }
.rev-ok b, .rev-bad b { color:#111827; }
.rev-small { font-size: 13px; color:#475569; margin-top:4px; }
.footer {
    text-align: center; color: #64748b; font-size: 13px;
    border-top: 1px solid #e2e8f0; margin-top: 34px; padding-top: 14px;
}
div.stButton > button { width: 100%; border-radius: 10px; font-weight: 600; padding: 0.55rem 1rem; }
@media (max-width: 640px) { .hero h1 { font-size: 1.5rem; } .block-container { padding-left: 1rem; padding-right: 1rem; } }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 4. SESSION STATE SETUP
# ---------------------------------------------------------------------------
def init_state():
    defaults = {
        "page": "home",          # home | quiz | result
        "quiz_questions": [],    # list of question dicts for this attempt
        "answers": {},           # {question_id: selected_option_index}
        "current": 0,            # index of the question being shown
        "confirm": False,        # submit confirmation flag
        "selected_cats": CATEGORIES.copy(),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


def start_quiz(categories):
    """Build the question list for the chosen categories and start the quiz."""
    questions = [q for q in ALL_QUESTIONS if q["category"] in categories]
    st.session_state.quiz_questions = questions
    st.session_state.answers = {}
    st.session_state.current = 0
    st.session_state.confirm = False
    st.session_state.selected_cats = categories
    st.session_state.page = "quiz"


def restart_quiz():
    """Clear everything and go back to the home page."""
    for key in ["page", "quiz_questions", "answers", "current", "confirm", "selected_cats"]:
        if key in st.session_state:
            del st.session_state[key]
    init_state()


def calculate_results():
    """Return score, percentage, grade, remark and category-wise statistics."""
    questions = st.session_state.quiz_questions
    answers = st.session_state.answers
    total = len(questions)
    score = 0
    cat_stats = {}

    for q in questions:
        selected = answers.get(q["id"])          # None means not answered -> no marks
        is_correct = (selected is not None and selected == q["answer"])
        if is_correct:
            score += 1
        cat = q["category"]
        cat_stats.setdefault(cat, {"total": 0, "correct": 0})
        cat_stats[cat]["total"] += 1
        if is_correct:
            cat_stats[cat]["correct"] += 1

    percentage = round((score / total) * 100, 2) if total else 0.0

    if percentage >= 80:
        grade, remark = "A", "Excellent performance! Outstanding work."
    elif percentage >= 60:
        grade, remark = "B", "Good job! A little more practice and you will reach an A."
    elif percentage >= 40:
        grade, remark = "C", "Average. Please revise the weaker topics."
    else:
        grade, remark = "D", "Needs improvement. Review the explanations and try again."

    for data in cat_stats.values():
        data["percentage"] = round((data["correct"] / data["total"]) * 100, 2) if data["total"] else 0.0

    return {
        "score": score, "total": total, "percentage": percentage,
        "grade": grade, "remark": remark, "cat_stats": cat_stats,
        "attempted": len([v for v in answers.values() if v is not None]),
    }


def footer():
    st.markdown(
        '<div class="footer">🎓 <b>PCU B.Tech CSE (AI &amp; ML) Mini Project</b><br>'
        'Smart Quiz &amp; Performance Analyzer · Built with Python 3 &amp; Streamlit</div>',
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 5. HOME PAGE
# ---------------------------------------------------------------------------
def page_home():
    st.markdown("""
    <div class="hero">
      <span class="tagpill">PCU · B.Tech CSE (AI &amp; ML) Mini Project</span>
      <h1>🧠 Smart Quiz &amp; Performance Analyzer</h1>
      <p>Attempt multiple-choice questions, get an instant score, percentage, grade,
      category-wise analysis and a full answer review with explanations.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Questions", len(ALL_QUESTIONS))
    c2.metric("Categories", len(CATEGORIES))
    c3.metric("Options / Question", 4)

    st.subheader("📋 Instructions for first-time users")
    st.info(
        "1. Choose one or more categories below.\n"
        "2. Click **Start Quiz**.\n"
        "3. One question is shown at a time with four options.\n"
        "4. Select an option, then use **Next ➡️** / **⬅️ Previous** to move around. "
        "Your answers are saved automatically.\n"
        "5. You may skip a question, but **unanswered questions get 0 marks**.\n"
        "6. On the last question click **Submit Quiz** and confirm.\n"
        "7. View your score, percentage, grade, category chart and answer review.\n"
        "8. Click **Restart Quiz** any time to start again."
    )

    st.subheader("🎯 Select categories")
    chosen = []
    cols = st.columns(3)
    for i, cat in enumerate(CATEGORIES):
        count = len([q for q in ALL_QUESTIONS if q["category"] == cat])
        with cols[i]:
            if st.checkbox(f"{cat} ({count})", value=True, key=f"cat_{i}"):
                chosen.append(cat)

    st.write("")
    if len(chosen) == 0:
        st.error("⚠️ Please select at least one category to begin.")
        st.button("🚀 Start Quiz", disabled=True)
    else:
        total_sel = len([q for q in ALL_QUESTIONS if q["category"] in chosen])
        st.success(f"✅ Ready! {total_sel} question(s) selected from {len(chosen)} category(ies).")
        if st.button("🚀 Start Quiz", type="primary"):
            start_quiz(chosen)
            st.rerun()

    footer()


# ---------------------------------------------------------------------------
# 6. QUIZ PAGE
# ---------------------------------------------------------------------------
def page_quiz():
    questions = st.session_state.quiz_questions
    total = len(questions)

    if total == 0:
        st.warning("No questions available. Please restart.")
        if st.button("🔄 Back to Home"):
            restart_quiz()
            st.rerun()
        return

    idx = max(0, min(st.session_state.current, total - 1))
    st.session_state.current = idx
    q = questions[idx]

    answered = len([v for v in st.session_state.answers.values() if v is not None])
    unanswered = total - answered

    # ---- progress header ----
    st.markdown(f"**Question {idx + 1} of {total}**")
    st.progress((idx + 1) / total)

    m1, m2, m3 = st.columns(3)
    m1.metric("Answered", answered)
    m2.metric("Unanswered", unanswered)
    m3.metric("Progress", f"{round((idx + 1) / total * 100)}%")

    # ---- question card ----
    st.markdown(
        f'<div class="qcard"><div class="catlabel">{q["category"]}</div>'
        f'<h3>Q{idx + 1}. {q["question"]}</h3></div>',
        unsafe_allow_html=True,
    )

    # ---- options (radio keeps the previously chosen answer) ----
    labels = [f"{OPTION_KEYS[i]}.  {opt}" for i, opt in enumerate(q["options"])]
    previous = st.session_state.answers.get(q["id"])

    choice = st.radio(
        "Choose your answer:",
        options=list(range(len(labels))),
        format_func=lambda i: labels[i],
        index=previous if previous is not None else None,
        key=f"radio_q{q['id']}",
    )

    # Save immediately so navigation never loses an answer.
    if choice is not None:
        st.session_state.answers[q["id"]] = choice

    if st.session_state.answers.get(q["id"]) is None:
        st.caption("ℹ️ Not answered yet — unanswered questions score 0 marks.")
    else:
        st.caption("✔️ Answer saved.")

    st.write("")

    # ---- navigation buttons ----
    b1, b2, b3 = st.columns(3)

    with b1:
        if st.button("⬅️ Previous", disabled=(idx == 0)):
            st.session_state.current = idx - 1
            st.rerun()

    with b2:
        if st.button("Next ➡️", disabled=(idx == total - 1)):
            st.session_state.current = idx + 1
            st.rerun()

    with b3:
        if st.button("✅ Submit Quiz", type="primary"):
            st.session_state.confirm = True

    # ---- submit confirmation ----
    if st.session_state.confirm:
        st.warning(
            f"Are you sure you want to submit? You have answered **{answered}** "
            f"of **{total}** questions. Unanswered questions will get 0 marks."
        )
        y, n = st.columns(2)
        with y:
            if st.button("Yes, submit my quiz"):
                st.session_state.confirm = False
                st.session_state.page = "result"
                st.rerun()
        with n:
            if st.button("No, continue the quiz"):
                st.session_state.confirm = False
                st.rerun()

    with st.expander("🔎 Question navigator / jump to a question"):
        nav_cols = st.columns(5)
        for i, item in enumerate(questions):
            mark = "🟢" if st.session_state.answers.get(item["id"]) is not None else "⚪"
            with nav_cols[i % 5]:
                if st.button(f"{mark} {i + 1}", key=f"jump_{item['id']}"):
                    st.session_state.current = i
                    st.rerun()

    st.divider()
    if st.button("🔄 Restart Quiz"):
        restart_quiz()
        st.rerun()

    footer()


# ---------------------------------------------------------------------------
# 7. RESULT PAGE
# ---------------------------------------------------------------------------
def page_result():
    r = calculate_results()
    questions = st.session_state.quiz_questions
    answers = st.session_state.answers

    st.markdown("""
    <div class="hero">
      <span class="tagpill">Performance Report</span>
      <h1>📊 Your Quiz Results</h1>
      <p>Score, percentage, grade and category-wise analysis</p>
    </div>
    """, unsafe_allow_html=True)

    if r["percentage"] >= 60:
        st.success(f"🎉 {r['remark']}")
    elif r["percentage"] >= 40:
        st.warning(f"📘 {r['remark']}")
    else:
        st.error(f"📕 {r['remark']}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Score", f"{r['score']} / {r['total']}")
    c2.metric("Percentage", f"{r['percentage']}%")
    c3.metric("Grade", r["grade"])
    c4.metric("Attempted", f"{r['attempted']} / {r['total']}")

    st.progress(r["percentage"] / 100)
    st.caption("Grade scale → A: 80% and above · B: 60–79.99% · C: 40–59.99% · D: below 40%")

    # ---- category-wise analysis ----
    st.subheader("📈 Category-wise Performance")
    rows = []
    for cat, d in r["cat_stats"].items():
        rows.append({
            "Category": cat,
            "Correct": d["correct"],
            "Total": d["total"],
            "Percentage": d["percentage"],
        })
    df = pd.DataFrame(rows)
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(df.set_index("Category")["Percentage"], height=260)

        best = df.loc[df["Percentage"].idxmax()]
        weak = df.loc[df["Percentage"].idxmin()]
        a, b = st.columns(2)
        a.success(f"💪 Strongest area: **{best['Category']}** ({best['Percentage']}%)")
        b.info(f"📚 Needs practice: **{weak['Category']}** ({weak['Percentage']}%)")

    # ---- answer review ----
    st.subheader("📝 Answer Review")
    filt = st.radio(
        "Show:", ["All", "Correct only", "Incorrect / Unanswered only"],
        horizontal=True, key="review_filter",
    )

    for i, q in enumerate(questions):
        sel = answers.get(q["id"])
        is_correct = (sel is not None and sel == q["answer"])
        if filt == "Correct only" and not is_correct:
            continue
        if filt == "Incorrect / Unanswered only" and is_correct:
            continue

        your_ans = f"{OPTION_KEYS[sel]}. {q['options'][sel]}" if sel is not None else "Not answered"
        right_ans = f"{OPTION_KEYS[q['answer']]}. {q['options'][q['answer']]}"
        css = "rev-ok" if is_correct else "rev-bad"
        tag = "✅ Correct" if is_correct else ("⚪ Not answered" if sel is None else "❌ Incorrect")

        st.markdown(
            f'<div class="{css}">'
            f'<b>Q{i + 1}. {q["question"]}</b><br>'
            f'<span class="rev-small">{tag} &nbsp;|&nbsp; Category: {q["category"]}</span><br>'
            f'<span class="rev-small">Your answer: <b>{your_ans}</b></span><br>'
            f'<span class="rev-small">Correct answer: <b>{right_ans}</b></span><br>'
            f'<span class="rev-small">💡 {q["explanation"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # ---- download report ----
    report_rows = []
    for i, q in enumerate(questions):
        sel = answers.get(q["id"])
        report_rows.append({
            "No": i + 1,
            "Category": q["category"],
            "Question": q["question"],
            "Your Answer": q["options"][sel] if sel is not None else "Not answered",
            "Correct Answer": q["options"][q["answer"]],
            "Result": "Correct" if (sel is not None and sel == q["answer"]) else "Incorrect",
        })
    csv = pd.DataFrame(report_rows).to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download report (CSV)", csv,
                       file_name="smart_quiz_report.csv", mime="text/csv")

    st.divider()
    x, y = st.columns(2)
    with x:
        if st.button("🔁 Retry same categories", type="primary"):
            start_quiz(st.session_state.selected_cats)
            st.rerun()
    with y:
        if st.button("🔄 Restart Quiz (Home)"):
            restart_quiz()
            st.rerun()

    footer()


# ---------------------------------------------------------------------------
# 8. ROUTER
# ---------------------------------------------------------------------------
def main():
    page = st.session_state.page
    if page == "quiz":
        page_quiz()
    elif page == "result":
        page_result()
    else:
        page_home()


main()
