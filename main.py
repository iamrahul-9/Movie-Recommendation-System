# first import streamlit and pickle
import streamlit as st
import pickle
import base64

# extract the new_df dataframe from movies.pkl
movies_list = pickle.load(open("movies.pkl", "rb"))
# extract the titles of movies
movies_list_title = movies_list["title"].values

# extract the similarity which contain our cosine similarity values
similarity = pickle.load(open("similarity.pkl", "rb"))


# make a recommend function which will take movie title and return 5 similar movies with their posters
def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    sorted_movie_list = sorted(list(enumerate(distances)), reverse=True,
                               key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in sorted_movie_list:
        poster_path = movies_list["poster_path"][i[0]]
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_posters.append(
            "https://image.tmdb.org/t/p/original"+poster_path)

    return recommended_movies,  recommended_posters

# Create title for your stream lit page
st.set_page_config(page_title="Movie Recommendation System", page_icon=":clapper:")
st.title("Movie Recommendation System")


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
             background-attachment: fixed;
             background-size: cover
         }}

        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

# Create a input box for movies name
selected_movie_name = st.selectbox(
    "What is the movie name?",
    movies_list_title
)

# create a recommend button with function of displaying recommended movies and movie posters
if st.button("Recommend"):
    recommendation, movie_posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.write(recommendation[i])
            st.image(movie_posters[i])
