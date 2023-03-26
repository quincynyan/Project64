# A record data structure is to be used to store the details of music albums.
# a the title of the album
# b the name of the artist
# c the year of release
# d the genre
# Develop a program that uses a record structure for storing the details of music albums. It must:
# a have fields for title, artist, year of release and genre
# b allow the user to input the details of new albums
# c allow the user to search for an album by name and display its details.

class Album:
    def __init__(self, title, artist, year, genre) -> None:
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre

    def __str__(self) -> str:
        return f"Title: {self.title} Artist: {self.artist} Year: {self.year} Genre: {self.genre}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if self.title == other.title:
            return True
        else:
            return False


def enterAlbum() -> Album:
    title: str = input("Enter title: ")
    artist: str = input("Enter artist: ")
    year: str = input("Enter year: ")
    genre: str = input("Enter genre: ")
    return Album(title, artist, year, genre)


def printAlbum(a) -> None:
    print(a)


def main() -> None:
    nxt = ""
    a = []
    while nxt != "e":
        if nxt == "n":
            a.append(enterAlbum())
        elif nxt == "v":
            for i in a:
                printAlbum(i)
        elif nxt == "s":
            title: str = input("Enter title: ")
            for i in a:
                if i.title == title:
                    printAlbum(i)
        nxt: str = input(
            "Would you like to enter a new record (n), view an existing record (v), search for an album (s), or exit (e)?").lower()


if __name__ == '__main__':
    main()
