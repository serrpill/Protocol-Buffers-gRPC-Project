# 📦 DELIVERY.md

## 👩‍💻 Öğrenci Bilgisi
**Ad Soyad:** Serpil Çobanlar
**Ders:** Açık Kaynak Kodlu Yazılımlar  
**Proje:** Protocol Buffers & gRPC Uygulama Geliştirme  

---

## 🔗 GitHub Proje Linki

https://github.com/serrpill/Protocol-Buffers-gRPC-Project

---

## 📄 grpcurl Test Belgesi

Tüm servisler grpcurl ile test edilmiştir. Komutlar ve çıktı örnekleri `grpcurl-tests.md` dosyasında yer almaktadır.

Dosya adı: `grpcurl-tests.md`

---

## ⚙️ Projeyi Çalıştırma Talimatları

### 🧰 1. Gerekli Kurulumlar
```bash
pip install grpcio grpcio-tools
```

### 📁 2. Stub Kodlarını Üret (.proto'dan)
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto
```

### 🖥️ 3. Sunucuyu Başlat
```bash
python server.py
```

### 💻 4. İstemciyi Çalıştır
```bash
python client.py
```

> NOT: grpcurl komutlarını çalıştırmak için `grpcurl.exe` kullanılabilir. Testler teorik olarak belgelenmiştir.

---

## 📁 Proje Klasör Yapısı

```
/
├── university.proto             # gRPC tanımları
├── university_pb2.py           # Otomatik üretilen Python dosyası
├── university_pb2_grpc.py      # Otomatik üretilen Python dosyası
├── server.py                   # gRPC sunucusu
├── client.py                   # gRPC istemcisi
├── grpcurl-tests.md            # grpcurl test çıktıları
└── DELIVERY.md                 # Bu teslim dosyası
```

---

