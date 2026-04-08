# STEP 1: IMPORT LIBRARIES

import os
import shutil
import pandas as pd
from tqdm import tqdm

# STEP 2: LOAD CLINICAL DATASET

clinical_path = "cleaned_clinical_features.csv"
df = pd.read_csv(clinical_path)

print("Clinical Dataset Loaded:")
print(df.shape)

# STEP 3: EXTRACT PATIENT IDs

patient_ids = set(df["ID"].astype(str))

print(f"Total Unique Patients in Clinical Data: {len(patient_ids)}")

# STEP 4: DEFINE IMAGE DATA PATH

cmmd_path = "CMMD"  # Folder containing all patient image folders

all_folders = os.listdir(cmmd_path)

print(f"Total Folders in CMMD: {len(all_folders)}")

# STEP 5: CREATE OUTPUT FOLDER (ALIGNED DATASET)

output_path = "CMMD_Aligned"

if not os.path.exists(output_path):
    os.makedirs(output_path)

print(f"Output folder created: {output_path}")

# STEP 6: MATCH & COPY ONLY REQUIRED PATIENTS

matched = 0
missing = []

for folder in tqdm(all_folders):

    folder_path = os.path.join(cmmd_path, folder)

    # Check if folder is a patient folder
    if folder in patient_ids:

        src = folder_path
        dst = os.path.join(output_path, folder)

        try:
            shutil.copytree(src, dst)
            matched += 1
        except Exception as e:
            print(f"Error copying {folder}: {e}")
    else:
        missing.append(folder)

# STEP 7: SUMMARY

print("\n========== ALIGNMENT SUMMARY ==========")
print(f"Total Clinical Patients: {len(patient_ids)}")
print(f"Matched Patients Copied: {matched}")
print(f"Unmatched Image Folders: {len(missing)}")

# STEP 8: SAVE MATCHED IDS TO A NEW CSV

matched_ids = list(set(all_folders).intersection(patient_ids))
matched_df = df[df["ID"].astype(str).isin(matched_ids)]

matched_df.to_csv("aligned_clinical_dataset.csv", index=False)

print("\nAligned clinical dataset saved as: aligned_clinical_dataset.csv")

# STEP 9: FINAL CHECK

aligned_folders = os.listdir(output_path)

print("\nFinal Check:")
print(f"Total folders in aligned dataset: {len(aligned_folders)}")