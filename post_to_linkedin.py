import os, json, requests

def main():
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_id = os.environ["LINKEDIN_PERSON_ID"]
    
    with open("generated_post.json") as f:
        data = json.load(f)

    urn = f"urn:li:person:{person_id}"

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
    r = requests.post("https://api.linkedin.com/v2/ugcPosts",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json",
                 "X-Restli-Protocol-Version": "2.0.0"},
        json=payload)
    r.raise_for_status()
    print("✅ Posted!", r.headers.get("x-restli-id"))

if __name__ == "__main__":
    main()
