"""
Multi-step workflow for the SoulVibes music recommender.
"""

import os
from datetime import datetime

from src.recommender import (
    recommend_songs,
    validate_user_preferences,
    validate_song_dataset,
    validate_recommendations
)


def run_agent(songs, user_prefs, k=5):
    trace = [
        "# SoulVibes Agent Execution Trace",
        f"\nRun time: {datetime.now().isoformat(timespec='seconds')}",
        "\n## Workflow Steps"
    ]

    # Step 1: Check dataset
    trace.append("1. Checking song dataset.")
    errors = validate_song_dataset(songs)

    if errors:
        trace.append(f"Dataset validation failed: {errors}")
        save_trace(trace)
        raise ValueError("Dataset validation failed.")

    trace.append("Dataset validation passed.")

    # Step 2: Check user preferences
    trace.append("2. Checking user preferences.")
    errors = validate_user_preferences(user_prefs)

    if errors:
        trace.append(f"Preference validation failed: {errors}")
        save_trace(trace)
        raise ValueError("Preference validation failed.")

    trace.append("Preference validation passed.")

    # Step 3: Generate recommendations
    trace.append("3. Generating recommendations.")
    recommendations = recommend_songs(user_prefs, songs, k=k)

    # Step 4: Check recommendation output
    trace.append("4. Checking recommendation quality.")
    errors = validate_recommendations(recommendations)

    if errors:
        trace.append(f"Recommendation validation failed: {errors}")
        save_trace(trace)
        raise ValueError("Recommendation validation failed.")

    trace.append("Recommendation validation passed.")
    trace.append("5. Displaying validated recommendations.")

    save_trace(trace)
    return recommendations


def save_trace(trace):
    os.makedirs("logs", exist_ok=True)

    with open("logs/agent_trace.md", "a", encoding="utf-8") as file:
        file.write("\n".join(trace) + "\n\n---\n\n")