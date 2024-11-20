# Doom: Spotify Mood Detector

## Project Overview
**Doom: Spotify Mood Detector** is a web application that provides dynamic song search, playback, and recommendations based on the user's mood. The project integrates **Spotify API** for music search and playback and **Echo Nest API** for analyzing song moods. The recommendation algorithm utilizes **Python** and **Node.js** to provide personalized song recommendations.

## Features
- **Search and Playback**: Users can search for songs and play them directly from the app using the Spotify API.
- **Mood-Based Recommendations**: Songs are recommended based on mood analysis using the Echo Nest API.
- **User-Friendly Interface**: The front-end is built with **HTML**, **CSS**, and **TypeScript**, providing a simple, clean interface.
- **Backend with Node.js**: Handles API requests and serves data to the front-end.
- **Recommendation Algorithm**: The recommendation logic is implemented in Python and integrated into the Node.js backend.

## Tech Stack
- **Frontend**: HTML, CSS, TypeScript
- **Backend**: Node.js, Express, Python
- **APIs**: Spotify API, Echo Nest API
- **Database**: MongoDB (for storing user preferences)
- **Version Control**: Git

## Project Structure
```bash
doom-spotify-mood-detector/
│
├── public/              # Static assets (images, icons, etc.)
├── src/                 # Frontend source files
│   ├── app.ts           # Main TypeScript app logic
│   ├── index.html       # Main HTML file
│   ├── styles.css       # Application styles
│
├── server.js            # Node.js server
├── recommendation.py    # Python file for song mood analysis and recommendation
├── manifest.json        # Chrome Extension manifest
├── package.json         # Project dependencies
├── README.md            # Documentation
