from profiles import SCOREBOARD_PROFILES


def crop_region(image, region_profile):
    image_height, image_width = image.shape[:2]

    return image[
        int(image_height * region_profile["top"]):
        int(image_height * region_profile["bottom"]),

        int(image_width * region_profile["left"]):
        int(image_width * region_profile["right"])
    ]


def analyze_scoreboard(image, profile_name="sample_game"):
    profile = SCOREBOARD_PROFILES[profile_name]

    scoreboard = crop_region(
        image,
        profile["scoreboard"]
    )

    regions = {
        "scoreboard": scoreboard
    }

    for region_name, region_profile in profile.items():
        if region_name == "scoreboard":
            continue

        regions[region_name] = crop_region(
            scoreboard,
            region_profile
        )

    return regions