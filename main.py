import openai

openai.api_key = "YOUR_API_KEY"

def analyze_log(log):
    prompt = f"""
You are a technical support engineer.

Analyze the log below and provide:
- Error type
- Possible cause
- Suggested fix

Log:
{log}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]


with open("logs.txt", "r") as file:
    log_data = file.read()

result = analyze_log(log_data)

print("\n=== AI ANALYSIS ===\n")
print(result)