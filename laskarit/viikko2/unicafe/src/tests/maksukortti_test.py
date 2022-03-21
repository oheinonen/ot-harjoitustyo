import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luotu_kortti_arvo_oikein(self):
        self.assertEqual( self.maksukortti.saldo, 10)
    def test_rahan_lataaminen_muuttaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual( self.maksukortti.saldo, 20)

    def test_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual( self.maksukortti.saldo,5 )

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
    
    def test_saldo_euroissa_näkyy_oikein(self):
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")
