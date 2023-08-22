import json
import os


class DataFile:
    def __init__(self, _path, _data):
        self.dir = os.path.dirname(_path)
        self.name = os.path.basename(_path)
        self.data = _data

    @property
    def path(self): return os.path.join(self.dir, self.name)

    def add_suffix(self, suffix: str):
        name_parts = self.name.split(".")
        self.name = name_parts[0] + suffix + "." + name_parts[1]


def compare_jsons(path1, path2):
    with open(path1, "r") as f:
        data1 = json.load(f)
    with open(path2, "r") as f:
        data2 = json.load(f)
    print("done")


def load_json(_path) -> DataFile:
    with open(_path, "r") as f:
        data = json.load(f)
    return DataFile(_data=data, _path=_path)


# TODO: move this function to the linguistic tokenizer
def trim_special_tags(data: DataFile, inplace=False):
    for row in data.data:
        while row['caption'].lstrip().startswith('<#'):
            row['caption'] = row['caption'][8:].lstrip()
    if not inplace:
        data.add_suffix("_trim")

def save_data_list(data_list, path=None):
    if not path: path = data_list.path
    with open(path, 'w') as f:
        json.dump(data_list.data, f)

def trim_results(path, dont_save=False, inplace=False):
    data: DataFile = load_json(path)
    trim_special_tags(data, inplace)
    if not dont_save: save_data_list(data)


def trim_all(folder, dont_save=False, inplace=False):
    for file in os.listdir(folder):
        if file.endswith(".json") and not file.endswith("_trim.json"):
            if file.replace('.json', '_trim.json') in os.listdir(folder):
                continue
            trim_results(os.path.join(folder, file), dont_save, inplace)

if __name__ == '__main__':
    # path = "results_coco_prefix-009_1_trim.json"
    folder = 'results'
    # data : DataFile = load_json()
    # trim_results(path)
    # data = load_json(path)
    trim_all(folder, inplace=False)
    print("done")
