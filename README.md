# Blog Optimizer AI

Blog yazılarını SEO uyumlu ve özgün bir şekilde yeniden yazan yapay zeka destekli bir web uygulaması.

## Özellikler

- Blog içeriğini SEO uyumlu hale getirme
- Özgün içerik oluşturma
- Meta açıklamaları ekleme
- Her paragraf için başlık önerisi
- İlgili anahtar kelimeler
- Modern ve kullanıcı dostu arayüz

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
cd Blog-Optimizer-AI
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun ve Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

4. Uygulamayı çalıştırın:
```bash
python app.py
```

5. Tarayıcınızda `http://localhost:5000` adresine gidin.

## Kullanım

1. Ana sayfadaki metin kutusuna orijinal blog içeriğinizi yapıştırın
2. "İçeriği Optimize Et" butonuna tıklayın
3. Optimize edilmiş içerik sağ taraftaki metin kutusunda görünecektir

## Teknolojiler

- Flask (Web Framework)
- Google Gemini API (AI Model)
- TailwindCSS (UI Framework)
- Font Awesome (Icons)

## Güvenlik Notları

- API anahtarınızı güvende tutun ve asla kaynak kodunuzda paylaşmayın
- `.env` dosyasını git versiyon kontrolüne eklemeyin

## Lisans

MIT 