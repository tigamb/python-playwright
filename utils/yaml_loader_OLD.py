import yaml
from pathlib import Path

class TestDataLoader:
    _cache = None

    @classmethod
    def load(cls):
        if cls._cache is None:
            project_root = Path(__file__).resolve().parents[1]
            data_file = project_root / "data" / "test_data.yaml"

            with open(data_file, encoding="utf-8") as f:
                cls._cache = yaml.safe_load(f)

        return cls._cache

    @classmethod
    def get(cls, *keys):
        data = cls.load()
        for key in keys:
            data = data[key]
        return data
