import urllib

from django.conf import settings
import requests


def search_tmdb(query):
    '''TMDb を検索して結果を返す

    parameters
    ----------
    query : str
        検索に使う文字列 (映画の邦題)

    returns
    -------
    list
        年でソートした映画情報 {題名, 年, 概要} のリスト
    '''
    params = urllib.parse.urlencode({
        'api_key': settings.TMDB_API_KEY,
        'query': query,
        'language': 'ja',
    })
    url = f'https://api.themoviedb.org/3/search/movie?{params}'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    res = requests.get(url, headers=headers)

    movies = []
    for m in res.json()['results']:
        movie = {
            'title': m['title'],
            'release_date': m['release_date'],
            'year': m['release_date'].split('-')[0],
            'overview': m['overview'].strip(),
        }
        movies.append(movie)
    return sorted(movies, key=lambda m: m['release_date'])
