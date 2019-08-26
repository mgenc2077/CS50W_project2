class mesaj:
    counter = 1
    def __init__(self, nick, soz, kanal, zaman):
        self.id = mesaj.counter
        mesaj.counter += 1
        self.nick = nick
        self.soz = soz
        self.kanal = kanal
        self.zaman = zaman

    def print_info(self):
        print(f"nick: {self.nick}")
        print(f"soz: {self.soz}")
        print(f"kanal: {self.kanal}")
        print(f"zaman: {self.zaman}")


#class uygun:
#    counter = 1
#    def __init__(self, nick, soz, zaman):
#        self.id = mesaj.counter
#        mesaj.counter += 1
#        self.nick = nick
#        self.soz = soz
#        self.zaman = zaman

class yeni_kanal:
    counter = 1
    def __init__(self, ad):
        self.id = mesaj.counter
        yeni_kanal.counter += 1
        self.ad = ad
        self.gecmis = []

    def add_mesaj(self, p):
        self.gecmis.append(p)
        p.mesaj_id = self.id

class kanal_listesi:
    counter = 1
    def __init__(self, ad):
        self.id = mesaj.counter
        kanal_listesi.counter += 1
        self.ad = ad
        self.liste = []

    def add_kanal(self, k):
        self.liste.append(k)
        k.yeni_id = self.id



