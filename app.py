from flask import Flask, render_template, request, jsonify
import pandas as pd
from recommender import df, get_recommendations, get_random_recommendations, get_movie_details, search_titles, get_all_genres

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('title', '')
    genre = data.get('genre', '')
    certificate = data.get('certificate', '')
    rating = data.get('rating', '')
    sort_by = data.get('sort_by', '')
    offset = int(data.get('offset', 0))

    if movie_name.strip():
        recs = get_recommendations(movie_name, rating, genre, certificate, sort_by)
    else:
       
        filtered_df = df.copy()
        if genre:
            filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
        if certificate:
            filtered_df = filtered_df[filtered_df['Certificate'].str.contains(certificate, case=False, na=False)]
        if rating:
            try:
                filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= float(rating)]
            except:
                pass
        if sort_by:
            if sort_by == 'az':
                filtered_df = filtered_df.sort_values(by='Series_Title')
            elif sort_by == 'za':
                filtered_df = filtered_df.sort_values(by='Series_Title', ascending=False)
            elif sort_by == 'rating':
                filtered_df = filtered_df.sort_values(by='IMDB_Rating', ascending=False)
            elif sort_by == 'year':
                filtered_df = filtered_df.sort_values(by='Released_Year', ascending=False)
            elif sort_by == 'votes':
                filtered_df = filtered_df.sort_values(by='No_of_Votes', ascending=False)
            elif sort_by == 'gross':
                filtered_df['Gross'] = filtered_df['Gross'].replace('[\$,]', '', regex=True)
                filtered_df['Gross'] = pd.to_numeric(filtered_df['Gross'], errors='coerce').fillna(0)
                filtered_df = filtered_df.sort_values(by='Gross', ascending=False)
        recs = filtered_df.head(100).to_dict(orient='records') 


    rec_list = recs[offset:offset+10]
    return jsonify(rec_list)

@app.route('/surprise')
def surprise():
    return jsonify(get_random_recommendations())

@app.route('/details')
def details():
    title = request.args.get('title', '')
    return jsonify(get_movie_details(title))

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return jsonify(search_titles(query))

@app.route('/genres')
def genres():
    return jsonify(get_all_genres())

if __name__ == '__main__':
    app.run(debug=True)
