# Data Directory

This directory contains all data files for the Short Form Video Narrative Perception experiment.

## Data Structure (Sample Data)

### Raw Data
- `SML+Narrative+Resolution+-+REP_October+7,+2025_16.56.csv` - Original Qualtrics export with raw participant responses
  - **Size**: 132 rows × 1,156 columns
  - **Format**: Wide format with duplicate headers (first 2 rows removed during cleaning)
  - **Content**: All participant responses and survey metadata

### Processed Data
- `video_narrative_cleaned_wide_format.csv` - Cleaned data in wide format (one row per participant)
  - **Size**: 122 rows × 1,157 columns
  - **Format**: Wide format with standardized column names
  - **Content**: Participant demographics and all video responses
  
- `video_narrative_cleaned_long_format.csv` - Cleaned data in long format (one row per participant-video combination)
  - **Size**: 4,880 rows × 45 columns (488 actual responses + 4,392 missing)
  - **Format**: Long format for analysis
  - **Content**: Participant-video level responses with standardized variables

- `video_narrative_cleaned_quality_report.txt` - Data quality validation report
  - **Content**: Summary of data cleaning procedures and quality metrics

### Data Dictionary (Sample Data Variables)

#### Participant-Level Variables (Individual Characteristics)
- `ResponseId` - Unique identifier for each participant
- `StartDate`, `EndDate` - Session timing
- `Duration (in seconds)` - Total session duration
- `UserLanguage` - Participant's language setting (EN)
- `IPAddress`, `Progress`, `Finished` - Survey completion tracking
- `RecipientLastName`, `RecipientFirstName`, `RecipientEmail` - Participant identification
- `ExternalReference`, `LocationLatitude`, `LocationLongitude` - Optional tracking data
- `DistributionChannel` - Survey distribution method

#### Video-Level Variables (Responses to Each Video)
- `video_id` - Video identifier (clip_1 to clip_40)

**Timing Variables:**
- `timing_first_click` - Time to first click (seconds)
- `timing_last_click` - Time to last click (seconds)
- `timing_page_submit` - Time to page submission (seconds)
- `timing_click_count` - Number of clicks on page

**Familiarity Variables:**
- `familiarity_seen` - Prior exposure to content (categorical)
- `familiarity_plot` - Familiarity with plot (1-7 Likert scale)
- `familiarity_characters` - Familiarity with characters (1-7 Likert scale)

**Comprehension Variables:**
- `clear_starting_point` - Narrative starting point clarity (1-7 Likert scale)
- `inferring_context` - Context inference ability (1-7 Likert scale)
- `built_interest_tension` - Interest and tension building (1-7 Likert scale)
- `clear_outcome` - Narrative outcome clarity (1-7 Likert scale)
- `logical_flow` - Logical narrative flow (1-7 Likert scale)

**Tension Variables:**
- `tension_beginning` - Tension level at beginning (0-100 scale)
- `tension_middle` - Tension level in middle (0-100 scale)
- `tension_end` - Tension level at end (0-100 scale)
- `introduced_tension` - Tension introduction effectiveness (1-7 Likert scale)
- `resolved_tension` - Tension resolution effectiveness (1-7 Likert scale)

**Resolution Variables:**
- `narrative_resolution` - Presence of narrative resolution (Yes/No)
- `satisfactory_resolution` - Satisfaction with resolution (Yes/No)
- `concluded_scene` - Scene conclusion (Yes/No)
- `episode_position` - Perceived episode position (Beginning/Middle/End/Unknown)
- `season_position` - Perceived season position (Beginning/Middle/End/Unknown)

**Future Behavior Variables:**
- `want_next_story` - Desire for next story (1-7 Likert scale)
- `want_broader_context` - Desire for broader context (1-7 Likert scale)
- `watch_full_episode` - Interest in full episode (1-7 Likert scale)
- `read_comments` - Interest in reading comments (1-7 Likert scale)
- `comments_purpose` - Purpose for reading comments (categorical)
- `comments_purpose_text` - Open-ended comment purpose (text)

## Data Collection Protocol (Sample Data)

1. **Participants**: 122 participants recruited over 12 days (Sept 25 - Oct 7, 2025)
2. **Video Assignment**: Each participant was randomly assigned 4 videos out of 40 available videos
3. **Response Collection**: After watching each video, participants provided ratings on 28 different measures
4. **Session Duration**: Mean 34.7 minutes (range: varied significantly)
5. **Data Format**: Collected via Qualtrics survey platform

## Data Quality Assessment (Completed)

- ✅ **Data cleaning procedures documented** - See `docs/data_cleaning_documentation.md`
- ✅ **Missing data patterns identified** - 90% missing data expected (participants only rated 4/40 videos)
- ✅ **Outlier detection performed** - Session duration outliers identified and documented
- ✅ **Data validation checks completed** - All 488 actual responses validated
- ✅ **Experimental design validation** - Confirmed each participant rated exactly 4 videos
- ✅ **Response completeness** - 100% response rates for all measures in actual responses

## Privacy and Ethics

- All participant data is anonymized
- Personal identifiers have been removed
- Data is stored securely and access is restricted
- Participants provided informed consent for data use
