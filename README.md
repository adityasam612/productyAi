<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>AI Personal Productivity Assistant — Project Roadmap</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet"/>
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --card: #16161f;
    --border: #2a2a3a;
    --accent1: #7fff6a;
    --accent2: #5b8fff;
    --accent3: #ff6a8a;
    --accent4: #ffbe6a;
    --text: #e8e8f0;
    --muted: #7070a0;
    --font-head: 'Syne', sans-serif;
    --font-mono: 'Space Mono', monospace;
    --font-body: 'DM Mono', monospace;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 14px;
    line-height: 1.75;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Background grid */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(91,143,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(91,143,255,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrapper { position: relative; z-index: 1; max-width: 960px; margin: 0 auto; padding: 60px 24px 100px; }

  /* Header */
  .hero {
    text-align: center;
    padding: 60px 0 80px;
    position: relative;
  }
  .hero-tag {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent1);
    border: 1px solid var(--accent1);
    padding: 4px 14px;
    border-radius: 2px;
    margin-bottom: 28px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.1s forwards;
  }
  .hero h1 {
    font-family: var(--font-head);
    font-size: clamp(36px, 6vw, 68px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.02em;
    margin-bottom: 20px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.25s forwards;
  }
  .hero h1 span { color: var(--accent1); }
  .hero p {
    color: var(--muted);
    font-size: 15px;
    max-width: 520px;
    margin: 0 auto 40px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.4s forwards;
  }

  /* Tech stack pills */
  .stack-row {
    display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;
    opacity: 0; animation: fadeUp 0.6s ease 0.55s forwards;
  }
  .pill {
    font-family: var(--font-mono);
    font-size: 11px;
    padding: 5px 14px;
    border-radius: 99px;
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    letter-spacing: 0.05em;
  }
  .pill.green { border-color: var(--accent1); color: var(--accent1); }
  .pill.blue  { border-color: var(--accent2); color: var(--accent2); }
  .pill.pink  { border-color: var(--accent3); color: var(--accent3); }
  .pill.gold  { border-color: var(--accent4); color: var(--accent4); }

  /* Section label */
  .section-label {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  /* Phase cards */
  .phases { display: flex; flex-direction: column; gap: 48px; margin-bottom: 64px; }

  .phase {
    opacity: 0;
    transform: translateY(24px);
    animation: fadeUp 0.55s ease forwards;
  }
  .phase:nth-child(1) { animation-delay: 0.1s; }
  .phase:nth-child(2) { animation-delay: 0.2s; }
  .phase:nth-child(3) { animation-delay: 0.3s; }
  .phase:nth-child(4) { animation-delay: 0.4s; }
  .phase:nth-child(5) { animation-delay: 0.5s; }

  .phase-header {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    margin-bottom: 20px;
  }
  .phase-num {
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 4px;
    min-width: 64px;
    text-align: center;
    flex-shrink: 0;
    margin-top: 4px;
  }
  .num-1 { background: rgba(127,255,106,0.1); color: var(--accent1); border: 1px solid rgba(127,255,106,0.3); }
  .num-2 { background: rgba(91,143,255,0.1); color: var(--accent2); border: 1px solid rgba(91,143,255,0.3); }
  .num-3 { background: rgba(255,106,138,0.1); color: var(--accent3); border: 1px solid rgba(255,106,138,0.3); }
  .num-4 { background: rgba(255,190,106,0.1); color: var(--accent4); border: 1px solid rgba(255,190,106,0.3); }
  .num-5 { background: rgba(180,100,255,0.1); color: #c06aff; border: 1px solid rgba(180,100,255,0.3); }

  .phase-title-wrap { flex: 1; }
  .phase-title {
    font-family: var(--font-head);
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
  }
  .phase-subtitle { color: var(--muted); font-size: 13px; }

  /* Steps grid */
  .steps { display: flex; flex-direction: column; gap: 2px; }

  .step {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px 24px;
    transition: border-color 0.2s, background 0.2s;
    position: relative;
    overflow: hidden;
  }
  .step:hover { border-color: #3a3a5a; background: #1a1a24; }
  .step::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
  }
  .step.c1::before { background: var(--accent1); }
  .step.c2::before { background: var(--accent2); }
  .step.c3::before { background: var(--accent3); }
  .step.c4::before { background: var(--accent4); }
  .step.c5::before { background: #c06aff; }

  .step-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 8px;
  }
  .step-name {
    font-family: var(--font-head);
    font-size: 15px;
    font-weight: 600;
  }
  .step-tags { display: flex; gap: 6px; flex-wrap: wrap; }
  .step-tag {
    font-family: var(--font-mono);
    font-size: 9px;
    letter-spacing: 0.08em;
    padding: 2px 8px;
    border-radius: 2px;
    background: rgba(255,255,255,0.05);
    color: var(--muted);
    text-transform: uppercase;
  }

  .step-desc { color: var(--muted); font-size: 13px; margin-bottom: 12px; }

  /* Code block */
  .codeblock {
    background: #0d0d14;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 14px 18px;
    font-family: var(--font-mono);
    font-size: 12px;
    color: #b0b0d0;
    overflow-x: auto;
    margin: 10px 0;
    position: relative;
  }
  .codeblock .comment { color: #404060; }
  .codeblock .kw { color: var(--accent2); }
  .codeblock .str { color: var(--accent1); }
  .codeblock .fn { color: var(--accent3); }
  .codeblock .num { color: var(--accent4); }

  /* Learn box */
  .learn-box {
    background: rgba(127,255,106,0.04);
    border: 1px dashed rgba(127,255,106,0.2);
    border-radius: 6px;
    padding: 12px 16px;
    margin-top: 12px;
  }
  .learn-box-title {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent1);
    margin-bottom: 6px;
  }
  .learn-box p { font-size: 12px; color: var(--muted); }

  /* Checklist */
  .checklist { list-style: none; margin: 8px 0; }
  .checklist li {
    font-size: 12.5px;
    color: var(--muted);
    padding: 3px 0;
    padding-left: 20px;
    position: relative;
  }
  .checklist li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--border);
    font-size: 11px;
  }

  /* Summary table */
  .summary-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 12px;
    font-size: 12.5px;
  }
  .summary-table th {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    text-align: left;
    padding: 8px 12px;
    border-bottom: 1px solid var(--border);
  }
  .summary-table td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.03);
    vertical-align: top;
    color: var(--muted);
  }
  .summary-table td:first-child { color: var(--text); font-weight: 600; }
  .summary-table tr:hover td { background: rgba(255,255,255,0.02); }

  /* Final card */
  .finale {
    background: linear-gradient(135deg, rgba(127,255,106,0.06), rgba(91,143,255,0.06));
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    margin-top: 64px;
  }
  .finale h2 {
    font-family: var(--font-head);
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 12px;
  }
  .finale p { color: var(--muted); max-width: 420px; margin: 0 auto 24px; font-size: 13px; }
  .finale-row { display: flex; justify-content: center; gap: 32px; flex-wrap: wrap; margin-top: 16px; }
  .finale-stat { text-align: center; }
  .finale-stat .val {
    font-family: var(--font-mono);
    font-size: 28px;
    font-weight: 700;
    color: var(--accent1);
    display: block;
  }
  .finale-stat .lbl { font-size: 11px; color: var(--muted); letter-spacing: 0.1em; text-transform: uppercase; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 600px) {
    .phase-header { flex-direction: column; gap: 12px; }
    .finale { padding: 28px 20px; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-tag">Project-Based Learning · Python + AI</div>
    <h1>Build Your <span>AI Productivity</span><br/>Assistant</h1>
    <p>A complete step-by-step roadmap. Every phase teaches real skills while building something you'll actually use every day.</p>
    <div class="stack-row">
      <span class="pill green">Python 3.11+</span>
      <span class="pill blue">OpenAI API</span>
      <span class="pill blue">LangChain</span>
      <span class="pill pink">Streamlit</span>
      <span class="pill gold">SQLite</span>
      <span class="pill gold">python-docx</span>
      <span class="pill">JSON / File I/O</span>
      <span class="pill">NLP</span>
    </div>
  </div>

  <!-- PHASE 1 -->
  <div class="section-label">Phase 01</div>
  <div class="phases">
    <div class="phase">
      <div class="phase-header">
        <div class="phase-num num-1">PHASE 1</div>
        <div class="phase-title-wrap">
          <div class="phase-title">Setup & Project Foundation</div>
          <div class="phase-subtitle">Environment, folder structure, and your first Python file</div>
        </div>
      </div>
      <div class="steps">

        <div class="step c1">
          <div class="step-top">
            <div class="step-name">Step 1 — Install Python & create a virtual environment</div>
            <div class="step-tags"><span class="step-tag">Python</span><span class="step-tag">Terminal</span></div>
          </div>
          <div class="step-desc">Virtual environments keep your project's libraries separate from your system Python. Think of it as a clean room for your project.</div>
          <div class="codeblock"><span class="comment"># Install Python 3.11+ from python.org, then:</span>
<span class="kw">python</span> -m venv venv
<span class="comment"># Activate it:</span>
<span class="comment"># Windows:</span>  venv\Scripts\activate
<span class="comment"># Mac/Linux:</span> source venv/bin/activate</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Virtual environments, pip, and why dependency isolation matters in real projects.</p>
          </div>
        </div>

        <div class="step c1">
          <div class="step-top">
            <div class="step-name">Step 2 — Install all libraries at once</div>
            <div class="step-tags"><span class="step-tag">pip</span></div>
          </div>
          <div class="codeblock"><span class="kw">pip</span> install openai langchain streamlit python-docx sqlite3 schedule rich</div>
          <div class="step-desc">Each library has a job: <strong>openai</strong> talks to GPT, <strong>streamlit</strong> makes the UI, <strong>python-docx</strong> writes Word docs, <strong>rich</strong> makes your terminal pretty, <strong>schedule</strong> runs reminders.</div>
        </div>

        <div class="step c1">
          <div class="step-top">
            <div class="step-name">Step 3 — Create your project folder structure</div>
            <div class="step-tags"><span class="step-tag">File I/O</span></div>
          </div>
          <div class="codeblock">ai_assistant/
├── app.py              <span class="comment"># Streamlit UI (main entry point)</span>
├── core/
│   ├── tasks.py        <span class="comment"># Task management logic</span>
│   ├── notes.py        <span class="comment"># Notes & summarizer</span>
│   ├── ai_helper.py    <span class="comment"># All OpenAI/LangChain calls</span>
│   └── records.py      <span class="comment"># Doc export & progress tracking</span>
├── data/
│   ├── tasks.db        <span class="comment"># SQLite database (auto-created)</span>
│   └── notes/          <span class="comment"># Raw note text files</span>
├── exports/            <span class="comment"># Word docs saved here</span>
├── .env                <span class="comment"># Your API keys (NEVER commit this!)</span>
└── requirements.txt</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>How professional Python projects are structured. Separation of concerns — UI, logic, and data stay in different files.</p>
          </div>
        </div>

        <div class="step c1">
          <div class="step-top">
            <div class="step-name">Step 4 — Securely store your OpenAI API key</div>
            <div class="step-tags"><span class="step-tag">Security</span><span class="step-tag">.env</span></div>
          </div>
          <div class="codeblock"><span class="comment"># .env file (never push to GitHub!)</span>
OPENAI_API_KEY=sk-...your-key-here...

<span class="comment"># In Python, load it like this:</span>
<span class="kw">from</span> dotenv <span class="kw">import</span> load_dotenv
<span class="kw">import</span> os
load_dotenv()
api_key = os.getenv(<span class="str">"OPENAI_API_KEY"</span>)</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Environment variables, the python-dotenv library, and a critical security habit every developer needs.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- PHASE 2 -->
    <div class="section-label">Phase 02</div>
    <div class="phase">
      <div class="phase-header">
        <div class="phase-num num-2">PHASE 2</div>
        <div class="phase-title-wrap">
          <div class="phase-title">Task Manager with SQLite</div>
          <div class="phase-subtitle">Add, complete, and delete tasks — saved to a real database</div>
        </div>
      </div>
      <div class="steps">

        <div class="step c2">
          <div class="step-top">
            <div class="step-name">Step 5 — Create the SQLite database and tasks table</div>
            <div class="step-tags"><span class="step-tag">SQLite</span><span class="step-tag">Databases</span></div>
          </div>
          <div class="step-desc">SQLite is a lightweight database built into Python — no setup needed. Perfect for local apps.</div>
          <div class="codeblock"><span class="comment"># core/tasks.py</span>
<span class="kw">import</span> sqlite3
<span class="kw">from</span> datetime <span class="kw">import</span> datetime

<span class="kw">def</span> <span class="fn">init_db</span>():
    conn = sqlite3.connect(<span class="str">"data/tasks.db"</span>)
    cursor = conn.cursor()
    cursor.execute(<span class="str">"""
        CREATE TABLE IF NOT EXISTS tasks (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT NOT NULL,
            priority  TEXT DEFAULT 'medium',
            due_date  TEXT,
            done      INTEGER DEFAULT 0,
            created   TEXT
        )
    """</span>)
    conn.commit()
    conn.close()</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>SQL basics: CREATE TABLE, data types, primary keys. How Python talks to databases using sqlite3.</p>
          </div>
        </div>

        <div class="step c2">
          <div class="step-top">
            <div class="step-name">Step 6 — CRUD operations (Add, View, Complete, Delete)</div>
            <div class="step-tags"><span class="step-tag">CRUD</span><span class="step-tag">SQL</span></div>
          </div>
          <div class="codeblock"><span class="kw">def</span> <span class="fn">add_task</span>(title, priority=<span class="str">"medium"</span>, due_date=<span class="kw">None</span>):
    conn = sqlite3.connect(<span class="str">"data/tasks.db"</span>)
    conn.execute(<span class="str">"INSERT INTO tasks (title, priority, due_date, created) VALUES (?,?,?,?)"</span>,
                 (title, priority, due_date, datetime.now().isoformat()))
    conn.commit(); conn.close()

<span class="kw">def</span> <span class="fn">get_tasks</span>(done=<span class="num">0</span>):
    conn = sqlite3.connect(<span class="str">"data/tasks.db"</span>)
    rows = conn.execute(<span class="str">"SELECT * FROM tasks WHERE done=? ORDER BY priority"</span>, (done,)).fetchall()
    conn.close(); <span class="kw">return</span> rows

<span class="kw">def</span> <span class="fn">complete_task</span>(task_id):
    conn = sqlite3.connect(<span class="str">"data/tasks.db"</span>)
    conn.execute(<span class="str">"UPDATE tasks SET done=1 WHERE id=?"</span>, (task_id,))
    conn.commit(); conn.close()</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>The 4 fundamental database operations every app uses. Parameterized queries to prevent SQL injection.</p>
          </div>
        </div>

        <div class="step c2">
          <div class="step-top">
            <div class="step-name">Step 7 — Build the Task UI in Streamlit</div>
            <div class="step-tags"><span class="step-tag">Streamlit</span><span class="step-tag">UI</span></div>
          </div>
          <div class="codeblock"><span class="comment"># app.py</span>
<span class="kw">import</span> streamlit <span class="kw">as</span> st
<span class="kw">from</span> core.tasks <span class="kw">import</span> add_task, get_tasks, complete_task

st.title(<span class="str">"🧠 AI Productivity Assistant"</span>)

<span class="kw">with</span> st.form(<span class="str">"new_task"</span>):
    title    = st.text_input(<span class="str">"Task"</span>)
    priority = st.selectbox(<span class="str">"Priority"</span>, [<span class="str">"high"</span>, <span class="str">"medium"</span>, <span class="str">"low"</span>])
    due      = st.date_input(<span class="str">"Due date"</span>)
    <span class="kw">if</span> st.form_submit_button(<span class="str">"Add Task"</span>) <span class="kw">and</span> title:
        add_task(title, priority, str(due))
        st.success(<span class="str">"Task added!"</span>)

<span class="comment"># Show tasks as checkboxes</span>
<span class="kw">for</span> task <span class="kw">in</span> get_tasks():
    col1, col2 = st.columns([<span class="num">5</span>, <span class="num">1</span>])
    col1.write(<span class="str">f"**{task[1]}** — {task[2]}"</span>)
    <span class="kw">if</span> col2.button(<span class="str">"✓"</span>, key=task[<span class="num">0</span>]):
        complete_task(task[<span class="num">0</span>]); st.rerun()</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Streamlit's reactive model — the whole script reruns when something changes. Forms, columns, buttons, state management.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- PHASE 3 -->
    <div class="section-label">Phase 03</div>
    <div class="phase">
      <div class="phase-header">
        <div class="phase-num num-3">PHASE 3</div>
        <div class="phase-title-wrap">
          <div class="phase-title">AI Features — Summarize & Q&A</div>
          <div class="phase-subtitle">Plug in OpenAI to make your notes smart</div>
        </div>
      </div>
      <div class="steps">

        <div class="step c3">
          <div class="step-top">
            <div class="step-name">Step 8 — Connect to OpenAI and write your first AI call</div>
            <div class="step-tags"><span class="step-tag">OpenAI API</span><span class="step-tag">LLM</span></div>
          </div>
          <div class="step-desc">The OpenAI API works like a text-in, text-out function. You send a "message" and get a reply from GPT.</div>
          <div class="codeblock"><span class="comment"># core/ai_helper.py</span>
<span class="kw">from</span> openai <span class="kw">import</span> OpenAI
<span class="kw">import</span> os

client = OpenAI(api_key=os.getenv(<span class="str">"OPENAI_API_KEY"</span>))

<span class="kw">def</span> <span class="fn">ask_ai</span>(prompt: str, system: str = <span class="str">"You are a helpful productivity assistant."</span>) -> str:
    response = client.chat.completions.create(
        model=<span class="str">"gpt-4o-mini"</span>,   <span class="comment"># cheap & fast</span>
        messages=[
            {<span class="str">"role"</span>: <span class="str">"system"</span>,  <span class="str">"content"</span>: system},
            {<span class="str">"role"</span>: <span class="str">"user"</span>,    <span class="str">"content"</span>: prompt}
        ]
    )
    <span class="kw">return</span> response.choices[<span class="num">0</span>].message.content</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>How LLMs work via API calls. The system/user message structure. Model selection and cost awareness.</p>
          </div>
        </div>

        <div class="step c3">
          <div class="step-top">
            <div class="step-name">Step 9 — Build the Note Summarizer</div>
            <div class="step-tags"><span class="step-tag">NLP</span><span class="step-tag">File I/O</span></div>
          </div>
          <div class="codeblock"><span class="comment"># core/notes.py</span>
<span class="kw">from</span> core.ai_helper <span class="kw">import</span> ask_ai
<span class="kw">import</span> os, pathlib

<span class="kw">def</span> <span class="fn">save_note</span>(name: str, content: str):
    pathlib.Path(<span class="str">"data/notes"</span>).mkdir(exist_ok=<span class="kw">True</span>)
    <span class="kw">with</span> open(<span class="str">f"data/notes/{name}.txt"</span>, <span class="str">"w"</span>) <span class="kw">as</span> f:
        f.write(content)

<span class="kw">def</span> <span class="fn">summarize_note</span>(name: str) -> str:
    <span class="kw">with</span> open(<span class="str">f"data/notes/{name}.txt"</span>) <span class="kw">as</span> f:
        text = f.read()
    prompt = <span class="str">f"Summarize this note in 3 bullet points:\n\n{text}"</span>
    <span class="kw">return</span> ask_ai(prompt)

<span class="kw">def</span> <span class="fn">ask_from_note</span>(name: str, question: str) -> str:
    <span class="kw">with</span> open(<span class="str">f"data/notes/{name}.txt"</span>) <span class="kw">as</span> f:
        text = f.read()
    prompt = <span class="str">f"Based on this note:\n{text}\n\nAnswer: {question}"</span>
    <span class="kw">return</span> ask_ai(prompt)</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Prompt engineering — how you word the prompt changes the output quality. File I/O (read/write). Context injection into LLMs.</p>
          </div>
        </div>

        <div class="step c3">
          <div class="step-top">
            <div class="step-name">Step 10 — Daily Productivity Suggestions with AI</div>
            <div class="step-tags"><span class="step-tag">Prompt Engineering</span></div>
          </div>
          <div class="codeblock"><span class="kw">def</span> <span class="fn">get_daily_suggestion</span>(tasks: list) -> str:
    task_list = <span class="str">"\n"</span>.join([<span class="str">f"- {t[1]} ({t[2]})"</span> <span class="kw">for</span> t <span class="kw">in</span> tasks])
    prompt = <span class="str">f"""
I have these tasks today:
{task_list}

Give me:
1. Which task to tackle first and why
2. One productivity tip for my day
3. An estimated realistic time for each task
"""</span>
    <span class="kw">return</span> ask_ai(prompt)</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Multi-part prompts. Formatting AI output. Injecting dynamic data (your real tasks) into prompts — a core LLM app pattern.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- PHASE 4 -->
    <div class="section-label">Phase 04</div>
    <div class="phase">
      <div class="phase-header">
        <div class="phase-num num-4">PHASE 4</div>
        <div class="phase-title-wrap">
          <div class="phase-title">Progress Records — Export to Word Doc</div>
          <div class="phase-subtitle">Automatically generate .docx reports of your productivity</div>
        </div>
      </div>
      <div class="steps">

        <div class="step c4">
          <div class="step-top">
            <div class="step-name">Step 11 — Build the Word doc exporter</div>
            <div class="step-tags"><span class="step-tag">python-docx</span><span class="step-tag">Reports</span></div>
          </div>
          <div class="step-desc">Every week (or on demand), your assistant generates a Word document showing completed tasks, note summaries, and AI insights — a real progress record.</div>
          <div class="codeblock"><span class="comment"># core/records.py</span>
<span class="kw">from</span> docx <span class="kw">import</span> Document
<span class="kw">from</span> docx.shared <span class="kw">import</span> Pt, RGBColor
<span class="kw">from</span> datetime <span class="kw">import</span> datetime
<span class="kw">from</span> core.tasks <span class="kw">import</span> get_tasks

<span class="kw">def</span> <span class="fn">export_weekly_report</span>():
    doc = Document()

    <span class="comment"># Title</span>
    title = doc.add_heading(<span class="str">f"Weekly Productivity Report — {datetime.now():%B %d, %Y}"</span>, <span class="num">0</span>)
    title.runs[<span class="num">0</span>].font.color.rgb = RGBColor(<span class="num">0x1a</span>, <span class="num">0x73</span>, <span class="num">0xe8</span>)

    <span class="comment"># Completed tasks section</span>
    doc.add_heading(<span class="str">"✅ Completed Tasks"</span>, level=<span class="num">1</span>)
    completed = get_tasks(done=<span class="num">1</span>)
    <span class="kw">if</span> completed:
        <span class="kw">for</span> t <span class="kw">in</span> completed:
            p = doc.add_paragraph(style=<span class="str">"List Bullet"</span>)
            p.add_run(<span class="str">f"{t[1]}"</span>).bold = <span class="kw">True</span>
            p.add_run(<span class="str">f" — {t[2]} priority"</span>)
    <span class="kw">else</span>:
        doc.add_paragraph(<span class="str">"No tasks completed this period."</span>)

    <span class="comment"># Stats</span>
    doc.add_heading(<span class="str">"📊 Stats"</span>, level=<span class="num">1</span>)
    pending = get_tasks(done=<span class="num">0</span>)
    table = doc.add_table(rows=<span class="num">1</span>, cols=<span class="num">2</span>)
    table.style = <span class="str">"Table Grid"</span>
    hdr = table.rows[<span class="num">0</span>].cells
    hdr[<span class="num">0</span>].text = <span class="str">"Completed"</span>; hdr[<span class="num">1</span>].text = <span class="str">"Pending"</span>
    row = table.add_row().cells
    row[<span class="num">0</span>].text = str(len(completed)); row[<span class="num">1</span>].text = str(len(pending))

    filename = <span class="str">f"exports/report_{datetime.now():%Y_%m_%d}.docx"</span>
    doc.save(filename)
    <span class="kw">return</span> filename</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>python-docx: headings, paragraphs, bullet lists, tables, font styling. How to programmatically generate formatted documents — a hugely practical skill.</p>
          </div>
        </div>

        <div class="step c4">
          <div class="step-top">
            <div class="step-name">Step 12 — Add a Download button in Streamlit</div>
            <div class="step-tags"><span class="step-tag">Streamlit</span><span class="step-tag">File Download</span></div>
          </div>
          <div class="codeblock"><span class="comment"># In app.py — Reports tab</span>
<span class="kw">if</span> st.button(<span class="str">"📄 Generate Weekly Report"</span>):
    path = export_weekly_report()
    <span class="kw">with</span> open(path, <span class="str">"rb"</span>) <span class="kw">as</span> f:
        st.download_button(
            label=<span class="str">"⬇ Download .docx"</span>,
            data=f,
            file_name=<span class="str">"weekly_report.docx"</span>,
            mime=<span class="str">"application/vnd.openxmlformats-officedocument.wordprocessingml.document"</span>
        )
    st.success(<span class="str">"Report ready!"</span>)</div>
        </div>

      </div>
    </div>

    <!-- PHASE 5 -->
    <div class="section-label">Phase 05</div>
    <div class="phase">
      <div class="phase-header">
        <div class="phase-num num-5">PHASE 5</div>
        <div class="phase-title-wrap">
          <div class="phase-title">Polish, LangChain & Final Touches</div>
          <div class="phase-subtitle">Make it feel like a real product</div>
        </div>
      </div>
      <div class="steps">

        <div class="step c5">
          <div class="step-top">
            <div class="step-name">Step 13 — Replace raw OpenAI with LangChain chains</div>
            <div class="step-tags"><span class="step-tag">LangChain</span><span class="step-tag">Chains</span></div>
          </div>
          <div class="step-desc">LangChain lets you build multi-step AI pipelines (chains). Refactor your AI calls to use PromptTemplate and LLMChain for cleaner, reusable code.</div>
          <div class="codeblock"><span class="kw">from</span> langchain_openai <span class="kw">import</span> ChatOpenAI
<span class="kw">from</span> langchain.prompts <span class="kw">import</span> PromptTemplate
<span class="kw">from</span> langchain.chains <span class="kw">import</span> LLMChain

llm = ChatOpenAI(model=<span class="str">"gpt-4o-mini"</span>, temperature=<span class="num">0.7</span>)

summarize_prompt = PromptTemplate(
    input_variables=[<span class="str">"text"</span>],
    template=<span class="str">"Summarize in 3 bullet points:\n\n{text}"</span>
)
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

<span class="comment"># Use it:</span>
result = summarize_chain.run(text=my_note_text)</div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>LangChain's core concepts: LLMs, PromptTemplates, Chains. How frameworks abstract API complexity for scalable AI apps.</p>
          </div>
        </div>

        <div class="step c5">
          <div class="step-top">
            <div class="step-name">Step 14 — Add tabbed navigation in Streamlit</div>
            <div class="step-tags"><span class="step-tag">Streamlit</span><span class="step-tag">UI/UX</span></div>
          </div>
          <div class="codeblock">tab1, tab2, tab3, tab4 = st.tabs([
    <span class="str">"📋 Tasks"</span>, <span class="str">"📝 Notes & AI"</span>, <span class="str">"💡 Daily Plan"</span>, <span class="str">"📊 Reports"</span>
])

<span class="kw">with</span> tab1:
    <span class="comment"># Task CRUD UI here</span>
<span class="kw">with</span> tab2:
    <span class="comment"># Note writing + summarize + Q&A</span>
<span class="kw">with</span> tab3:
    <span class="comment"># Daily AI suggestion</span>
<span class="kw">with</span> tab4:
    <span class="comment"># Export to Word doc</span></div>
        </div>

        <div class="step c5">
          <div class="step-top">
            <div class="step-name">Step 15 — Run and ship it!</div>
            <div class="step-tags"><span class="step-tag">Deployment</span></div>
          </div>
          <div class="codeblock"><span class="comment"># Run locally</span>
streamlit run app.py

<span class="comment"># Optional: deploy free on Streamlit Community Cloud</span>
<span class="comment"># 1. Push to GitHub (add .env to .gitignore!)</span>
<span class="comment"># 2. Go to share.streamlit.io</span>
<span class="comment"># 3. Connect repo → add API key in Secrets → Deploy</span></div>
          <div class="learn-box">
            <div class="learn-box-title">💡 What you learn</div>
            <p>Deploying Python web apps for free. Environment secrets in cloud platforms. The full journey from idea → deployed product.</p>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- SUMMARY TABLE -->
  <div class="section-label">Skills Map</div>
  <div class="step c2" style="margin-bottom: 64px;">
    <div class="step-name" style="margin-bottom: 12px;">Everything you'll have learned by the end</div>
    <table class="summary-table">
      <thead>
        <tr>
          <th>Skill</th>
          <th>Where you use it</th>
          <th>Real-world value</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Python fundamentals</td><td>Every file</td><td>Foundation of everything</td></tr>
        <tr><td>SQLite / SQL</td><td>tasks.py</td><td>Used in almost every app</td></tr>
        <tr><td>REST APIs (OpenAI)</td><td>ai_helper.py</td><td>Connect any AI service</td></tr>
        <tr><td>Prompt engineering</td><td>ai_helper.py, notes.py</td><td>Get better AI outputs</td></tr>
        <tr><td>LangChain</td><td>Phase 5</td><td>Build production AI pipelines</td></tr>
        <tr><td>Streamlit</td><td>app.py</td><td>Ship Python apps without web dev</td></tr>
        <tr><td>File I/O</td><td>notes.py, records.py</td><td>Handle real data in any project</td></tr>
        <tr><td>python-docx</td><td>records.py</td><td>Generate reports programmatically</td></tr>
        <tr><td>Security (.env)</td><td>Setup</td><td>Essential professional practice</td></tr>
        <tr><td>Deployment</td><td>Phase 5</td><td>Show your work to the world</td></tr>
      </tbody>
    </table>
  </div>

  <!-- FINALE -->
  <div class="finale">
    <h2>You're building a real product. 🚀</h2>
    <p>By the end of this project you'll have a working AI-powered app you built from scratch — and the skills to build the next one faster.</p>
    <div class="finale-row">
      <div class="finale-stat"><span class="val">5</span><span class="lbl">Phases</span></div>
      <div class="finale-stat"><span class="val">15</span><span class="lbl">Steps</span></div>
      <div class="finale-stat"><span class="val">10+</span><span class="lbl">Skills</span></div>
      <div class="finale-stat"><span class="val">1</span><span class="lbl">Deployed App</span></div>
    </div>
  </div>

</div>
</body>
</html>
