# -*- coding: utf-8 -*-
import pandas as pd
from rentsite.rent_site.models import Place
from django.utils.text import slugify

ind = pd.read_excel("1.xlsx")
for row in ind.iterrows():
    print row[1]
    x = Place()
    x.city = "Киев"
    x.street = row[1].Street
    x.building = row[1].House
    x.type = row[1].Item
    x.total_footage = row[1]["Total footage"]
    x.living_footage = row[1]["Living footage"]
    x.floor_number = row[1]["Floor"]
    x.region = row[1]["Region"]
    x.price = row[1]["Price"]
    x.slug = slugify('-'.join([x.street, str(x.building), x.region]), allow_unicode=True)
    try:
        x.save()
    except:
        continue

