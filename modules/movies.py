import modules.files as FILE
import modules.screen as SCREEN

# Function to add users to a json file 
def addMovie():
    SCREEN.cleanScreen() # Cleans terminal content
    FILE.checkFile('movies.json') # Checks if movies.json exists
    jsonFileData = FILE.readFile('movies.json') # Read and load json file content into a variable
    # Create the structure of the movie inf0
    movie = {
        "id" : "",
        "name" : "",
        'duration' : '',
        'sypnosis' : '',
        'genres' : [],
        'actors' : [],
        'format' : []
    }
    
