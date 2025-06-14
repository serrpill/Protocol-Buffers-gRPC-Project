import grpc
from concurrent import futures
import time
import uuid
from grpc_reflection.v1alpha import reflection
import university_pb2
import university_pb2_grpc

# 📚 Örnek veriler (mock)
books = {}
students = {}
loans = {}

# 📘 BookService
class BookService(university_pb2_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        return university_pb2.BookList(books=list(books.values()))

    def GetBook(self, request, context):
        return books.get(request.id, university_pb2.Book())

    def AddBook(self, request, context):
        book_id = request.id or str(uuid.uuid4())
        book = university_pb2.Book(
            id=book_id,
            title=request.title,
            author=request.author,
            isbn=request.isbn,
            publisher=request.publisher,
            pageCount=request.pageCount,
            stock=request.stock
        )
        books[book.id] = book
        return book

    def UpdateBook(self, request, context):
        if request.id in books:
            books[request.id] = request
        return books.get(request.id, university_pb2.Book())

    def DeleteBook(self, request, context):
        books.pop(request.id, None)
        return university_pb2.Empty()

# 👤 StudentService
class StudentService(university_pb2_grpc.StudentServiceServicer):
    def ListStudents(self, request, context):
        return university_pb2.StudentList(students=list(students.values()))

    def GetStudent(self, request, context):
        return students.get(request.id, university_pb2.Student())

    def AddStudent(self, request, context):
        student_id = request.id or str(uuid.uuid4())
        student = university_pb2.Student(
            id=student_id,
            name=request.name,
            studentNumber=request.studentNumber,
            email=request.email,
            isActive=request.isActive
        )
        students[student.id] = student
        return student

    def UpdateStudent(self, request, context):
        if request.id in students:
            students[request.id] = request
        return students.get(request.id, university_pb2.Student())

    def DeleteStudent(self, request, context):
        students.pop(request.id, None)
        return university_pb2.Empty()

# 🔁 LoanService
class LoanService(university_pb2_grpc.LoanServiceServicer):
    def ListLoans(self, request, context):
        return university_pb2.LoanList(loans=list(loans.values()))

    def GetLoan(self, request, context):
        return loans.get(request.id, university_pb2.Loan())

    def BorrowBook(self, request, context):
        loan_id = request.id or str(uuid.uuid4())
        loan = university_pb2.Loan(
            id=loan_id,
            studentId=request.studentId,
            bookId=request.bookId,
            loanDate=request.loanDate,
            returnDate="",
            status=university_pb2.ONGOING
        )
        loans[loan.id] = loan
        return loan

    def ReturnBook(self, request, context):
        loan = loans.get(request.id)
        if loan:
            updated = university_pb2.Loan(
                id=loan.id,
                studentId=loan.studentId,
                bookId=loan.bookId,
                loanDate=loan.loanDate,
                returnDate="2024-06-14",
                status=university_pb2.RETURNED
            )
            loans[loan.id] = updated
            return updated
        return university_pb2.Loan()

# 🚀 gRPC Sunucu Başlatıcı
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    university_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    university_pb2_grpc.add_LoanServiceServicer_to_server(LoanService(), server)
    server.add_insecure_port('[::]:50051')
    SERVICE_NAMES = (
        university_pb2.DESCRIPTOR.services_by_name['BookService'].full_name,
        university_pb2.DESCRIPTOR.services_by_name['StudentService'].full_name,
        university_pb2.DESCRIPTOR.services_by_name['LoanService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    print("✅ gRPC Server started on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
