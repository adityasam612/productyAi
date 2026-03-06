# app.py  ← goes in ai_assistant/ (root folder, NOT inside core/)

import os
import streamlit as st

os.makedirs("data", exist_ok=True)
os.makedirs("data/notes", exist_ok=True)
os.makedirs("exports", exist_ok=True)

from core.tasks import init_db, add_task, get_tasks, complete_task, delete_task
from core.notes import save_note, list_notes, summarize_note, ask_from_note
from core.records import export_weekly_report
from core.ai_helper import ask_ai

# ── Init ─────────────────────────────────────────────────
init_db()
st.set_page_config(page_title="AI Productivity Assistant", page_icon="🧠", layout="wide")
st.title("🧠 AI Productivity Assistant")

# ── Tabs ─────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📋 Tasks", "📝 Notes & AI", "💡 Daily Plan", "📊 Reports"])


# ════════════════════════════════
# TAB 1 — TASKS
# ════════════════════════════════
with tab1:
    st.subheader("Add a Task")
    with st.form("new_task"):
        title    = st.text_input("Task title")
        priority = st.selectbox("Priority", ["high", "medium", "low"])
        due      = st.date_input("Due date")
        submitted = st.form_submit_button("➕ Add Task")
        if submitted and title:
            add_task(title, priority, str(due))
            st.success(f"Task '{title}' added!")

    st.divider()
    st.subheader("Pending Tasks")
    pending = get_tasks(done=0)
    if not pending:
        st.info("No pending tasks. Add one above!")
    for task in pending:
        col1, col2, col3 = st.columns([5, 1, 1])
        col1.write(f"**{task[1]}** — `{task[2]}` priority | due: {task[3] or '—'}")
        if col2.button("✅", key=f"done_{task[0]}"):
            complete_task(task[0])
            st.rerun()
        if col3.button("🗑", key=f"del_{task[0]}"):
            delete_task(task[0])
            st.rerun()

    st.divider()
    st.subheader("Completed Tasks")
    done_tasks = get_tasks(done=1)
    if not done_tasks:
        st.info("Nothing completed yet.")
    for task in done_tasks:
        st.write(f"~~{task[1]}~~ — {task[2]} | due: {task[3] or '—'}")


# ════════════════════════════════
# TAB 2 — NOTES & AI
# ════════════════════════════════
with tab2:
    st.subheader("Save a Note")
    note_name    = st.text_input("Note name (no spaces)", key="nname")
    note_content = st.text_area("Note content", height=150, key="ncontent")
    if st.button("💾 Save Note"):
        if note_name and note_content:
            save_note(note_name, note_content)
            st.success(f"Note '{note_name}' saved!")
        else:
            st.warning("Fill in both fields.")

    st.divider()
    st.subheader("AI — Summarize or Ask")
    notes = list_notes()
    if not notes:
        st.info("No notes yet. Save one above.")
    else:
        selected = st.selectbox("Choose a note", notes)
        col1, col2 = st.columns(2)
        if col1.button("📋 Summarize"):
            with st.spinner("Summarizing..."):
                result = summarize_note(selected)
            st.markdown("**Summary:**")
            st.write(result)
        question = st.text_input("Ask a question about this note")
        if col2.button("❓ Ask AI") and question:
            with st.spinner("Thinking..."):
                result = ask_from_note(selected, question)
            st.markdown("**Answer:**")
            st.write(result)


# ════════════════════════════════
# TAB 3 — DAILY PLAN
# ════════════════════════════════
with tab3:
    st.subheader("Get Your Daily AI Plan")
    if st.button("💡 Generate Daily Plan"):
        tasks = get_tasks(done=0)
        if not tasks:
            st.warning("No pending tasks found. Add tasks first!")
        else:
            task_list = "\n".join([f"- {t[1]} ({t[2]} priority, due {t[3] or 'no date'})" for t in tasks])
            prompt = f"""I have these tasks today:
{task_list}

Please give me:
1. Which task to tackle first and why
2. A realistic time estimate for each task
3. One productivity tip for my day
"""
            with st.spinner("Planning your day..."):
                plan = ask_ai(prompt)
            st.markdown("### 📅 Your Plan")
            st.write(plan)


# ════════════════════════════════
# TAB 4 — REPORTS
# ════════════════════════════════
with tab4:
    st.subheader("Weekly Progress Report")
    st.write("Generate a Word document summarizing your completed and pending tasks.")
    if st.button("📄 Generate Report"):
        with st.spinner("Creating report..."):
            path = export_weekly_report()
        with open(path, "rb") as f:
            st.download_button(
                label="⬇️ Download .docx",
                data=f,
                file_name="weekly_report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        st.success("Report ready!")