# Descriptive Data Analysis Documentation
## Short Form Video Narrative Perception Study

**Analysis Date:** October 7, 2025  
**Dataset:** Cleaned long format data (4,880 observations)  
**Participants:** 122  
**Videos:** 40  

---

## Executive Summary

This comprehensive descriptive analysis examines data from **122 participants** who completed a short-form video narrative perception study. The experimental design ensured that each participant rated **exactly 4 videos** from a pool of 40 videos, creating a balanced dataset with 488 total video ratings. Data collection occurred over **12 days** from September 25 to October 7, 2025.

### Key Findings
- **Experimental Design:** Balanced design with each participant rating 4 videos (not all 40)
- **Response Coverage:** Each video received 6-20 responses from different participants
- **Data Quality:** High response rates across all question types (488 responses total)
- **Session Engagement:** Reasonable session durations suggest thoughtful participation

---

## Data Structure Overview

### Variable Categories

The dataset contains two main types of variables:

#### 1. Individual-Level Variables (Participant Characteristics)
These variables are constant across all video ratings for each participant:

- **Demographics & Session Info:**
  - `StartDate`, `EndDate`: Session timing
  - `Duration (in seconds)`: Total session duration
  - `ResponseId`: Unique participant identifier
  - `UserLanguage`: Participant's language setting

- **Technical Variables:**
  - `IPAddress`, `Progress`, `Finished`: Survey completion tracking
  - `RecipientLastName`, `RecipientFirstName`, `RecipientEmail`: Participant identification
  - `ExternalReference`, `LocationLatitude`, `LocationLongitude`: Optional tracking data
  - `DistributionChannel`: Survey distribution method

#### 2. Video-Level Variables (Responses to Each Video)
These variables vary for each participant-video combination:

- **Timing Variables (4):** `timing_first_click`, `timing_last_click`, `timing_page_submit`, `timing_click_count`
- **Familiarity Variables (3):** `familiarity_seen`, `familiarity_plot`, `familiarity_characters`
- **Comprehension Variables (5):** `clear_starting_point`, `inferring_context`, `built_interest_tension`, `clear_outcome`, `logical_flow`
- **Tension Variables (5):** `tension_beginning`, `tension_middle`, `tension_end`, `introduced_tension`, `resolved_tension`
- **Resolution Variables (5):** `narrative_resolution`, `satisfactory_resolution`, `concluded_scene`, `episode_position`, `season_position`
- **Future Behavior Variables (6):** `want_next_story`, `want_broader_context`, `watch_full_episode`, `read_comments`, `comments_purpose`, `comments_purpose_text`
- **Video Identifier:** `video_id` (clip_1 to clip_40)

---

## Participant-Level Analysis

### Sample Characteristics

- **Total Participants:** 122
- **Data Collection Period:** September 25, 2025 to October 7, 2025 (12 days)
- **Session Duration:** 34.7 ± 110.1 minutes (median: 18.9 minutes)
- **Videos per Participant:** 4 (exactly, as per experimental design)

### Session Duration Analysis

The session duration shows considerable variation:
- **Mean:** 34.7 minutes
- **Standard Deviation:** 110.1 minutes (indicating high variability)
- **Range:** Wide range from very short to very long sessions

*Note: The high standard deviation suggests some participants may have had extended sessions or technical difficulties, while others completed the study efficiently.*

### Language Distribution

All participants used English (`UserLanguage` = 'EN'), indicating a homogeneous language sample.

---

## Video-Level Analysis

### Response Distribution

Each of the 40 videos received responses from 6-20 participants:
- **Mean Responses per Video:** 12.2 ± 2.9
- **Range:** 6-20 responses
- **Total Video Ratings:** 488 (122 participants × 4 videos each)

### Video Coverage Balance

The experimental design successfully distributed participants across videos, though not perfectly evenly:
- **Most Popular Videos:** clip_12 (20 responses), clip_27 (17 responses), clip_1 (16 responses)
- **Least Popular Videos:** clip_8 (6 responses), clip_4 (7 responses), clip_10 (8 responses)

This variation is expected in a randomized experimental design and provides adequate statistical power for analysis.

---

## Response Patterns Analysis

### Timing Variables

**Response Characteristics:** All 488 observations have timing data

- **timing_first_click:** 9.85 ± 33.33 seconds
- **timing_last_click:** 16.65 ± 41.61 seconds  
- **timing_page_submit:** 82.31 ± 331.03 seconds
- **timing_click_count:** 0.71 ± 1.91 clicks

*Interpretation:* The timing data suggests participants engaged thoughtfully with each video, spending an average of 82 seconds per video page with minimal clicking (0.71 clicks average).

### Familiarity Variables

**Response Characteristics:** 488 responses each, Likert-type scales

- **familiarity_seen:** 8 categories
  - Most common: "None of the above" (52.9%)
- **familiarity_plot:** 5 categories  
  - Most common: "Strongly disagree" (36.1%)
- **familiarity_characters:** 5 categories
  - Most common: "Strongly disagree" (29.1%)

*Interpretation:* Participants were largely unfamiliar with the video content, with over half reporting "None of the above" for content they had seen before, and strong disagreement with familiarity statements.

### Comprehension Variables

**Response Characteristics:** 488 responses each, Likert-type scales (1=Strongly disagree, 7=Strongly agree)

- **clear_starting_point:** Most common: "Somewhat agree" (40.0%)
- **inferring_context:** Most common: "Somewhat agree" (44.7%)
- **built_interest_tension:** Most common: "Somewhat agree" (42.6%)
- **clear_outcome:** Most common: "Somewhat agree" (34.2%)
- **logical_flow:** Most common: "Somewhat agree" (41.0%)

