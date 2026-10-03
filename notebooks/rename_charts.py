from pathlib import Path

folder = Path("Visualizations")

rename_map = {
    "visualization_01.png": "match_wise_total_runs.png",
    "visualization_02.png": "match_total_runs_distribution.png",
    "visualization_03.png": "average_match_total_by_venue.png",
    "visualization_04.png": "first_vs_second_innings_scores.png",
    "visualization_05.png": "completed_match_innings_comparison.png",
    "visualization_06.png": "top_10_run_scorers_step09.png",
    "visualization_07.png": "top_10_run_scorers_strike_rate.png",
    "visualization_08.png": "runs_vs_strike_rate_top_10.png",
    "visualization_09.png": "fours_and_sixes_top_10_batters.png",
    "visualization_10.png": "boundary_run_contribution.png",
    "visualization_11.png": "team_wise_total_runs.png",
    "visualization_12.png": "team_average_runs_per_innings.png",
    "visualization_13.png": "team_innings_score_distribution.png",
    "visualization_14.png": "phase_wise_run_rate.png",
    "visualization_15.png": "phase_wise_wicket_rate.png",
    "visualization_16.png": "top_10_wicket_takers.png",
    "visualization_17.png": "wickets_vs_economy_top_10_bowlers.png",
    "visualization_18.png": "team_wise_bowling_performance.png",
    "visualization_19.png": "team_wise_batting_performance.png",
    "visualization_20.png": "team_wise_recorded_wins.png",
    "visualization_21.png": "toss_decision_distribution.png",
    "visualization_22.png": "toss_winner_win_percentage_by_decision.png",
    "visualization_23.png": "match_wins_by_type.png",
    "visualization_24.png": "combined_winning_margin_distribution.png",
    "visualization_25.png": "separate_winning_margin_distributions.png",
    "visualization_26.png": "player_of_the_match_awards.png",
    "visualization_27.png": "top_10_run_scorers_step27.png",
    "visualization_28.png": "top_10_batters_by_strike_rate.png",
    "visualization_29.png": "all_batters_runs_vs_strike_rate.png",
    "visualization_30.png": "batter_runs_distribution.png",
    "visualization_31.png": "batter_runs_vs_balls_faced.png"
}

# Validate before renaming
missing = [
    old for old in rename_map
    if not (folder / old).exists()
]

conflicts = [
    new for old, new in rename_map.items()
    if (folder / new).exists() and old != new
]

if missing:
    print("Missing files:", missing)
elif conflicts:
    print("Destination files already exist:", conflicts)
else:
    for old, new in rename_map.items():
        (folder / old).rename(folder / new)

    print("Successfully renamed all 31 visualizations!")