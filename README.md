# 🎓 ÜNİVERSİTE KÜTÜPHANE SİSTEMİ – gRPC TABANLI

Bu proje, **Açık Kaynak Kodlu Yazılımlar** dersi kapsamında geliştirilmiş bir gRPC tabanlı üniversite kütüphane sistemidir. Uygulama, Protocol Buffers (.proto) kullanılarak tanımlanan veri yapıları üzerinden kitap, öğrenci ve ödünç alma işlemlerini yönetmektedir.

---

## 🎯 PROJENİN AMAÇLARI

- **Protobuf** ile API tanımı yapmak  
- **gRPC** ile sunucu ve istemci uygulamaları geliştirmek  
- Kitap, öğrenci ve ödünç işlemleri için **CRUD servisleri** oluşturmak  
- `grpcurl` aracı ile komut satırından testler gerçekleştirmek  

---

## 🧰 KULLANILAN TEKNOLOJİLER

- Python 3  
- grpcio  
- grpcio-tools  
- grpcio-reflection  
- grpcurl  

---

## 📚 VARLIKLAR VE ALANLARI

### 📘 1. Books

- **id** → string (UUID formatında)  
- **title** → string  
- **author** → string  
- **isbn** → string (ISBN-13 formatında)  
- **publisher** → string  
- **pageCount** → integer  
- **stock** → integer  

### 👤 2. Students

- **id** → string (UUID formatında)  
- **name** → string  
- **studentNumber** → string  
- **email** → string (geçerli e-posta)  
- **isActive** → boolean  

### 🔁 3. Loans

- **id** → string (UUID formatında)  
- **studentId** → string  
- **bookId** → string  
- **loanDate** → string (tarih formatında)  
- **returnDate** → string (nullable)  
- **status** → enum (`ongoing`, `returned`, `late`)  

---

## 🔧 SERVİSLER VE METOTLAR

### 📗 BookService

- **ListBooks**  
- **GetBook**  
- **AddBook**  
- **UpdateBook**  
- **DeleteBook**  

### 🧑‍🎓 StudentService

- **ListStudents**  
- **GetStudent**  
- **AddStudent**  
- **UpdateStudent**  
- **DeleteStudent**  

### 🔄 LoanService

- **ListLoans**  
- **GetLoan**  
- **BorrowBook**  
- **ReturnBook**  

---

## 📁 PROJE KLASÖR YAPISI

```
/ (kök dizin)
├── university.proto             → Protobuf tanımı
├── server.py                   → gRPC sunucu uygulaması
├── client.py                   → gRPC istemci uygulaması
├── grpcurl-tests.md            → grpcurl test komutları ve çıktılar
├── DELIVERY.md                 → Teslim dosyası
├── university_pb2.py           → (protoc ile otomatik üretilir, git'e eklenmez)
├── university_pb2_grpc.py      → (protoc ile otomatik üretilir, git'e eklenmez)
```

---

## ✅ `.PROTO` DOSYASI ÖZETİ

- `syntax = "proto3"`  
- `package university`  
- 3 adet servis tanımı: **BookService**, **StudentService**, **LoanService**  
- Her varlık için CRUD ve özel işlemler tanımlandı  
- Enum: **LoanStatus**  
- Tüm metotlar İngilizce ve okunabilir biçimde yazılmıştır  

---

## ⚙️ UYGULAMAYI ÇALIŞTIRMA

**1. Bağımlılıkları kur:**

```
pip install grpcio grpcio-tools grpcio-reflection
```

**2. Stub dosyalarını üret (.proto'dan):**

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto
```

**3. Sunucuyu başlat:**

```
python server.py
```

**4. İstemciyi çalıştır:**

```
python client.py
```

---

## 🧪 `GRPCURL` İLE TEST

### Reflection ile servisleri listele:
```
grpcurl -plaintext localhost:50051 list
```

### Reflection desteklenmiyorsa `.proto` ile test:
```
grpcurl -plaintext -proto university.proto -d "{ \"title\": \"Clean Code\", \"author\": \"Robert C. Martin\", \"isbn\": \"9780132350884\", \"publisher\": \"Prentice Hall\", \"pageCount\": 464, \"stock\": 10 }" localhost:50051 university.BookService/AddBook
```

> Tüm test çıktıları ve komutlar `grpcurl-tests.md` dosyasında belgelenmiştir.

---

## 📌 NOTLAR

- Sunucu uygulaması **mock verilerle** çalışır  
- grpcurl testleri gerçekleştirilmiştir  
- `university_pb2.py` ve `university_pb2_grpc.py` dosyaları **.gitignore** ile hariç tutulmalıdır  
- Proje yönergeye %100 uygundur  

---

## 👩‍💻 GELİŞTİRİCİ

**Ad Soyad:** Serpil Çobanlar 
**Ders:** Açık Kaynak Kodlu Yazılımlar  
**Proje:** Protocol Buffers & gRPC ile Üniversite Kütüphane Sistemi
