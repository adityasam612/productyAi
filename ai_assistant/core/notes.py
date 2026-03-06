import os
import pathlib
from core.ai_helper import ask_ai

NOTES_DIR = "data/notes"

def save_note(name: str, content: str):
    pathlib.Path(NOTES_DIR).mkdir(parents=True, exist_ok=True)
    with open(f"{NOTES_DIR}/{name}.txt", "w") as f:
        f.write(content)

def list_notes() -> list:
    pathlib.Path(NOTES_DIR).mkdir(parents=True, exist_ok=True)
    return [f.replace(".txt", "") for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]

def read_note(name: str) -> str:
    with open(f"{NOTES_DIR}/{name}.txt") as f:
        return f.read()

def summarize_note(name: str) -> str:
    text = read_note(name)
    return ask_ai(f"Summarize this note in 3 clear bullet points:\n\n{text}")

def ask_from_note(name: str, question: str) -> str:
    text = read_note(name)
    return ask_ai(f"Based on this note:\n{text}\n\nAnswer this question: {question}")