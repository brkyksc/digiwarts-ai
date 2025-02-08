from app import app, db

with app.app_context():
    print("Veritabanı tabloları siliniyor...")
    db.drop_all()
    print("Veritabanı tabloları yeniden oluşturuluyor...")
    db.create_all()
    print("İşlem tamamlandı!") 