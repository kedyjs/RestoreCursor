# 🔄 Cursor ID Sıfırlama Aracı
<div align="center">

![GitHub stars](https://img.shields.io/github/stars/kedyjs/RestoreCursor?style=social)
![GitHub forks](https://img.shields.io/github/forks/kedyjs/RestoreCursor?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/kedyjs/RestoreCursor?style=social)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img src="cursor-logo.jpg" alt="Cursor Logo" width="200"/>

*Cursor editörü için geliştirilmiş telemetri ID sıfırlama aracı*

[🚀 Hızlı Başlangıç](#-hızlı-başlangıç) •
[📖 Dökümantasyon](#-dökümantasyon) •
[🛠️ Kurulum](#%EF%B8%8F-kurulum) •
[💡 Örnekler](#-örnekler) •
[🤝 Katkıda Bulunun](#-katkıda-bulunun)

</div>

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Sistem Gereksinimleri](#-sistem-gereksinimleri)
- [Kurulum](#%EF%B8%8F-kurulum)
- [Kullanım](#-kullanım)
- [Sık Sorulan Sorular](#-sık-sorulan-sorular)
- [Sorun Giderme](#-sorun-giderme)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Değişiklik Günlüğü](#-değişiklik-günlüğü)
- [Lisans](#-lisans)
- [İletişim](#-iletişim)

## 🎯 Proje Hakkında

Cursor ID Sıfırlama Aracı, Cursor editörünün telemetri verilerini yönetmenizi sağlayan güçlü bir Python uygulamasıdır. Bu araç sayesinde:

- Telemetri ID'lerinizi güvenli bir şekilde sıfırlayabilir
- Otomatik yedekleme ile veri kaybını önleyebilir
- Çoklu işletim sistemi desteği ile her platformda çalışabilirsiniz

## ✨ Özellikler

### 🛡️ Güvenlik Özellikleri
- Otomatik yedekleme sistemi
- Tarih-saat damgalı yedek dosyaları

### 💻 Platform Desteği
- Windows 10/11
- macOS (Catalina ve üzeri)
- Linux (Ubuntu, Fedora, Debian)

### 🎛️ Gelişmiş Özellikler
- JSON yapılandırma desteği
- Özelleştirilebilir yedekleme konumları
- Detaylı hata ayıklama çıktıları

## 🔧 Sistem Gereksinimleri

- Python 3.6+
- 50MB boş disk alanı
- İnternet bağlantısı (kurulum için)

## 🛠️ Kurulum

### 1. Repository'yi Klonlayın
```bash
git clone https://github.com/kedyjs/RestoreCursor.git
cd RestoreCursor
```


### 2. Bağımlılıkları Yükleyin
```bash
python main.py
```


### Çıktı Örneği
```json
{
"machineId": "1a2b3c4d5e6f...",
"macMachineId": "7g8h9i0j...",
"devDeviceId": "550e8400-e29b-41d4-a716..."
}
```

## 📁 Dosya Yapısı
```bash
RestoreCursor/
├── main.py # Ana program dosyası
├── requirements.txt # Bağımlılıklar
├── LICENSE # Lisans dosyası
├── README.md # Dökümantasyon
└── tests/ # Test dosyaları
└── test_main.py # Birim testleri
```


## ❓ Sık Sorulan Sorular

<details>
<summary><b>Program güvenli mi?</b></summary>
Evet, program açık kaynak kodludur ve tüm işlemler şeffaf bir şekilde gerçekleştirilir.
</details>

<details>
<summary><b>Eski ID'lerimi geri yükleyebilir miyim?</b></summary>
Evet, program otomatik olarak yedek aldığı için eski dosyalarınızı geri yükleyebilirsiniz.
</details>

## 🔍 Sorun Giderme

### Genel Sorunlar ve Çözümleri

| Sorun | Çözüm |
|-------|--------|
| Program başlatılamıyor | Python sürümünüzü kontrol edin |
| Dosya bulunamadı hatası | Cursor'un yüklü olduğundan emin olun |
| Yetki hatası | Yönetici olarak çalıştırın |

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📜 Değişiklik Günlüğü

### [1.0.0] - 2024-03-XX
- İlk sürüm yayınlandı
- Temel özellikler eklendi
- Çoklu platform desteği

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

Proje Sahibi - [@Githubkedyjs](https://github.com/kedyjs)

Proje Linki: [https://github.com/kedyjs/RestoreCursor](https://github.com/kedyjs/RestoreCursor)

---

<div align="center">

### ⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

<a href="https://github.com/kedyjs/RestoreCursor/stargazers">
    <img src="https://img.shields.io/github/stars/kedyjs/RestoreCursor?style=social" alt="stars">
</a>

</div>
