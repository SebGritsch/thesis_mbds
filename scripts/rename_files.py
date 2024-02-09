import os
import csv

PROJ_DIR = "/media/sf_vmshare/Projects/thesis_mbds"
MZML_DIR = os.path.join(PROJ_DIR, "data", "ms_data", "mzml")

infile = os.path.join(PROJ_DIR, "data", "samplelist.csv")

with open(infile, mode="r") as ifile:
    csv_reader = csv.reader(ifile, delimiter=";")

    # skip header
    next(csv_reader, None)

    # Iterate through each row in the CSV
    for row in csv_reader:
        old_name = os.path.join(MZML_DIR, row[1].split(".")[0] + ".mzML")
        new_name = os.path.join(MZML_DIR, (row[2] + ".mzML"))
        # print(f">{old_name}\n{new_name}")

        # Rename the file
        try:
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print(f"File not found: {old_name}")
        except FileExistsError:
            print(f"File already exists: {new_name}")

print("Renaming completed.")
