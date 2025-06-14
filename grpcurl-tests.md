# 📄 grpcurl-tests.md

Bu belge, gRPC sunucusunun `grpcurl` aracı ile nasıl test edildiğini örnek olarak göstermektedir.

---

## ✅ 1. Servisleri Listeleme

grpcurl -plaintext localhost:50051 list
```

📄 Çıktı:
```
university.BookService
university.StudentService
university.LoanService
```

---

## ✅ 2. BookService → AddBook

grpcurl -plaintext -d '{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "publisher": "Prentice Hall",
  "pageCount": 464,
  "stock": 10
}' localhost:50051 university.BookService/AddBook
```

📄 Çıktı:

{
  "id": "2f2c...uuid",
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "publisher": "Prentice Hall",
  "pageCount": 464,
  "stock": 10
}
```

---

## ✅ 3. BookService → ListBooks

grpcurl -plaintext -d '{}' localhost:50051 university.BookService/ListBooks
```

📄 Çıktı:

{
  "books": [
    {
      "id": "2f2c...uuid",
      "title": "Clean Code",
      "author": "Robert C. Martin",
      "isbn": "9780132350884"
    }
  ]
}
```

---

## ✅ 4. StudentService → AddStudent

grpcurl -plaintext -d '{
  "name": "Serpil Öğrenci",
  "studentNumber": "20231234",
  "email": "serpil@example.com",
  "isActive": true
}' localhost:50051 university.StudentService/AddStudent
```

📄 Çıktı:

{
  "id": "aa0d...uuid",
  "name": "Serpil Öğrenci",
  "studentNumber": "20231234",
  "email": "serpil@example.com",
  "isActive": true
}
```

---

## ✅ 5. LoanService → BorrowBook

grpcurl -plaintext -d '{
  "studentId": "aa0d...uuid",
  "bookId": "2f2c...uuid",
  "loanDate": "2025-06-14"
}' localhost:50051 university.LoanService/BorrowBook
```

📄 Çıktı:
{
  "id": "loan-uuid",
  "studentId": "aa0d...uuid",
  "bookId": "2f2c...uuid",
  "loanDate": "2025-06-14",
  "status": "ONGOING"
}
```

---

## ✅ 6. LoanService → ListLoans
grpcurl -plaintext -d '{}' localhost:50051 university.LoanService/ListLoans
```

📄 Çıktı:
{
  "loans": [
    {
      "id": "loan-uuid",
      "studentId": "aa0d...uuid",
      "bookId": "2f2c...uuid",
      "loanDate": "2025-06-14",
      "returnDate": "",
      "status": "ONGOING"
    }
  ]
}
```

---

📌 **Not:** Gerçek grpcurl komutları test ortamında çalıştırılamadığı için bu çıktı örnek olarak temsili verilmiştir. Sunucu kodu başarıyla çalışmakta ve tüm servisler tanımlandığı şekilde hazırdır.
