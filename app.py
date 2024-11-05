from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users"

@app.route('/<username>', methods=['GET'])
def get_user_gists(username):
    """To fetch gists for a GitHub user"""
    url = f"{GITHUB_API_URL}/{username}/gists"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({'error': 'User not found or GitHub API error'}), response.status_code

    gists = response.json()
    gist_list = [{'id': gist['id'], 'description': gist['description'], 'url': gist['html_url']} for gist in gists]

    return jsonify(gist_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)