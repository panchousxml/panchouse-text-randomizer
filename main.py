from text_randomizer import Template


template = Template('''🔥 Мы компания УралПеллет, которая занимается {поставкой|продажей|реализацией} и монтажом пеллетных котлов. Предлагаем широкий {ассортимент|выбор|сортамент} пеллетных котлов от проверенных {поставщиков|производителей|изготовителей} по доступным ценам мощностью от 11 кВт до 1,2 МВт. Работаем с такими производителями как [+,+| Vulkan| ТЕПЛОДАР| Lavoro Eco| PELLETOR| FACI| ZOTA| ROTEKS| METAL-FACH| BIODOM| RIDAN| AMTEO| VSKZ| TERMODINAMIK| GAMLET| DOZA TECH| СВЕТЛОБОР| ACV| ОБЩЕМАШ| ПЕЛЛЕТРОН| СТАРТ]

<strong> МЫ ПЕРВЫЙ ОПТОВЫЙ СКЛАД ПЕЛЛЕТНО/УГОЛЬНЫХ КОТЛОВ </strong>

📱 <strong> Напишите нам прямо сейчас и мы перезвоним вам с предложением </strong>

{<strong>Почему выбирают нас?</strong>|<strong>Почему мы?</strong>|<strong>Почему работают с нами?</strong>}

[+
+✅ Большой выбор от надежных брендов|✅ Только сертифицированная и качественная продукция|✅ Бесплатный теплорасчет и подбор оборудования|✅ Работаем напрямую с поставщиками, без посредников|✅ Гарантия на все оборудование|✅ Возможность приобретения в кредит|✅ Доставка по всей России]

🎁{В ПОДАРОК|БЕСПЛАТНО|ЗА НАШ СЧЕТ}!! Группа безопасности (обязательный узел при монтаже котлов, без него нельзя)!

<strong>Характеристики:</strong>

[+
+Страна производитель: Россия|Мощность: 15 кВт|Отапливаемая площадь: 140 кв.м|Основное топливо: Пеллеты, Измельченный уголь, Эко-горошек, Орешек, Уголь фракционный|Резервное топливо: Уголь, Дрова, Брикеты|Назначение: Для дома, Для дачи, Для предприятия|КПД: 90 %|Давление: 2.5 бар|Напряжение: 220 В|Температура продуктов сгорания: 200 °C|Диаметр дымохода: 160 мм|Вместимость теплообменника: 40 л|Ёмкость бункера: 200 л|Потребляемая мощность: 350 Вт|Температура теплоносителя: 90 °C|Вес: 320 кг|Габариты: 1165х1325х790 мм]
_________________________________________________________

📱 {Пишите|Звоните|Свяжитесь с нами} прямо сейчас, мы сделаем <strong>БЕСПЛАТНЫЙ</strong> тепловой расчет вашего помещения
💗 Добавляйте наше объявление в избранное, чтобы не потерять!''')
print(template.render())