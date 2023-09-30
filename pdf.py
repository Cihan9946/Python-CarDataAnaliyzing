import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages 
import pandas as pd
 
df=pd.read_csv("cars.csv")


# PDF dosyasını oluşturmak için PdfPages kullanın 
with PdfPages('grafik_ve_yorum_v3.pdf') as pdf: 



# Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """
CARS . CSV VERIANALIZI
Bu sunumda bir csv veri setini
python içinde pandas ile okuyarak
analiz yapmayı ve python
kütüphanesindeki matplotlibi
kullanarak grafiği elde etmeyi
yorumlamayı ve veri incelemesinde
kolaylık sağlar.
        
Bu veri seti farklı araç modellerine ait bilgileri gösteren tablodur.
Bu tablo 9 sütun ve 4340 satırdan oluşur.


=> name => araç marka model adı
=> year => ara. üretim yılı
=> selling_price => araç satış fiyatı(TL)
=> km_driven => aracın kilometre kullanımı
=> fuel => arac yakıt tipi
=> seller_type => araç satıcı tipi
=> transmission => arac vites tipi (manual or automatic)
=> owner => aracın sahiplik durumudur""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
 
    # Yorumları PDF dosyasına ekleyin 
    pdf.savefig() 

 
  # 1. Yakıt türlerine göre satış fiyatı dağılımı
    plt.figure(figsize=(10, 6))
    for fuel_type in df['fuel'].unique():
        plt.hist(df[df['fuel'] == fuel_type]['selling_price'], alpha=0.6, label=fuel_type)
    plt.xlabel('Satış Fiyatı')
    plt.ylabel('Araç Sayısı')
    plt.title('Yakıt Türlerine Göre Satış Fiyatı Dağılımı')
    plt.legend()
    # Yorumlar için yeni bir sayfa oluşturun ve grafiği ekleyin 
    pdf.savefig() 
 

    # Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Bu grafikte petrol kullanan araç sayısı fazla olmasını 
    rağmen fiyatı en düşük seviyedefakat dizel araçlarında 
    kullanımı fazla olmasına rağmen fiyat olarak herzaman 
    en uygun araçları sunmaz. Dizel araç fiyatları değişiklik gösterebilir.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
 
    # Yorumları PDF dosyasına ekleyin 
    pdf.savefig() 
 

# 2. Vites tipine göre yakıt türü dağılımı
    plt.figure(figsize=(8, 6))
    pd.crosstab(df['transmission'], df['fuel']).plot(kind='bar', stacked=True)
    plt.xlabel('Vites Tipi')
    plt.ylabel('Araç Sayısı')
    plt.title('Vites Tipine Göre Yakıt Türü Dağılımı')
    plt.legend(title='Yakıt Türü')

    pdf.savefig() 
 
 
    # Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Vites Türü ve Yakıt Türü Arasındaki Bağlantı

Grafiği incelediğmizde manuel
araçlardaki yakıttüründe
çeşitlilik görünürken otomatik
araçlarda bu çeşitliliğe
rastlamıyoruz.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
    
    # Yorumları PDF dosyasına ekleyin 
    pdf.savefig() 


