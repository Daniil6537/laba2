name = ['Жабин', 'Кузнецов', 'Чепурнова', 'Хлуднева']
predmet = ['Английский язык', 'Теория вероятности', 'Математика']
ocenka = ['5', '4', '3', '2']
data = ['3.03', '4.04', '5.05']

filter_predmet = {'Математика', 'Английский язык'}
filter_data = {'3.03', '5.05'}

used_ocenka = set()

for a in name:
    for b in predmet:
        for c in data:
            if b in filter_predmet and c in filter_data:
                o = ''
                for d in ocenka:
                    if d not in used_ocenka:
                        o = d
                        used_ocenka.add(d)
                        break
                print(a, b, c, o)