import os, json, requests
from datetime import datetime

TOPICS = [
    "AI-powered zero-day exploit detection in 2025",
    "LLMs as both threat and defence in cybersecurity",
    "Quantum computing breaking current encryption",
    "Deepfake threats and biometric authentication",
    "Prompt injection attacks on AI systems",
    "Zero-trust architecture in an AI-first world",
    "Autonomous AI agents in offensive security",
]

def generate():
    day = datetime.utcnow().timetuple().tm_yday
    topic = TOPICS[day % len(TOPICS)]
    prompt = f"""Write a LinkedIn post about: "{topic}"
- Max 200 words, punchy opening, end with question, 5 hashtags
- Tone: expert, human, forward-looking. Only output post text."""

    resp = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
                 "Content-Type": "application/json"},
        json={"model": "llama3-8b-8192",
              "messages": [{"role": "user", "content": prompt}],
              "max_tokens": 300}
    )
    resp.raise_for_status()
    post = resp.json()["choices"][0]["message"]["content"].strip()
    data = {"post": post, "topic": topic,
            "generated_at": datetime.utcnow().isoformat()+"Z"}
    with open("generated_post.json","w") as f:
        json.dump(data, f, indent=2)
    print(post)

if __name__ == "__main__":
    generate()
