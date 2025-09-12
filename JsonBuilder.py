# Импортируем модуль для открытия веб-браузера
import webbrowser

# Определяем класс Builder для построения страниц
class Builder:
    # Конструктор класса с именем страницы, подзаголовком и режимом отладки
    def __init__(self, page_name, page_subname, debug=False):
        # Запоминаем флаг отладки
        self.debug = debug
        # Инициализация имени файла пустой строкой
        self.fname = ''
        # Создаем структуру JSON с метками и пустыми HTML/ CSS блоками
        self.json = {"label": page_name, "describe": page_subname, "html": {}, "css": {}}
        # Инициализируем список для временного хранения элементов страницы
        self.pre = []
        # Шаблон HTML страницы с плейсхолдерами для HEAD и BODY
        self.html = '<html><head>$HEAD</head><body><jsonbuild>$BODY</body></html>'
        # Шаблон CSS с плейсхолдерами для разных свойств элементов
        self.css = '<style>#name{background-color:$name.background-color$;font-size:$name.font-size$;margin-bottom:$name.margin-bottom$;margin-left:$name.margin-left$;}#subname{background-color:$subname.background-color$;font-size:$subname.font-size$;margin-top:$subname.margin-top$;margin-left:$subname.margin-left$;}#info{font-size:$info.font-size$;margin-left:$info.margin-left$;margin-right:$info.margin-right$;background-color:$info.background-color$}body{background-color:$body.background-color$;}img{border-radius:$img.border-radius$;height:$img.height$;width:$img.width$;margin-left:$img.margin-left$}img:hover{height:$img:hover.height$;width:$img:hover.width$;}a{color:$a.color$;margin-left:$a.margin-left$;margin-bottom:$a.margin-bottom$}#label{text-align:$label.text-align$}</style>'

    # Инициализация списков для разных типов HTML блоков
    def _setDivs(self):
        # Список для блоков с изображениями
        self.json["html"]["div_png"] = []
        # Список для текстовых блоков
        self.json["html"]["div_text"] = []
        # Список для ссылок
        self.json["html"]["div_link"] = []

    # Установка начальных значений CSS свойств
    def _setCss(self):
        # Цвет фона имени
        self.json["css"]["name.background-color"] = 'whitesmoke'
        # Размер шрифта имени
        self.json["css"]["name.font-size"] = '600%'
        # Отступ снизу имени
        self.json["css"]["name.margin-bottom"] = '0px'
        # Отступ слева имени
        self.json["css"]["name.margin-left"] = '4%'
        # Цвет фона подназвания
        self.json["css"]["subname.background-color"] = 'ghostwhite'
        # Размер шрифта подназвания
        self.json["css"]["subname.font-size"] = '300%'
        # Отступ сверху подназвания
        self.json["css"]["subname.margin-top"] = '0px'
        # Отступ слева подназвания
        self.json["css"]["subname.margin-left"] = '4%'
        # Цвет фона информации
        self.json["css"]["info.background-color"] = 'white'
        # Отступ слева информации
        self.json["css"]["info.margin-left"] = '0%'
        # Отступ справа информации
        self.json["css"]["info.margin-right"] = '0%'
        # Размер шрифта информации
        self.json["css"]["info.font-size"] = '25px'
        # Цвет фона тела страницы
        self.json["css"]["body.background-color"] = 'white'
        # Высота изображений
        self.json["css"]["img.height"] = '200px'
        # Ширина изображений
        self.json["css"]["img.width"] = '300px'
        # Отступ слева у изображений
        self.json["css"]["img.margin-left"] = '2%'
        # Радиус скругления углов изображения
        self.json["css"]["img.border-radius"] = '0%'
        # Высота изображения при наведении курсора
        self.json["css"]["img:hover.height"] = '220px'
        # Ширина изображения при наведении курсора
        self.json["css"]["img:hover.width"] = '320px'
        # Цвет ссылок
        self.json["css"]["a.color"] = 'black'
        # Отступ слева у ссылок
        self.json["css"]["a.margin-left"] = '4%'
        # Отступ снизу у ссылок
        self.json["css"]["a.margin-bottom"] = '4%'
        # Выравнивание текста для label
        self.json["css"]["label.text-align"] = 'center'

    # Добавление изображения в HTML блок div_png
    def AddPng(self, src, tag=None):
        self.json["html"]["div_png"].append({"src": src})

    # Добавление текстового блока с заголовком и описанием
    def AddChapter(self, label, describe, tag=None):
        self.json["html"]["div_text"].append({"label": label, "describe": describe})

    # Добавление ссылки с текстом и URL
    def AddLink(self, label, href, tag=None):
        self.json["html"]["div_link"].append({"label": label, "href": href})

    # Создание элементов предварительного HTML кода для страницы
    def _generatePre(self):
        # Добавляем открывающий div
        self.pre.append(f'<div>')
        # Добавляем заголовок уровня 1 с id Name и текстом из json label
        self.pre.append(f'<h1 id="Name">{self.json["label"]}</h1>')
        # Добавляем заголовок уровня 2 с id SubName и текстом из json describe
        self.pre.append(f'<h2 id="SubName">{self.json["describe"]}</h2>')
        # Закрываем div
        self.pre.append(f'</div>')
        # Добавляем горизонтальную линию (хотя тег </hr> некорректен, скорее всего опечатка)
        self.pre.append(f'</hr>')
        # Добавляем открывающий div с выравниванием по центру
        self.pre.append(f'<div align="center">')
        # Для каждого изображения добавляем тег img с src из json
        for i in range(len(self.json["html"]["div_png"])):
            self.pre.append(f'<img src="{self.json["html"]["div_png"][i]["src"]}">')
        # Закрываем div с изображениями
        self.pre.append(f'</div>')
        # Для каждого текстового блока (предполагается равенство длины с div_png)
        for i in range(len(self.json["html"]["div_png"])):
            # Открываем div с id info и выравниванием по ширине
            self.pre.append(f'<div id="info" align="justify">')
            # Добавляем заголовок 3-го уровня с id label и текстом label из div_text
            self.pre.append(f'<h3 id="label">{self.json["html"]["div_text"][i]["label"]}</h3>')
            # Добавляем заголовок 4-го уровня с описанием
            self.pre.append(f'<h4>{self.json["html"]["div_text"][i]["describe"]}</h4>')
            # Закрываем div
            self.pre.append(f'</div>')
        # Открываем div для ссылок
        self.pre.append(f'<div>')
        # Для каждой ссылки добавляем тег a с href и текстом
        for i in range(len(self.json["html"]["div_link"])):
            self.pre.append(f'<a href="{self.json["html"]["div_link"][i]["href"]}">{self.json["html"]["div_link"][i]["label"]}</a>')
        # Закрываем div
        self.pre.append(f'</div>')

    # Заменяем плейсхолдеры в CSS шаблоне на значения из json
    def _generateCss(self):
        # Получаем список всех CSS ключей
        elements = list(self.json["css"].keys())
        # Проходим по каждому ключу и заменяем в шаблоне
        for _, element in enumerate(elements):
            # Если включена отладка, выводим текущий элемент и значение
            if self.debug: print(f'{element}', self.json["css"][element])
            # Заменяем плейсхолдеры в CSS на соответствующие значения
            self.css = self.css.replace(f'${element}$', str(self.json["css"][element]))

    # Генерируем окончательный HTML файл
    def _generateHtml(self):
        # Временная строка для сборки всего тела страницы
        tmp = ''
        # Конкатенируем все элементы из списка pre в одну строку
        for element in self.pre:
            tmp += element
        # Заменяем плейсхолдер тела страницы на собранный HTML
        self.html = self.html.replace('$BODY', tmp)
        # Заменяем плейсхолдер шапки на сгенерированный CSS код
        self.html = self.html.replace('$HEAD', self.css)
        # Открываем файл с именем fname.html для записи в кодировке UTF-8
        file = open(f'{self.fname}.html', 'w', encoding='utf-8')
        # Записываем готовый HTML в файл
        file.write(self.html)

    # Основной метод для генерации страницы
    def Build(self, html_func, css=None):
        # Инициализируем списки div'ов
        self._setDivs()
        # Заполняем CSS значениями
        self._setCss()
        # Вызываем функцию, которая задает содержимое страницы (например, добавляет картинки, тексты)
        html_func()
        # Генерируем предварительный HTML-код страницы
        self._generatePre()
        # Генерируем CSS код
        self._generateCss()
        # Генерируем итоговый HTML файл
        self._generateHtml()
        # Открываем созданный HTML файл в браузере
        webbrowser.open(f'{self.fname}.html')

    # Привязываем имя файла к имени функции и возвращаем её
    def Generic(self, func):
        # Устанавливаем имя файла в имя функции
        self.fname = func.__name__
        # Возвращаем оригинальную функцию без изменений
        return func