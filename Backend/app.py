from flask import Flask, request, jsonify
from data import movies

app = Flask(__name__)

# Endpoint para agregar una película
@app.route('/api/new-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    if 'movieId' in data and 'name' in data and 'genre' in data:
        movie = {
            'movieId': data['movieId'],
            'name': data['name'],
            'genre': data['genre']
        }
        movies.append(movie)
        with open('data.py', 'w', encoding="utf-8") as f:
            f.write(f'movies = {movies}')
        return jsonify("¡La película fue agregada con éxito!"), 201
    else:
        return jsonify("¡Los datos proporcionados son incompletos!"), 400

# Endpoint para obtener todas las películas por género
@app.route('/api/all-movies-by-genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    movie_names = [movie['name'] for movie in movies if movie['genre'] == genre]
    return jsonify(f'¡Las películas de {genre} son: {movie_names}!')

# Endpoint para actualizar una película 
def actualizar():
    with open ('data.py', 'w', encoding='utf-8') as f:
        f.write(f'movies = {movies}')

@app.route('/api/update-movie', methods=['PUT'])
def update_movie():
    data = request.get_json()
    if 'movieId' in data and 'name' in data and 'genre' in data:
        movie_id = data['movieId']
        for movie in movies:
            if movie['movieId'] == movie_id:
                movie['name'] = data['name']
                movie['genre'] = data['genre']

                actualizar()

                return jsonify("¡La película fue actualizada con éxito!"), 200
        
        return jsonify("¡La película no fue encontrada!"), 404
    else:
        return jsonify("¡Los datos proporcionados son incompletos!"), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
