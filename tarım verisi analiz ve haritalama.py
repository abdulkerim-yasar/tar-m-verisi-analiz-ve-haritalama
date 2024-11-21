import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. CSV Dosyasını Oku
# -------------------------------------------------
def load_csv(file_path):
    """Belirtilen dosyayi yükler ve DataFrame döndürür."""
    try:
        data = pd.read_csv(file_path)
        print("Veri başariyla yüklendi.")
        return data
    except FileNotFoundError:
        print(f"HATA: '{file_path}' bulunamadi. Lütfen doğru dosya yolunu kontrol edin.")
        return None
    except Exception as e:
        print(f"HATA: Dosya yüklenirken bir sorun oluştu: {e}")
        return None

# -------------------------------------------------
# 2. Harita Oluştur
# -------------------------------------------------
def create_map():
    """Örnek haritayi oluşturur ve 'map.html' olarak kaydeder."""
    try:
        # Harita merkezini belirle ve başlat
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Örnek veri noktaları
        folium.Marker([37.7749, -122.4194], popup='Buğday Alani').add_to(m)
        folium.Marker([35.6895, 139.6917], popup='Pirinç Alani').add_to(m)

        # Haritayı kaydet
        m.save('map.html')
        print("Harita başariyla 'map.html' dosyasina kaydedildi.")
    except Exception as e:
        print(f"HATA: Harita oluşturulurken bir sorun oluştu: {e}")

# -------------------------------------------------
# 3. Görselleştirme
# -------------------------------------------------
def plot_yield_analysis():
    """Mahsul verimliliği analizi grafiğini oluşturur."""
    # Örnek veri
    yield_data = {
        'Region': ['North America', 'Asia', 'Europe', 'Africa', 'South America'],
        'Wheat': [3.2, 4.1, 3.9, 2.1, 2.5],
        'Rice': [2.0, 4.5, 3.0, 1.8, 2.3],
        'Corn': [3.5, 4.0, 3.8, 2.0, 2.7]
    }

    try:
        # Veri çerçevesi oluştur
        df = pd.DataFrame(yield_data)

        # Veri çerçevesini görselleştirme için dönüştür
        df = df.melt(id_vars='Region', var_name='Crop', value_name='Yield')

        # Grafik oluştur
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Region', y='Yield', hue='Crop', data=df)
        plt.title('Verimlilik Analizi')
        plt.xlabel('Bölge')
        plt.ylabel('Verim (ton/ha)')
        plt.tight_layout()  # Görsel düzeni
        plt.show()
    except Exception as e:
        print(f"HATA: Grafik oluşturulurken bir sorun oluştu: {e}")

# -------------------------------------------------
# Ana Çalışma Bloğu
# -------------------------------------------------
if __name__ == "__main__":
    print("Tarim Verisi Analiz ve Haritalama Programi")

    # 1. Veri Yükleme
    csv_file = 'agriculture_data.csv'
    data = load_csv(csv_file)

    # 2. Harita Oluşturma
    create_map()

    # 3. Verimlilik Grafiği
    plot_yield_analysis()
