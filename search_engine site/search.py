import pandas as pd
import numpy as np
import spacy
import os
import re
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en')
nlp.remove_pipe('parser')
nlp.remove_pipe('ner')


file = '/home/hawkash/mysite/new_career.csv'
# file = 'new_career.csv'
data = pd.read_csv(file)
data['nlp_tokens'] = data['nlp_tokens'].apply(lambda x: literal_eval(x))

# print(data.head())

def nlp_preprocessing(data):

    def token_filter(token):

        return not token.is_stop and token.is_alpha and token.pos_ in ['NOUN', 'VERB', 'PROPN', 'ADJ', 'INTJ', 'X']

    data = [re.compile(r'<[^>]+>').sub('', x) for x in data] #Remove HTML-tags
    processed_tokens = []
    data_pipe = nlp.pipe(data)
    for doc in data_pipe:
        filtered_tokens = [token.lemma_.lower() for token in doc if token_filter(token)]
        processed_tokens.append(filtered_tokens)
    return processed_tokens



def search(questions_text, num):

    questions_text = [questions_text]
    nlp_corpus = [' '.join(x) for x in data['nlp_tokens']]
    nlp_text = [' '.join(x) for x in nlp_preprocessing(questions_text)]
    vectorizer = TfidfVectorizer()
    vectorizer.fit(nlp_corpus)
    corpus_tfidf = vectorizer.transform(nlp_corpus)

    text_tfidf = vectorizer.transform(nlp_text)
    sim = cosine_similarity(corpus_tfidf, text_tfidf)
    result = pd.DataFrame({'url':np.tile(data['url'], sim.shape[1]),
                           'title':np.tile(data['title'], sim.shape[1]),
                           'similarity':np.round(sim.reshape(-1,),2),
                          'scores':np.tile(data['scores'], sim.shape[1])},
                         index=np.tile(data.index, sim.shape[1]))


    result = result[result['similarity'] >= 0.01].sort_values('similarity', ascending=False).head(num).reset_index(drop=True)
    search_results = []
    # output = ''
    for index, row in result.iterrows():
        temp = {}
        temp['url'] = str(row.url)
        temp['title'] = row.title
        temp['similarityScore'] = row.similarity
        temp['sareerVillageScores'] = row.scores
        search_results.append(temp)
    return search_results