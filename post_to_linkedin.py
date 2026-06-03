import os, json, requests

def main():
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_id = os.environ["LINKEDIN_PERSON_ID"]

    with open("generated_post.json") as f:
        data = json.load(f)

    payload = {
        "content": {
            "contentEntities": [],
            "title": "AI & Cybersecurity Insight"
        },
        "distribution": {
            "linkedInDistributionTarget": {}
        },
        "owner": f"urn:li:person:{person_id}",
        "subject": "AI & Cybersecurity",
        "text": {"text": data["post"]}
    }

    r = requests.post(
        "https://api.linkedin.com/v2/shares",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        },
        json=payload
    )
    print("Status:", r.status_code)
    print("Response:", r.text)
    r.raise_for_status()
    print("✅ Posted!")

if __name__ == "__main__":
    main()
