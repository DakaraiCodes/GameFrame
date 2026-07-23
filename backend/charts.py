import matplotlib.pyplot as plt

def create_score_progression_chart(score_progression, team_names):
    clocks = []
    left_scores = []
    right_scores = []

    for entry in score_progression:
        left_score, right_score = map(
            int,
            entry["score"].split("-")
        )

        clocks.append(entry["game_clock"])
        left_scores.append(left_score)
        right_scores.append(right_score)

    plt.figure(figsize=(10, 5))

    plt.plot(
        clocks,
        left_scores,
        marker="o",
        label=team_names["left"]
    )

    plt.plot(
        clocks,
        right_scores,
        marker="o",
        label=team_names["right"],
    )

    plt.title("Score Progression")
    plt.xlabel("Game Clock")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("../data/score_progression.png")

    print(
        "Saved score progression char to"
        "../data/score_progression.png"
    )

    plt.close()