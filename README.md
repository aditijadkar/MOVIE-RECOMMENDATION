# Movie Recommendation System:

A Flask‑based web application that provides personalized movie recommendations using content‑based filtering. By leveraging natural language processing (NLP) and TF‑IDF vectorization on movie metadata, this system suggests films tailored to user preferences.

---

## 🔍 Key Features

* **Content‑Based Recommendations**: Uses TF‑IDF and cosine similarity on combined movie metadata (genres, synopsis, director, and top cast) to find similar titles.
* **Advanced Filtering & Sorting**:

  * Filter by genre, certificate, IMDb rating threshold, and release year.
  * Sort results alphabetically (A→Z, Z→A), by rating, release year, number of votes, or box‑office gross.
* **Search & Autocomplete**: Instant title search with up to 5 suggestions.
* **"Surprise Me" Mode**: Returns a random movie recommendation set for exploration.
* **Movie Details API**: Fetch full metadata (title, overview, director, cast, ratings, etc.) for a selected movie.

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Data Processing**: Pandas, NumPy
* **Machine Learning / NLP**: scikit‑learn (TF‑IDF, cosine similarity)
* **Frontend**: HTML/CSS/JavaScript (in `templates/index.html` + optional `static/` assets)
* **Dataset**: `imdb_top_1000 (1).csv` (IMDb Top 1000 movies)

---

## 📂 Repository Structure

```
movie-recommendation-system/
├── app.py                  # Flask application and API endpoints
├── recommender.py          # Recommendation logic and data preprocessing
├── imdb_top_1000 (1).csv   # Movie metadata CSV dataset
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Main frontend template (UI layout)
├── static/                 # (Optional) CSS, JS, images
└── README.md               # Project documentation (this file)
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the dataset**

   * Ensure `imdb_top_1000 (1).csv` is placed in the project root.
   * If your CSV has a different name, update the file path in `recommender.py` accordingly.

---

## ▶️ Running the Application

```bash
python app.py
```

* By default, the Flask server runs on `http://127.0.0.1:5000/`.
* Open this URL in your browser to access the movie recommendation UI.

---

## 🚀 API Endpoints

| Endpoint     | Method | Parameters                                                     | Description                                          |
| ------------ | ------ | -------------------------------------------------------------- | ---------------------------------------------------- |
| `/`          | GET    | —                                                              | Renders the main recommendation page (`index.html`). |
| `/recommend` | POST   | `title`, `genre`, `certificate`, `rating`, `sort_by`, `offset` | Returns JSON list of recommended movies.             |
| `/surprise`  | GET    | —                                                              | Returns JSON list of random movie recommendations.   |
| `/details`   | GET    | `title`                                                        | Returns JSON metadata for the specified movie.       |
| `/search`    | GET    | `query`                                                        | Returns JSON list of up to 5 matching titles.        |
| `/genres`    | GET    | —                                                              | Returns JSON list of all available genres.           |

---

## 🔧 Customization

* **Dataset Updates**: Replace the CSV with your own movie dataset. Ensure column names match those used in `recommender.py` (`Series_Title`, `Genre`, `Overview`, `Director`, `Star1`–`Star4`, `IMDB_Rating`, `Released_Year`, `No_of_Votes`, `Certificate`, `Gross`).
* **UI Enhancements**: Modify `templates/index.html` and add CSS/JS in `static/` to change the look & feel.
* **Algorithm Tuning**: Adjust TF‑IDF parameters or integrate collaborative filtering from user ratings.

