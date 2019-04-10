import unittest
import src.get_voucher as get_voucher

class TestGetVoucher(unittest.TestCase):
    def test_html(self):
        self.assertIsNotNone(get_voucher.open_url("http://lafuenteunlp.com.ar/web/"), "Should be 6")

    def test_sum_tuple(self):
        self.assertTrue(get_voucher.get_voucher(get_voucher.open_url("http://lafuenteunlp.com.ar/web/")) != "0")

