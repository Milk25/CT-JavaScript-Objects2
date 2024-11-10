


function formatBookTitlesAndAuthors() {
    return library.map(book => ({
        title: `Title: ${book.title}`,
        author: `Author: ${book.author}`,
        pages: book.pages
    }));
}


// Example usage:
addBook("The Great Gatsby", "F. Scott Fitzgerald", 180);
addBook("To Kill a Mockingbird", "Harper Lee", 90);
addBook("1984", "George Orwell", 328);

// Display books in the library
console.log("Library Collection:");
library.forEach(book => console.log(book.displayInfo()));

// Search for books by title
console.log("Search by Title '1984':", searchByTitle("1984"));

// Search for books by author
console.log("Search by Author 'Harper Lee':", searchByAuthor("Harper Lee"));

// Filter books with 100 pages or less
console.log("Books with 100 pages or less:", filterShortBooks());

// Format book titles and authors
console.log("Formatted Titles and Authors:", formatBookTitlesAndAuthors());