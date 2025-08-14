# 🎬 Movie Recommendation System

A machine learning-powered movie recommendation system built with Streamlit that suggests similar movies based on your preferences.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.29.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **Smart Recommendations**: Get 5 similar movies based on your selection
- **Movie Posters**: Visual display with TMDB API integration
- **Dark/Light Mode**: Toggle between themes for better user experience
- **Responsive Design**: Clean and intuitive interface
- **Fast Performance**: Cached data loading for quick responses

## 🚀 Demo

[Live Demo](https://your-app-name.onrender.com) (Replace with your Render URL)

## 📸 Screenshots

### Light Mode
![Light Mode](https://via.placeholder.com/800x400?text=Light+Mode+Screenshot)

### Dark Mode
![Dark Mode](https://via.placeholder.com/800x400?text=Dark+Mode+Screenshot)

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/movie-recommendor-system.git
cd movie-recommendor-system
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app1.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

## 📁 Project Structure

```
movie-recommendor-system/
│
├── app1.py                 # Main Streamlit application
├── movies_dict.pkl         # Preprocessed movie data
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
│
├── data/                  # Raw data files
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── notebooks/             # Jupyter notebooks
    └── movie-recommendor-system.ipynb
```

## 🔧 Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn (Cosine Similarity)
- **Data Processing**: Pandas, NumPy
- **API**: The Movie Database (TMDB)
- **Deployment**: Render

## 📊 How It Works

1. **Data Preprocessing**: Movie data is cleaned and vectorized using TF-IDF
2. **Similarity Calculation**: Cosine similarity is computed between movie vectors
3. **Recommendation Engine**: Returns top 5 most similar movies
4. **Poster Fetching**: TMDB API provides movie posters dynamically

## 🌐 Deployment

### Deploy on Render

1. Fork this repository
2. Create account on [Render](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app1.py --server.port $PORT --server.address 0.0.0.0`

### Deploy on Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy directly from your repository

## 🔑 API Configuration

Get your TMDB API key:
1. Create account at [TMDB](https://www.themoviedb.org/)
2. Go to Settings → API
3. Copy your API key
4. Replace in `app1.py` or set as environment variable

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for movie data and posters
- [Streamlit](https://streamlit.io/) for the amazing framework
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools

## 📈 Future Enhancements

- [ ] User rating system
- [ ] Genre-based filtering
- [ ] Movie trailers integration
- [ ] User authentication
- [ ] Watchlist functionality
- [ ] Advanced ML algorithms (Neural Collaborative Filtering)

---

⭐ **Star this repository if you found it helpful!**