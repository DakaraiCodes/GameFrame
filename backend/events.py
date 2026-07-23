def get_previous_valid_clock(timeline, index):
    for previous_index in range(index, -1, -1):
        game_clock = timeline[previous_index]["game_clock"]

        if game_clock is not None:
            return game_clock

    return None

def detect_scoring_events(timeline):
    events = []

    for index in range(1, len(timeline)):
        previous = timeline[index - 1]
        current = timeline[index]

        previous_left = previous["left_score"]
        previous_right = previous["right_score"]

        current_left = current["left_score"]
        current_right = current["right_score"]

        left_change = current_left - previous_left
        right_change = current_right - previous_right

        if left_change > 0:
            events.append({
                "frame": index + 1,
                "team": "left",
                "points": left_change,
                "game_clock": (
                    current["game_clock"]
                    or get_previous_valid_clock(timeline, index - 1)
                ),
                "score": f"{current_left}-{current_right}",
            })
        if right_change > 0:
            events.append({
                "frame": index + 1,
                "team": "right",
                "points": right_change,
                "game_clock": (
                    current["game_clock"]
                    or get_previous_valid_clock(timeline, index - 1)
                ),
                "score": f"{current_left}-{current_right}",
            })

    return events

def get_leader(left_score, right_score):
    if left_score > right_score:
        return "left"

    if right_score > left_score:
        return "right"

    return "tie"

def detect_lead_changes(scoring_events):
    lead_changes = []
    previous_leader = "tie"

    for event in scoring_events:
        left_score, right_score = map(
            int,
            event["score"].split("-")
        )

        current_leader = get_leader(
            left_score,
            right_score
        )

        if (
            current_leader != "tie"
            and current_leader != previous_leader
        ):
            lead_changes.append({
                "frame": event["frame"],
                "new_leader": current_leader,
                "game_clock": event["game_clock"],
                "score": event["score"],
            })

        previous_leader = current_leader

    return lead_changes

def build_score_progression(scoring_events):
    progression = [
        {
            "score": "0-0",
            "game_clock": "12:00",
        }
    ]

    for event in scoring_events:
        progression.append({
            "score": event["score"],
            "game_clock": event["game_clock"]
        })

    return progression 
