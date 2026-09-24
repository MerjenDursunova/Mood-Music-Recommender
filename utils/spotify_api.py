
import logging
from urllib.parse import quote

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_spotify_search_url(song_name, artist):
    """
    Create a Spotify search URL without using the Spotify API.
    """
    query = f"{song_name} {artist}"
    encoded_query = quote(query)

    return f"https://open.spotify.com/search/{encoded_query}"


def create_spotify_song(song_name, artist):
    """
    Create Spotify-style song information for a local recommendation.
    """
    return {
        "name": song_name,
        "artist": artist,
        "url": create_spotify_search_url(song_name, artist)
    }

