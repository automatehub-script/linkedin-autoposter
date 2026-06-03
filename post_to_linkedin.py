import os, json

def main():
    with open("generated_post.json") as f:
        data = json.load(f)
    
    post = data["post"]
    print("✅ Post generated successfully!")
    print("=" * 50)
    print(post)
    print("=" * 50)
    print("\n📋 Copy above text and post manually on LinkedIn")
    print("OR use this auto-share URL:")
    import urllib.parse
    encoded = urllib.parse.quote(post[:700])
    print(f"\nhttps://www.linkedin.com/shareArticle?mini=true&summary={encoded}")

if __name__ == "__main__":
    main()
