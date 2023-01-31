# Define the record structure
class MusicAlbum:
    def __init__(self, title: str, artist: str, year: int, genre: str):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre


# Create a list to store the albums
albums = []

# Function to input the details of a new album


def add_album():
    title = input("Enter the title of the album: ")
    artist = input("Enter the name of the artist: ")
    year = int(input("Enter the year of release: "))
    genre = input("Enter the genre of the album: ")
    # Create a new MusicAlbum object and append it to the list
    albums.append(MusicAlbum(title, artist, year, genre))

# Function to search for an album by name and display its details


def search_album(name: str):
    # Search through the list of albums
    for album in albums:
        if album.title == name:
            # Display the details of the album
            print("Title:", album.title)
            print("Artist:", album.artist)
            print("Year:", album.year)
            print("Genre:", album.genre)
            return
    print("Album not found")


# Test the functions
add_album()
add_album()
search_album("Thriller")
search_album("Born in the U.S.A.")
