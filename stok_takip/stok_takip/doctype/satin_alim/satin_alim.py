# Copyright (c) 2023, py2krnl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SatinAlim(Document):
	def before_save(self):
		print("\n\n\n")
		genel_toplam = 0
		for child_grid in self.urun_child:
			child_doc = frappe.get_doc('Urun', child_grid.urun)
			urun_toplam_fiyat = child_doc.urun_fiyati * child_grid.adet
			child_grid.toplam_fiyat = urun_toplam_fiyat
			genel_toplam += urun_toplam_fiyat
		self.genel_toplam = genel_toplam
		print("\n\n\n")
