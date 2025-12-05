"""
Song Player Service
This Flask app plays individual songs from the catalog.
The audio_mp3 filename from Redis is used in the URL to identify which song to play.
Only displays ONE song at a time - the song list is shown on shop-front page.
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

# Base URL where MP3 files are served by nginx (running on port 8081)
AUDIO_BASE_URL = "http://localhost:8081/"


@app.route('/play-songs/<audio_filename>')
def play_song(audio_filename):
    """
    Play a single song based on the audio_mp3 filename in the URL.
    
    Example URL: /play-songs/Pharrell%20Williams%20-%20Freedom%20(Video).mp3
    
    How it works:
    1. Get the audio filename from the URL (e.g., "Pharrell Williams - Freedom (Video).mp3")
    2. Fetch all songs from the catalog service
    3. Find the song that matches this audio_mp3 filename
    4. Display only that one song with its audio player
    """
    # Fetch all songs from the catalog service (which reads from Redis)
    response = requests.get("http://catalog-svc:5000/get-catalog", timeout=5)
    catalog = response.json()
    
    # Search through all songs to find the one with matching audio_mp3 filename
    song_to_play = None
    for song in catalog['catalog'].values():
        if song.get('audio_mp3') == audio_filename:
            song_to_play = song
            break
    
    # Render the template with the single song (or None if not found)
    return render_template("song-player.html.j2", 
                           song=song_to_play, 
                           audio_base_url=AUDIO_BASE_URL,
                           audio_filename=audio_filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
