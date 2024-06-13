def print_itineraries(itineraries):
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print_itineraries(itineraries)

def add_book(library, title, author):
    # Check if the book is already in the library
    for existing_title, existing_author in library:
        if title == existing_title and author == existing_author:
            print(f"'{title}' by {author} is already in the library.")
            return

    # If not, add the book to the library
    library.append((title, author))
    print(f"'{title}' by {author} has been added to the library.")

# Example usage:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library, "Animal Farm", "George Orwell")
add_book(library, "1984", "George Orwell")  # This will print a message about the duplicate book
