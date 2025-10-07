# Data Cleaning Documentation: Short Form Video Narrative Perception Study

## Overview

This document provides a comprehensive overview of the data cleaning process for the Short Form Video Narrative Perception study. The cleaning process transforms raw Qualtrics survey data from wide format (one row per participant) to long format (one row per participant-video combination) for analysis.

## Data Source

- **File**: `SML+Narrative+Resolution+-+REP_October+7,+2025_16.56.csv`
- **Source**: Qualtrics survey export
- **Original Format**: Wide format with 1,156 columns
- **Total Participants**: 132 (raw), 122 (after cleaning)
- **Videos**: 40 short-form video clips

## Data Cleaning Pipeline

### 1. Initial Data Loading

**Process**: 
- Load CSV file with `skiprows=[1]` to remove the descriptive header row
- Qualtrics exports typically have two header rows: actual column names and descriptive labels

**Results**:
- Loaded 132 rows and 1,156 columns
- Removed 1 metadata row containing ImportId values

### 2. Data Filtering and Exclusions

#### 2.1 Metadata Row Removal
- **Excluded**: 1 row where `ResponseId` contained "ImportId"
- **Rationale**: These are system metadata rows, not actual participant responses

#### 2.2 Preview Response Filtering
- **Excluded**: 0 preview responses
- **Method**: Filtered out rows where `Status` contained "Preview"
- **Rationale**: Preview responses are test responses by researchers, not valid participant data

#### 2.3 Incomplete Response Filtering
- **Excluded**: 9 responses where `Finished != True`
- **Method**: Kept only responses where `Finished` column was `True`
- **Rationale**: Incomplete responses may not provide valid data for analysis

#### 2.4 Duration-Based Filtering
- **Excluded**: 10 responses with duration < 60 seconds
- **Method**: Converted `Duration (in seconds)` to numeric and filtered
- **Rationale**: Very short durations likely indicate test responses or technical issues

#### 2.5 Response ID Validation
- **Excluded**: 10 responses with missing or invalid `ResponseId`
- **Method**: Removed rows where `ResponseId` was null, empty, or contained "ImportId"
- **Rationale**: Valid ResponseId is essential for tracking participants

### 3. Wide-to-Long Transformation

#### 3.1 Video Structure Identification
- **Videos**: 40 clips numbered 1-40
- **Pattern**: Each video has columns following `{clip_number}_{question_type}` format
- **Example**: `1_Stim_plot`, `1_Cpl_start`, `1_Tns_level_1`, etc.

#### 3.2 Question Mapping
Each video contains 28 standardized question types:

**Timing Variables**:
- `timing_first_click`: First click timing
- `timing_last_click`: Last click timing  
- `timing_page_submit`: Page submit timing
- `timing_click_count`: Click count

**Stimulus Familiarity**:
- `familiarity_seen`: Whether participant had seen the content before
- `familiarity_plot`: Familiarity with plot
- `familiarity_characters`: Familiarity with characters

**Comprehension Questions**:
- `clear_starting_point`: Clear starting point established
- `inferring_context`: Inferring context during viewing
- `built_interest_tension`: Built interest or tension
- `clear_outcome`: Clear and understandable outcome
- `logical_flow`: Clear and logical story flow

**Tension Ratings**:
- `tension_beginning`: Tension level at beginning
- `tension_middle`: Tension level at middle
- `tension_end`: Tension level at end
- `introduced_tension`: Whether tension was introduced
- `resolved_tension`: Whether tension was resolved

**Resolution Questions**:
- `narrative_resolution`: Whether clip presented narrative resolution
- `satisfactory_resolution`: Whether resolution was satisfactory
- `concluded_scene`: Whether clip concluded at scene end
- `episode_position`: Position within episode (beginning/middle/end)
- `season_position`: Position within season (beginning/middle/end)

**Future Behavior**:
- `want_next_story`: Want to see what happens next
- `want_broader_context`: Want broader storyline context
- `watch_full_episode`: Would consider watching full episode
- `read_comments`: Likely to read comments
- `comments_purpose`: Purpose for reading comments
- `comments_purpose_text`: Open-text response for comment purpose

### 4. Final Data Structure

#### 4.1 Long Format Output
- **Rows**: 4,880 (122 participants × 40 videos)
- **Columns**: 45 (demographics + standardized questions + video identifier)
- **Structure**: One row per participant-video combination

