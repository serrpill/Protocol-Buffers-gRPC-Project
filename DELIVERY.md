# gRPC Uygulama Geliştirme Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri
- **Ad Soyad**: Serpil Çobanlar
- **Öğrenci Numarası**: 170422055
- **Kullanılan Programlama Dili**: Python 3

---

## 📦 GitHub Repo

Lütfen projenizin tamamını bir GitHub reposuna yükleyiniz. `.proto` dosyasından üretilecek stub kodlar hariç!

### 🔗 GitHub Repo Linki
https://github.com/serrpill/Protocol-Buffers-gRPC-Project

---

## 📄 .proto Dosyası

- `.proto` dosyasının adı(ları): `university.proto`
- Tanımlanan servisler ve metod sayısı: 3 servis (BookService, StudentService, LoanService) – toplam 14 metod
- Enum kullanımınız var mı? Hangi mesajda?: Evet, `LoanStatus` isimli enum `Loan` mesajında kullanıldı.
- Dili (Türkçe/İngilizce) nasıl kullandınız?: Mesaj ve metot isimlerinde İngilizce kullanılmıştır, açıklamalar Türkçedir.

---

## 🧪 grpcurl Test Dokümantasyonu

`grpcurl-tests.md` dosyasında servisler ile ilgili kullanılmak istenen tüm komutlar örnek olarak belirtilmiştir. Ancak:

- grpcurl çalıştırılmak istendiğinde reflection desteği olmadığı için `list` komutu çalışmadı.
- Bu durumu çözmek için `grpcio-reflection` eklendi ve sunucuya reflection entegre edildi.
- Ancak sistem `grpcurl` aracını çalıştırırken Windows tarafında `cmdlet` hatası verdi ve `exe` dosyası çalışmadı.
- Bunun üzerine ilgili komutlar hazırlandı ve manuel testlerle işlevsellik doğrulandı.
- grpcurl çıktıları doğrudan alınamasa da alternatif test yöntemleriyle servislerin çalıştığı belgelenmiştir.

---

## 🛠️ Derleme ve Çalıştırma Adımları

Projeyi çalıştırmak için şu komutlar uygulanmıştır:

```bash
# Python için:
pip install grpcio grpcio-tools grpcio-reflection

# .proto dosyasından stub üretme:
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto

# Sunucuyu çalıştırma:
python server.py

# İstemciyi çalıştırma:
python client.py


## ⚠️ Kontrol Listesi

- [x] Stub dosyaları GitHub reposuna eklenmedi  
- [x] grpcurl komutları test belgesinde yer alıyor  
- [x] Ekran görüntüleri test belgesine eklendi (varsa)  
- [x] Tüm servisler çalışır durumda  
- [x] README.md içinde yeterli açıklama var  

---

## 📌 Ek Açıklamalar

- `grpcurl.exe`, Windows işletim sisteminde doğrudan çalıştırılamadığı için test komutları hazırlanmış ancak çalıştırılamamıştır.  
- Bu nedenle sunucu ve istemci uygulamaları üzerinden işlevsel testler yapılmıştır.  
- `client.py` üzerinden tüm servis metotları çağrılarak uygulamanın çalıştığı doğrulanmıştır.  
- `.proto`, `README.md`, `grpcurl-tests.md` ve Python uygulama dosyaları teslimde eksiksiz olarak yer almaktadır.

---

