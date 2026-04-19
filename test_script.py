import json
import os

def test_questions_file_count():
    files = os.listdir('saa-c03-questions')
    md_files = [f for f in files if f.endswith('.md')]
    assert len(md_files) == 100, f"Expected 100 MD files, got {len(md_files)}"
    print("Test passed: 100 Markdown files exist.")

def test_json_count():
    with open('questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 100, f"Expected 100 questions in JSON, got {len(data)}"
    print("Test passed: 100 questions in questions.json.")

if __name__ == "__main__":
    test_questions_file_count()
    test_json_count()
