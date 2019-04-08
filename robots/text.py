import Algorithmia
import spacy



class Text:

    def fetchContentFromWikipedia(self, searchTerm):
        algorithmiaAutenticaded = Algorithmia.client('')
        wikipediaAlgorithm = algorithmiaAutenticaded.algo('web/WikipediaParser/0.1.2')
        query = {
                "articleName": searchTerm,
                "lang": "en"
                }
        wikipediaResponse = wikipediaAlgorithm.pipe(query).result
        return wikipediaResponse
    
    def removeBlankLinesAndMarkdown(self,sourceContentOriginal):
        allLines = str(sourceContentOriginal).split('\n')
        withoutBlankLinesAndMarkdown = ""
        for line in allLines:
            if ((len(line.strip()) > 0) or (line.strip()[0] != '=')):
                withoutBlankLinesAndMarkdown = withoutBlankLinesAndMarkdown + line
        return withoutBlankLinesAndMarkdown
    
    def breakIntoSentences(self,text):
        nlp = spacy.load('en')
        doc = nlp(str(text))
        sentences = []
        for sentence in doc.sents:
            sentences.append(sentence)
        return sentences
            






