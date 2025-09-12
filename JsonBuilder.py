# ����������� ������ ��� �������� ���-��������
import webbrowser

# ���������� ����� Builder ��� ���������� �������
class Builder:
    # ����������� ������ � ������ ��������, ������������� � ������� �������
    def __init__(self, page_name, page_subname, debug=False):
        # ���������� ���� �������
        self.debug = debug
        # ������������� ����� ����� ������ �������
        self.fname = ''
        # ������� ��������� JSON � ������� � ������� HTML/ CSS �������
        self.json = {"label": page_name, "describe": page_subname, "html": {}, "css": {}}
        # �������������� ������ ��� ���������� �������� ��������� ��������
        self.pre = []
        # ������ HTML �������� � �������������� ��� HEAD � BODY
        self.html = '<html><head>$HEAD</head><body><jsonbuild>$BODY</body></html>'
        # ������ CSS � �������������� ��� ������ ������� ���������
        self.css = '<style>#name{background-color:$name.background-color$;font-size:$name.font-size$;margin-bottom:$name.margin-bottom$;margin-left:$name.margin-left$;}#subname{background-color:$subname.background-color$;font-size:$subname.font-size$;margin-top:$subname.margin-top$;margin-left:$subname.margin-left$;}#info{font-size:$info.font-size$;margin-left:$info.margin-left$;margin-right:$info.margin-right$;background-color:$info.background-color$}body{background-color:$body.background-color$;}img{border-radius:$img.border-radius$;height:$img.height$;width:$img.width$;margin-left:$img.margin-left$}img:hover{height:$img:hover.height$;width:$img:hover.width$;}a{color:$a.color$;margin-left:$a.margin-left$;margin-bottom:$a.margin-bottom$}#label{text-align:$label.text-align$}</style>'

    # ������������� ������� ��� ������ ����� HTML ������
    def _setDivs(self):
        # ������ ��� ������ � �������������
        self.json["html"]["div_png"] = []
        # ������ ��� ��������� ������
        self.json["html"]["div_text"] = []
        # ������ ��� ������
        self.json["html"]["div_link"] = []

    # ��������� ��������� �������� CSS �������
    def _setCss(self):
        # ���� ���� �����
        self.json["css"]["name.background-color"] = 'whitesmoke'
        # ������ ������ �����
        self.json["css"]["name.font-size"] = '600%'
        # ������ ����� �����
        self.json["css"]["name.margin-bottom"] = '0px'
        # ������ ����� �����
        self.json["css"]["name.margin-left"] = '4%'
        # ���� ���� �����������
        self.json["css"]["subname.background-color"] = 'ghostwhite'
        # ������ ������ �����������
        self.json["css"]["subname.font-size"] = '300%'
        # ������ ������ �����������
        self.json["css"]["subname.margin-top"] = '0px'
        # ������ ����� �����������
        self.json["css"]["subname.margin-left"] = '4%'
        # ���� ���� ����������
        self.json["css"]["info.background-color"] = 'white'
        # ������ ����� ����������
        self.json["css"]["info.margin-left"] = '0%'
        # ������ ������ ����������
        self.json["css"]["info.margin-right"] = '0%'
        # ������ ������ ����������
        self.json["css"]["info.font-size"] = '25px'
        # ���� ���� ���� ��������
        self.json["css"]["body.background-color"] = 'white'
        # ������ �����������
        self.json["css"]["img.height"] = '200px'
        # ������ �����������
        self.json["css"]["img.width"] = '300px'
        # ������ ����� � �����������
        self.json["css"]["img.margin-left"] = '2%'
        # ������ ���������� ����� �����������
        self.json["css"]["img.border-radius"] = '0%'
        # ������ ����������� ��� ��������� �������
        self.json["css"]["img:hover.height"] = '220px'
        # ������ ����������� ��� ��������� �������
        self.json["css"]["img:hover.width"] = '320px'
        # ���� ������
        self.json["css"]["a.color"] = 'black'
        # ������ ����� � ������
        self.json["css"]["a.margin-left"] = '4%'
        # ������ ����� � ������
        self.json["css"]["a.margin-bottom"] = '4%'
        # ������������ ������ ��� label
        self.json["css"]["label.text-align"] = 'center'

    # ���������� ����������� � HTML ���� div_png
    def AddPng(self, src, tag=None):
        self.json["html"]["div_png"].append({"src": src})

    # ���������� ���������� ����� � ���������� � ���������
    def AddChapter(self, label, describe, tag=None):
        self.json["html"]["div_text"].append({"label": label, "describe": describe})

    # ���������� ������ � ������� � URL
    def AddLink(self, label, href, tag=None):
        self.json["html"]["div_link"].append({"label": label, "href": href})

    # �������� ��������� ���������������� HTML ���� ��� ��������
    def _generatePre(self):
        # ��������� ����������� div
        self.pre.append(f'<div>')
        # ��������� ��������� ������ 1 � id Name � ������� �� json label
        self.pre.append(f'<h1 id="Name">{self.json["label"]}</h1>')
        # ��������� ��������� ������ 2 � id SubName � ������� �� json describe
        self.pre.append(f'<h2 id="SubName">{self.json["describe"]}</h2>')
        # ��������� div
        self.pre.append(f'</div>')
        # ��������� �������������� ����� (���� ��� </hr> �����������, ������ ����� ��������)
        self.pre.append(f'</hr>')
        # ��������� ����������� div � ������������� �� ������
        self.pre.append(f'<div align="center">')
        # ��� ������� ����������� ��������� ��� img � src �� json
        for i in range(len(self.json["html"]["div_png"])):
            self.pre.append(f'<img src="{self.json["html"]["div_png"][i]["src"]}">')
        # ��������� div � �������������
        self.pre.append(f'</div>')
        # ��� ������� ���������� ����� (�������������� ��������� ����� � div_png)
        for i in range(len(self.json["html"]["div_png"])):
            # ��������� div � id info � ������������� �� ������
            self.pre.append(f'<div id="info" align="justify">')
            # ��������� ��������� 3-�� ������ � id label � ������� label �� div_text
            self.pre.append(f'<h3 id="label">{self.json["html"]["div_text"][i]["label"]}</h3>')
            # ��������� ��������� 4-�� ������ � ���������
            self.pre.append(f'<h4>{self.json["html"]["div_text"][i]["describe"]}</h4>')
            # ��������� div
            self.pre.append(f'</div>')
        # ��������� div ��� ������
        self.pre.append(f'<div>')
        # ��� ������ ������ ��������� ��� a � href � �������
        for i in range(len(self.json["html"]["div_link"])):
            self.pre.append(f'<a href="{self.json["html"]["div_link"][i]["href"]}">{self.json["html"]["div_link"][i]["label"]}</a>')
        # ��������� div
        self.pre.append(f'</div>')

    # �������� ������������ � CSS ������� �� �������� �� json
    def _generateCss(self):
        # �������� ������ ���� CSS ������
        elements = list(self.json["css"].keys())
        # �������� �� ������� ����� � �������� � �������
        for _, element in enumerate(elements):
            # ���� �������� �������, ������� ������� ������� � ��������
            if self.debug: print(f'{element}', self.json["css"][element])
            # �������� ������������ � CSS �� ��������������� ��������
            self.css = self.css.replace(f'${element}$', str(self.json["css"][element]))

    # ���������� ������������� HTML ����
    def _generateHtml(self):
        # ��������� ������ ��� ������ ����� ���� ��������
        tmp = ''
        # ������������� ��� �������� �� ������ pre � ���� ������
        for element in self.pre:
            tmp += element
        # �������� ����������� ���� �������� �� ��������� HTML
        self.html = self.html.replace('$BODY', tmp)
        # �������� ����������� ����� �� ��������������� CSS ���
        self.html = self.html.replace('$HEAD', self.css)
        # ��������� ���� � ������ fname.html ��� ������ � ��������� UTF-8
        file = open(f'{self.fname}.html', 'w', encoding='utf-8')
        # ���������� ������� HTML � ����
        file.write(self.html)

    # �������� ����� ��� ��������� ��������
    def Build(self, html_func, css=None):
        # �������������� ������ div'��
        self._setDivs()
        # ��������� CSS ����������
        self._setCss()
        # �������� �������, ������� ������ ���������� �������� (��������, ��������� ��������, ������)
        html_func()
        # ���������� ��������������� HTML-��� ��������
        self._generatePre()
        # ���������� CSS ���
        self._generateCss()
        # ���������� �������� HTML ����
        self._generateHtml()
        # ��������� ��������� HTML ���� � ��������
        webbrowser.open(f'{self.fname}.html')

    # ����������� ��� ����� � ����� ������� � ���������� �
    def Generic(self, func):
        # ������������� ��� ����� � ��� �������
        self.fname = func.__name__
        # ���������� ������������ ������� ��� ���������
        return func