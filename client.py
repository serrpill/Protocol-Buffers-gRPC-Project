import grpc
import university_pb2
import university_pb2_grpc

def run():
    # Sunucuya bağlan
    channel = grpc.insecure_channel('localhost:50051')

    # Stub'ları oluştur
    book_stub = university_pb2_grpc.BookServiceStub(channel)
    student_stub = university_pb2_grpc.StudentServiceStub(channel)
    loan_stub = university_pb2_grpc.LoanServiceStub(channel)

    print("\n📚 1) Kitap ekleniyor...")
    book = book_stub.AddBook(university_pb2.Book(
        title="Clean Code",
        author="Robert C. Martin",
        isbn="9780132350884",
        publisher="Prentice Hall",
        pageCount=464,
        stock=10
    ))
    print("Kitap eklendi:", book.title, "| ID:", book.id)

    print("\n👤 2) Öğrenci ekleniyor...")
    student = student_stub.AddStudent(university_pb2.Student(
        name="Serpil Öğrenci",
        studentNumber="20231234",
        email="serpil@example.com",
        isActive=True
    ))
    print("Öğrenci eklendi:", student.name, "| ID:", student.id)

    print("\n🔁 3) Ödünç alma işlemi yapılıyor...")
    loan = loan_stub.BorrowBook(university_pb2.Loan(
        studentId=student.id,
        bookId=book.id,
        loanDate="2025-06-14"
    ))
    print("Ödünç alındı:", loan.id, "| Durum:", loan.status)

    print("\n📄 4) Kitaplar listeleniyor...")
    books = book_stub.ListBooks(university_pb2.Empty())
    for b in books.books:
        print("-", b.title)

    print("\n📄 5) Öğrenciler listeleniyor...")
    students = student_stub.ListStudents(university_pb2.Empty())
    for s in students.students:
        print("-", s.name)

    print("\n📄 6) Loan listesi alınıyor...")
    loans = loan_stub.ListLoans(university_pb2.Empty())
    for l in loans.loans:
        print(f"- {l.id}: {l.studentId} -> {l.bookId} ({l.status})")

if __name__ == "__main__":
    run()
