import csv

# Klassen representerar ett supportärende.
# Varje ärende har id, kund, kategori, prioritet och status.
# Metoden visa_info visar information om ärendet.
# CSV-filen läses utanför klassen.

class SupportArende:
 
    def __init__(self, id, kund, kategori, prioritet, status):
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status
 
    def visa_info(self):
        return (
            f"ID: {self.id}, "
            f"Kund: {self.kund}, "
            f"Kategori: {self.kategori}, "
            f"Prioritet: {self.prioritet}, "
            f"Status: {self.status}"
        )
 
 
arenden = []
 
with open("data/supportarenden.csv", "r", encoding="utf-8") as fil:
    reader = csv.DictReader(fil)
 
    for rad in reader:
        arende = SupportArende(
            rad["id"],
            rad["kund"],
            rad["kategori"],
            rad["prioritet"],
            rad["status"]
        )
 
        arenden.append(arende)
 
 
for arende in arenden:
    print(arende.visa_info())