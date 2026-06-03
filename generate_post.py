import google.generativeai as genai
import os, json
from datetime import datetime

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
- Max 200 words
- Punchy opening line
- End with a question for comments
- Add 5 hashtags at the end
- Tone: expert, human, forward-looking
Only output the post text."""

    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt,
        generation_config={"max_output_tokens": 300})
    post = resp.text.strip()
    data = {"post": post, "topic": topic,
            "generated_at": datetime.utcnow().isoformat()+"Z"}
    with open("generated_post.json","w") as f:
        json.dump(data, f, indent=2)
    print(post)

if __name__ == "__main__":
    generate()
