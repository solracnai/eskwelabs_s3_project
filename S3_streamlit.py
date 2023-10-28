import streamlit as st

st.set_page_config(
    page_title="Eraserheads Music Recommendation System",
    page_icon="🎵",
    initial_sidebar_state="expanded"
)


st.sidebar.header("Dashboard")

# Radio buttons for navigation options
navigation_option = st.sidebar.radio("Select an option", ["Home", "Background", "Exploratory Data Analysis", "Objectives", "Machine Learning Pipeline", "Genre Classification", "Recommender Engine", "Spotify Deployment"])

# Content based on the selected option
if navigation_option == "Home":
    st.markdown(
        """
        <style>
        #home-container {
          text-align: center;
          margin: 0 auto;
        }
        </style>
        <div id="home-container", class="center-text">
            <header>
                <h1>Welcome to Eraserheads Music Recommendation System</h1>
            </header>
                <p>
                    This Streamlit application serves as a straightforward platform for the Eraserheads Music Recommendation System.
                </p>
                <p>
                    Feel free to dive in and enjoy the experience!
                </p>
        </div>

        """,
        unsafe_allow_html=True,
    )
    st.image('./image/ehead_logo_01.jpg')


elif navigation_option == "Background":
    st.image('./image/eheads_1.jpg')
    st.markdown(
        """
        <div id="history-container">
            <header>
                <h1>History</h1>
            </header>
                <p>
                    Eraserheads, at times stylized as ERASƎRHEADS or ƎRASƎRHƎADS, established themselves as a Filipino alternative rock force in 1989. 
                    Consisting of Ely Buendia, Buddy Zabala, Marcus Adoro, and Raimund Marasigan, he band has left an indelible mark as one of the most 
                    influential and successful acts in Filipino music history. Often hailed as "The Beatles of the Philippines," 
                    they boast an impressive record of selling 9 million albums and pioneering a resurgence of Manila bands, setting the stage for a wave of 
                    Filipino alternative rock groups, including Rivermaya.
                </p>
                <p>
                    The band unveiled a diverse collection of singles, albums, and EPs throughout their musical journey. Their pinnacle of 
                    commercial success was marked by the release of their third album, Cutterpillow (1995), a multiple-platinum achiever. Adding to their 
                    accolades, they secured the esteemed International Viewer's Choice Award (MTV Asia) at the 1997 MTV Video Music Awards in New York. 
                    Notably, they stood as the sole Filipino artist to claim this honor before the establishment of the MTV Asia Awards.
                </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div id="history-container", class="center-text">
            <header>
                <h1>More than 9 million albums sold</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image('./image/eheads_album.jpg')
    st.markdown(
        """
        <div id="history-container", class="center-text">
            <header>
                <h1>2.95 million monthly listeners</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image('./image/eheads_spotify.png')
    st.markdown(
        """
        <div id="history-container", class="center-text">
            <header>
                <h1>Eraserheads Top 10 Spotify songs</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image('./image/eheads_spotify_songs.png')


elif navigation_option == "Exploratory Data Analysis":
    st.markdown(
    """
        <div id="eda-container", class="center-text">
            <header>
                <h1>Eraserheads Spotify Yearly Streams</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/eheads_chart_02.png')

    st.markdown(
    """
        <div id="eda-container", class="center-text">
            <header>
                <h1>Spotify Daily Streams: Eraserheads - Ang Huling El Bimbo</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/eheads_chart_01.png')

    st.markdown(
    """
        <div id="eda-container", class="center-text">
            <header>
                <h1>Ang Huling El Bimbo Audio Features</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/ehead_audio_features.png')

    st.markdown(
    """
        <div id="eda-container", class="center-text">
            <header>
                <h1>Ang Huling El Bimbo Daily Chart Ranking</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/ehead_daily_charts.png')


elif navigation_option == "Objectives":
    st.markdown(
        """
        <style>
        #objectives-container {
          text-align: center;
          margin: 0 auto;
          color: red; 
        }
        </style>
        <div id="objectives-container" class="center-text">
            <header>
                <h1>Objective</h1>
                <h2 style="font-size: 24px;">Explore potential collaborations with the Eraserheads by identifying the most suitable partners among the current charting artists, paving the way for an anticipated comeback.</h2>
            </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image('./image/local_artist.jpg')


elif navigation_option == "Machine Learning Pipeline":
    st.markdown(
        """
        <style>
        #pipeline-container {
          text-align: center;
          margin: 0 auto;
          color: red; 
        }
        </style>
        <div id="pipeline-container" class="center-text">
            <header>
                <h1>Machine Learning Pipeline</h1>
                </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image('./image/ml_pipeline.jpg')


elif navigation_option == "Genre Classification":
    st.markdown(
    """
        <div id="genre-container", class="center-text">
            <header>
                <h1>Genre Classifier</h1>
            </header>
            <ul>
                <li>To assign a genre to each track of Eraserheads and determine their most prominent genre, facilitating the creation of a recommender engine for discovering relevant songs and artists</li>
                <li>Genre: Rock, Country, Jazz, R&B</li>
                <li>Features: acousticness, danceability, energy, instrumentalness, liveness, loudness, popularity, speechiness, valence</li>
                <li>Models considered: K-Nearest Neighbors, Supported Vector Model, Random Forest Classifier</li>
                <li>Best model: Random Forest Classifier</li>
                <li>Accuracy: --%</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
    """
        <div id="genre-container", class="center-text">
            <header>
                <h1>
                    Eraserheads' songs primarily fall under the rock genre, with country being a secondary influence at a distance
                </h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/genre_1.png')
    st.image('./image/ml_model_prediction.jpg')


elif navigation_option == "Recommender Engine":
    # st.markdown(
    # """
    #     <div id="engine-container", class="center-text">
    #         <header>
    #             <h1>Recommender Engine</h1>
    #         </header>
    #         <p>

    #         </p>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,    
    # )

    st.markdown(
    """
        <div id="engine-container", class="center-text">
            <header>
                <h1>Recommended Artist using Euclidean/Manhattan Distance</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/manhattan.jpg')

    st.markdown(
    """
        <div id="engine-container", class="center-text">
            <header>
                <h1>Recommended Artist using Cosine Distance</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,    
    )
    st.image('./image/cosine.jpg')


elif navigation_option == "Spotify Deployment":
    st.markdown(
        """
        <style>
        #deployment-container {
          text-align: center;
          margin: 0 auto;
        }
        </style>
        <div id="deployment-container" class="center-text">
            <header>
                <h1>Discover and enjoy the recommended songs on Spotify!</h1>
            </header>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Spotify playlist embed code
    spotify_playlist_embed_code = """
    <iframe src="https://open.spotify.com/embed/playlist/0DotnwkzjQ0ezS86P9TmVY?utm_source=generator" width="700" height="700" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    """
    st.markdown(spotify_playlist_embed_code, unsafe_allow_html=True)


