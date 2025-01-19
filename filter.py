import configparser
import json
from os import remove
from sys import meta_path

from class_predefine import *
from requirement import *

import pandas as pd
import geopandas as gpd
import unicodedata
import unicodedata
import re

# get into config.ini
config = configparser.ConfigParser()
config.read('config.ini')
metadata_path = config['Paths']['raw_metadata']

# Load JSON data into a Python variable
def load_metadata(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file_path)
    return data

def check_theme(metadata):
    """Check if the dataset's theme matches the required themes."""
    return metadata['theme']['themeCode'] in themeR

def check_spatial_scope(metadata):
    """Check if the dataset's spatial scope overlaps with the required scope."""
    dataset_scope = metadata['space_time']['space']['spatialScope']['spatialScope']
    return any(item in spatialScopeR for item in dataset_scope)

def check_temporal_scope(metadata):
    """Check if the dataset's temporal scope overlaps with the required years."""
    dataset_start_year = pd.to_datetime(metadata['space_time']['time']['temporalScope']['temporalScopeStart']).year
    dataset_end_year = pd.to_datetime(metadata['space_time']['time']['temporalScope']['temporalScopeEnd']).year
    return temporalScopeStratR <= dataset_end_year and temporalScopeEndR >= dataset_start_year


def check_granularity(metadata):

    dataset_spatial_granularity = metadata['space_time']['space']['spatialGranularity']['spatialGranularity']
    dataset_temporal_granularity = metadata['space_time']['time']['temporalGranularity']['temporalGranularity']

    spatial_finer = False
    temporal_finer = False

    for spatial_hierarchy_key, spatial_hierarchy in hS_F.items():
        for temporal_hierarchy_key, temporal_hierarchy in hT_F.items():
            spatial_finer = spatial_hierarchy.get(dataset_spatial_granularity, -1) >= spatial_hierarchy.get(
                spatialGranularityR, -1)
            temporal_finer = temporal_hierarchy.get(dataset_temporal_granularity, -1) >= temporal_hierarchy.get(
                temporalGranularityR, -1)
            break  # Stop checking other hierarchies once a match is found for this dataset
    return spatial_finer and temporal_finer

def filter_datasets(metadata_list):
    filtered_datasets = []
    for metadata in metadata_list:
        if (check_theme(metadata)
            and check_granularity(metadata)
            and check_spatial_scope(metadata)
            and check_temporal_scope(metadata)
        ):
            filtered_datasets.append(metadata)
    return filtered_datasets

# Apply the filter to the example metadata list
metadata_list = load_metadata(metadata_path)
filtered_datasets = filter_datasets(metadata_list)
print("Filtered Datasets:", filtered_datasets)