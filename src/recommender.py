import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Stores song information
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Stores user music perferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    Recommends songs based on user preferences.
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(user.__dict__, song.__dict__)[0],
            reverse=True     
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = score_song(user.__dict__, song.__dict__)
        return "; ".join(reasons) if reasons else "Matches your overall preferences."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file using Python's csv module.
    Returns a list of dictionaries, one per song.
    """
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append({key: value for key, value in row.items()})

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a song based on user experiences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    
    if user_prefs["favorite_genre"].lower() == song["genre"].lower():
        score += 2
        reasons.append("Matches your favorite genre")
        
    if user_prefs["favorite_mood"].lower() == song["mood"].lower():
            score += 1
            reasons.append("Matches your preferred mood")
    energy_difference = abs(
        float(user_prefs["target_energy"]) - float(song["energy"])
    )
    score += max(0, 1.5 - energy_difference * 1.5)
    
    if user_prefs.get("likes_acoustic", False):
        if float(song["acousticness"]) >= 0.5:
            score += 0.5
            reasons.append("Has an acoustic sound")
    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Returns the highest-ranked songs.
    Required by src/main.py
    """
    
    results = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "Matches your overall preferences"
        results.append((song, score, explanation))
        
    results.sort(key=lambda item: item[1], reverse=True)
    return results[:k]
def validate_user_preferences(user_prefs: Dict) -> List[str]:
    errors = []
    
    if not user_prefs.get("favorite_genre"):
        errors.append("Favorite genre is required.")
    if not user_prefs.get("favorite_mood"):
        errors.append("Favorite mood is required.")
    
    try:
        energy = float(user_prefs.get("target_energy"))
        if not 0 <= energy <= 1:
            errors.append("Target energy must be between 0 and 1.")
    except (TypeError, ValueError):
        errors.append("Target energy must be a number.")
    if not isinstance(user_prefs.get("likes_acoustic"), bool):
        errors.append("Acostic preference must be True or False.")
    
    return errors
def validate_recommendations(recommendations) -> List [str]:
    errors = []
    
    if not recommendations:
        return ["No recommendations were generated."]
    for song, score, explanation in recommendations:
        if not song.get("title"):
            errors.append("Recommendation is missing a song title.")
        if not isinstance(score, (int, float)) or not 0 <= score <= 5:
            errors.append("Recommendation has an invalid score.")
        if not explanation.strip():
            errors.append("Recommendation is missing an explanation.")
    return errors
def validate_song_dataset(songs: List[Dict]) -> List[str]:
    errors = []
    required = ["title", "artist", "genre", "mood", "energy", "acousticness"]
    
    if not songs:
        return ["Song dataset is empty."]
    
    for i, song in enumerate(songs):
        for field in required:
            if not song.get(field):
                errors.append(f"Song {i+1}: missing {field}.")
        for field in ["energy", "acousticness"]:
            try:
                if not 0 <= float(song[field]) <= 1:
                    errors.append(f"Song {i+1}: invalid {field}.")
            except (ValueError, TypeError, KeyError):
                errors.append(f"Song {i+1}: invalid {field}.")
    return errors
    
        
