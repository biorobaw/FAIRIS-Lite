import xml.etree.ElementTree as ET

import pandas as pd


def parse_goal(xml_goal):
    fid = int(xml_goal.get('id'))
    x = float(xml_goal.get('x'))
    y = float(xml_goal.get('y'))
    return pd.DataFrame(data=[[fid, x, y]], columns=['id', 'x', 'y'])

def parse_all_goals(root):
    return pd.concat([pd.DataFrame(columns=['id', 'x', 'y'])] + [parse_goal(xml_goal) for xml_goal in
                                                                 root.findall('goal')]).reset_index(drop=True)
def parse_all_goals(root):
    # Define the columns for the DataFrame
    columns = ['id', 'x', 'y']

    # Parse each goal and create a list of DataFrames
    data_frames = [parse_goal(xml_goal) for xml_goal in root.findall('goal')]

    # Check if there are any valid data frames to concatenate
    valid_data_frames = [df for df in data_frames if not df.empty and not df.isna().all().all()]
    if not valid_data_frames:
        return pd.DataFrame(columns=columns)

    # Concatenate the valid data frames
    return pd.concat(valid_data_frames, ignore_index=True)

def parse_wall(xml_wall):
    data = [[float(xml_wall.get(coord)) for coord in ['x1', 'y1', 'x2', 'y2']]]
    return pd.DataFrame(data=data, columns=['x1', 'y1', 'x2', 'y2'])

def parse_all_obsticles(xml_root):
    # Define the columns for the DataFrame
    columns = ['x1', 'y1', 'x2', 'y2']

    # Parse each wall and create a list of DataFrames
    data_frames = [parse_wall(xml_wall) for xml_wall in xml_root.findall('wall')]

    # Check if there are any valid data frames to concatenate
    valid_data_frames = [df for df in data_frames if not df.empty and not df.isna().all().all()]
    if not valid_data_frames:
        return pd.DataFrame(columns=columns)

    # Concatenate the valid data frames
    return pd.concat(valid_data_frames, ignore_index=True)

def parse_landmark(xml_landmark):
    data = [[float(xml_landmark.get(data)) for data in ['x', 'y', 'height', 'red', 'green', 'blue']]]
    return pd.DataFrame(data=data, columns=['x', 'y', 'height', 'red', 'green', 'blue'])

def parse_all_landmarks(xml_root):
    # Define the columns for the DataFrame
    columns = ['x', 'y', 'height', 'red', 'green', 'blue']

    # Parse each landmark and create a list of DataFrames
    data_frames = [parse_landmark(xml_landmark) for xml_landmark in xml_root.findall('landmark')]

    # Check if there are any valid data frames to concatenate
    valid_data_frames = [df for df in data_frames if not df.empty and not df.isna().all().all()]
    if not valid_data_frames:
        return pd.DataFrame(columns=columns)

    # Concatenate the valid data frames
    return pd.concat(valid_data_frames, ignore_index=True)

def parse_position(xml_position):
    return pd.DataFrame(data=[[float(xml_position.get(p)) for p in ['x', 'y', 'theta']]], columns=['x', 'y', 'theta'])
def parse_all_positions(xml_positions):
    # Define the columns for the DataFrame
    columns = ['x', 'y', 'theta']

    # Handle the case where xml_positions is None
    if xml_positions is None or not xml_positions.findall('pos'):
        return pd.DataFrame(columns=columns)

    # Parse each position and create a list of DataFrames
    data_frames = [parse_position(xml_pos) for xml_pos in xml_positions.findall('pos')]

    # Check if there are any valid data frames to concatenate
    valid_data_frames = [df for df in data_frames if not df.empty and not df.isna().all().all()]
    if not valid_data_frames:
        return pd.DataFrame(columns=columns)

    # Concatenate the valid data frames
    return pd.concat(valid_data_frames, ignore_index=True)


def parse_maze(file):
    root = ET.parse(file).getroot()
    start_positions = parse_all_positions(root.find('startPositions'))
    walls = parse_all_obsticles(root)
    goals = parse_all_goals(root)
    landmarks = parse_all_landmarks(root)

    return walls, goals, start_positions, landmarks
