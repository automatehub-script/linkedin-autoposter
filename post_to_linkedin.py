import os, json, requests

def main():
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_id = os.environ["LINKEDIN_PERSON_ID"]

    with open("generated_post.json") as f:
        data = json.load(f)

    payload = {
        "author": f"urn:li:person:{person_id}",
        "commentary": data["post"],
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }

    r = requests.post(
        "https://api.linkedin.com/rest/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "LinkedIn-Version": "202410"
        },
        json=payload
    )
    print("Status:", r.status_code, r.text)
    r.raise_for_status()
    print("✅ Posted!")

if __name__ == "__main__":
    main()
