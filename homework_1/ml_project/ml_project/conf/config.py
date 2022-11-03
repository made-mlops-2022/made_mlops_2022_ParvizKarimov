from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass
class SplitParams:
    shuffle: bool
    test_size: float
    random_state: int 

@dataclass
class Split:
    split_method: str
    params: SplitParams

@dataclass
class Dataset:
    features: Dict[str, List[str]]
    folder_path: str
    name: str

@dataclass
class TargetDataset(Dataset):
    target: str

@dataclass
class Preprocessor:
    scaler: Any


@dataclass
class TrainConfig:
    dataset: TargetDataset
    split: Split  # Unused if fit == "all"
    fit: str  # Either "all" or "split"
    model: Any
    model_path: str

@dataclass
class PredictConfig:
    dataset: Dataset
    model_path: str
    predict_path: str


@dataclass
class DatasetMaker:
    folder_path: str
    save_folder_path: str
    name: str
    preprocessing: Preprocessor
    features_to_process: Dict[str, Optional[List[str]]]


@dataclass
class FakeDataGeneratorCfg:
    original_folder: str
    name: str
    save_path: str