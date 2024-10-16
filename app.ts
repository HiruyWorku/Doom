import { getRecommendations } from './recommendation';

const searchButton = document.getElementById("searchBtn");
const songInput = document.getElementById("songSearch") as HTMLInputElement;
const songList = document.getElementById("songList");
const recommendationDiv = document.getElementById("recommendation");

searchButton?.addEventListener('click', async () => {
  const searchTerm = songInput.value;

  // Fetch songs from Spotify API
  const songs = await fetch(`/api/search?song=${encodeURIComponent(searchTerm)}`);
  const songData = await songs.json();

  // Display songs
  if (songList) {
    songList.innerHTML = '';
    songData.forEach((song: any) => {
      const songItem = document.createElement('div');
      songItem.textContent = `${song.name} by ${song.artist}`;
      songList.appendChild(songItem);
    });
  }

  // Fetch recommendations
  const recommendation = await getRecommendations(searchTerm);
  if (recommendationDiv) {
    recommendationDiv.textContent = `Recommended song based on mood: ${recommendation}`;
  }
});
