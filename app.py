import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

# Gemini API yapılandırması
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def rewrite_blog_content(original_content):
    prompt = f"""
    Aşağıdaki blog yazısını SEO uyumlu, özgün ve daha kapsamlı bir şekilde yeniden yaz.
    Şu noktalara dikkat et:
    - Orijinal içeriğin ana fikrini koru
    - SEO için anahtar kelimeleri doğal bir şekilde yerleştir
    - Daha detaylı ve zengin bir içerik oluştur
    - Tamamen özgün cümleler kullan
    - Meta açıklaması için uygun bir özet ekle
    - Her paragrafın başına uygun bir başlık ekle
    - Sonuna 5 adet alakalı anahtar kelime ekle
    
    Orijinal İçerik:
    {original_content}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"API Hatası: {str(e)}")
        raise Exception("İçerik oluşturulurken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json()
    original_content = data.get('content')
    
    if not original_content:
        return jsonify({'error': 'İçerik bulunamadı'}), 400
    
    try:
        rewritten_content = rewrite_blog_content(original_content)
        return jsonify({'rewritten_content': rewritten_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY bulunamadı. Lütfen .env dosyasını kontrol edin.")
    app.run(host='0.0.0.0', port=8080) 