def print_game_summary(summary, team_names):
    print("\n========================")
    print("     GAME SUMMARY")
    print("========================")

    print(f"\nQuarter: {summary['quarter']}")

    print("\nFinal Score")
    print(
        f"{team_names['left']} "
        f"{summary['final_score']['left']}"
    )
    print(
        f"{team_names['right']} "
        f"{summary['final_score']['right']}"
    )

    largest = summary["largest_lead"]

    if largest["team"] is not None:
        print("\nLargest Lead")

        print(
            f"{team_names[largest['team']]}"
            f"+{largest['lead']}"
        )

    largest_run = summary["largest_run"]

    if largest_run is not None:
        print("\nLargest Run")

        print(
            f"{team_names[largest_run ['team']]}"
            f"{largest_run['run']}"
        )

    print(
        f"\nScoring Events: {summary['total_scoring_events']}"
    )
    print(
        f"Lead Changes : {summary['lead_changes']}"
    )
    print(
        f"Scoring Runs : {summary['scoring_runs']}"
    )

    print("\n========================")