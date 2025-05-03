import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random


df = pd.read_csv("imdb_top_1000 (1).csv")
df.dropna(subset=['Overview', 'Director', 'Genre', 'Star1'], inplace=True)
df.fillna('', inplace=True)


df['Combined'] = (df['Genre'] + ' ' + df['Overview'] + ' ' +
                  df['Director'] + ' ' + df['Star1'] + ' ' +
                  df['Star2'] + ' ' + df['Star3'] + ' ' + df['Star4'])

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Combined'])
similarity = cosine_similarity(tfidf_matrix)

def get_recommendations(title, rating=None, genre=None, certificate=None, year=None, sort_by=None):
    title = title.strip().lower()
  
    indices = df[df['Series_Title'].str.lower().str.contains(title)].index
    if len(indices) > 0:
        idx = indices[0]
        scores = list(enumerate(similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:50]  
        recommended = df.iloc[[i[0] for i in scores]]
    else:
        
        recommended = df.copy()


    if rating:
        try:
            recommended = recommended[recommended['IMDB_Rating'] >= float(rating)]
        except:
            pass
    if genre:
        recommended = recommended[recommended['Genre'].str.contains(genre, case=False, na=False)]
    if certificate:
        recommended = recommended[recommended['Certificate'].str.contains(certificate, case=False, na=False)]
    if year:
        try:
            recommended = recommended[recommended['Released_Year'] == int(year)]
        except:
            pass


    if sort_by:
        if sort_by == 'az':
            recommended = recommended.sort_values(by='Series_Title')
        elif sort_by == 'za':
            recommended = recommended.sort_values(by='Series_Title', ascending=False)
        elif sort_by == 'rating':
            recommended = recommended.sort_values(by='IMDB_Rating', ascending=False)
        elif sort_by == 'year':
            recommended = recommended.sort_values(by='Released_Year', ascending=False)
        elif sort_by == 'votes':
            recommended = recommended.sort_values(by='No_of_Votes', ascending=False)
        elif sort_by == 'gross':
        
            recommended['Gross'] = recommended['Gross'].replace('[\$,]', '', regex=True)
            recommended['Gross'] = pd.to_numeric(recommended['Gross'], errors='coerce').fillna(0)
            recommended = recommended.sort_values(by='Gross', ascending=False)
    return recommended.head(10).to_dict(orient='records')

def get_random_recommendations():
    random_title = random.choice(df['Series_Title'].tolist())
    return get_recommendations(random_title)

def get_movie_details(title):
    movie = df[df['Series_Title'].str.lower() == title.strip().lower()]
    if movie.empty:
        return {}
    return movie.iloc[0].to_dict()

def search_titles(query):
    return df[df['Series_Title'].str.contains(query, case=False, na=False)]['Series_Title'].head(5).tolist()

def get_all_genres():
    genres = set()
    for row in df['Genre'].dropna():
        for g in row.split(','):
            genres.add(g.strip())
    return sorted(list(genres))
