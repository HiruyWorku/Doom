# Doom - Spotify Mood Detector 🎵

A beautiful web application that analyzes your Spotify listening patterns and provides intelligent mood-based music recommendations using AI-powered audio feature analysis.

## ✨ Features

- **🎯 Mood Analysis**: AI-powered analysis of your music's emotional characteristics using Spotify's audio features
- **🎵 Smart Recommendations**: Get personalized song suggestions based on your current mood
- **📊 Listening Insights**: Understand your music preferences and patterns
- **🎧 Audio Previews**: Listen to song previews directly in the app
- **📱 Responsive Design**: Beautiful, modern UI that works on all devices
- **🔐 Secure Authentication**: OAuth2 integration with Spotify for secure access

## 🚀 Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: Spotify Web API
- **Styling**: Custom CSS with modern design patterns
- **Authentication**: Spotify OAuth2
- **Data Analysis**: Pandas for audio feature processing

## 📋 Prerequisites

Before running this application, you'll need:

1. **Python 3.8+** installed on your system
2. **Spotify Developer Account** with API credentials
3. **Git** for cloning the repository

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd doom-spotify-mood-detector
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the example environment file:
```bash
cp env.example .env
```

2. Edit `.env` and add your Spotify API credentials:
```env
# Spotify API Configuration
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:5000/callback

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key_here
FLASK_ENV=development
```

### 5. Get Spotify API Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Add `http://localhost:5000/callback` to your Redirect URIs
4. Copy your Client ID and Client Secret to the `.env` file

## 🎯 Usage

### Running the Application

```bash
# Make sure you're in the src directory
cd src

# Run the Flask application
python app.py
```

The application will be available at `http://localhost:5000`

### How to Use

1. **Visit the Application**: Open your browser and go to `http://localhost:5000`
2. **Connect Spotify**: Click "Connect with Spotify" to authorize the application
3. **View Your Mood**: The app will analyze your recent tracks and display your current music mood
4. **Get Recommendations**: Browse personalized song recommendations based on your mood
5. **Listen to Previews**: Click the play button to hear song previews
6. **Open in Spotify**: Click the Spotify icon to open songs in your Spotify app

## 📁 Project Structure

```
doom-spotify-mood-detector/
├── src/
│   ├── app.py                 # Main Flask application
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Application styles
│   │   └── js/
│   │       └── dashboard.js   # Dashboard functionality
│   └── templates/
│       ├── index.html         # Landing page
│       └── dashboard.html     # User dashboard
├── requirements.txt           # Python dependencies
├── package.json              # Node.js dependencies (if needed)
├── env.example              # Environment variables template
└── README.md                # This file
```

## 🎨 Features in Detail

### Mood Analysis
The application analyzes your music using Spotify's audio features:
- **Valence**: Measures musical positivity
- **Energy**: Represents intensity and activity
- **Danceability**: How suitable a track is for dancing
- **Tempo**: Beats per minute (BPM)
- **Acousticness**: Acoustic vs electronic sound
- **Instrumentalness**: Presence of vocals

### Mood Categories
- 🎉 **Happy and Energetic**: High valence and energy
- 😌 **Chill and Uplifting**: High valence, low energy
- 😢 **Sad or Melancholic**: Low valence and energy
- 💃 **Danceable and Upbeat**: High danceability and valence
- 🌿 **Ambient or Acoustic**: High acousticness and instrumentalness
- 😐 **Neutral or Mixed Mood**: Balanced features

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SPOTIFY_CLIENT_ID` | Your Spotify app client ID | Yes |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify app client secret | Yes |
| `SPOTIFY_REDIRECT_URI` | OAuth redirect URI | Yes |
| `FLASK_SECRET_KEY` | Flask session secret key | Yes |
| `FLASK_ENV` | Flask environment (development/production) | No |

### Customization

You can customize the application by modifying:

- **Mood Analysis**: Edit the `categorize_mood()` function in `app.py`
- **Recommendations**: Modify the `get_mood_recommendations()` function
- **Styling**: Update `src/static/css/style.css`
- **UI**: Edit the HTML templates in `src/templates/`

## 🚀 Deployment

### Local Development
```bash
cd src
python app.py
```

### Production Deployment
For production deployment, consider using:
- **WSGI Server**: Gunicorn or uWSGI
- **Reverse Proxy**: Nginx
- **Process Manager**: PM2 or Supervisor
- **Environment**: Set `FLASK_ENV=production`

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) for music data
- [Spotipy](https://spotipy.readthedocs.io/) for Python Spotify API wrapper
- [Font Awesome](https://fontawesome.com/) for icons
- [Inter Font](https://rsms.me/inter/) for typography

## 🐛 Troubleshooting

### Common Issues

1. **"Invalid redirect URI" error**
   - Make sure your redirect URI in Spotify Dashboard matches exactly: `http://localhost:5000/callback`

2. **"Module not found" errors**
   - Ensure you've activated your virtual environment
   - Run `pip install -r requirements.txt`

3. **Authentication errors**
   - Check that your Spotify API credentials are correct in `.env`
   - Verify your app has the required scopes

4. **No tracks showing**
   - Make sure you have recent listening history on Spotify
   - Check that your Spotify account has public listening activity

### Getting Help

If you encounter any issues:
1. Check the console for error messages
2. Verify your environment variables are set correctly
3. Ensure your Spotify app has the required permissions
4. Open an issue on GitHub with detailed error information

## 📊 Future Enhancements

- [ ] User accounts and preferences
- [ ] Playlist generation based on mood
- [ ] Historical mood tracking
- [ ] Social features and sharing
- [ ] Mobile app version
- [ ] Advanced audio analysis
- [ ] Integration with other music services

---

Made with ❤️ for music lovers everywhere
