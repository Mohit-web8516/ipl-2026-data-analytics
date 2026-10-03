# IPL 2026 Data Analytics

An end-to-end data analytics project exploring IPL 2026 match and player performance using Python, Pandas, NumPy, Matplotlib, Seaborn, and Power BI.

## Project Overview

This project analyzes IPL 2026 data to identify patterns in team performance, batting, bowling, match results, and player contributions. It follows a structured analytics workflow, from raw data auditing and cleaning to exploratory data analysis and visualization.

**Project Status:** Data auditing, integration, exploratory data analysis, and Python visualizations completed. Power BI dashboard development is planned.

## Dataset

The project uses IPL 2026 data stored in CSV format.

The dataset includes the following files:

| File | Description |
|---|---|
| `matches.csv` | Match-level information and results |
| `deliveries.csv` | Ball-by-ball match data |
| `batting_stats.csv` | Batting performance statistics |
| `bowling_stats.csv` | Bowling performance statistics |
| `fielding_stats.csv` | Fielding performance statistics |
| `points_table.csv` | Team points table data |
| `squads.csv` | Team squad information |
| `venues.csv` | Venue information |

**Note:** The analysis focuses on the available 2026 dataset. Some records and match metadata may be incomplete.

## Tools and Technologies

- **Python:** Data processing and analysis
- **Pandas:** Data cleaning, manipulation, and aggregation
- **NumPy:** Numerical operations
- **Matplotlib and Seaborn:** Data visualization
- **Jupyter Notebook:** Exploratory analysis and documentation
- **Power BI:** Interactive dashboard development (planned)
- **Git and GitHub:** Version control and project hosting

## Project Workflow

The project follows a structured data analytics workflow:

1. **Data Collection**  
   Collected the available IPL 2026 datasets in CSV format and organized the original files.

2. **Data Auditing**  
   Inspected dataset dimensions, column names, data types, missing values, duplicate records, and consistency between match and delivery data.

3. **Data Cleaning and Integration**  
   Prepared the data for analysis, investigated data quality issues, and integrated ball-by-ball delivery records with match-level information.

4. **Exploratory Data Analysis (EDA)**  
   Analyzed match results, team performance, batting and bowling statistics, innings scores, and match-level trends using Python.

5. **Data Visualization**  
   Created charts to communicate key patterns and findings, including scoring trends, player performance, team comparisons, and match outcomes.

6. **Power BI Dashboard (Planned)**  
   Use the prepared data to build an interactive dashboard for exploring IPL 2026 team, player, and match performance.

## Key Analysis Areas

The project explores the following areas using IPL 2026 data:

- **Match Analysis:** Match-wise scores, innings comparisons, scoring patterns, and match outcomes.
- **Team Performance:** Team scoring trends, average runs, recorded wins, and batting and bowling performance.
- **Batting Analysis:** Top run scorers, batting strike rates, boundaries, and individual scoring patterns.
- **Bowling Analysis:** Top wicket-takers, economy rates, and bowling performance across teams.
- **Innings Phase Analysis:** Run rates and wicket rates during the powerplay, middle overs, and death overs.
- **Toss and Match Outcomes:** Toss decisions, toss-related results, winning margins, and player-of-the-match awards.

## Key Findings

The exploratory data analysis revealed several patterns in IPL 2026:

- **High-Scoring Matches:** The average combined score across the 74 matches represented in the delivery data was approximately 370 runs.
- **Innings Scoring:** First innings had an average score of approximately 195 runs, compared with 180 runs in the second innings.
- **Batting Leaders:** Vaibhav Sooryavanshi (776 runs), Shubman Gill (732 runs), and Sai Sudharsan (722 runs) were among the leading run scorers in the analyzed data.
- **Scoring by Match Phase:** The death overs had the highest run rate (10.76 runs per over), followed by the powerplay (10.08) and middle overs (9.29).
- **Wickets by Match Phase:** The death overs had the highest wicket rate, at approximately 7.66 wickets per 100 legal balls.
- **Data Quality:** The analysis identified inconsistencies between match-level and delivery-level records, including incomplete match data and score mismatches.

**Note:** These findings describe the available dataset and may be affected by incomplete or inconsistent records. They should not be interpreted as final official season statistics.

## Visualizations

The project includes 31 visualizations created using Matplotlib and Seaborn to explore IPL 2026 match and player performance.

Some of the key visualizations include:

| Visualization | Description |
|---|---|
| Match-wise Total Runs | Compares total runs scored across matches |
| First vs Second Innings Scores | Examines scoring differences between innings |
| Top 10 Run Scorers | Highlights leading batters by total runs |
| Runs vs Strike Rate | Compares batting output and scoring rate |
| Phase-wise Run Rate | Analyzes scoring patterns across innings phases |
| Top 10 Wicket Takers | Shows leading bowlers by wickets |
| Team-wise Recorded Wins | Compares wins recorded in the available match data |
| Toss Decision Analysis | Explores toss decisions and match outcomes |

All charts are available in the [`Visualizations`](Visualizations/) folder.

## Project Structure

```text
ipl-2026-analytic/
│
├── Cleaned-Data/       # Processed and integrated datasets
├── Docs/               # Project documentation 
├── notebooks/          # Jupyter notebooks for analysis
├── Original-Data/      # Original IPL 2026 datasets
├── PowerBI/            # Power BI dashboard 

├── Visualizations/     # Exported charts and graphs
├── README.md
└── requirements.txt
```

## Installation and Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Mohit-web8516/ipl-2026-data-analytics.git
cd ipl-2026-data-analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` folder and run the cells to explore the analysis.

### 6. Deactivate the Virtual Environment

When you're finished, run:

```bash
deactivate
```

## Conclusion

This project explores IPL 2026 data through data auditing, cleaning, exploratory data analysis, and visualization using Python.

The analysis provides insights into team performance, batting and bowling statistics, scoring patterns, and match outcomes. It also highlights data quality issues that are important to consider when interpreting the results.

The next stage of the project is to develop an interactive Power BI dashboard to present the findings and make the analysis easier to explore.