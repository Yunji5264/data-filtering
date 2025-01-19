# Folder structure that has already been created
theme_folder_structure = {
    "Income and Wealth": {
        "Current and future consumption possibilities": {},
        "Realised material well-being": {},
        "Satisfaction with material conditions": {}
    },
    "Jobs and Earnings": {
        "Quantity of jobs": {},
        "Quality of jobs": {}
    },
    "Housing conditions": {
        "Length of life": {},
        "Morbidity in its  different dimensions": {}
    },
    "Work-life balance": {
        "Work-life time balance": {},
        "Satisfacton with work-life time balance": {},
        "Ability to reconcile family and work": {}
    },
    "Education and skills": {
        "Quantity of education": {},
        "Quality of education": {}
    },
    "Social connections": {
        "Personal relationships": {},
        "Community relationships": {},
        "Norms and values": {}
    },
    "Civic engagement and governance": {
        "Civic engagement": {},
        "Quality of governance": {},
        "People's confidence in their public institutions": {}
    },
    "Environmental quality": {
        "Quality of environment": {},
        "Impact of environmental hazards on human health": {},
        "Subjective perceptions of environment": {}
    },
    "Personal security": {
        "Opportunities to live in a safe environment": {},
        "Fear of crime": {}
    },
    "Subjective Well-Being": {
        "Evaluation of life": {},
        "Positive and negative feelings": {}
    }
}


# Define hierarchies
hS_F = {
    'hS_F0': {'COUNTRY': 0, 'REGION': 1, 'DEPARTEMENT': 2, 'ARRONDISSEMENT': 3, 'CANTON': 4, 'COMMUNE': 5, 'IRIS': 6, 'GEOPOINT': 7},
    'hS_F1': {'COUNTRY': 0, 'EPCI': 1, 'COMMUNE': 5, 'IRIS': 6, 'GEOPOINT': 7}
}

hT_F = {
    'hT_F0': {'YEAR': 0, 'QUARTER': 1, 'MONTH': 2, 'DATE': 3},
    'hT_F1': {'YEAR': 0, 'WEEK': 1, 'DATE': 3}
}

spatial_granularity_mapping = {}
for hierarchy in hS_F:
    spatial_granularity_mapping.update({level: value for value, level in hierarchy})

temporal_granularity_mapping = {}
for hierarchy in hT_F:
    temporal_granularity_mapping.update({level: value for value, level in hierarchy})