#!/usr/bin/env python3
"""
Data Cleaning Script for Short Form Video Narrative Perception Study

This script processes raw Qualtrics survey data and transforms it from wide to long format
for analysis. It handles:
1. Removal of duplicate header rows
2. Filtering out preview/test responses
3. Wide-to-long transformation based on experimental design
4. Data quality checks and validation

Author: Generated for Short Form Video Narrative Analysis Project
Date: 2025
"""

import pandas as pd
import numpy as np
import re
import os
from pathlib import Path
import logging
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VideoNarrativeDataCleaner:
    """
    Main class for cleaning and transforming video narrative perception data
    """
    
    def __init__(self, data_path: str, output_dir: str = None):
        """
        Initialize the data cleaner
    
    Args:
            data_path: Path to the raw CSV file
            output_dir: Directory to save cleaned data (defaults to data directory)
        """
        self.data_path = Path(data_path)
        self.output_dir = Path(output_dir) if output_dir else self.data_path.parent
        self.raw_data = None
        self.cleaned_data = None
        self.long_data = None
        
        # Video IDs extracted from column names (these represent the 40 video clips)
        self.video_ids = self._extract_video_ids()
        
        # Question mappings for each video block
        self.question_mappings = self._create_question_mappings()
        
    def _extract_video_ids(self) -> List[str]:
        """
        Extract unique video IDs from the raw data column names
        Video IDs follow the pattern N_Reso_clip where N is the clip number
        """
        if not self.data_path.exists():
            logger.error(f"Data file not found: {self.data_path}")
            return []
            
        # Read just the header row to extract video IDs
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                header = f.readline().strip()
            
            # Find all clip patterns in the header
            clip_pattern = r'(\d+)_Reso_clip(?!_)'  # Match N_Reso_clip but not N_Reso_clip_end
            clip_matches = re.findall(clip_pattern, header)
            
            # Convert to video IDs
            video_ids = [f"clip_{match}" for match in clip_matches]
            
            # Remove duplicates and sort
            video_ids = sorted(list(set(video_ids)))
            
            logger.info(f"Found {len(video_ids)} unique video IDs")
            logger.info(f"Video IDs: {video_ids[:5]}...")  # Show first 5
            
            return video_ids
            
        except Exception as e:
            logger.error(f"Error extracting video IDs: {e}")
            return []
    
    def _create_question_mappings(self) -> Dict[str, str]:
        """
        Create mappings for standardized question names based on the actual column structure
        """
        return {
            # Timing variables
            'timing_first_click': 'Stim_timer_First Click',
            'timing_last_click': 'Stim_timer_Last Click', 
            'timing_page_submit': 'Stim_timer_Page Submit',
            'timing_click_count': 'Stim_timer_Click Count',
            
            # Stimulus familiarity
            'familiarity_seen': 'Stim_seen',
            'familiarity_plot': 'Stim_plot',
            'familiarity_characters': 'Stim_characters',
            
            # Comprehension questions
            'clear_starting_point': 'Cpl_start',
            'inferring_context': 'Cpl_context', 
            'built_interest_tension': 'Cpl_built',
            'clear_outcome': 'Cpl_outcome',
            'logical_flow': 'Cpl_flow',
            
            # Tension ratings
            'tension_beginning': 'Tns_level_1',
            'tension_middle': 'Tns_level_2',
            'tension_end': 'Tns_level_3',
            'introduced_tension': 'Tns_intro',
            'resolved_tension': 'Tns_reso',
            
            # Resolution questions
            'narrative_resolution': 'Reso_clip',
            'satisfactory_resolution': 'Reso_satis',
            'concluded_scene': 'Reso_clip_end',
            'episode_position': 'Reso_ep',
            'season_position': 'Reso_szn',
            
            # Future behavior
            'want_next_story': 'FutBhvr_next',
            'want_broader_context': 'FutBhvr_broad',
            'watch_full_episode': 'FutBhvr_fullep',
            'read_comments': 'FutBhvr_comment',
            'comments_purpose': 'FutBhvr_whycomment',
            'comments_purpose_text': 'FutBhvr_whycomment_7_TEXT'
        }
    
    def load_raw_data(self) -> pd.DataFrame:
        """
        Load and perform initial cleaning of raw data
        """
        logger.info(f"Loading data from {self.data_path}")
        
        try:
            # Read the CSV file, skipping the second row (descriptive headers)
            self.raw_data = pd.read_csv(self.data_path, skiprows=[1])
            
            logger.info(f"Loaded {len(self.raw_data)} rows and {len(self.raw_data.columns)} columns")
            
            # Remove rows that are completely empty or contain only NaN values
            initial_rows = len(self.raw_data)
            self.raw_data = self.raw_data.dropna(how='all')
            removed_empty = initial_rows - len(self.raw_data)
            
            if removed_empty > 0:
                logger.info(f"Removed {removed_empty} completely empty rows")
            
            return self.raw_data
            
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def filter_preview_responses(self) -> pd.DataFrame:
        """
        Filter out preview/test responses and incomplete responses
        """
        if self.raw_data is None:
            raise ValueError("Raw data not loaded. Call load_raw_data() first.")
        
        logger.info("Filtering preview and incomplete responses...")
        
        initial_rows = len(self.raw_data)
        
        # Create a copy for filtering
        self.cleaned_data = self.raw_data.copy()
        
        # Remove rows where ResponseId contains ImportId (these are metadata rows)
        if 'ResponseId' in self.cleaned_data.columns:
            import_id_mask = self.cleaned_data['ResponseId'].str.contains('ImportId', na=False)
            self.cleaned_data = self.cleaned_data[~import_id_mask]
            logger.info(f"Removed {import_id_mask.sum()} metadata rows (containing ImportId)")
        
        # Filter out preview responses (Status == 'Preview' or similar)
        if 'Status' in self.cleaned_data.columns:
            preview_mask = self.cleaned_data['Status'].str.contains('Preview', case=False, na=False)
            self.cleaned_data = self.cleaned_data[~preview_mask]
            logger.info(f"Removed {preview_mask.sum()} preview responses")
        
        # Filter out responses that are not finished (handle mixed data types)
        if 'Finished' in self.cleaned_data.columns:
            # Convert to string to handle mixed types, then filter
            finished_str = self.cleaned_data['Finished'].astype(str)
            finished_mask = finished_str == 'True'
            self.cleaned_data = self.cleaned_data[finished_mask]
            logger.info(f"Kept {finished_mask.sum()} finished responses")
        
        # Remove responses with very short duration (likely test responses)
        # First convert duration to numeric, handling non-numeric values
        if 'Duration (in seconds)' in self.cleaned_data.columns:
            # Convert to numeric, coercing errors to NaN
            self.cleaned_data['Duration (in seconds)'] = pd.to_numeric(
                self.cleaned_data['Duration (in seconds)'], errors='coerce'
            )
            
            duration_threshold = 60  # Minimum 1 minute
            duration_mask = self.cleaned_data['Duration (in seconds)'] >= duration_threshold
            self.cleaned_data = self.cleaned_data[duration_mask]
            logger.info(f"Removed {len(self.raw_data) - duration_mask.sum()} responses with duration < {duration_threshold} seconds")
        
        # Remove responses with missing or invalid ResponseId
        if 'ResponseId' in self.cleaned_data.columns:
            valid_id_mask = (self.cleaned_data['ResponseId'].notna() & 
                           ~self.cleaned_data['ResponseId'].str.contains('ImportId', na=False) &
                           (self.cleaned_data['ResponseId'] != ''))
            self.cleaned_data = self.cleaned_data[valid_id_mask]
            logger.info(f"Removed {len(self.raw_data) - valid_id_mask.sum()} responses with invalid ResponseId")
        
        final_rows = len(self.cleaned_data)
        removed_total = initial_rows - final_rows
        
        logger.info(f"Data filtering complete: {initial_rows} → {final_rows} rows ({removed_total} removed)")
        
        return self.cleaned_data
    
    def transform_to_long_format(self) -> pd.DataFrame:
        """
        Transform data from wide format (one row per participant) to long format (one row per participant-video combination)
        """
        if self.cleaned_data is None:
            raise ValueError("Cleaned data not available. Run filtering first.")
        
        logger.info("Transforming data to long format...")
        
        # Start with demographic and metadata columns that don't vary by video
        base_columns = [
            'StartDate', 'EndDate', 'IPAddress', 'Progress', 'Duration (in seconds)', 
            'Finished', 'RecordedDate', 'ResponseId', 'RecipientLastName', 'RecipientFirstName',
            'RecipientEmail', 'ExternalReference', 'LocationLatitude', 'LocationLongitude',
            'DistributionChannel', 'UserLanguage'
        ]
        
        # Add consent and demographic columns (these appear at the end)
        demo_columns = [
            'QID50', 'QID54', 'QID55', 'QID55_4_TEXT', 'QID56', 'QID56_6_TEXT', 
            'QID56_7_TEXT', 'QID56_8_TEXT', 'QID59_TEXT'
        ]
        
        # Keep only columns that actually exist in the data
        available_base_columns = [col for col in base_columns if col in self.cleaned_data.columns]
        available_demo_columns = [col for col in demo_columns if col in self.cleaned_data.columns]
        
        # Create list to store long format dataframes
        long_dataframes = []
        
        for video_id in self.video_ids:
            logger.info(f"Processing video: {video_id}")
            
            # Extract clip number from video_id (e.g., "clip_1" -> "1")
            clip_num = video_id.replace('clip_', '')
            
            # Find all columns related to this video (start with clip number + underscore)
            video_columns = [col for col in self.cleaned_data.columns if col.startswith(f"{clip_num}_")]
            
            if not video_columns:
                logger.warning(f"No columns found for video {video_id} (looking for {clip_num}_*)")
                continue
            
            # Create a subset dataframe for this video
            video_data = self.cleaned_data[available_base_columns + video_columns + available_demo_columns].copy()
            
            # Add video identifier
            video_data['video_id'] = video_id
            
            # Rename columns to standardized names
            video_data = self._standardize_video_columns(video_data, video_id)
            
            long_dataframes.append(video_data)
        
        # Combine all video dataframes
        if long_dataframes:
            self.long_data = pd.concat(long_dataframes, ignore_index=True, sort=False)
            logger.info(f"Long format transformation complete: {len(self.long_data)} rows")
        else:
            logger.error("No video data found for transformation")
            self.long_data = pd.DataFrame()
        
        return self.long_data
    
    def _standardize_video_columns(self, video_data: pd.DataFrame, video_id: str) -> pd.DataFrame:
        """
        Standardize column names for a specific video block
        """
        # Extract clip number from video_id (e.g., "clip_1" -> "1")
        clip_num = video_id.replace('clip_', '')
        
        # Create mapping from actual column names to standardized names
        column_mapping = {}
        
        for standardized_name, question_suffix in self.question_mappings.items():
            # Create the expected column name for this clip
            expected_col = f"{clip_num}_{question_suffix}"
            
            # Find matching column (case-insensitive)
            matching_cols = [col for col in video_data.columns if col == expected_col]
            
            if matching_cols:
                # Take the first matching column
                column_mapping[matching_cols[0]] = standardized_name
            else:
                logger.warning(f"No column found for: {expected_col} (standardized: {standardized_name})")
        
        # Apply the column mapping
        video_data = video_data.rename(columns=column_mapping)
        
        return video_data
    
    def validate_data_quality(self) -> Dict[str, any]:
        """
        Perform data quality checks and return validation results
        """
        if self.long_data is None:
            raise ValueError("Long format data not available. Run transformation first.")
        
        logger.info("Performing data quality validation...")
        
        validation_results = {
            'total_observations': len(self.long_data),
            'unique_participants': self.long_data['ResponseId'].nunique() if 'ResponseId' in self.long_data.columns else 0,
            'unique_videos': self.long_data['video_id'].nunique() if 'video_id' in self.long_data.columns else 0,
            'missing_data_summary': {},
            'response_distribution': {},
            'quality_issues': []
        }
        
        # Check for missing data in key columns
        key_columns = ['video_id', 'ResponseId']
        if 'ResponseId' in self.long_data.columns:
            for col in key_columns:
                if col in self.long_data.columns:
                    missing_count = self.long_data[col].isna().sum()
                    validation_results['missing_data_summary'][col] = {
                        'missing_count': int(missing_count),
                        'missing_percentage': float(missing_count / len(self.long_data) * 100)
                    }
        
        # Check response distributions for key questions
        response_questions = ['familiarity_plot', 'clear_starting_point', 'logical_flow']
        for question in response_questions:
            if question in self.long_data.columns:
                validation_results['response_distribution'][question] = self.long_data[question].value_counts().to_dict()
        
        # Identify potential quality issues
        if validation_results['unique_participants'] == 0:
            validation_results['quality_issues'].append("No valid participants found")
        
        if validation_results['unique_videos'] < 10:
            validation_results['quality_issues'].append(f"Very few videos found: {validation_results['unique_videos']}")
        
        # Check for duplicate participant-video combinations
        if 'ResponseId' in self.long_data.columns and 'video_id' in self.long_data.columns:
            duplicates = self.long_data.duplicated(subset=['ResponseId', 'video_id']).sum()
            if duplicates > 0:
                validation_results['quality_issues'].append(f"Found {duplicates} duplicate participant-video combinations")
        
        logger.info(f"Data quality validation complete. Found {len(validation_results['quality_issues'])} issues.")
        
        return validation_results
    
    def save_cleaned_data(self, filename_prefix: str = "cleaned_data") -> Dict[str, str]:
        """
        Save cleaned data in multiple formats
        """
        if self.long_data is None:
            raise ValueError("No cleaned data to save. Run cleaning pipeline first.")
        
        logger.info("Saving cleaned data...")
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        saved_files = {}
        
        # Save long format data (main output)
        long_file = self.output_dir / f"{filename_prefix}_long_format.csv"
        self.long_data.to_csv(long_file, index=False)
        saved_files['long_format'] = str(long_file)
        logger.info(f"Saved long format data: {long_file}")
        
        # Save cleaned wide format data
        if self.cleaned_data is not None:
            wide_file = self.output_dir / f"{filename_prefix}_wide_format.csv"
            self.cleaned_data.to_csv(wide_file, index=False)
            saved_files['wide_format'] = str(wide_file)
            logger.info(f"Saved wide format data: {wide_file}")
        
        # Save data quality report
        validation_results = self.validate_data_quality()
        report_file = self.output_dir / f"{filename_prefix}_quality_report.txt"
        with open(report_file, 'w') as f:
            f.write("DATA QUALITY REPORT\n")
            f.write("==================\n\n")
            f.write(f"Total observations: {validation_results['total_observations']}\n")
            f.write(f"Unique participants: {validation_results['unique_participants']}\n")
            f.write(f"Unique videos: {validation_results['unique_videos']}\n\n")
            
            f.write("Missing Data Summary:\n")
            for col, info in validation_results['missing_data_summary'].items():
                f.write(f"  {col}: {info['missing_count']} ({info['missing_percentage']:.1f}%)\n")
            
            f.write("\nQuality Issues:\n")
            for issue in validation_results['quality_issues']:
                f.write(f"  - {issue}\n")
        
        saved_files['quality_report'] = str(report_file)
        logger.info(f"Saved quality report: {report_file}")
        
        return saved_files
    
    def run_full_pipeline(self, filename_prefix: str = "cleaned_data") -> Dict[str, str]:
        """
        Run the complete data cleaning pipeline
        """
        logger.info("Starting full data cleaning pipeline...")
        
        try:
            # Step 1: Load raw data
            self.load_raw_data()
            
            # Step 2: Filter preview responses
            self.filter_preview_responses()
            
            # Step 3: Transform to long format
            self.transform_to_long_format()
            
            # Step 4: Save cleaned data
            saved_files = self.save_cleaned_data(filename_prefix)
            
            logger.info("Data cleaning pipeline completed successfully!")
            
            return saved_files
            
        except Exception as e:
            logger.error(f"Error in data cleaning pipeline: {e}")
            raise


def main():
    """
    Main function to run the data cleaning script
    """
    # Define paths
    data_path = "/Users/yaojunyan/Desktop/short-form-video-narrative-analysis/data/SML+Narrative+Resolution+-+REP_October+7,+2025_16.56.csv"
    output_dir = "/Users/yaojunyan/Desktop/short-form-video-narrative-analysis/data"
    
    # Initialize cleaner
    cleaner = VideoNarrativeDataCleaner(data_path, output_dir)
    
    # Run the full pipeline
    try:
        saved_files = cleaner.run_full_pipeline("video_narrative_cleaned")
        
        print("\n" + "="*50)
        print("DATA CLEANING COMPLETED SUCCESSFULLY")
        print("="*50)
        print(f"Files saved:")
        for file_type, file_path in saved_files.items():
            print(f"  {file_type}: {file_path}")
        print("\nNext steps:")
        print("1. Review the quality report for any issues")
        print("2. Examine the long format data structure")
        print("3. Proceed with exploratory data analysis")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())