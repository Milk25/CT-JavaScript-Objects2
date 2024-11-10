function Book(title, author, pages) {
    this.title = title;
    this.author = author;
    this.pages = pages;
}


Book.prototype.displayInfo = function() {
    console.log(`Title: ${this.title}\nAuthor: ${this.author}\nPages: ${this.pages}`);
};


let library = [];

// Function to add a book to the library
function addBook(title, author, pages) {
    const book = new Book(title, author, pages);
    library.push(book);
}

// Function to search for books by title
function searchByTitle(title) {
    return library.filter(book => book.title.toLowerCase().includes(title.toLowerCase()));
}

// Function to search for books by author
function searchByAuthor(author) {
    return library.filter(book => book.author.toLowerCase().includes(author.toLowerCase()));
}


// Function to filter books with more than 100 pages
function filterBooksByPages() {
    return library.filter(book => book.pages <= 100);
}

// Function to map books and add "Title: " and "Author: " to the title and author properties
function formatBookInfo() {
    return library.map(book => {
        return {
            title: `Title: ${book.title}`,
            author: `Author: ${book.author}`,
            pages: book.pages
        };
    });
}


// Add books to the library
addBook('The Great Gatsby', 'F. Scott Fitzgerald', 218);
addBook('1984', 'George Orwell', 328);
addBook('To Kill a Mockingbird', 'Harper Lee', 281);
addBook('The Catcher in the Rye', 'J.D. Salinger', 277);
addBook('The Hobbit', 'J.R.R. Tolkien', 310);
addBook('Animal Farm', 'George Orwell', 112);
addBook('The Alchemist', 'Paulo Coelho', 198);

// Display information about a specific book
library[0].displayInfo(); // Display information about the first book in the library

// Search for books by title or author
console.log(searchByTitle('1984')); // Search for books by title
console.log(searchByAuthor('George Orwell')); // Search for books by author

// Filter out books with more than 100 pages
console.log(filterBooksByPages()); // Books with 100 pages or less

// Format book info with "Title: " and "Author: "
console.log(formatBookInfo()); // Formatted book information


// Example output for filtering books with more than 100 pages
[
    { title: 'Title: Animal Farm', author: 'Author: George Orwell', pages: 112 },
    { title: 'Title: The Alchemist', author: 'Author: Paulo Coelho', pages: 198 }
]


