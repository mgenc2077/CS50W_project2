class mesaj:
    counter = 1
    def __init__(self, nick, soz, kanal, zaman):
        self.id = mesaj.counter
        mesaj.counter += 1
        self.nick = nick
        self.soz = soz
        self.kanal = kanal
        self.zaman = zaman