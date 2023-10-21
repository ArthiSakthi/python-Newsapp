from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
recent_searches = [
    {'query': 'Education', 'timestamp': '10:15 am'},
    {'query': 'Politics', 'timestamp': '11:45 am'},
    {'query': 'Sports', 'timestamp': '05:00 pm'},
]


newsapi = NewsApiClient(api_key='6946a04fdd4c409b87a74eabcadb272b')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_query = request.form['query']
        top_headlines = newsapi.get_top_headlines(q=user_query,language='en',country='us')
        top_headlines = top_headlines['articles'][:10]
        all_articles = newsapi.get_everything(q=user_query,language='en',sort_by='relevancy')
        all_articles = all_articles['articles'][:15]

        return render_template('index.html', user_query=user_query, top_headlines=top_headlines,all_articles=all_articles)

    return render_template('index.html',recent_searches=recent_searches)


if __name__ == '__main__':
    app.run(debug=True)