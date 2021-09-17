"""
------------------------------------------------------------------------------------------
DESCRIPTION:
This file takes in path to the default folder containing images and xml files and then 
splits them into train and test data with a specified ratio. The images and xml files are 
moved to folders named train and test respetively.
------------------------------------------------------------------------------------------
USAGE:
python train_test_split.py  -i [INPUT FOLDER] -o [OUTPUT FOLDER] -r [RATIO] -x [COPY XML]
------------------------------------------------------------------------------------------
"""


import math
import random
import argparse
from tqdm import tqdm
from pathlib import Path
from shutil import copyfile


def train_test_split(source, dest, ratio, copy_xml):
    source = Path(source)
    dest = Path(dest)
    train_dir = dest / "train"
    test_dir = dest / "test"

    if not Path.exists(train_dir):
        Path.mkdir(train_dir)
    if not Path.exists(test_dir):
        Path.mkdir(test_dir)

    images = [
        file.parts[-1]
        for file in Path.iterdir(source)
        if file.suffix in [".png", ".jpg", ".jpeg"]
    ]

    num_images = len(images)
    num_test_images = math.ceil(ratio * num_images)

    test_samples = random.sample(images, num_test_images)
    train_samples = [sample for sample in images if sample not in test_samples]

    def move_data(samples: list, directory: str):
        for image in tqdm(samples, ascii=True, desc="Moving"):
            copyfile(source / image, directory / image)
            if copy_xml:
                xml = image.split(".")[0] + ".xml"
                copyfile(source / xml, directory / xml)

    move_data(train_samples, train_dir)
    move_data(test_samples, test_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Partition dataset of images into training and testing sets",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--imageDir",
        help="Path to the folder where the image dataset is stored. If not specified, the CWD will be used.",
        type=str,
        default=Path.cwd(),
    )
    parser.add_argument(
        "-o",
        "--outputDir",
        help="Path to the output folder where the train and test dirs should be created. "
        "Defaults to the same directory as IMAGEDIR.",
        type=str,
        default=None,
    )
    parser.add_argument(
        "-r",
        "--ratio",
        help="The ratio of the number of test images over the total number of images. The default is 0.1.",
        default=0.1,
        type=float,
    )
    parser.add_argument(
        "-x",
        "--xml",
        help="Set this flag if you want the xml annotation files to be processed and copied over.",
        action="store_true",
    )
    args = parser.parse_args()

    if args.outputDir is None:
        args.outputDir = args.imageDir

    train_test_split(args.imageDir, args.outputDir, args.ratio, args.xml)


if __name__ == "__main__":
    main()
