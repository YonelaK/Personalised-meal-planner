public class BookService {
    private final BookRepository bookRepo;

    public BookService(BookRepository bookRepo) {
        this.bookRepo = bookRepo;
    }

    public Book checkoutBook(String bookId) {
        Book book = bookRepo.findById(bookId)
                .orElseThrow(() -> new BookNotFoundException(bookId));
        if (book.isCheckedOut()) {
            throw new BookAlreadyCheckedOutException(bookId);
        }
        book.checkOut();
        return bookRepo.save(book);
    }

    public List<Book> getAllBooks() {
        return bookRepo.findAll();
    }

    public Book createBook(Book book) {
        return bookRepo.save(book);
    }

    public Book updateBook(String id, Book book) {
        return bookRepo.update(id, book);
    }
}
