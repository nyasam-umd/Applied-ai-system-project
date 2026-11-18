🎵 SoulVibes - Music Recommender Simulation

Project Summary

SoulVibes is a Python-based music recommendation system that suggests songs based on a user's preferred genre, mood, energy level, and acoustic preference. It uses a content-based scoring algorithm to rank songs and explain why each recommendation matches the the user's preferences.

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

1. Load songs from the dataset.
2. Use a user preference profile.
3. Calculate recommendation scores.
4. Rank songs
5. Validate the recommendations.
6. Display recommendations with explanations.

Multi-Step Python Workflow

SoulVibes includes a multi-step Python workflow in src/agent.py

The workflow:

1. Validates the song dataset.
2. Validates user preferences.
3. Generates recommendations.
4. Validates recommendation results.
5. Saves an executon trace to logs/agent_trace.md.

## The workflow uses predefined Python steps and validation functions. It is not an autonomous large language model agent.

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
python -m pytest
The project currently includes 6 automated tests.
```

You can add more tests in `tests/test_recommender.py`.

Running the Evaluation Script

Run:
python -m src.evaluate

The evaluation script tests 3 user preference profiles and displays a pass/fail summary.

The latest test run completed with 3 passed tests and 0 failed tests.

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

**Screenshot or video** _(optional)_:
Link to video:

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
- Does not analyze song lyrics.
- Recommendations depend on accurate song data.
- May favor certain genres or moods.
- The evaluation script checks basic recommendation validity rather than fully measuring recommendation relevance or user satisfaction.

---

## Reflection

I learned how recommendation systems use user preferences and scoring algorithms to suggest songs. I also learned how bias can affect recommendations, such as favoring certain genres and limiting music variety. Testing different preferences helped me understand how recommendation systems can be improved. I also learned the importance of validating data and checking recommendation results before displaying them.

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

I learned that recommendation systems use data and scoring to predict what users might enjoy. They compare user preferences with song features such as genre, mood and energy to generate personalized recommendations.

I also learned that bias can happen when certain genres are overrepresented or some preferences receive more points than others. This can cause the system to recommend certain types of music more often while overlooking other preferences. Recommendation systems should consider fairness and diversity to provide better recommendations for different users.
Evaluation

SoulVibes includes an evaluation script that tests the recommendation workflow using three user preference profiles.

To run the evaluation:
python -m src.evaluate

The script reports individual test results and a summary of passed and failed tests.

## Demo Video

https://github.com/nyasam-umd/Applied-ai-system-project/blob/main/assets/demo-video/SoulVibes-Demo.webm
