import wikipedia

def WikipediaFunction(malumot):
    wikipedia.set_lang("uz")
    return wikipedia.summary(malumot)
    