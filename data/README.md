# Data Directory

This directory contains all data files for the Short Form Video Narrative Perception experiment.

## Data Structure

### Raw Data
- `raw/` - Contains original, unprocessed data files
  - `participant_responses.csv` - Raw participant survey responses
  - `video_metadata.csv` - Information about the 40 videos used in the experiment
  - `experiment_log.csv` - Log of which videos each participant watched

### Processed Data
- `processed/` - Contains cleaned and processed data files
  - `cleaned_data.csv` - Merged and cleaned dataset ready for analysis
  - `participant_demographics.csv` - Cleaned participant demographic information
  - `video_ratings.csv` - Cleaned narrative perception ratings

### Data Dictionary

#### Participant Data
- `participant_id` - Unique identifier for each participant
- `age` - Participant age
- `gender` - Participant gender
- `education` - Highest level of education
- `video_consumption_frequency` - How often participant watches short form videos

#### Video Data
- `video_id` - Unique identifier for each video (1-40)
- `video_title` - Title or description of the video
- `video_duration` - Length of video in seconds
- `video_category` - Category/genre of the video

#### Rating Data
- `narrative_clarity` - Rating of how clear the narrative was (1-7 scale)
- `emotional_impact` - Rating of emotional impact (1-7 scale)
- `story_coherence` - Rating of story coherence (1-7 scale)
- `engagement` - Rating of overall engagement (1-7 scale)
- `narrative_complexity` - Rating of narrative complexity (1-7 scale)

## Data Collection Protocol

1. Participants were randomly assigned 4 videos out of 40 available videos
2. After watching each video, participants rated various narrative perception dimensions
3. Demographic information was collected at the end of the session
4. All responses were recorded electronically

## Data Quality Notes

- [ ] Data cleaning procedures documented
- [ ] Missing data patterns identified
- [ ] Outlier detection performed
- [ ] Data validation checks completed

## Privacy and Ethics

- All participant data is anonymized
- Personal identifiers have been removed
- Data is stored securely and access is restricted
- Participants provided informed consent for data use
