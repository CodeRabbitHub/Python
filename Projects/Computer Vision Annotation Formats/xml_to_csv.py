"""
--------------------------------------------------------------------------------------------
DESCRIPTION:
This file takes in .xml files and and combines them into single dataframe to a .csv file.
--------------------------------------------------------------------------------------------
Usage:
python xml_to_csv -i [PATH_TO_FOLDER_CONTAINING_XML] -o [PATH_TO_OUTPUT_FOLDER_FOR_CSV_FILE]
--------------------------------------------------------------------------------------------
"""

import os
import glob
import pandas as pd
import argparse
import xml.etree.ElementTree as ET


def xml_to_csv(path: str) -> pd.DataFrame:

    xml_list = []
    for xml_file in glob.glob(path + "/*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            value = [
                root.find("filename").text,
                int(root.find("size")[0].text),
                int(root.find("size")[1].text),
                member[0].text,
                int(member[4][0].text),
                int(member[4][1].text),
                int(member[4][2].text),
                int(member[4][3].text),
            ]
            xml_list.append(value)
    column_name = [
        "filename",
        "width",
        "height",
        "class",
        "xmin",
        "ymin",
        "xmax",
        "ymax",
    ]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():

    parser = argparse.ArgumentParser(
        description="XML-to-CSV converter for TF Object Detection API"
    )
    parser.add_argument(
        "-i",
        "--input_directory",
        help="Path to the folder where the input .xml files are stored",
        metavar="",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_file_path",
        help="Path to output .csv file (include name of file)",
        metavar="",
        type=str,
    )
    args = parser.parse_args()

    if not args.input_directory:
        args.input_directory = os.getcwd()
    if not args.output_file_path:
        args.output_file_path = args.input_directory + "\labels.csv"

    assert os.path.isdir(args.input_directory)

    xml_df = xml_to_csv(args.input_directory)
    xml_df.to_csv(args.output_file_path, index=None)
    print("Successfully converted xml to csv.")
    print("Output path", args.output_file_path)


if __name__ == "__main__":
    main()
