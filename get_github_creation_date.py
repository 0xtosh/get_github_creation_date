import sys
import requests
import json

def main():
    # Check if a URL is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_repo_url>")
        sys.exit(1)

    # Extract the URL from the command line arguments
    original_url = sys.argv[1]

    # Replace 'github.com' with 'api.github.com/repos' in the URL
    api_url = original_url.replace('github.com', 'api.github.com/repos')

    # Make a GET request to the modified URL
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the 'created_at' value
        creation_date = data.get('created_at', 'Not available')

        # Print the original URL and the creation date
        print(f"{original_url}; {creation_date}")
    else:
        print("Failed to fetch data from GitHub API.")

if __name__ == "__main__":
    main()

