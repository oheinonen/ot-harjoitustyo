import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_rahaa_kassassa_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_lounaita_myyty_nolla(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat,0)

    # Käteisostot
    def test_edullisen_lounaan_osto_käteisellä_muuttaa_kassan_arvoa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_maukkaan_lounaan_osto_käteisellä_muuttaa_kassan_arvoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullisen_lounaan_osto_käteisellä_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
  
    def test_maukkaan_lounaan_osto_käteisellä_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edullisen_lounaan_osto_käteisellä_muokkaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukkaan_lounaan_osto_käteisellä_muokkaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def edullisen_lounaan_osto_liian_vähän_käteistä_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def maukkaan_lounaan_osto_liian_vähän_käteistä_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_osto_käteisellä_vaihtoraha_oikein_rahat_ei_riitä(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
    
    def test_edullisen_lounaan_osto_käteisellä_vaihtoraha_oikein_rahat_ei_riitä(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_edullisen_lounaan_osto_käteisellä_liian_vähän_rahaa_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukkaan_lounaan_osto_käteisellä_liian_vähän_rahaa_lounaat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat,0)
 
    # Korttiostot

    def test_edullisen_lounaan_osto_kortilla_toimii_kun_rahaa_riittää(self):
        maksukortti = Maksukortti(10000)
        res = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(True,res)
        self.assertEqual(maksukortti.saldo, 9760)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukkaan_lounaan_osto_kortilla_toimii_kun_rahaa_riittää(self):
        maksukortti = Maksukortti(10000)
        res = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(True,res)
        self.assertEqual(maksukortti.saldo,9600)
        self.assertEqual(self.kassapaate.maukkaat,1)


    def test_edullisen_lounaan_osto_kortilla_ei_toimi_kun_raha_loppu(self):
        maksukortti = Maksukortti(100)
        res = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(False,res)
        self.assertEqual(maksukortti.saldo,100)
        self.assertEqual(self.kassapaate.edulliset,0)


    def test_maukkaan_lounaan_osto_kortilla_ei_toimi_kun_raha_loppu(self):
        maksukortti = Maksukortti(100)
        res = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(False,res)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_lataa_rahaa_kortille_muuttaa_kortin_ja_kassan_saldoa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100500)
        self.assertEqual(maksukortti.saldo,1500)
    
    def test_lataa_rahaa_kortille_negatiivinen_arvo_ei_tee_muutoksia(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,-500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(maksukortti.saldo,1000)