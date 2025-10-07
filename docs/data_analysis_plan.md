# Data Analysis Plan: Short Form Video Narrative Perceptions

## Analysis Overview

This document outlines the comprehensive data analysis plan for the short form video narrative perception experiment. The analysis will progress from descriptive statistics through inferential tests to advanced modeling techniques.

## Phase 1: Data Preparation and Quality Assessment ✅ COMPLETED

### Data Cleaning ✅ COMPLETED
1. **Missing Data Assessment** ✅ COMPLETED
   - ✅ Identified patterns: 90% missing data expected (participants only rated 4/40 videos)
   - ✅ Documented reasons: Experimental design - each participant rated exactly 4 videos
   - ✅ Implemented appropriate handling: Analyzed only actual responses (488 out of 4,880 rows)

2. **Outlier Detection** ✅ COMPLETED
   - ✅ Session duration outliers identified (mean 34.7 ± 110.1 minutes)
   - ✅ Response time analysis completed for timing variables
   - ✅ Visual inspection of rating distributions completed

3. **Data Validation** ✅ COMPLETED
   - ✅ Checked for impossible or inconsistent responses
   - ✅ Verified random assignment was successful (balanced video coverage)
   - ✅ Validated data entry accuracy (100% response rates for actual responses)

### Data Transformation
1. **Scale Reliability**
   - Calculate Cronbach's alpha for multi-item measures
   - Assess internal consistency of rating scales

2. **Variable Creation**
   - Composite scores for related measures
   - Categorical variables from continuous demographics
   - Video-level aggregate statistics

## Phase 2: Descriptive Analysis ✅ COMPLETED

### Participant Characteristics ✅ COMPLETED
- ✅ Demographic profile summary: 122 participants, English interface, 12-day collection period
- ✅ Session duration analysis: Mean 34.7 ± 110.1 minutes (median: 18.9 minutes)
- ✅ Sample representativeness assessment: Balanced experimental design confirmed

### Video Characteristics ✅ COMPLETED
- ✅ Descriptive statistics for each of the 40 videos: 6-20 responses per video (mean: 12.2 ± 2.9)
- ✅ Video coverage analysis: All 40 videos received responses from multiple participants
- ✅ Summary of video-level rating patterns: Balanced distribution across videos

### Rating Patterns ✅ COMPLETED
- ✅ Distribution of all narrative perception ratings: 488 total responses analyzed
- ✅ Response patterns by category: Timing, Familiarity, Comprehension, Tension, Resolution, Future Behavior
- ✅ Individual differences in rating patterns: Each participant provided 4 complete video ratings

### Visualizations ✅ COMPLETED
- ✅ Session duration distribution histogram
- ✅ Videos per participant distribution
- ✅ Response count by video bar chart
- ✅ Response pattern pie charts for key questions

## Phase 3: Primary Analysis 🔄 PLANNED

### Video-Level Analysis 🔄 PLANNED
1. **ANOVA Models** 🔄 PLANNED
   - One-way ANOVA: Video category effects on each rating dimension
   - Two-way ANOVA: Video category × demographic interactions
   - Post-hoc comparisons with Bonferroni correction

2. **Video Ranking and Clustering** 🔄 PLANNED
   - Rank videos by mean ratings on each dimension
   - Hierarchical clustering of videos based on rating patterns
   - K-means clustering to identify video types

### Key Findings from Descriptive Analysis
- **Moderate Comprehension**: Participants found videos somewhat comprehensible (most common: "Somewhat agree")
- **Effective Tension Building**: Tension increased from beginning (31.5) to middle/end (~47)
- **Resolution Challenges**: 60% of videos lacked clear narrative resolution
- **Moderate Engagement**: Participants showed moderate interest in future engagement

### Individual Differences Analysis
1. **Demographic Effects**
   - T-tests for gender differences
   - ANOVA for age group differences
   - Correlation analysis for continuous demographics

2. **Person-Level Patterns**
   - Individual consistency in rating patterns
   - Identification of rating response styles
   - Factor analysis of individual differences

## Phase 4: Advanced Analysis

### Multilevel Modeling
- **Model Structure**: Ratings nested within participants and videos
- **Fixed Effects**: Video characteristics, participant demographics
- **Random Effects**: Participant and video random intercepts
- **Model Selection**: Information criteria for model comparison

### Principal Component Analysis (PCA)
- **Objective**: Reduce dimensionality of rating measures
- **Analysis**: Extract principal components of narrative perceptions
- **Interpretation**: Identify underlying narrative perception factors

### Machine Learning Approaches
1. **Prediction Models**
   - Random Forest to predict narrative perceptions
   - Feature importance analysis
   - Cross-validation for model performance

2. **Classification**
   - Video type classification based on perception patterns
   - Participant type classification based on rating patterns

## Phase 5: Exploratory Analysis

### Pattern Discovery
- Association rule mining for rating patterns
- Network analysis of video similarities
- Time series analysis (if applicable)

### Subgroup Analysis
- Analysis within demographic subgroups
- Video category-specific analyses
- Interaction effect exploration

## Statistical Software and Tools

### Primary Software
- **R**: Statistical analysis and visualization
- **Python**: Data processing and machine learning
- **Jupyter Notebooks**: Reproducible analysis workflow

### Key Packages
- **R**: lme4, ggplot2, dplyr, corrplot, cluster
- **Python**: pandas, numpy, scikit-learn, matplotlib, seaborn

## Effect Size and Power Analysis

### Effect Size Calculations
- Cohen's d for group differences
- Eta-squared for ANOVA effects
- R-squared for regression models

### Power Analysis (Post-hoc)
- Calculate achieved power for significant effects
- Document minimum detectable effect sizes
- Plan for future replication studies

## Assumptions and Limitations

### Statistical Assumptions
- Normality of residuals
- Homoscedasticity
- Independence of observations
- Linearity of relationships

### Study Limitations
- Sample size constraints
- Video selection bias
- Self-report measurement limitations
- Cross-sectional design

## Reporting Standards

### Transparency
- All analysis code will be publicly available
- Pre-registration of analysis plan
- Clear documentation of all decisions

### Reproducibility
- Version control for all analysis files
- Detailed documentation of data processing steps
- Sharing of analysis scripts and data (where appropriate)

## Timeline for Analysis

- **Week 1**: Data cleaning and quality assessment
- **Week 2**: Descriptive analysis and visualization
- **Week 3**: Primary inferential analysis
- **Week 4**: Advanced modeling and machine learning
- **Week 5**: Exploratory analysis and pattern discovery
- **Week 6**: Results synthesis and interpretation

## Deliverables

1. **Technical Report**: Detailed methodology and results
2. **Data Analysis Scripts**: Fully documented, reproducible code
3. **Visualizations**: Publication-ready figures and tables
4. **Data Documentation**: Codebook and analysis notes
5. **Presentation Materials**: Conference presentations and reports
