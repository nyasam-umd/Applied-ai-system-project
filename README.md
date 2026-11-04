🎵 SoulVibes - Music Recommender Simulation

## Project Summary

## SoulVibes is a Python-based music recommendation system that suggests songs based on a user's preferred genre, mood, energy level, and acoustic preference. It uses a content-based scoring algorithm to rank songs and explain why each recommendation matches the the user's preferences.

## How The System Works

Song features

Each Song contains:

- ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo (BPM)
- Valence
- Danceability
- Acousticeness

User Profile

The UserProfile stores:

- Favorite genre
- Favorite mood
- Target energy
- Acoustic preference

Recommendation Algorithm

The Recommender scores songs based on user preferences:

- Genre match: +2
- Mood match: +1
- Energy similarity: Up to +1.5
- Acoustic preference: +0.5

Songs are ranked by score, and the top five are recommended.

Project Workflow

1. Load songs using Pandas.
2. Collect user preferences.
3. Calculate matching scores.
4. Rank songs
5. Display recommendations with explanations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Welcome to SoulVibes!

Top recommendations:

Sunrise City - Score: 4.47
Because: Matches your favorite genre; Matches your preferred mood

Gym Hero - Score: 3.30
Because: Matches your favorite genre

Rooftop Lights - Score: 2.44
Because: Matches your preferred mood

Night Drive Loop - Score: 1.42
Because: Matches your overall preferences

Storm Runner - Score: 1.33
Because: Matches your overall preferences

```
# e.g.:
# User profile: genre=pop, mood=happy, energy=0.8, likes_acoustic=False
# Recommendations:
#   1. Sunrise City - Score: 4.47
#   2. Gym Hero - Score: 3.30
#   3. Rooftop Lights - Score: 2.44
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran.

Tested different genre and mood preferences.
Compared recommendations with different energy levels.
Explored how acoustic preferences affect scores.

---

## Limitations and Risks

Summarize some limitations of your recommender.

- Uses a small song dataset.
- Does not analyze lyrics.
- Recommendations depend on accurate song data.
- May favor certain genres or moods.

---

## Reflection

I learned how recommendation systems use user preferences and scoring algorithms to suggest songs. I also learned how bias can affect recommendations, such as favoring certain genres and limiting music variety. Testing different preferences helped me understand how recommendation systems can be improved.

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

I learned that recommendation systems use data and scoring to predict what users might enjoy. They compare user preferences with song features such as genre, mood and energy to generate personalized recommendations.

I also learned that bias can happen when certain genres are overrepresented or some preferences receive more points than others. This can cause the system to recommend certain types of music more often while overlooking other preferences. Recommendation systems should consider fairness and diversity to provide better recommendations for different users.
