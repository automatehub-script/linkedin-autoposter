import os, json, requests
from datetime import datetime

def main():
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    with open("generated_post.json") as f:
        data = json.load(f)

    # Get user ID via /v2/me
    r = requests.get("https://api.linkedin.com/v2/me",
        headers={"Authorization": f"Bearer {token}",
                 "X-Restli-Protocol-Version": "2.0.0"})
    r.raise_for_status()
    urn = f"urn:li:person:{r.json()['id']}"

    # Post to LinkedIn
    payload = {
        "author": urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {"com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": data["post"]},
            "shareMediaCategory": "NONE"
        }},
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    r2 = requests.post("https://api.linkedin.com/v2/ugcPosts",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json",
                 "X-Restli-Protocol-Version": "2.0.0"},
        json=payload)
    r2.raise_for_status()
    print("✅ Posted!", r2.headers.get("x-restli-id"))

if __name__ == "__main__":
    main()
