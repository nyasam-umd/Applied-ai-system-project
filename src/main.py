"""
Command line runner for SoulVibes.
"""
from src.agent import run_agent
from src.recommender import(
    load_songs,
    recommend_songs,
    validate_user_preferences,
    validate_song_dataset,
    validate_recommendations
)


def main() -> None:
    songs = load_songs("data/songs.csv") 

    errors = validate_song_dataset(songs)
    if errors:
        print("Dataset errors:", errors)
        return
    
    user_prefs = {"favorite_genre": "pop", 
                  "favorite_mood": "happy", 
                  "target_energy": 0.8, 
                  "likes_acoustic": False
                  }
    errors = validate_user_preferences(user_prefs)
    if errors:
        print("Perferencw errors:", errors)
        return
    recommendations = run_agent(songs, user_prefs, k=5)
    
    errors = validate_recommendations(recommendations)
    if errors:
        print("Recommendation errors:", errors)
        return
    
    print("\nWelcome to SoulVibes!")
    print("\nTop recommendations:\n")
    
    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}\n")
        print()


if __name__ == "__main__":
    main()
