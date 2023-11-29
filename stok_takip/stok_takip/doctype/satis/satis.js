// Copyright (c) 2023, py2krnl and contributors
// For license information, please see license.txt

frappe.ui.form.on('Satis', {
    kar_payi(frm,cdt,cdn){
        frm.doc.urun_satis_tablo.forEach(function(row) {
            var karPayiYuzde = parseFloat(frm.doc.kar_payi) / 100;

            if(row.adet && row.urun)
            {
                frappe.db.get_doc("Urun", row.urun).then(doc => {
                   var normalFiyat = (doc.urun_fiyati * row.adet);
                   var karliSatisFiyati = normalFiyat + (normalFiyat * karPayiYuzde);
                   row.toplam_fiyat = karliSatisFiyati;
                   refresh_field("toplam_fiyat", cdn, "urun_satis_tablo");
               });
            }


        });
    }
})





frappe.ui.form.on('urun_child', {
	adet(frm, cdt, cdn) {
        //console.log(frm);
        //console.log(cdt);
		//console.log(cdn);
		var row = locals[cdt][cdn];
        var urun = row.urun;
        var karPayiYuzde = parseFloat(frm.doc.kar_payi) / 100;

        if(row.urun && row.adet)
        {
            frappe.db.get_doc("Urun", urun)
            .then(doc => {
                var normalFiyat = (doc.urun_fiyati * row.adet);
                var karliSatisFiyati = normalFiyat + (normalFiyat * karPayiYuzde);
                console.log("Doc İçeriği:", doc);
                console.log("Urun Adı:", doc.urun_adi);
                console.log("Urun Fiyati:", doc.urun_fiyati);
                console.log("Kâr Payı: ", frm.doc.kar_payi);
                row.toplam_fiyat = karliSatisFiyati;
                refresh_field("toplam_fiyat", cdn, "urun_satis_tablo");
    
            })
            .catch(err => {
                console.error("Hata:", err);
            });
        }
        


        //debugger;
	}
})