#### 4.2 Key Variables
- `ResponseId`: Unique participant identifier
- `video_id`: Video identifier (clip_1 to clip_40)
- Standardized question responses
- Demographic information
- Timing data

## Data Quality Assessment

### Quality Metrics
- **Total Observations**: 4,880
- **Unique Participants**: 122
- **Unique Videos**: 40
- **Missing Data**: 0% for key identifiers

### Quality Issues
- **None identified**: All data quality checks passed
- **No duplicate participant-video combinations**
- **Complete participant and video coverage**

## Exclusions Summary

| Exclusion Type | Count | Percentage | Rationale |
|----------------|-------|------------|-----------|
| Metadata rows | 1 | 0.8% | System metadata, not participant data |
| Preview responses | 0 | 0% | No preview responses found |
| Incomplete responses | 9 | 6.8% | Incomplete survey responses |
| Short duration | 10 | 7.6% | Likely test responses |
| Invalid ResponseId | 10 | 7.6% | Missing or invalid identifiers |
| **Total Excluded** | **10** | **7.6%** | **Final sample: 122 participants** |

## Data Files Generated

### 1. `video_narrative_cleaned_long_format.csv`
- **Purpose**: Main analysis dataset
- **Format**: Long format (participant-video level)
- **Use**: Primary dataset for statistical analysis

### 2. `video_narrative_cleaned_wide_format.csv`
- **Purpose**: Reference dataset
- **Format**: Wide format (participant level)
- **Use**: Participant-level analysis and reference

### 3. `video_narrative_cleaned_quality_report.txt`
- **Purpose**: Data quality documentation
- **Content**: Quality metrics and validation results
- **Use**: Documentation and validation

## Usage Instructions

### Running the Cleaning Script
```bash
# Activate conda environment
conda activate tf

# Run the cleaning script
python code/data_cleaning.py
```

### Script Features
- **Automated Pipeline**: Complete cleaning process in one command
- **Logging**: Detailed logging of all cleaning steps
- **Validation**: Automatic data quality checks
- **Error Handling**: Robust error handling and reporting

## Data Analysis Considerations

### Missing Data
- Some questions may have missing responses (participant choice)
- Missing data should be handled appropriately in analysis
- Consider missing data patterns for validity assessment

### Response Scales
- Most questions use Likert-type scales
- Some questions use categorical responses
- Timing variables are continuous (seconds)

### Participant Characteristics
- 122 valid participants
- Each participant rated 40 videos
- Balanced design across videos (122 responses per video)

## Technical Notes

### Column Naming Convention
- Original: `{clip_number}_{question_type}` (e.g., `1_Stim_plot`)
- Standardized: `{standardized_name}` (e.g., `familiarity_plot`)
- Mapping maintained in `_create_question_mappings()` method

### Video Identification
- Videos numbered 1-40 in original data
- Standardized to `clip_1` to `clip_40` format
- Maintains original ordering for analysis

### Data Types
- String responses: Likert scales, categorical choices
- Numeric responses: Timing data, some ratings
- Mixed types handled appropriately in cleaning

## Validation and Reproducibility

### Validation Steps
1. **Row Count Validation**: Expected 122 × 40 = 4,880 rows
2. **Column Validation**: All expected columns present
3. **ID Validation**: No missing ResponseId or video_id
4. **Duplicate Check**: No duplicate participant-video combinations

### Reproducibility
- **Script**: Fully documented and reproducible
- **Parameters**: All filtering criteria documented
- **Logging**: Complete audit trail of cleaning decisions
- **Version Control**: Script versioned for reproducibility

## Future Considerations

### Scalability
- Script designed to handle larger datasets
- Pattern-based column identification
- Configurable filtering parameters

### Extensions
- Additional quality checks can be added
- Custom filtering criteria can be implemented
- Output formats can be customized

## Contact and Support

For questions about the data cleaning process or to request modifications:
- Review the cleaning script: `code/data_cleaning.py`
- Check quality reports: `data/video_narrative_cleaned_quality_report.txt`
- Examine sample outputs: `data/video_narrative_cleaned_long_format.csv`

---

*Documentation generated: October 7, 2025*
*Data cleaning completed: October 7, 2025*
*Script version: 1.0*
