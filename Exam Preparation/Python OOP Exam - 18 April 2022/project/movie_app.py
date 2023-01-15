from project.user import User
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []     # An empty list that will contain all the movies (objects)
        self.users_collection = []      # An empty list that will contain all the users (objects)

    def check_if_user_exists(self, username: str):
        for user in self.users_collection:
            if user.username == username:
                return True

    def check_if_movie_exists(self, title: str):
        for movie in self.movies_collection:
            if movie.title == title:
                return True

    @staticmethod
    def find_user_by_username(username: str, collection):
        for user in collection:
            if user.username == username:
                return user

    def check_if_user_liked_movie(self, username, title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == title:
                        return True

    def register_user(self, username: str, age: int):
        if self.check_if_user_exists(username):
            raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        if not self.check_if_user_exists(username):
            raise Exception("This user does not exist!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if self.check_if_movie_exists(movie.title):
            raise Exception("Movie already added to the collection!")

        current_user = self.find_user_by_username(username, self.users_collection)
        current_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{current_user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_user = self.find_user_by_username(username, self.users_collection)
        self.movies_collection.remove(movie)
        current_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        current_user = self.find_user_by_username(username, self.users_collection)

        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        current_user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_username(username, self.users_collection)

        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        current_user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        if not self.users_collection:
            users = "No users."
        else:
            users = ', '.join(u.username for u in self.users_collection)

        if not self.movies_collection:
            movies = "No movies."
        else:
            movies = ', '.join(m.title for m in self.movies_collection)

        return f"All users: {users}\nAll movies: {movies}"

