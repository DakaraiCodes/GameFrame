def detect_scoring_runs(scoring_events):
    runs = []

    current_team = None
    current_points = 0
    start_event = None

    for event in scoring_events:
        team = event["team"]
        points = event["points"]

        if team == current_team:
            current_points += points

        else:
            if current_team is not None:
                runs.append({
                    "team": current_team,
                    "points": current_points,
                    "start_clock": start_event["game_clock"],
                    "end_clock": event["game_clock"],
                })

            current_team = team
            current_points = points
            start_event = event

    # Save the final run after the loop finishes
    if current_team is not None:
        runs.append({
            "team": current_team,
            "points": current_points,
            "start_clock": start_event["game_clock"],
            "end_clock": scoring_events[-1]["game_clock"],
        })

    return runs