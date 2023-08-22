import json
import os
def compare_jsons(path1, path2):
    name_1 = os.path.basename(path1)
    name_2 = os.path.basename(path2)
    mismatch = 0
    with open(path1, "r") as f:
        data1 = json.load(f)
    with open(path2, "r") as f:
        data2 = json.load(f)
    assert len(data1) == len(data2)
    for i in range(len(data1)):
        assert data1[i]["image_id"] == data2[i]["image_id"]
        if data1[i]["caption"] != data2[i]["caption"]:
            print(f"caption mismatch: {data1[i]['image_id']}")
            print(f'{name_1}: {data1[i]["caption"]}')
            print(f'{name_2}: {data2[i]["caption"]}')
            mismatch+=1
    print(f"mismatch: {mismatch} out of {len(data1)}")

if __name__ == '__main__':
    path1 = 'evaluate/results/results_check_test_eval_1.json'
    path2 = 'evaluate/results/results_test_eval_1.json'
    compare_jsons(path1,path2)