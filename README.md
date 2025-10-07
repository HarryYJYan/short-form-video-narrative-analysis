# Short Form Video Narrative Perception Analysis

## Project Overview

This repository contains the data analysis for an experiment investigating people's narrative perceptions of short form videos. The study examines how individuals perceive and evaluate narrative elements in short-form video content, with the goal of understanding the psychological factors that influence narrative comprehension and engagement.

## Experiment Design (Sample Data)

> **Note**: This repository contains analysis of sample data from an ongoing study. Results are preliminary and for demonstration purposes.

- **Participants**: 122 participants recruited for the study
- **Videos**: 40 short form videos representing diverse content types
- **Procedure**: Each participant watched 4 randomly selected videos and provided narrative perception ratings
- **Total Responses**: 488 video ratings (122 participants × 4 videos each)
- **Data Collection Period**: September 25 - October 7, 2025 (12 days)
- **Measures**: Comprehensive ratings on timing, familiarity, comprehension, tension, resolution, and future behavior

## Repository Structure

```
short-form-video-narrative-analysis/
├── README.md                                    # This file
├── .gitignore                                  # Git ignore rules
├── code/                                       # Analysis code
│   ├── data_cleaning.py                       # Data cleaning and preprocessing
│   └── simple_descriptive_analysis.py         # Descriptive analysis functions
├── data/                                       # Data files
│   ├── README.md                              # Data documentation
│   ├── SML+Narrative+Resolution+-+REP_October+7,+2025_16.56.csv  # Raw data
│   ├── video_narrative_cleaned_wide_format.csv # Cleaned wide format data
│   ├── video_narrative_cleaned_long_format.csv # Cleaned long format data
│   └── video_narrative_cleaned_quality_report.txt # Data quality report
├── docs/                                       # Documentation
│   ├── experiment_design.md                   # Detailed experiment methodology
│   ├── data_analysis_plan.md                  # Comprehensive analysis plan
│   ├── data_cleaning_documentation.md         # Data cleaning procedures
│   └── descriptive_analysis_documentation.md  # Analysis results and findings
├── analysis_outputs/                           # Analysis results
│   ├── simple_descriptive_analysis_report.md  # Summary report
│   └── simple_descriptive_analysis.png        # Key visualizations
└── scripts/                                    # Utility scripts
    └── setup_environment.py                   # Environment setup script
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd short-form-video-narrative-analysis
   ```

2. Set up the Python environment:
   ```bash
   python scripts/setup_environment.py
   ```

3. Run the descriptive analysis:
   ```bash
   python code/simple_descriptive_analysis.py
   ```

### Required Packages

- pandas >= 1.5.0
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0
- scipy >= 1.9.0
- scikit-learn >= 1.1.0
- jupyter >= 1.0.0

## Research Questions

1. **Primary**: How do people perceive narratives in short form videos across different content types?
2. **Secondary**: What individual differences predict narrative perception patterns?
3. **Exploratory**: Are there consistent patterns in how different narrative elements are evaluated?

## Key Measures (Sample Data Results)

### Timing Variables
- **timing_first_click**: 9.85 ± 33.33 seconds
- **timing_last_click**: 16.65 ± 41.61 seconds  
- **timing_page_submit**: 82.31 ± 331.03 seconds
- **timing_click_count**: 0.71 ± 1.91 clicks

### Familiarity Variables
- **familiarity_seen**: 52.9% "None of the above"
- **familiarity_plot**: 36.1% "Strongly disagree"
- **familiarity_characters**: 29.1% "Strongly disagree"

### Comprehension Variables
- **clear_starting_point**: 40.0% "Somewhat agree"
- **inferring_context**: 44.7% "Somewhat agree"
- **built_interest_tension**: 42.6% "Somewhat agree"
- **clear_outcome**: 34.2% "Somewhat agree"
- **logical_flow**: 41.0% "Somewhat agree"

### Tension Variables
- **tension_beginning**: 31.50 ± 25.46 (scale 0-100)
- **tension_middle**: 46.99 ± 24.70 (scale 0-100)
- **tension_end**: 47.05 ± 31.73 (scale 0-100)

### Resolution Variables
- **narrative_resolution**: 60.0% "No"
- **satisfactory_resolution**: 79.5% "Yes" (when resolution present)
- **concluded_scene**: 65.0% "No"

### Future Behavior Variables
- **want_next_story**: 35.2% "Somewhat agree"
- **want_broader_context**: 36.1% "Somewhat agree"
- **watch_full_episode**: 27.3% "Somewhat agree"

## Analysis Status

### ✅ Completed
1. **Data Preparation**: ✅ Cleaning, validation, and quality assessment completed
2. **Descriptive Analysis**: ✅ Comprehensive descriptive analysis with 488 responses analyzed
3. **Data Quality Assessment**: ✅ 100% response rates, balanced video coverage

### 🔄 In Progress / Planned
4. **Primary Analysis**: Statistical tests for main research questions
5. **Advanced Modeling**: Multilevel modeling and machine learning approaches
6. **Exploratory Analysis**: Pattern discovery and subgroup analysis

### 📊 Current Findings
- **Sample Quality**: Excellent data completeness with 122 participants, 40 videos, 488 total responses
- **Experimental Design**: Successfully implemented balanced sampling (each participant rated 4 videos)
- **Response Patterns**: Moderate narrative comprehension, effective tension building, resolution challenges

## Data Privacy and Ethics

- All participant data is anonymized and stored securely
- Personal identifiers have been removed from the dataset
- Participants provided informed consent for data use
- Data access is restricted to authorized research team members

## Contributing

This is a research repository. For questions about the analysis or data, please contact the research team.

## License

[To be determined based on institutional requirements]

## Contact

- **Repository**: [https://github.com/HarryYJYan/short-form-video-narrative-analysis](https://github.com/HarryYJYan/short-form-video-narrative-analysis)
- **Data Analysis**: This repository contains sample data analysis for demonstration purposes

## Citation

If you use this code or data in your research, please cite:

```
[Citation format to be added once paper is published]
```

## Acknowledgments

- Thanks to all participants who contributed their time to this research
- Sample data provided for analysis demonstration and method validation
