import os
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, redirect, session, url_for, render_template, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

# Spotify OAuth configuration
sp_oauth = SpotifyOAuth(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:5000/callback'),
    scope='user-library-read user-read-recently-played user-top-read'
)

def get_recent_tracks(sp, limit=10):
    """Fetch recently played tracks with audio features"""
    try:
        results = sp.current_user_recently_played(limit=limit)
        tracks_data = []
        
        for item in results['items']:
            track = item['track']
            features = sp.audio_features(track['id'])[0]
            
            if features:
                tracks_data.append({
                    'id': track['id'],
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'album': track['album']['name'],
                    'preview_url': track['preview_url'],
                    'external_url': track['external_urls']['spotify'],
                    'valence': features['valence'],
                    'energy': features['energy'],
                    'danceability': features['danceability'],
                    'tempo': features['tempo'],
                    'speechiness': features['speechiness'],
                    'acousticness': features['acousticness'],
                    'instrumentalness': features['instrumentalness']
                })
        
        return pd.DataFrame(tracks_data)
    except Exception as e:
        print(f"Error fetching recent tracks: {e}")
        return pd.DataFrame()

def categorize_mood(row):
    """Categorize track mood based on audio features"""
    valence = row['valence']
    energy = row['energy']
    danceability = row['danceability']
    acousticness = row['acousticness']
    instrumentalness = row['instrumentalness']
    
    if valence > 0.7 and energy > 0.7:
        return 'Happy and Energetic'
    elif valence > 0.7 and energy < 0.4:
        return 'Chill and Uplifting'
    elif valence < 0.4 and energy > 0.7:
        return 'Angry or Intense'
    elif valence < 0.4 and energy < 0.4:
        return 'Sad or Melancholic'
    elif danceability > 0.6 and valence > 0.6:
        return 'Danceable and Upbeat'
    elif acousticness > 0.5 and instrumentalness > 0.5:
        return 'Ambient or Acoustic'
    else:
        return 'Neutral or Mixed Mood'

def get_mood_recommendations(sp, mood, limit=5):
    """Get song recommendations based on mood"""
    try:
        # Define target audio features based on mood
        target_features = {
            'Happy and Energetic': {'valence': 0.8, 'energy': 0.8, 'danceability': 0.7},
            'Chill and Uplifting': {'valence': 0.8, 'energy': 0.3, 'acousticness': 0.6},
            'Sad or Melancholic': {'valence': 0.3, 'energy': 0.3, 'acousticness': 0.7},
            'Danceable and Upbeat': {'valence': 0.7, 'energy': 0.7, 'danceability': 0.8},
            'Ambient or Acoustic': {'acousticness': 0.8, 'instrumentalness': 0.6, 'energy': 0.3}
        }
        
        features = target_features.get(mood, {'valence': 0.5, 'energy': 0.5})
        
        # Get recommendations from Spotify
        recommendations = sp.recommendations(
            seed_genres=['pop', 'rock', 'electronic'],
            target_valence=features.get('valence', 0.5),
            target_energy=features.get('energy', 0.5),
            target_danceability=features.get('danceability', 0.5),
            target_acousticness=features.get('acousticness', 0.5),
            limit=limit
        )
        
        return [{
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'preview_url': track['preview_url'],
            'external_url': track['external_urls']['spotify']
        } for track in recommendations['tracks']]
        
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return []

@app.route('/')
def index():
    """Main application page"""
    return render_template('index.html')

@app.route('/login')
def login():
    """Initiate Spotify OAuth login"""
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    """Handle Spotify OAuth callback"""
    try:
        code = request.args.get('code')
        token_info = sp_oauth.get_access_token(code)
        session['token_info'] = token_info
        return redirect(url_for('dashboard'))
    except Exception as e:
        print(f"Error in callback: {e}")
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """User dashboard with mood analysis"""
    token_info = session.get('token_info')
    if not token_info:
        return redirect(url_for('login'))
    
    try:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        df = get_recent_tracks(sp)
        
        if df.empty:
            return render_template('dashboard.html', tracks=[], recommendations=[])
        
        # Categorize mood for each track
        df['mood'] = df.apply(categorize_mood, axis=1)
        
        # Get overall mood (most common)
        overall_mood = df['mood'].mode().iloc[0] if not df['mood'].mode().empty else 'Neutral or Mixed Mood'
        
        # Get recommendations based on overall mood
        recommendations = get_mood_recommendations(sp, overall_mood)
        
        tracks = df[['name', 'artist', 'album', 'mood', 'preview_url', 'external_url']].to_dict('records')
        
        return render_template('dashboard.html', 
                             tracks=tracks, 
                             recommendations=recommendations,
                             overall_mood=overall_mood)
                             
    except Exception as e:
        print(f"Error in dashboard: {e}")
        return render_template('dashboard.html', tracks=[], recommendations=[])

@app.route('/api/tracks')
def api_tracks():
    """API endpoint for getting user tracks"""
    token_info = session.get('token_info')
    if not token_info:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        df = get_recent_tracks(sp)
        
        if df.empty:
            return jsonify({'tracks': []})
        
        df['mood'] = df.apply(categorize_mood, axis=1)
        tracks = df[['name', 'artist', 'album', 'mood', 'preview_url', 'external_url']].to_dict('records')
        
        return jsonify({'tracks': tracks})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 