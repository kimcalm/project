import requests
import json
from openpyxl import load_workbook

wb = load_workbook('./연도별 박스오피스 순위.xlsx')
ws = wb.active

API_KEY='1c04f38f1d2f0979baea5787bc0cbdd8'

def get_movie_datas():
  total_data = []

  # for r in range(3, ws.max_row+1):
  for r in range(3, 10):
    movie_title = ws.cell(row=r, column=6).value
    print(movie_title)
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&page=1&include_adult=false&query={movie_title}'

    movies = requests.get(url).json()
    print(movies)
    for movie in movies['results']:
      if movie['poster_path'] and movie.get('release_date', ''):
        fields = {
                    'title_en': movie_title,
                    'title_kr': movie['title'],
                    'released_date': movie['release_date'],
                    'genres': movie['genre_ids'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                  }
        
        data = {
                  "TMDB_pk": movie['id'],
                  "model": "movies.movie",
                  "fields": fields
                }
        
        total_data.append(data)

  with open("movie_data.json", 'w', encoding='utf-8') as w:
    json.dump(total_data, w, indent="\\t", ensure_ascii=False)

get_movie_datas()

