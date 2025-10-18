# Doom — Spotify Mood Detector
Doom is a web application that analyzes your Spotify listening patterns and generates mood-based music recommendations using Spotify’s audio features and intelligent mood classification.
## Features
- **Mood Analysis** — Interprets emotional characteristics of your music using Spotify audio feature data
- **Personalized Recommendations** — Suggests songs aligned with your detected mood
- **Listening Insights** — Provides an overview of your listening patterns and preferences
- **Audio Preview Playback** — Play 30-second previews directly in the application
- **Responsive Interface** — Optimized for desktop and mobile use
- **Secure Authentication** — Spotify OAuth2 integration for safe and private access
## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **API**: Spotify Web API
- **Authentication**: Spotify OAuth2
- **Data Processing**: Pandas
## Prerequisites
You will need:
- Python 3.8+
- Spotify Developer Account and API credentials
- Git (optional, for cloning)
## Installation
```bash
git clone <your-repo-url>
cd doom-spotify-mood-detector
python -m venv venv
source venv/bin/activate   # macOS / Linux 
# or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp env.example .env
```
Update .env with your Spotify Client ID, Client Secret, and Redirect URI

##Running the Application
```bash
cd src
python app.py
```

Visit http://localhost:5000 in your browser.
<img width="1708" height="975" alt="doom" src="https://github.com/user-attachments/assets/ebc547f9-98ed-4872-9bca-350ee6f2c495" />



##Project Structure
```bash
doom-spotify-mood-detector/
├── src/
│   ├── app.py
│   ├── static/
│   └── templates/
├── requirements.txt
├── env.example
└── README.md
```
## Mood Classification
Spotify’s audio features are used to determine mood based on values such as:
- **Valence** (positivity)
- **Energy**
- **Danceability**
- **Acousticness**
- **Tempo**
- **Instrumentalness**
These signals are mapped into categories like energetic, melancholic, chill, or ambient.
## Deployment
For production environments, consider:
- **Gunicorn or uWSGI** for WSGI serving
- **Nginx** as a reverse proxy
- `FLASK_ENV=production`
## License
MIT License
## Acknowledgments
Spotify Web API, Spotipy, Font Awesome, Inter Typeface
