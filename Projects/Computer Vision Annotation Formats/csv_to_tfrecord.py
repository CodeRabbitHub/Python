import os
import io
import pandas as pd
import tensorflow as tf
from PIL import Image

from object_detection.utils import dataset_util
from object_detection.utils import label_map_util
from collections import namedtuple
import argparse
from tqdm import tqdm


def split(df, group):
    data = namedtuple("data", ["filename", "object"])
    gb = df.groupby(group)
    return [
        data(filename, gb.get_group(x))
        for filename, x in zip(gb.groups.keys(), gb.groups)
    ]


def category_idx(row_label):
    return label_map_dict[row_label]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, "{}".format(group.filename)), "rb") as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode("utf8")
    image_format = b"jpg"
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row["xmin"] / width)
        xmaxs.append(row["xmax"] / width)
        ymins.append(row["ymin"] / height)
        ymaxs.append(row["ymax"] / height)
        classes_text.append(row["class"].encode("utf8"))
        classes.append(category_idx(row["class"]))

    tf_example = tf.train.Example(
        features=tf.train.Features(
            feature={
                "image/height": dataset_util.int64_feature(height),
                "image/width": dataset_util.int64_feature(width),
                "image/filename": dataset_util.bytes_feature(filename),
                "image/source_id": dataset_util.bytes_feature(filename),
                "image/encoded": dataset_util.bytes_feature(encoded_jpg),
                "image/format": dataset_util.bytes_feature(image_format),
                "image/object/bbox/xmin": dataset_util.float_list_feature(xmins),
                "image/object/bbox/xmax": dataset_util.float_list_feature(xmaxs),
                "image/object/bbox/ymin": dataset_util.float_list_feature(ymins),
                "image/object/bbox/ymax": dataset_util.float_list_feature(ymaxs),
                "image/object/class/text": dataset_util.bytes_list_feature(
                    classes_text
                ),
                "image/object/class/label": dataset_util.int64_list_feature(classes),
            }
        )
    )
    return tf_example


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generating TFRecords (.record) from Images and CSV file"
    )
    parser.add_argument(
        "--path_to_images",
        type=str,
        help="folder containing images",
        metavar="PATH/IMAGE_DIR",
    )
    parser.add_argument(
        "--path_to_csv",
        type=str,
        help="full path to annotations csv file",
        metavar="PATH/FILENAME.csv",
    )
    parser.add_argument(
        "--path_to_label_map",
        type=str,
        help="full path to label_map file",
        metavar="PATH/label_map.pbtxt",
    )
    parser.add_argument(
        "--path_to_save_tfrecords",
        type=str,
        help="full path to generated tfrecords",
        metavar="PATH/FILENAME.record",
    )

    args = parser.parse_args()
    csv_path = args.path_to_csv
    images_path = args.path_to_images
    label_map_path = args.path_to_label_map
    tfrecords_path = args.path_to_save_tfrecords

    print("Images path : ", images_path)
    print("CSV file path : ", csv_path)
    print("Output TFRecords path : ", tfrecords_path)

    label_map = label_map_util.load_labelmap(label_map_path)
    label_map_dict = label_map_util.get_label_map_dict(label_map)

    writer = tf.io.TFRecordWriter(tfrecords_path)
    examples = pd.read_csv(csv_path)
    print("Generating tfrecord .... ")

    grouped = split(examples, "filename")

    for group in tqdm(grouped, desc="groups"):
        tf_example = create_tf_example(group, images_path)
        writer.write(tf_example.SerializeToString())
    writer.close()

    print("Successfully created the TFRecord file: {}".format(tfrecords_path))
