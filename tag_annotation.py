import linguistic_tokenizer as lt
import json

CAPTION = 'caption'
ANNOTATIONS = 'annotations'

def load_captions(json_path: str) -> dict:
    '''
    load captions from the json file
    :return:
    '''
    with open(json_path, "r") as f:
        annot_dict = json.load(f)
    return annot_dict

def add_tags_to_captions(captions: dict) -> None:
    """
    merge the linguistic tags into the captions
    :return:
    """
    for row in captions[ANNOTATIONS]:
        caption = row[CAPTION]
        for tag in lt.TAGS:
            if row[lt.TAGS[tag]]:
                caption = lt.create_tag(tag) + caption
        row[CAPTION] = caption


def remove_tags_keys(captions):
    for row in captions[ANNOTATIONS]:
        keys = list(row.keys())
        for key in keys:
            if key not in [CAPTION, 'image_id', 'id']:
                del row[key]


def cast_ids_to_string(captions):
    for row in captions[ANNOTATIONS]:
        row['image_id'] = str(row['image_id'])


def add_tags_to_annotations(path):
    captions_dict = load_captions(path)
    add_tags_to_captions(captions_dict)
    remove_tags_keys(captions_dict)
    cast_ids_to_string(captions_dict)
    with open('data/tagged_train_caption.json', 'w') as f:
        json.dump(captions_dict[ANNOTATIONS], f)
    print("done")


if __name__ == '__main__':
    path = 'data/captions_train2014.json'
    add_tags_to_annotations(path)
