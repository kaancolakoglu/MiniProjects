#!/usr/bin/env python3
"""
Test script for text_to_csv_parser.py
Bu script temel işlevselliği test eder.
"""

import os
import csv
from text_to_csv_parser import parse_and_convert_to_csv

def test_basic_functionality():
    """Temel işlevselliği test eder"""
    print("Test 1: Temel işlevsellik testi...")
    
    # Test verisi - basit bir tablo yapısı (4 sütun format)
    test_input = """
    | | Test Article 1.pdf | KEEP | Model Önerisi: Test model açıklaması. | Girdi Gereksinimi: Test gereksinimi. Kod/Denklik: Test formülü. |
    | | Test Article 2.pdf | DISCARD | Model Önerisi: Başka bir test. | Girdi Gereksinimi: Başka gereksinim. Kod/Denklik: Başka formül. |
    """
    
    test_filename = "test_output.csv"
    
    # Test et
    result = parse_and_convert_to_csv(test_input, test_filename)
    
    if result == 2:
        print("✓ Test geçti: 2 kayıt başarıyla ayrıştırıldı")
        
        # CSV dosyasını kontrol et
        if os.path.exists(test_filename):
            with open(test_filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                rows = list(reader)
                
                if len(rows) == 2:
                    print("✓ Test geçti: CSV dosyasında doğru sayıda kayıt")
                    
                    # İlk kaydı kontrol et
                    first_row = rows[0]
                    if (first_row['Makale Adı'].strip() == 'Test Article 1.pdf' and 
                        first_row['Karar'].strip() == 'KEEP'):
                        print("✓ Test geçti: Veri doğru ayrıştırıldı")
                    else:
                        print("✗ Test başarısız: Veri yanlış ayrıştırıldı")
                        print(f"Beklenen: Test Article 1.pdf, KEEP")
                        print(f"Bulunan: {first_row['Makale Adı']}, {first_row['Karar']}")
                else:
                    print(f"✗ Test başarısız: Beklenen 2 kayıt, bulunan {len(rows)}")
            
            # Test dosyasını temizle
            os.remove(test_filename)
        else:
            print("✗ Test başarısız: CSV dosyası oluşturulmadı")
    else:
        print(f"✗ Test başarısız: Beklenen 2 kayıt, ayrıştırılan {result}")

def test_empty_input():
    """Boş girdi testi"""
    print("\nTest 2: Boş girdi testi...")
    
    result = parse_and_convert_to_csv("", "empty_test.csv")
    
    if result == 0:
        print("✓ Test geçti: Boş girdi doğru şekilde işlendi")
    else:
        print(f"✗ Test başarısız: Boş girdi için beklenmeyen sonuç: {result}")

def test_invalid_format():
    """Geçersiz format testi"""
    print("\nTest 3: Geçersiz format testi...")
    
    invalid_input = "Bu sadece düz metin, tablo formatı değil"
    result = parse_and_convert_to_csv(invalid_input, "invalid_test.csv")
    
    if result == 0:
        print("✓ Test geçti: Geçersiz format doğru şekilde reddedildi")
    else:
        print(f"✗ Test başarısız: Geçersiz format için beklenmeyen sonuç: {result}")

def test_sample_data():
    """Örnek veri ile test"""
    print("\nTest 4: Mevcut örnek veri testi...")
    
    # Original sample data'dan bir kısmını test et
    sample_input = """
    | | Abreu et al. - 2013 - Using Multivariate Adaptive Regression Splines in the Construction of Simulated Soccer Team's Behavi.pdf | DISCARD | Model Önerisi: Bir futbol takımının davranış modellerini oluşturmak için Çok Değişkenli Uyarlanabilir Regresyon Splinleri (MARS) kullanılarak simüle edilmiş modeller geliştirilmiştir. | Girdi Gereksinimi: Yaklaşık altmış adet final oyun istatistiği gereklidir. Kod/Denklik: diff(A, I1, I2) formülleri. |
    """
    
    result = parse_and_convert_to_csv(sample_input, "sample_test.csv")
    
    if result == 1:
        print("✓ Test geçti: Örnek veri başarıyla ayrıştırıldı")
        # Test dosyasını temizle
        if os.path.exists("sample_test.csv"):
            os.remove("sample_test.csv")
    else:
        print(f"✗ Test başarısız: Örnek veri için beklenmeyen sonuç: {result}")

if __name__ == "__main__":
    print("Text to CSV Parser Test Süreci Başlıyor...\n")
    
    test_basic_functionality()
    test_empty_input()
    test_invalid_format()
    test_sample_data()
    
    print("\nTüm testler tamamlandı!")