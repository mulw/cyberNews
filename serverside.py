from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def fetch_news(language='en', category='all'):
    try:
        api_key = 'ENTER YOUR API KEY'
        url = f'https://newsapi.org/v2/top-headlines?category=technology&keyword=cybersecurity&language={language}&apiKey={api_key}'

        if category != 'all':
            url += f'&category={category}'

        response = requests.get(url)
        data = response.json()

        # Transform the data to include image URLs
        articles_with_images = []
        for article in data.get('articles', []):
            # Include only necessary information
            new_article = {
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'publishedAt': article.get('publishedAt', ''),
                'url': article.get('url', ''),
                'image': article.get('urlToImage', '')  # Include the image URL
            }
            articles_with_images.append(new_article)

        return jsonify({'articles': articles_with_images})

    except Exception as e:
        print('Error fetching news:', e)
        return jsonify(error='Internal Server Error'), 500

# Endpoint to fetch news
@app.route('/news', methods=['GET'])
def get_news():
    language = request.args.get('language', 'en')
    category = request.args.get('category', 'all')
    return fetch_news(language, category)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
