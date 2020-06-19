import yaml

def get_config(configFileName="config.yaml"):
    with open("config.yaml", 'r') as f:
        _config = yaml.safe_load(f)
    return _config