const express = require('express');
const axios = require('axios');
const { getRecommendations } = require('./recommendation');
const app = express();

app.use(express.json());
app.use(express.static('public'));

app.get('/api/search', async (req, res) => {
  const searchTerm = req.query.song;
  const token = await getSpotifyToken();
  
  const response = await axios.get(`https://api.spotify.com/v1/search`, {
    headers: {
      'Authorization': `Bearer ${token}`
    },
    params: {
      q: searchTerm,
      type: 'track'
    }
  });

  const songs = response.data.tracks.items.map(item => ({
    name: item.name,
    artist: item.artists[0].name,
    preview: item.preview_url
  }));

  res.json(songs);
});

app.get('/api/recommend', async (req, res) => {
  const song = req.query.song;
  const recommendation = await getRecommendations(song);
  res.json({ recommendation });
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});

async function getSpotifyToken() {
  // Logic to get OAuth token from Spotify API
}
