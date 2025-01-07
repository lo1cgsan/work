from peewee import *

baza = SqliteDatabase('slownik_p.db', pragmas={'foreign_keys': 1})

class Wyraz(Model):
    wyraz = CharField()

    class Meta:
        database = baza


class Znaczenie(Model):
    wyraz = ForeignKeyField(Wyraz, backref='znaczenia')
    znaczenie = CharField()

    class Meta:
        database = baza

def polacz():
    baza.connect()
    baza.create_tables([Wyraz, Znaczenie])

def zapisz_dane():
    if Wyraz.select().count() > 0:
        return
    slownik = {'go':['iść', 'biec'], 'watch': ['oglądać', 'uważać']}
    for k, v in slownik.items():
        w = Wyraz(wyraz=k)
        w.save()
        for z in v:
            z_obj = Znaczenie(wyraz=w, znaczenie=z)
            z_obj.save()
    baza.commit()

polacz()
zapisz_dane()

wyrazy = Wyraz.select(Wyraz, Znaczenie).join(Znaczenie).dicts()
for w in wyrazy:
    print(w['id'], w['wyraz'], w['znaczenie'])

# wyraz = Wyraz.select().where(Wyraz.wyraz == 'go2').get()
# print(wyraz.id, wyraz.wyraz)
# wyraz.wyraz = 'go2'
# wyraz.save()

wyraz = Wyraz.select().where(Wyraz.wyraz == 'go2').get()
print(wyraz.id, wyraz.wyraz)
wyraz.delete_instance()
baza.commit()
