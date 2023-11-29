# Copyright (c) 2023, py2krnl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Satis(Document):
	def before_save(self):
		self.elde_edilen_kazanc = 0
		self.satis_genel_toplam = 0
		kar_payi = float(self.kar_payi / 100) # 0.kar_payi Örneğin =>> (15.0 / 100) = 0.15
		for doc in self.urun_satis_tablo:
			doc_urun = frappe.get_doc('Urun', doc.urun)
			toplam_fiyat = (doc_urun.urun_fiyati * doc.adet)
			karli_satis_fiyati = toplam_fiyat + (toplam_fiyat * kar_payi)
			doc.toplam_fiyat = karli_satis_fiyati
			self.satis_genel_toplam += karli_satis_fiyati
			self.elde_edilen_kazanc += (karli_satis_fiyati - toplam_fiyat)