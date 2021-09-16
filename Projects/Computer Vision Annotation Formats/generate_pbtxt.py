"""
------------------------------------------------------------------------------------------
DESCRIPTION:
This file takes in .txt or .csv file and combines and then generates a .pbtxt file output.
------------------------------------------------------------------------------------------
USAGE:
python generate_pbtxt.py input [PATH_TO_CSV_OR_TXT_FILE] output [PATH_TO_OUTPUT_PBXT_FILE]
------------------------------------------------------------------------------------------
"""

import argparse
import pandas as pd


def pbtxt_from_classlist(class_list: list, pbtxt_path: str):
    pbtxt_text = ""

    for i, c in enumerate(class_list):
        pbtxt_text += (
            "item {\n    id: "
            + str(i + 1)
            + '\n    display_name: "'
            + str(c)
            + '"\n}\n\n'
        )

    with open(pbtxt_path, "w+") as pbtxt_file:
        pbtxt_file.write(pbtxt_text)


def pbtxt_from_csv(csv_path: str, pbtxt_path: str):
    class_list = list(pd.read_csv(csv_path)["class"].unique())
    pbtxt_from_classlist(class_list, pbtxt_path)


def pbtxt_from_txt(txt_path: str, pbtxt_path: str):
    data = list()
    with open(txt_path, "r", encoding="UTF-8") as file:
        while line := file.readline().strip():
            data.append(line)
    pbtxt_from_classlist(data, pbtxt_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="creates a .pbtxt file from a .csv ot .txt input file"
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
        help="Path to the input txt or csv file (including  complete name of file)",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        metavar="",
        type=str,
        required=True,
        help="Path where the .pbtxt output will be created (including complete name of the file)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    parser.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    args = parser.parse_args()

    if args.input_type == "csv":
        pbtxt_from_csv(args.input_file, args.output_file)
    elif args.input_type == "txt":
        pbtxt_from_txt(args.input_file, args.output_file)

    if args.verbose:
        print("Succesfully created .pbtxt file")
        print("Input file path:", args.input_file)
        print("Output file path:", args.output_file)
    elif args.quiet:
        print("Output file path:", args.output_file)
    else:
        print("Succesfully created .pbtxt file")
        print("Output file path:", args.output_file)
