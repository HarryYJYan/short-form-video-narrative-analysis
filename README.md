# Short Form Video Narrative Perception Analysis

## Project Overview

This repository contains the data analysis for an experiment investigating people's narrative perceptions of short form videos. The study examines how individuals perceive and evaluate narrative elements in short-form video content, with the goal of understanding the psychological factors that influence narrative comprehension and engagement.

## Experiment Design

- **Participants**: [Number] participants recruited for the study
- **Videos**: 40 short form videos representing diverse content types
- **Procedure**: Each participant watched 4 randomly selected videos and provided narrative perception ratings
- **Measures**: Ratings on narrative clarity, emotional impact, story coherence, engagement, and complexity

## Repository Structure

```
short-form-video-narrative-analysis/
├── README.md                           # This file
├── .gitignore                         # Git ignore rules
├── code/                              # Analysis code
│   ├── data_cleaning.py              # Data cleaning and preprocessing
│   └── analysis.py                   # Statistical analysis functions
├── data/                              # Data files
│   ├── README.md                     # Data documentation
│   ├── raw/                          # Original, unprocessed data
│   └── processed/                    # Cleaned and processed data
├── docs/                              # Documentation
│   ├── experiment_design.md          # Detailed experiment methodology
│   └── data_analysis_plan.md         # Comprehensive analysis plan
├── notebooks/                         # Jupyter notebooks
│   └── exploratory_analysis.ipynb    # Exploratory data analysis
└── scripts/                           # Utility scripts
    └── setup_environment.py          # Environment setup script
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

3. Start Jupyter notebook for exploratory analysis:
   ```bash
   jupyter notebook notebooks/exploratory_analysis.ipynb
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

## Key Measures

- **Narrative Clarity**: How clear and understandable is the narrative structure?
- **Emotional Impact**: How emotionally engaging is the video content?
- **Story Coherence**: How well-structured and coherent is the story?
- **Engagement**: How engaging and compelling is the overall experience?
- **Narrative Complexity**: How complex or simple is the narrative structure?

## Analysis Approach

The analysis follows a comprehensive multi-phase approach:

1. **Data Preparation**: Cleaning, validation, and quality assessment
2. **Descriptive Analysis**: Understanding patterns in the data
3. **Primary Analysis**: Statistical tests for main research questions
4. **Advanced Modeling**: Multilevel modeling and machine learning approaches
5. **Exploratory Analysis**: Pattern discovery and subgroup analysis

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

- **Principal Investigator**: [Name and contact information]
- **Research Team**: [Additional team member information]

## Citation

If you use this code or data in your research, please cite:

```
[Citation format to be added once paper is published]
```

## Acknowledgments

- Thanks to all participants who contributed their time to this research
- [Additional acknowledgments for funding, collaborators, etc.]
