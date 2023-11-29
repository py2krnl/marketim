# Copyright (c) 2023, py2krnl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SatinAlim(Document):
	def before_save(self):
		print("\n\n\n")
		for doc in self.urun_child:
			doc_urun = frappe.get_doc('Urun', doc.urun)
			_toplam_fiyat = (doc_urun.urun_fiyati * doc.adet)
			doc.toplam_fiyat = _toplam_fiyat
			self.genel_toplam += _toplam_fiyat
		print("\n\n\n")
