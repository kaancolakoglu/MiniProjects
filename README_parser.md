# Text to CSV Parser

Bu proje, yapılandırılmış tablo verilerini ayrıştırarak CSV formatına dönüştüren bir Python scripti içermektedir.

## Dosyalar

- `text_to_csv_parser.py` - Ana parser scripti
- `test_parser.py` - Test scripti
- `output.csv` - Örnek çıktı dosyası
- `README_parser.md` - Bu dokümantasyon

## Kullanım

### Basit Kullanım

```python
from text_to_csv_parser import parse_and_convert_to_csv

# Metninizi buraya yapıştırın
text_input = """
| | Article Name.pdf | KEEP | Reason text here | Input requirements. Kod/Denklik: Formula here. |
"""

# Parse et ve CSV'ye dönüştür
record_count = parse_and_convert_to_csv(text_input, "my_output.csv")
print(f"{record_count} kayıt işlendi")
```

### Komut Satırından Çalıştırma

```bash
python text_to_csv_parser.py
```

Bu komut, script içindeki örnek metni işleyerek `output.csv` dosyasını oluşturur.

## Beklenen Metin Formatı

Parser aşağıdaki formatta tablo verilerini bekler:

```
| | Makale_Adı.pdf | KARAR | Açıklama metni | Girdi gereksinimi. Kod/Denklik: Formül. |
```

### Sütun Açıklamaları

1. **Boş sütun** - İlk sütun boş olmalıdır
2. **Makale Adı** - Dosya adı veya makale adı
3. **Karar** - `KEEP`, `DISCARD`, veya `MAYBE` değerlerinden biri
4. **Neden** - Model açıklaması ve gerekçe
5. **Kombine alan** - "Girdi Gereksinimi" ve "Kod/Denklik" bilgileri

Son alan otomatik olarak iki ayrı sütuna bölünür:
- **Girdi Gereksinimi** - Girdi gereksinimleri
- **Kod/Denklik** - Kodlar ve formüller

## Test Etme

Test scriptini çalıştırmak için:

```bash
python test_parser.py
```

Bu script şu testleri yapar:
- Temel işlevsellik testi
- Boş girdi kontrolü
- Geçersiz format kontrolü
- Örnek veri testi

## Çıktı Formatı

CSV dosyası şu sütunları içerir:
- Makale Adı
- Karar
- Neden
- Girdi Gereksinimi
- Kod/Denklik

Ayırıcı karakter olarak noktalı virgül (`;`) kullanılır ve UTF-8 encoding ile kaydedilir.

## Hata Yönetimi

Script şu durumları kontrol eder:
- Boş veya geçersiz girdi metni
- Uygun olmayan tablo formatı
- Dosya yazma hataları

Hata durumlarında uygun mesajlar gösterilir ve fonksiyon 0 döndürür.