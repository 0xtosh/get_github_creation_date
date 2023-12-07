import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_repo_url>")
        sys.exit(1)

    original_url = sys.argv[1]
    # replace 'github.com' with 'api.github.com/repos' in the URL
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        creation_date = data.get('created_at', 'Not available')
        print(f"{original_url}; {creation_date}")
    else:
        print("Failed to fetch data from GitHub API.")

if __name__ == "__main__":
    main()
