import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'demo-secret-key'

# Mock data for demonstration
MOCK_TRACKS = [
    {
        'name': 'Blinding Lights',
        'artist': 'The Weeknd',
        'album': 'After Hours',
        'mood': 'Happy and Energetic',
        'preview_url': 'https://p.scdn.co/mp3-preview/1234567890abcdef',
        'external_url': 'https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b'
    },
    {
        'name': 'Bohemian Rhapsody',
        'artist': 'Queen',
        'album': 'A Night at the Opera',
        'mood': 'Danceable and Upbeat',
        'preview_url': 'https://p.scdn.co/mp3-preview/abcdef1234567890',
        'external_url': 'https://open.spotify.com/track/3z8h0TU7ReDPLIbEnYhWZb'
    },
    {
        'name': 'See You Again',
        'artist': 'Tyler, The Creator',
        'album': 'Flower Boy',
        'mood': 'Sad or Melancholic',
        'preview_url': 'https://p.scdn.co/mp3-preview/tylerseeagain',
        'external_url': 'https://open.spotify.com/track/0rZ4w3f1GgRkym1P1h8n5z'
    },
    {
        'name': 'HUMBLE.',
        'artist': 'Kendrick Lamar',
        'album': 'DAMN.',
        'mood': 'Danceable and Upbeat',
        'preview_url': 'https://p.scdn.co/mp3-preview/kendrickhumble',
        'external_url': 'https://open.spotify.com/track/7KXjTSCq5nL1LoYtL7XAwS'
    },
    {
        'name': 'Clocks',
        'artist': 'Coldplay',
        'album': 'A Rush of Blood to the Head',
        'mood': 'Chill and Uplifting',
        'preview_url': 'https://p.scdn.co/mp3-preview/1122334455667788',
        'external_url': 'https://open.spotify.com/track/0BCPKOYdS2jbQ8iyB56Zns'
    }
]

MOCK_RECOMMENDATIONS = [
    {
        'name': 'Uptown Funk',
        'artist': 'Mark Ronson ft. Bruno Mars',
        'album': 'Uptown Special',
        'preview_url': 'https://p.scdn.co/mp3-preview/9988776655443322',
        'external_url': 'https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS'
    },
    {
        'name': 'Happy',
        'artist': 'Pharrell Williams',
        'album': 'G I R L',
        'preview_url': 'https://p.scdn.co/mp3-preview/5544332211009988',
        'external_url': 'https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH'
    },
    {
        'name': 'Can\'t Stop the Feeling!',
        'artist': 'Justin Timberlake',
        'album': 'Trolls (Original Motion Picture Soundtrack)',
        'preview_url': 'https://p.scdn.co/mp3-preview/6677889900112233',
        'external_url': 'https://open.spotify.com/track/6JV2JOE0o4LgnY4FXZqM6u'
    },
    {
        'name': 'Shake It Off',
        'artist': 'Taylor Swift',
        'album': '1989',
        'preview_url': 'https://p.scdn.co/mp3-preview/7788990011223344',
        'external_url': 'https://open.spotify.com/track/5y9shQDXq9arqF7mFo9V3a'
    },
    {
        'name': 'Good Time',
        'artist': 'Owl City & Carly Rae Jepsen',
        'album': 'The Midsummer Station',
        'preview_url': 'https://p.scdn.co/mp3-preview/8899001122334455',
        'external_url': 'https://open.spotify.com/track/1kP5gvLrlsMQdqb1zM9Oz9'
    }
]

@app.route('/')
def index():
    """Demo landing page"""
    return render_template('index.html')

@app.route('/demo')
def demo_dashboard():
    """Demo dashboard with mock data"""
    return render_template('dashboard.html', 
                         tracks=MOCK_TRACKS, 
                         recommendations=MOCK_RECOMMENDATIONS,
                         overall_mood='Happy and Energetic')

@app.route('/demo-tracks')
def demo_tracks():
    """Demo API endpoint"""
    return {'tracks': MOCK_TRACKS}

if __name__ == '__main__':
    print("🎵 Doom - Spotify Mood Detector DEMO")
    print("=" * 40)
    print("📍 Demo available at: http://localhost:5000/demo")
    print("📍 Landing page at: http://localhost:5000")
    print("=" * 40)
    app.run(debug=True, host='0.0.0.0', port=5050) 