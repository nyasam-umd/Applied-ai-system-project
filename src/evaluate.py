
"""
Evaluation script for the SoulVibes recommendation system.
Tests multiple user preference profiles and reports pass/fail results.
"""

from src.agent import run_agent
from src.recommender import load_songs, validate_recommendations


def main():
    songs = load_songs("data/songs.csv")

    if not songs:
        print("FAIL: Song dataset is empty.")
        return

    # Create three test profiles using actual songs in the dataset.
    test_profiles = []

    for song in songs[:3]:
        profile = {
            "favorite_genre": song["genre"],
            "favorite_mood": song["mood"],
            "target_energy": float(song["energy"]),
            "likes_acoustic": float(song["acousticness"]) >= 0.5
        }
        test_profiles.append(profile)

    passed = 0
    failed = 0

    print("\nSoulVibes Evaluation Results")
    print("----------------------------")

    for number, profile in enumerate(test_profiles, start=1):
        try:
            recommendations = run_agent(songs, profile, k=5)
            errors = validate_recommendations(recommendations)

            if not errors and recommendations:
                print(f"Test {number}: PASS")
                passed += 1
            else:
                print(f"Test {number}: FAIL - {errors}")
                failed += 1

        except (ValueError, KeyError, TypeError) as error:
            print(f"Test {number}: FAIL - {error}")
            failed += 1

    print("\nEvaluation Summary")
    print("------------------")
    print(f"Total tests: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()