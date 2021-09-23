"""
Author: Aman Roland
------------------------------------------------------------------------------------------
DESCRIPTION:
This file takes in .txt or .csv file and combines and then generates a .pbtxt file output.
------------------------------------------------------------------------------------------
USAGE:
python generate_pbtxt.py -t [csv or txt] -i [PATH_TO_INPUT_FILE] -o [PATH_TO_OUTPUT_FILE]
------------------------------------------------------------------------------------------
"""

import argparse
import pandas as pd
from pathlib import Path


def pbtxt_from_csv(csv_path, pbtxt_path):
    class_list = list(pd.read_csv(csv_path)["class"].unique())
    pbtxt_from_classlist(class_list, pbtxt_path)


# Python 3.9 and above can use this function
# def pbtxt_from_txt(txt_path, pbtxt_path):
#     data = list()
#     with open(txt_path, "r", encoding="UTF-8") as file:
#         while line := file.readline().strip():
#             data.append(line)
#     pbtxt_from_classlist(data, pbtxt_path)


def pbtxt_from_txt(txt_path, pbtxt_path):
    data = [l.strip() for l in open(txt_path, "r", encoding="utf-8-sig")]
    data = [l for l in data if len(l) > 0]
    pbtxt_from_classlist(data, pbtxt_path)


def pbtxt_from_classlist(class_list: list, pbtxt_path):
    pbtxt_text = ""

    for i, c in enumerate(class_list):
        pbtxt_text += (
            "item {\n    id: " + str(i + 1) + "\n    name: '" + str(c) + "'\n}\n\n"
        )

    with open(pbtxt_path, "w+") as pbtxt_file:
        pbtxt_file.write(pbtxt_text)


def main():
    parser = argparse.ArgumentParser(
        description="creates a .pbtxt file from a .csv or .txt input file"
    )
    parser.add_argument(
        "-t",
        "--input_type",
        choices=["csv", "txt"],
        required=True,
        help="type of input file (csv with at least one 'class' column or txt with one class name by line)",
    )
    parser.add_argument(
        "-i",
        "--input_file",
        metavar="",
        type=str,
        required=True,
        help="Path to the input txt or csv file (include name of file)",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        metavar="",
        type=str,
        required=True,
        help="Path where the .pbtxt output will be created (include name of the file)",
    )

    args = parser.parse_args()

    inputPath = Path(args.input_file)
    outputPath = Path(args.output_file)

    if args.input_type == "csv":
        pbtxt_from_csv(inputPath, outputPath)
    elif args.input_type == "txt":
        pbtxt_from_txt(inputPath, outputPath)

    print("Succesfully created .pbtxt file")
    print("Input file path:", inputPath)
    print("Output file path:", outputPath)


if __name__ == "__main__":
    main()
