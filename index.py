import robots.text
class Conteudo:
    def __init__(self):
        self.searchTerm = ""
        self.prefix = ""
        self.sourceContentOriginal = ""
        self.sourceContentSanitized = ""
        self.sentences = []
        
class Sentencas:
    def __init__(self):
        self.text = ""
        self.keywords = []
        self.images = []

def askAndReturnSearchTerm():
    print("Digite o termo de pesquisa do Wikipedia")
    searchTerm = input()
    return searchTerm

def askAndReturnPrefix():
    prefixes = ["Who is", "What is", "The history of"]
    print ("Choose an option:")
    print("[0] "+prefixes[0])
    print("[1] "+prefixes[1])
    print("[2] "+prefixes[2])

    prefix = input()
    return prefixes[int(prefix)]

def start():
    conteudo = Conteudo()
    conteudo.searchTerm = askAndReturnSearchTerm()
    conteudo.prefix = askAndReturnPrefix()
    conteudo.sourceContentOriginal = robots.text.Text().fetchContentFromWikipedia(conteudo.searchTerm)
    conteudo.sourceContentSanitized = robots.text.Text().removeBlankLinesAndMarkdown(conteudo.sourceContentOriginal)
    sentences = robots.text.Text().breakIntoSentences(conteudo.sourceContentSanitized)
    for lines in sentences:
        sentencas = Sentencas()
        sentencas.text = lines
        conteudo.sentences.append(sentencas)
    print(conteudo.sentences[10].text)


start()