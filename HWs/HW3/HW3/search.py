# IMPORT LIBRARIES
import sys
from sqlalchemy import create_engine
import pymysql
import pandas as pd

# NOTE: DO NOT modify any variable or function names given in the template!

# Choose EITHER SQLAlchemy OR PyMySQL:

# OPTION 1: SQLAlchemy
# DATABASE_URI = ''

# OPTION 2: PyMySQL
# Replace the placeholders with the actual database connection details
# DATABASE_CONNECTION_PARAMS = {

# }
DATABASE_CONNECTION_PARAMS = {
    'host': 'localhost',
    'user': 'dsci551',
    'password': 'Dsci-551',
    'database': 'CINEMA',
    'cursorclass': pymysql.cursors.DictCursor
}


def get_movies_by_actor(actor_name):
    """
    Fetches titles of movies that the specified actor has acted in.
    INPUT: actor_name (str) - The name of the actor
    RETURN: A list of movie titles (list)
    
    Sample Terminal Command:python3 search.py "John Doe"
    Expected Sample Output: Movies featuring John Doe: ['The Great Adventure', 'Dreams of Space']
    """

    # Placeholder for the result list:
    movies = []
    connection=None;
    try:
        # Connect to the database
        connection = pymysql.connect(**DATABASE_CONNECTION_PARAMS)
        
        # Create a cursor object
        with connection.cursor() as cursor:
            # Construct the SQL query to retrieve movie titles by actor
            sql = """
            SELECT m.title
            FROM Movies m
            INNER JOIN ActIn ai ON m.id = ai.movie_id
            INNER JOIN Actors a ON ai.actor_id = a.id
            WHERE a.name = %s
            """
            cursor.execute(sql, (actor_name,))     
            result = cursor.fetchall()
            movies = [row['title'] for row in result]
            
    except pymysql.Error as e:
        print("Error:", e)
    finally:
        # Close the database connection
        if connection:
            connection.close()

    return movies


# Use the below main method to test your code
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py '<actor_name>'")
        sys.exit(1)
    actor_name = sys.argv[1]
    movies = get_movies_by_actor(actor_name)
    if movies:
        print(f"Movies featuring {actor_name}: {movies}")
    else:
        print(f"No movies found for actor {actor_name}.")
