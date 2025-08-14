# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import time

# # Page configuration
# st.set_page_config(
#     page_title="🎬 CineMatch",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for dark/light mode
# def load_css(theme="light"):
#     if theme == "dark":
#         st.markdown("""
#         <style>
#         .main-header {
#             background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
#             padding: 2rem;
#             border-radius: 15px;
#             margin-bottom: 2rem;
#             text-align: center;
#             color: white;
#         }
#         .movie-card {
#             background: #2d3748;
#             border-radius: 15px;
#             padding: 1rem;
#             margin: 0.5rem;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
#             transition: transform 0.3s ease;
#             border: 1px solid #4a5568;
#         }
#         .movie-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
#         }
#         .search-container {
#             background: #2d3748;
#             padding: 2rem;
#             border-radius: 15px;
#             margin-bottom: 2rem;
#             border: 1px solid #4a5568;
#         }
#         .stSelectbox > div > div {
#             background-color: #4a5568;
#             color: white;
#         }
#         </style>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown("""
#         <style>
#         .main-header {
#             background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#             padding: 2rem;
#             border-radius: 15px;
#             margin-bottom: 2rem;
#             text-align: center;
#             color: white;
#         }
#         .movie-card {
#             background: white;
#             border-radius: 15px;
#             padding: 1rem;
#             margin: 0.5rem;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             transition: transform 0.3s ease;
#             border: 1px solid #e2e8f0;
#         }
#         .movie-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
#         }
#         .search-container {
#             background: #f7fafc;
#             padding: 2rem;
#             border-radius: 15px;
#             margin-bottom: 2rem;
#             border: 1px solid #e2e8f0;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# # Initialize session state
# if 'theme' not in st.session_state:
#     st.session_state.theme = 'light'
# if 'recommendations' not in st.session_state:
#     st.session_state.recommendations = None

# # Load data
# @st.cache_data
# def load_data():
#     movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
#     movies = pd.DataFrame(movies_dict)
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     return movies, similarity

# # Fetch movie poster
# @st.cache_data
# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0e8185d38ccf0feb2788164e60b1bbf8&language=en-US"
#         response = requests.get(url, timeout=5)
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return "https://via.placeholder.com/500x750?text=No+Image"
#     except:
#         return "https://via.placeholder.com/500x750?text=No+Image"

# # Get movie recommendations
# def get_recommendations(movie_title, movies, similarity, num_recommendations=6):
#     try:
#         movie_index = movies[movies['title'] == movie_title].index[0]
#         distances = similarity[movie_index]
#         movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num_recommendations+1]
        
#         recommendations = []
#         for i in movies_list:
#             movie_data = movies.iloc[i[0]]
#             recommendations.append({
#                 'title': movie_data.title,
#                 'movie_id': movie_data.movie_id,
#                 'similarity_score': round(i[1] * 100, 1)
#             })
#         return recommendations
#     except:
#         return []

# # Sidebar
# with st.sidebar:
#     st.markdown("### 🎨 Theme Settings")
#     theme_toggle = st.toggle("🌙 Dark Mode", value=st.session_state.theme == 'dark')
    
#     if theme_toggle:
#         st.session_state.theme = 'dark'
#     else:
#         st.session_state.theme = 'light'
    
#     st.markdown("---")
#     st.markdown("### 📊 App Info")
#     st.info("CineMatch uses advanced ML algorithms to find movies similar to your favorites!")
    
#     st.markdown("### 🔧 Settings")
#     num_recommendations = st.slider("Number of recommendations", 3, 10, 6)

# # Load CSS based on theme
# load_css(st.session_state.theme)

# # Load data
# movies, similarity = load_data()

# # Main header
# st.markdown("""
# <div class="main-header">
#     <h1>🎬 CineMatch</h1>
#     <p>Discover your next favorite movie with AI-powered recommendations</p>
# </div>
# """, unsafe_allow_html=True)

# # Search section
# st.markdown('<div class="search-container">', unsafe_allow_html=True)
# col1, col2 = st.columns([3, 1])

# with col1:
#     st.markdown("### 🔍 Find Similar Movies")
#     selected_movie = st.selectbox(
#         "Choose a movie you love:",
#         movies['title'].values,
#         index=0,
#         help="Select a movie to get personalized recommendations"
#     )

# with col2:
#     st.markdown("### ")
#     if st.button("🚀 Get Recommendations", type="primary", use_container_width=True):
#         with st.spinner("Finding perfect matches..."):
#             time.sleep(1)  # Add slight delay for better UX
#             st.session_state.recommendations = get_recommendations(
#                 selected_movie, movies, similarity, num_recommendations
#             )

# st.markdown('</div>', unsafe_allow_html=True)

# # Display recommendations
# if st.session_state.recommendations:
#     st.markdown("### 🎯 Recommended Movies")
    
#     # Create responsive columns
#     cols_per_row = 3
#     recommendations = st.session_state.recommendations
    
#     for i in range(0, len(recommendations), cols_per_row):
#         cols = st.columns(cols_per_row)
        
#         for j, col in enumerate(cols):
#             if i + j < len(recommendations):
#                 movie = recommendations[i + j]
                
#                 with col:
#                     st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                    
#                     # Movie poster
#                     poster_url = fetch_poster(movie['movie_id'])
#                     st.image(poster_url, use_column_width=True)
                    
#                     # Movie details
#                     st.markdown(f"**{movie['title']}**")
#                     st.markdown(f"🎯 Match: {movie['similarity_score']}%")
                    
#                     # Progress bar for similarity
#                     st.progress(movie['similarity_score'] / 100)
                    
#                     st.markdown('</div>', unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.markdown(
#         "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</div>",
#         unsafe_allow_html=True
#     )

import streamlit as st
import pickle
import pandas as pd
import requests

# Page config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Theme toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Simple CSS for themes
if st.session_state.dark_mode:
    st.markdown("""
    <style>
    .stApp { background-color: #1e1e1e; color: white; }
    .stSelectbox > div > div { background-color: #333; }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0e8185d38ccf0feb2788164e60b1bbf8"
    try:
        response = requests.get(url)
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    except:
        return None

def recommend(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_posters

# Load data
movies, similarity = load_data()

# Header with theme toggle
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🎬 Movie Recommender")
with col2:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Movie selection
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

# Recommendation button
if st.button("Get Recommendations", type="primary"):
    names, posters = recommend(selected_movie, movies, similarity)
    
    st.subheader("Recommended Movies:")
    cols = st.columns(5)
    
    for i, col in enumerate(cols):
        with col:
            st.write(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.write("No poster available")