#4.Sahip sayısına göre araç sayısı dağılımı
    plt.figure(figsize=(16, 12))
    df['owner'].value_counts().plot(kind='bar')
    plt.xlabel('Sahip Sayısı')
    plt.ylabel('Araç Sayısı')
    plt.title('Sahip Sayısına Göre Araç Sayısı Dağılımı')
 
    pdf.savefig() 
 
 
    # Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Satıcı Tipi Fiyat İlişkisi
    Grafiği incelediğimizde aracın ilk
    sahibinin daha pahalıya sattığını
    görebiliriz. Ayrıca aracın el
    değiştirmesiyle fiyatı arasında
    ters orantı olduğunuda
    görebiliyoruz.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
 
    # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()


    # 8. Yakıt türüne göre ortalama satış fiyatı
    avg_price_by_fuel = df.groupby('fuel')['selling_price'].mean()
    plt.figure(figsize=(8, 6))
    avg_price_by_fuel.plot(kind='bar')
    plt.xlabel('Yakıt Türü')
    plt.ylabel('Ortalama Satış Fiyatı')
    plt.title('Yakıt Türüne Göre Ortalama Satış Fiyatı')

    pdf.savefig() 
 

    # Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Bu grafikte :
    Dizel araçların ortalama satış fiyatı belirgin şekilde diğer 
    yakıt türlerine göre yüksek görnmektedir. CNG , petrol ve elektrik türlerinin
    ortalama satış fiyatları ise neredeyse benzer görünmektedir.LPG ise maliyet 
    olarak en düşüğüdür.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
 
    # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()


    # 9. Vites tipine göre satış fiyatı dağılımı
    plt.figure(figsize=(10, 6))
    for transmission_type in df['transmission'].unique():
            plt.hist(df[df['transmission'] == transmission_type]['selling_price'], alpha=0.6, label=transmission_type)
    plt.xlabel('Satış Fiyatı')
    plt.ylabel('Araç Sayısı')
    plt.title('Vites Tipine Göre Satış Fiyatı Dağılımı')
    plt.legend()

    pdf.savefig()


    # Metin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Bu grafikte :
    Manuel araç sayısının otomotik araç sayısına oranın çok daha fazla 
    olduğu görülüyor. Bunun yanı sıra manuel araçların fiyatlarıda otomotik
    araçlara göre oldukça avantajlı olduğu gözleniyor. 
    Otomotik araç fiyatları ise oldukça değişkenlik gösteriyor manuelde ise bunun tam 
    zıttı olarak manuel araç fiyatları arasındaki fark oldulça düşük.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 
    
        # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()


   


    # 11. Yakıt türü ve vites tipine göre araç sayısı dağılımı
    grouped_df = df.groupby(['fuel', 'transmission']).size().unstack()
    grouped_df.plot(kind='bar', stacked=True, figsize=(10, 8))
    plt.xlabel('Yakıt Türü')
    plt.ylabel('Araç Sayısı')
    plt.title('Yakıt Türü ve Vites Tipine Göre Araç Sayısı')
    pdf.savefig()


    # Mtin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Bu grafikte :
    LPG ve CNG yakıt türlerinde otomotik seçeneğinin sunulmadığı gözleniyor
    bu yakıt türlerinin tamamı manuel. diğer yakıt türlerinde ise manuel 
    sayısının otomotiğe göre çok daha fazla olduğu görülüyor. Verinin diğer
    grafikleri de incelendiğinde LPG ve CNG türlerinin ekonomik araçlarda kullanıldığı
    ve manuel araç maliyetinin otomotikten  daha düşük olduğu gözleniyor. """ 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 

        # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()


    # 12 Sahip sayısına göre bir pasta grafiği oluşturma
    owner_counts = df['owner'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(owner_counts, labels=owner_counts.index, autopct='%1.1f%%')
    plt.title('Araç Sahip Sayısı Dağılımı')
    pdf.savefig()


    # Mtin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """Bu grafikte :
    Genelde araçların sahipleri araçlarını uzun süre kullanıldığı anlaşılıyor.
    Kullanıcılar araçlarından çabuk sıkılmadıkları ve ticari kaygı gütmedikleride bu 
    grafikten çıkabilcek bir sonuçtur.""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 

        # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()


    # Mtin kutusunu oluşturun ve özelliklerini belirleyin (yorumlarınızı buraya yazın) 
    textbox_text = """


    Mustafa Cihan İNCİR     




""" 
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ax.axis('off') 
    textbox_kwargs = dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.5) 
    ax.text(0.5, 0.5, textbox_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='center', horizontalalignment='center', bbox=textbox_kwargs) 

        # Yorumları PDF dosyasına ekleyin 
    pdf.savefig()
