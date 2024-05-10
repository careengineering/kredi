import model
import streamlit as st


st.sidebar.title("Veriler")
yas = st.sidebar.slider('Yaş aralığı', 18, 100, (25, 65))

if yas[1]<=yas[0]:
  st.write("Yaş aralık şeklinde seçilmelidir")
  st.stop()

hedef_ay = (yas[1]-yas[0])*12

aylik_sabit_birikim_tutari =st.sidebar.number_input("Aylık sabit birikim tutarı", value=3000.0)
rezidans_alis_fiyati = st.sidebar.number_input("Rezidans Alış Fiyatı", value=1250000.0)
rezidans_kira_tutari = st.sidebar.number_input("Rezidans Kira Bedeli", value=8000.0)
pesinat_orani = st.sidebar.number_input("Peşinat Oranı (%)", value=20.0) / 100
kredi_faiz_orani = st.sidebar.number_input("Kredi Faiz Oranı (%)", value=1.0) / 100
faiz_süresi_yil = st.sidebar.number_input("Kredi Faiz Süresi (yıl)", value=15)
ev_pesinat_tutari = round(rezidans_alis_fiyati * pesinat_orani,2)
kredi_tutari = rezidans_alis_fiyati - ev_pesinat_tutari



toplam_birikim = 0
ev_sayisi = 0
krediler = []

for i in range(hedef_ay):
  if ev_sayisi>0:
    aylik_birikim_tutari = ev_sayisi*rezidans_kira_tutari + aylik_sabit_birikim_tutari
    for k in krediler:
      if k.taksitler:
        toplam_birikim -= k.taksitler[0]
        k.odeme()
  else:
    aylik_birikim_tutari = aylik_sabit_birikim_tutari

  toplam_birikim += aylik_birikim_tutari

  if toplam_birikim>=ev_pesinat_tutari:
    ev_sayisi +=1
    kredi = model.Kredi(kredi_tutari,kredi_faiz_orani,faiz_süresi_yil)
    krediler.append(kredi)
    toplam_birikim -= ev_pesinat_tutari

st.subheader("Hedef yıl sonunda: ")
st.write(f"Toplam aylık gelir: {aylik_birikim_tutari:,.2f} TL")
st.write(f"Toplam ev sayısı: {ev_sayisi}")



if krediler:
  toplam_borc = 0
  for k in krediler:
    if k.taksitler:
      toplam_borc += sum(k.taksitler)

  st.write(f"Toplam kalan kredi borcu: {toplam_borc:,.2f} TL")



  
