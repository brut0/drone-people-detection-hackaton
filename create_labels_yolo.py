from PIL import Image
import pandas as pd
import ast

TRAIN_DATA = "train.csv"
TRAIN_IMG = 'train/'  # paste path to train images
LABELS_PATH = 'labels/'


def main(data_path=TRAIN_DATA, images_path=TRAIN_IMG):
    df = pd.read_csv(data_path)

    for _, row in df.iterrows():
        if row.region_shape == '0.0':
            with open(f"{LABELS_PATH}{row.ID_img.split('.')[0]}.txt", 'w') as file:
                file.write('')
        else:
            with open(f"{LABELS_PATH}{row.ID_img.split('.')[0]}.txt", 'w') as file:
                with Image.open(f"{images_path}{row.ID_img}") as img:
                    x, y = img.size
                for d in ast.literal_eval(row.region_shape):
                    d = ast.literal_eval(d)
                    bbox = []
                    bbox.append(0)
                    bbox.append(round(float(d['cx']) / x, 6))
                    bbox.append(round(float(d['cy']) / y, 6))
                    bbox.append(round(float(d['r']) / x, 6))
                    bbox.append(round(float(d['r']) / y, 6))
                    file.write(' '.join(map(str, bbox)) + '\n')



if __name__ == "__main__":
    main()
    print("LABELS CREATED SUCCESSFULLY")
