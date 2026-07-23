def build_game_summary(
    timeline,
    scoring_events,
    lead_changes,
    scoring_runs,
    largest_lead,
    largest_run,
):
    final_state = timeline[-1]

    return {
        "quarter": final_state["quarter"],
        "final_score": {
            "left": final_state["left_score"],
            "right": final_state["right_score"],
        },
        "total_scoring_events": len(scoring_events),
        "lead_changes": len(lead_changes),
        "scoring_runs": len(scoring_runs),
        "largest_lead": largest_lead,
        "largest_run": largest_run,
    }
