import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):

    """
    Konstruktori
    """

    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-5, -50)
        self.varasto3 = Varasto(5, 10)

    def test_konstruktori_ylimaaraisena(self):
        # saldo ylittää varastotilan, saldo asetetaan tilavuudeksi
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_konstruktori_negatiivisena(self):
        # Tilavuus asetetaan nollaksi
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
        # Saldo asetetaan nollaksi
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    """
    Lisays
    """

    def test_tyhja_lisays(self):
        # Negatiivinen lisäys ei tee muutoksia
        self.varasto3.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto3.saldo, 5)

    def test_liika_lisays(self):
        # Lisääminen yli rajojen lisää ainoastaan
        # tilavuuteen asti
        self.varasto3.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    """
    Ottaminen
    """

    def test_negatiivinen_ottaminen(self):
        # Negatiivisella ottamisella ei ole vaikutusta
        self.varasto3.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto3.saldo, 5)

    def test_saldon_ylitys_ottaessa(self):
        # Liian suurella otolla menee saldo vain nollaan
        self.varasto3.ota_varastosta(6)
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    """
    Muut
    """

    def test_str_palautus(self):
        # Testataan __str__:n tuloste
        varasto4 = Varasto(100, 100)

        teksti = str(varasto4)

        self.assertEqual(teksti, "saldo = 100, vielä tilaa 0")

