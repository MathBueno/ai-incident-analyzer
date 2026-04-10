# 🔍 AI Incident Analyzer

A tool that analyzes system error logs using AI, identifies root causes, and suggests actionable resolutions. This project simulates a real-world Level 1/Level 2 support triage workflow to speed up the debugging process.

## 🧩 The Problem
When a production system fails, support engineers are often handed raw, cryptic error logs. Identifying the actual root cause manually is time-consuming and requires deep contextual knowledge.

## ✅ The Solution
This tool automates the first layer of log analysis. It processes error logs, leverages AI to interpret the issue, and outputs a structured summary containing the error type, probable cause, and a suggested fix.

## ⚙️ Tech Stack
- **Python** — Core logic and log processing
- **AI Integration (OpenAI API)** — Log interpretation and root cause analysis
- **JSON** — Structured data handling

## 📊 Example Output

**Input (Log Entry):**
`ERROR 500: Connection timeout while calling API /user/data`

**AI Output:**
```text
Error Type    : Timeout
Possible Cause: Network latency or API endpoint unavailability.
Suggested Fix : Check API health status and implement retry with exponential backoff.
```

## 🚀 How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API key: `export OPENAI_API_KEY='your_key_here'`
4. Run the analyzer: `python main.py`

## 💼 Skills Demonstrated
- AI integration with APIs for automation
- Log analysis and error interpretation
- Troubleshooting and incident response workflow
