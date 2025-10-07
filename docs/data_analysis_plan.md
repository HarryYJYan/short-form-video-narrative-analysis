# Data Analysis Plan: Short Form Video Narrative Perceptions

## Analysis Overview

This document outlines the comprehensive data analysis plan for the short form video narrative perception experiment. The analysis will progress from descriptive statistics through inferential tests to advanced modeling techniques.

## Phase 1: Data Preparation and Quality Assessment

### Data Cleaning
1. **Missing Data Assessment**
   - Identify patterns of missing data
   - Document reasons for missingness
   - Implement appropriate handling strategies (listwise deletion, imputation)

2. **Outlier Detection**
   - Statistical outliers using IQR and Z-score methods
   - Response time analysis for potential inattentive responding
   - Visual inspection of rating distributions

3. **Data Validation**
   - Check for impossible or inconsistent responses
   - Verify random assignment was successful
   - Validate data entry accuracy

### Data Transformation
1. **Scale Reliability**
   - Calculate Cronbach's alpha for multi-item measures
   - Assess internal consistency of rating scales

2. **Variable Creation**
   - Composite scores for related measures
   - Categorical variables from continuous demographics
   - Video-level aggregate statistics

## Phase 2: Descriptive Analysis

### Participant Characteristics
- Demographic profile summary
- Distribution of video consumption habits
- Sample representativeness assessment

### Video Characteristics
- Descriptive statistics for each of the 40 videos
- Distribution of video categories and durations
- Summary of video-level rating patterns

### Rating Patterns
- Distribution of all narrative perception ratings
- Correlation matrix of rating dimensions
- Individual differences in rating patterns

### Visualizations
- Histograms and density plots for all continuous variables
- Box plots for rating distributions by video category
- Heatmaps for correlation matrices
- Scatter plots for key relationships

## Phase 3: Primary Analysis

### Video-Level Analysis
1. **ANOVA Models**
   - One-way ANOVA: Video category effects on each rating dimension
   - Two-way ANOVA: Video category × demographic interactions
   - Post-hoc comparisons with Bonferroni correction

2. **Video Ranking and Clustering**
   - Rank videos by mean ratings on each dimension
   - Hierarchical clustering of videos based on rating patterns
   - K-means clustering to identify video types

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
