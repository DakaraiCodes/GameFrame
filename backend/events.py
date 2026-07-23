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