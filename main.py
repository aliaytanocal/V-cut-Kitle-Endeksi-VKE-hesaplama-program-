#Bu kısımda gerekli kütüphaneleri içe aktarıyoruz.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

#Bu kısımda bir pencere oluşturuyoruz.
class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vücut Kitle Endeksi Hesaplama")
        self.setGeometry(100, 100, 300, 200)

        #Bu kısımda pencerenin içeriğini oluşturuyoruz.
        #Bu içeriğe, boy ve kilo girdi alanları ve hesapla düğmesi ekliyoruz.
        self.boy = QtWidgets.QLineEdit(self)
        self.boy.move(100, 50)
        self.kilo = QtWidgets.QLineEdit(self)
        self.kilo.move(100, 75)
        self.hesapla = QtWidgets.QPushButton("Hesapla", self)
        self.hesapla.move(100, 100)
        self.hesapla.clicked.connect(self.vke_hesapla)

    #Bu kısımda VKE hesaplanıyor ve sonuç ekrana yazdırılıyor.
    def vke_hesapla(self):
        boy = float(self.boy.text())
        kilo = float(self.kilo.text())
        vke = kilo / (boy/100)**2
        self.sonuc = QtWidgets.QLabel("VKE: " + str(vke), self)
        self.sonuc.move(100, 125)
        self.sonuc.show()

#Bu kısımda pencere çalıştırılıyor.
if __name__ == "__main__":
    uygulama = QApplication([])
    pencere = Pencere()
    pencere.show()
    uygulama.exec_()
