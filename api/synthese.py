import requests as req
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import fr_core_news_sm


def synthese_automatique(url):
    reponse = req.get(url)
    soup = BeautifulSoup(reponse.text)

    article = ""
    for div in soup.find_all('div'):
        try:
            if 'desc' in div.attrs['class']:
                article = div.text
                break
        except:
            pass

    nlp = fr_core_news_sm.load()

    doc = nlp(article)

    corpus = [sent.text.lower() for sent in doc.sents]

    cv = CountVectorizer(stop_words=list(STOP_WORDS))

    cv_fit = cv.fit_transform(corpus)

    mots = cv.get_feature_names()
    occurs_mots = cv_fit.toarray().sum(axis=0)
    freq_mots = dict(zip(mots, occurs_mots))

    valeurs = sorted(freq_mots.values())

    mot_plus_freq = [mot for mot, freq in freq_mots.items()
                     if freq in valeurs[-3:]]

    freq_mot_plus_freq = valeurs[-1]

    for mot in freq_mots:
        freq_mots[mot] = (freq_mots[mot]/freq_mot_plus_freq)

    score_phrase = {}
    for phrase in doc.sents:
        for mot in phrase:
            if mot.text.lower() in freq_mots.keys():
                if phrase in score_phrase.keys():
                    score_phrase[phrase] += freq_mots[mot.text.lower()]
                else:
                    score_phrase[phrase] = freq_mots[mot.text.lower()]
    top_importante_phrase = (sorted(score_phrase.values())[::-1])
    top_synthese = top_importante_phrase[:3]

    brouillon = []
    resumer = ""
    for phrase, score in score_phrase.items():
        if score in top_synthese:
            brouillon.append(phrase)
        else:
            continue

    for phrase in brouillon:
        resume = '{} '.format(phrase)

    return {'article': article, 'resume': resume}


def synthese_automatique_with_article(article):

    nlp = fr_core_news_sm.load()

    doc = nlp(article)

    corpus = [sent.text.lower() for sent in doc.sents]

    cv = CountVectorizer(stop_words=list(STOP_WORDS))

    cv_fit = cv.fit_transform(corpus)

    mots = cv.get_feature_names()
    occurs_mots = cv_fit.toarray().sum(axis=0)
    freq_mots = dict(zip(mots, occurs_mots))

    valeurs = sorted(freq_mots.values())

    freq_mot_plus_freq = valeurs[-2]

    for mot in freq_mots:
        freq_mots[mot] = (freq_mots[mot]/freq_mot_plus_freq)

    score_phrase = {}
    for phrase in doc.sents:
        for mot in phrase:
            if mot.text.lower() in freq_mots.keys():
                if phrase in score_phrase.keys():
                    score_phrase[phrase] += freq_mots[mot.text.lower()]
                else:
                    score_phrase[phrase] = freq_mots[mot.text.lower()]
    top_importante_phrase = (sorted(score_phrase.values())[::-1])
    top_synthese = top_importante_phrase[:4]

    brouillon = []
    resumer = ""
    for phrase, score in score_phrase.items():
        if score in top_synthese:
            brouillon.append(phrase)
        else:
            continue

    for phrase in brouillon:
        resume = '{} '.format(phrase)

    return {'article': article, 'resume': resume}
