import yaml

def get_yaml(file_path):
    with open(file_path, mode="r", encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data

def write_yaml(file_path, data, mode="a"):
    with open(file_path, mode=mode, encoding='utf-8') as f:
        yaml.dump(data, f, encoding="utf-8", allow_unicode=True)


if __name__ == '__main__':
    print(get_yaml())
