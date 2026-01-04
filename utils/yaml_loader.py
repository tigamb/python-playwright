from pathlib import Path
import yaml


class TestDataLoader:
    _data = None

    @classmethod
    def load(cls):
        if cls._data is None:
            path = Path(__file__).parent.parent / "data" / "test_data.yaml"
            with open(path, encoding="utf-8") as f:
                cls._data = yaml.safe_load(f)
        return cls._data

    @classmethod
    def get(cls, section: str, case: str):
        return cls.load()[section][case]
