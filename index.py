class Conteudo:
    def __init__(self):
        self.searchTerm = None
        self.prefix = None
        self.sourceContentOriginal = None
        self.sentences = []
        
class Sentencas:
    def __init__(self):
        self.text = None
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
    print(conteudo.searchTerm, conteudo.prefix)



start()