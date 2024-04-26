import modules.files as FILE
import modules.screen as SCREEN

# Function to add users to a json file 
def addMovie():
    SCREEN.cleanScreen() # Cleans terminal content
    FILE.checkFile('movies.json') # Checks if movies.json exists
    jsonMoviesData = FILE.readFile('movies.json') # Read and load json file content into a variable
    # Create the structure of the movie info
    movie = {
        "id" : "",
        "name" : "",
        'duration' : '',
        'sypnosis' : '',
        'genres' : [],
        'actors' : [],
        'format' : []
    }
    # Inputs to store the movie information
    movie['id'] = str(input("Movie's ID: ")) 
    movie['name'] = str(input("Movie's name: "))
    movie['duration'] = str(input("Movie's duration: "))
    movie['sypnosis'] = str(input("Movie's sypnosis: "))
    SCREEN.cleanScreen() # Cleans screen
    movie['genres'] = str(input("Movie's genre/s"))
    movieToUpdate = {movie['id'] : movie} # Dict to store in json file
    FILE.updateFile('movies.json', movieToUpdate)
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # WAITING MY TEAM TO FINISH THE GENRES, ACTORS AND FORMATS JSON FILES TO COMPLETE THIS FUNCTION
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Function to remove a movie from the movies json file
def removeMovie():
    SCREEN.cleanScreen() #Cleans screen
    FILE.checkFile('movies.json') # Checks if movies.json exists
    jsonMoviesData = FILE.readFile()
    
