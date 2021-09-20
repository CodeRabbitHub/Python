"""
--------------------------------------------------------------------------------------------
DESCRIPTION:
This file takes in .xml files and and combines them into single dataframe to a .csv file.
--------------------------------------------------------------------------------------------
Usage:
python xml_to_csv -i [PATH_TO_FOLDER_CONTAINING_XML] -o [PATH_TO_OUTPUT_FOLDER_FOR_CSV_FILE]
--------------------------------------------------------------------------------------------
"""

import argparse
import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser(
        description="XML-to-CSV converter for TF Object Detection API"
    )
    parser.add_argument(
        "-i",
        "--input_directory",
        help="Path to the folder where the input .xml files are stored",
        metavar="INPUT DIRECTORY PATH",
        default=Path.cwd(),
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output_file_path",
        help="Path to output .csv file (include name of file)",
        metavar="OUTPUT FILE PATH",
        default=None,
        type=str,
    )
    args = parser.parse_args()

    if args.output_file_path is None:
        args.output_file_path = Path(args.input_directory) / "labels.csv"

    inputDir = Path(args.input_directory)
    outputDir = Path(args.output_file_path)

    assert inputDir.is_dir(), "Input directory doesn't exist"
    assert outputDir.parent.is_dir(), "Output directory doesn't exist"

    xml_to_csv(inputDir, outputDir)


def xml_to_csv(inputPath, outputPath):
    xml_list = []
    for xml_file in inputPath.glob("*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            value = [
                root.find("filename").text,
                int(root.find("size").find("width").text),
                int(root.find("size").find("height").text),
                str(member.find("name").text),
                int(member.find("bndbox").find("xmin").text),
                int(member.find("bndbox").find("ymin").text),
                int(member.find("bndbox").find("xmax").text),
                int(member.find("bndbox").find("ymax").text),
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
    xml_df.to_csv(outputPath, index=None)

    print("Successfully converted xml to csv.")
    print("Output path", outputPath)


if __name__ == "__main__":
    main()
