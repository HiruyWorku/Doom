from echo_nest_api import EchoNestAPI

def get_recommendation(song_name):
    api = EchoNestAPI("YOUR_ECHO_NEST_API_KEY")
    
    # Analyzing the song mood
    song_analysis = api.analyze_song(song_name)
    mood = song_analysis.get('mood')

    # Based on mood, recommending another song
    if mood == 'happy':
        return "Happy Song by Artist A"
    elif mood == 'sad':
        return "Sad Song by Artist B"
    else:
        return "Neutral Song by Artist C"
