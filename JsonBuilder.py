import webbrowser

#the Translator of json to html
class Translator:

    #initialization
    def __init__(self):

        #the global output html code
        self.html = '<html><head>$HEAD</head><body>$BODY</body></html>'

        #pre html code list
        self.pre = []

    #compiling the pre html code list
    def CompilePre(self, json):

        #project label
        self.pre.append(f"<h1 id='Name'>{json["title"]}</h1>")

        #project sublabel
        self.pre.append(f"<h2 id='SubName'>{json["subtitle"]}</h2>")

        #hr
        self.pre.append(f"<hr>")

        #project png rectangle generic
        self.pre.append(f"<div align='center'>")
        for i in range(len(json["data"]["div_png"])):
            self.pre.append(f'<img src="{json["data"]["div_png"][i]["src"]}">')
        self.pre.append(f"</div>")

        #project text rectangle generic
        for i in range(len(json["data"]["div_text"])):
            self.pre.append(f"<div id='info' align='center'>")
            self.pre.append(f"<h3>{json["data"]["div_text"][i]["label"]}</h3>")
            self.pre.append(f"<h4>{json["data"]["div_text"][i]["text"]}</h4>")
            self.pre.append(f"</div>")

        #project link string generic
        for i in range(len(json["data"]["div_link"])):
            self.pre.append(f'<a href="{json["data"]["div_link"][i]["href"]}">{json["data"]["div_link"][i]["text"]}</a>')

    #compiling pre to html
    def CompileHtml(self):

        #string object initizing
        string = ''

        #summ of all self.pre : list elements
        for i, el in enumerate(self.pre): string += el

        #entrance ( summ of all self.pre ) to main self.html
        self.html = self.html.replace('$BODY', string)
        self.html = self.html.replace('$HEAD', '<style>#Name{background-color:whitesmoke;font-size:600%;margin-bottom:0px;margin-left:4%;}#SubName{background-color:ghostwhite;font-size:300%;margin-top:0px;margin-left:4%;}#info{font-size:25px;background-color:white;}button{font-size:400%;background-size:500%;background-color:cyan;}button:hover{font-size:400%;background-size:500%;background-color:cyan;border-color:white;}body{background-color:white;}img{height:200px;width:300px;margin-left:2%}img:hover{height:220px;width:320px;}a{color:black;}</style>')

#the json creating class
class Project:

    #initialization
    def __init__(self, title, subtitle):
        
        #setup of json
        self.json = {"title": title, "subtitle": subtitle, "data": {}}

    #adding of main 3-rd divs
    def SetDivs(self):

        #div with png's
        self.json["data"]["div_png"] = []
        
        #div with chapter's
        self.json["data"]["div_text"] = []
        
        #div with link's
        self.json["data"]["div_link"] = []
    
    #adding the dict png (src) construction
    def AddPng(self, src):
        self.json["data"]["div_png"].append({"src": src})
        
    #adding the dict chapter (label, text) construction
    def AddChapter(self, label, text):
        self.json["data"]["div_text"].append({"label": label, "text": text})

    #adding the dict link (text, href) construction
    def AddLink(self, text, href):
        self.json["data"]["div_link"].append({"href": href, "text": text})

    #project .html gen and finish function
    def Finish(self):

        #translator (executer) object intialization
        translator = Translator()

        #json -> html element list
        translator.CompilePre(self.json)

        #html element list ->  full html code
        translator.CompileHtml()

        #file creating
        file = open('dist/index.html', 'w', encoding='utf-8')
        file.write(translator.html)

        #open
        webbrowser.open('file:///C:/Users/admin/OneDrive/Desktop/JsonBuilder/dist/index.html')
  

