"""
------------------------------------------------------------------------------------------
DESCRIPTION:
Partitions the dataset of images into training and testing sets in a specified ratio.
NOTE: All the images and their corresponding xml files should have similar names and they
must be in same folder.
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


def train_test_split(source, destination, ratio, copy_xml):

    images = [
        file.parts[-1]
        for file in Path.iterdir(source)
        if file.suffix in [".png", ".jpg", ".jpeg"]
    ]

    num_images = len(images)

    if num_images == 0:
        print("No valid images exist in the directory")
        return

    num_test_images = math.ceil(ratio * num_images)

    test_samples = random.sample(images, num_test_images)
    train_samples = [sample for sample in images if sample not in test_samples]

    train_dir = destination / "train"
    test_dir = destination / "test"

    if not Path.exists(train_dir):
        Path.mkdir(train_dir)
    if not Path.exists(test_dir):
        Path.mkdir(test_dir)

    def move_data(samples: list, directory: str):
        for image in tqdm(samples, ascii=True, desc="Moving"):
            copyfile(source / image, directory / image)
            if copy_xml:
                xml = image.split(".")[0] + ".xml"
                copyfile(source / xml, directory / xml)

    move_data(train_samples, train_dir)
    print(f">>> {len(train_samples)} samples were moved to train folder")
    move_data(test_samples, test_dir)
    print(f">>> {len(test_samples)} samples were moved to test folder")


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

    imageDir = Path(args.imageDir)
    outputDir = Path(args.outputDir)
    ratio = args.ratio
    copy_xml = args.xml

    assert imageDir.is_dir(), "Input directory doesn't exist"
    assert outputDir.is_dir(), "Output directory doesn't exist"

    train_test_split(imageDir, outputDir, ratio, copy_xml)


if __name__ == "__main__":
    main()
