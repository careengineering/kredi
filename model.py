class Kredi:
  son_kredi_no = 0

  def __init__(self,kredi_tutari,kredi_faiz_orani,faiz_suresi_yil):
    self.kredi_tutari = kredi_tutari
    self.kredi_faiz_orani = kredi_faiz_orani
    self.faiz_suresi_yil = faiz_suresi_yil

    self.taksitler = self.taksit_hesapla()

    Kredi.son_kredi_no += 1
    self.no = Kredi.son_kredi_no

  def taksit_hesapla(self):
    faiz_suresi_ay = self.faiz_suresi_yil * 12
    kredi_taksit_tutari = round(self.kredi_tutari / faiz_suresi_ay,2)
    son_kredi_taksit_tutari = round(self.kredi_tutari - round((faiz_suresi_ay-1)*kredi_taksit_tutari,2),2)

    taksitler = []
    for i in range(faiz_suresi_ay-1):
      taksitler.append(kredi_taksit_tutari)
    taksitler.append(son_kredi_taksit_tutari)
    return taksitler

  def odeme(self):
    self.taksitler.pop(0)
    return self.taksitler

