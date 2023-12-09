# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44*(1024**2)
pages = 100
strings = 50
symbols = 25
book_volume = symbols*strings*pages*4


print("Количество книг, помещающихся на дискету:", int(inf_volume//book_volume))
