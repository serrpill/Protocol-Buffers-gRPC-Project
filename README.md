🎓 Üniversite Kütüphane Sistemi – gRPC Tabanlı

Bu proje, Açık Kaynak Kodlu Yazılımlar dersi kapsamında geliştirilmiş bir gRPC tabanlı üniversite kütüphane sistemidir. Uygulama, Protocol Buffers (.proto) kullanılarak tanımlanmış veri yapıları ve servisler aracılığıyla kitap, öğrenci ve ödünç alma işlemlerini yönetir.

🎯 Projenin Amaçları
Protobuf ile API tanımı yapmak

gRPC kullanarak sunucu ve istemci oluşturmak

Kitap, öğrenci ve ödünç işlemleri için CRUD servisleri yazmak

grpcurl aracı ile test işlemlerini komut satırından gerçekleştirmek

📦 Kullanılan Teknolojiler
Python 3

grpcio

grpcio-tools

grpcio-reflection

grpcurl (komut satırı testi için)

📚 Varlıklar ve Alanları
books

id (string, UUID formatında)

title (string)

author (string)

isbn (string, ISBN-13 formatında)

publisher (string)

pageCount (integer)

stock (integer)

students

id (string, UUID formatında)

name (string)

studentNumber (string)

email (string, e-posta formatında)

isActive (boolean)

loans

id (string, UUID formatında)

studentId (string)

bookId (string)

loanDate (string, tarih formatında)

returnDate (string, tarih formatında, nullable olabilir)

status (enum: "ongoing", "returned", "late")

🔧 Zorunlu Servis Metotları
Aşağıdaki işlevler .proto dosyasında servis olarak tanımlanmıştır:

BookService

Listeleme

Tekil görüntüleme

Ekleme

Güncelleme

Silme

StudentService

Listeleme

Tekil görüntüleme

Ekleme

Güncelleme

Silme

LoanService

Listeleme

Tekil görüntüleme

Ödünç alma

Kitap iade etme

📁 Proje Klasör Yapısı
Kök dizin:

university.proto → Protobuf tanımı (.proto dosyası)

university_pb2.py → Protoc ile otomatik üretilir (sunulmamalı)

university_pb2_grpc.py → Protoc ile otomatik üretilir (sunulmamalı)

server.py → gRPC sunucu uygulaması

client.py → gRPC istemci uygulaması

grpcurl-tests.md → grpcurl ile yapılan test komutları ve çıktıları

DELIVERY.md → Teslim dosyası (Google Classroom için)

✅ .proto Dosyasında Bulunması Gerekenler
syntax, package, option tanımları bulunur

3 adet service tanımı: BookService, StudentService, LoanService

Her varlık için CRUD ve işlevsel rpc tanımları yapılmıştır

Request ve response mesajları ayrı message olarak tanımlanmıştır

loans varlığında enum (LoanStatus) tanımı yapılmıştır

Kod stili okunabilir, İngilizce isimlendirme tercih edilmiştir

⚙️ Projeyi Çalıştırmak İçin
Gerekli Python kütüphanelerini yükleyin:

pip install grpcio grpcio-tools grpcio-reflection

.proto dosyasını derleyin:

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto

Sunucuyu başlatın:

python server.py

İstemciyi çalıştırın:

python client.py

🧪 grpcurl ile Test
Reflection desteği varsa servisleri listelemek için:

grpcurl -plaintext localhost:50051 list

Eğer yoksa, proto dosyası ile doğrudan komut kullanılabilir:

grpcurl -plaintext -proto university.proto -d "{ "title": "Clean Code", "author": "Robert C. Martin", "isbn": "9780132350884", "publisher": "Prentice Hall", "pageCount": 464, "stock": 10 }" localhost:50051 university.BookService/AddBook

Tüm test komutları ve örnek çıktılar grpcurl-tests.md dosyasında belgelenmiştir.

📌 Notlar ve Gereksinimler
Sunucu uygulaması gRPC'ye uygun şekilde, mock veri ile çalışmaktadır

İstemci uygulaması servis metotlarını başarıyla çağırmaktadır

grpcurl ile test yapılmıştır

Stub dosyaları (_pb2.py) repoya eklenmemeli, build sırasında oluşturulmalıdır

👤 Geliştirici
Ad: Serpil
Ders: Açık Kaynak Kodlu Yazılımlar
Proje: Protocol Buffers & gRPC Servis Geliştirme

