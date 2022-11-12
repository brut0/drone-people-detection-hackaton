from os import walk
from PIL import Image
import pandas as pd

LABELS_PATH = 'yolov5/runs/detect/exp18/labels'
IMG_PATH = 'test'
SUBMIT_NUM = '21'


def main():
    solution = pd.read_csv('sample_solution.csv')

    images = solution.ID_img
    region_shapes_list = []
    for img in images:
        img_txt = img.split('.')[0] + '.txt'
        try:
            with open(f"{LABELS_PATH}/{img_txt}") as f:
                labels_list = []
                with Image.open(f"{IMG_PATH}/{img}") as im:
                    width, height = im.size
                dict_list = []
                for label in f.readlines():
                    d = {}
                    d['cx'] = int(float(label.split()[1]) * width)
                    d['cy'] = int(float(label.split()[2]) * height)
                    d['w'] = int(float(label.split()[3]) * width)
                    d['h'] = int(float(label.split()[4]) * height)
                    dict_list.append(d)
                dict_list = sorted(dict_list, key=lambda d: (d['cx'], d['cy']))
                labels_list = [f"{{\"cx\":{l['cx']},\"cy\":{l['cy']},\"r\":{max(l['w'], l['h'])}}}" for l in dict_list]
                region_shapes_list.append(labels_list)
        except:
            region_shapes_list.append(0)
            continue
    solution.region_shape = region_shapes_list

    solution.to_csv(f"submit_{SUBMIT_NUM}.csv", index=False)



if __name__ == "__main__":
    main()
    print("SUBMIT CREATED SUCCESSFULLY")
