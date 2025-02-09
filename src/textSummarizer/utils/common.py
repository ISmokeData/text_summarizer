import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and features

    Args:
    path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is not found

    Returns:
        ConfigBox: configbox types
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError(f"yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_direactories:list, verbose=True):
    """Create list of directories
    Args:
        path_to_direactories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for path in path_to_direactories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created Directory at {path}")