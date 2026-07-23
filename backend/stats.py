def count_ties(score_progression):
    tie_count = 0

    for entry in score_progression[1:]:
        left_score, right_score = map(
            int,
            entry["score"].split("-")
        )

        if left_score == right_score:
            tie_count += 1

    return tie_count

def get_previous_valid_clock(timeline, index):
    for previous_index in range(index, -1, -1):
        game_clock = timeline[previous_index]["game_clock"]

        if game_clock is not None:
            return game_clock

    return None

def get_largest_run(scoring_runs):
    if not scoring_runs:
        return None

    largest_run = scoring_runs[0]

    for scoring_run in scoring_runs[1:]:
        if scoring_run["points"] > largest_run["points"]:
            largest_run = scoring_run

    return largest_run

def get_largest_lead(timeline):
    largest_lead = 0
    leader = None
    game_clock = None

    for index, state in enumerate(timeline):
        left = state["left_score"]
        right = state["right_score"]

        lead = abs(left - right)

        if lead > largest_lead:
            largest_lead = lead

            if left > right:
                leader = "left"
            elif right > left:
                leader = "right"
            else:
                leader = None

            game_clock = (
                state["game_clock"]
                or get_previous_valid_clock(timeline, index - 1)
            )

    return {
        "team": leader,
        "lead": largest_lead,
        "game_clock": game_clock,
    }