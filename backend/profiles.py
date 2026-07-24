import json
from pathlib import Path

PROFILES_FOLDER = Path(__file__).parent / "profiles"

def load_scoreboard_profile(profile_name):
    profile_path = PROFILES_FOLDER / f"{profile_name}.json"

    if not profile_path.exists():
        raise FileNotFoundError(
            f"Scoreboard profile not found: {profile_path}"
        )

    with open(profile_path, "r", encoding="utf-8") as file:
        return json.load(file)