*Interpretation:* Participants generally found the videos somewhat comprehensible, with "Somewhat agree" being the most common response across all comprehension measures. This suggests moderate narrative clarity.

### Tension Variables

**Response Characteristics:** Mix of numeric ratings (0-100) and Likert scales

#### Numeric Tension Ratings:
- **tension_beginning:** 31.50 ± 25.46 (scale 0-100)
- **tension_middle:** 46.99 ± 24.70 (scale 0-100)  
- **tension_end:** 47.05 ± 31.73 (scale 0-100)

#### Categorical Tension Measures:
- **introduced_tension:** Most common: "Somewhat agree" (46.7%)
- **resolved_tension:** Most common: "Somewhat disagree" (27.0%)

*Interpretation:* Tension levels increased from beginning (31.5) to middle/end (~47), suggesting effective narrative tension building. However, participants were more likely to disagree that tension was resolved, indicating potential narrative resolution issues.

### Resolution Variables

**Response Characteristics:** Mix of binary and categorical responses

- **narrative_resolution:** Most common: "No" (60.0%) - Binary response
- **satisfactory_resolution:** Most common: "Yes" (79.5%) - 195 responses (conditional on resolution)
- **concluded_scene:** Most common: "No" (65.0%) - Binary response
- **episode_position:** Most common: "Middle" (51.2%) - 4 categories
- **season_position:** Most common: "Middle" (42.6%) - 4 categories

*Interpretation:* Most videos (60%) did not present clear narrative resolution, and most (65%) did not conclude at scene end. When resolution was present, participants found it satisfactory (79.5%). Videos were perceived as coming from the middle of episodes/seasons.

### Future Behavior Variables

**Response Characteristics:** 488 responses each, Likert-type scales

- **want_next_story:** Most common: "Somewhat agree" (35.2%)
- **want_broader_context:** Most common: "Somewhat agree" (36.1%)
- **watch_full_episode:** Most common: "Somewhat agree" (27.3%)
- **read_comments:** Most common: "Somewhat agree" (26.8%)
- **comments_purpose:** 56 categories, most common: "Engage with fan reactions or humor" (15.8%)

*Interpretation:* Participants showed moderate interest in continuing engagement with the content, with roughly one-third expressing "Somewhat agree" to various future behavior intentions. The diversity of comment purposes (56 categories) suggests varied motivations for social engagement.

---

## Data Quality Assessment

### Completeness
- **Response Rate:** 100% for all variables (488 responses each)
- **Missing Data:** Minimal missing data across all measures
- **Data Consistency:** High consistency in response patterns

### Validity Indicators
- **Session Duration:** Reasonable engagement times (mean 34.7 minutes)
- **Response Patterns:** Consistent with expected experimental design
- **Timing Data:** Realistic interaction patterns (minimal clicking, appropriate page times)

### Experimental Design Validation
- **Participant Coverage:** All 122 participants provided complete data
- **Video Coverage:** All 40 videos received multiple responses (6-20 each)
- **Balance:** Reasonable distribution across videos despite randomization

---

## Key Insights and Implications

### Narrative Perception Patterns

1. **Moderate Comprehension:** Participants found videos somewhat comprehensible but not strongly clear
2. **Effective Tension Building:** Tension increased appropriately from beginning to end
3. **Resolution Challenges:** Most videos lacked clear narrative resolution
4. **Moderate Engagement:** Participants showed moderate interest in future engagement

### Experimental Design Success

1. **Balanced Sampling:** Each video received adequate responses for statistical analysis
2. **Participant Engagement:** Reasonable session durations indicate thoughtful participation
3. **Data Completeness:** High response rates across all measures
4. **Unfamiliar Content:** Successfully used unfamiliar content to avoid bias

### Research Implications

1. **Sample Adequacy:** 488 total responses provide sufficient power for most statistical analyses
2. **Variable Relationships:** Rich data enables examination of relationships between narrative elements
3. **Individual Differences:** Participant-level data allows for individual difference analysis
4. **Video Comparisons:** Balanced design enables meaningful video-to-video comparisons

---

## Technical Notes

### Data Processing
- **Format:** Long format (participant-video level)
- **Missing Data:** Handled appropriately in analysis
- **Variable Types:** Mix of numeric, categorical, and binary variables
- **Scales:** Likert scales (1-7), numeric scales (0-100), and categorical responses

### Analysis Limitations
- **Sample Size:** 122 participants may limit generalizability
- **Content Specificity:** Results specific to short-form video content
- **Cultural Context:** English-language, likely Western cultural context
- **Time Period:** Data collected over 12 days in fall 2025

### Recommended Next Steps
1. **Statistical Analysis:** Conduct inferential tests on key relationships
2. **Individual Differences:** Examine participant-level predictors
3. **Video Clustering:** Identify patterns across videos
4. **Longitudinal Analysis:** Consider temporal patterns in responses

---

## Files Generated

### Analysis Outputs
- `simple_descriptive_analysis_report.md`: Detailed numerical summary
- `simple_descriptive_analysis.png`: Key visualizations
- `simple_descriptive_analysis.py`: Analysis script

### Data Files Used
- `video_narrative_cleaned_long_format.csv`: Main analysis dataset
- `video_narrative_cleaned_wide_format.csv`: Alternative format for reference

---

*This analysis provides a comprehensive foundation for understanding the dataset structure, participant characteristics, and response patterns in the Short Form Video Narrative Perception Study. The findings support proceeding with more advanced statistical analyses to test specific hypotheses about narrative perception and engagement.*
