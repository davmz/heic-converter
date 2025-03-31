# converter.py

import time
from utils import (
    get_input_file_path,
    create_output_folder,
    process_path
)

def main():
    print("📸 HEIC to JPG Converter\n")

    # Step 1: Get valid input path from user (file or folder)
    input_path = get_input_file_path()

    # Start timing after input
    start_time = time.time()

    # Step 2: Create output folder if it doesn't exist
    output_folder = create_output_folder()

    # Step 3: Process the input (file or folder)
    total, converted, failed_files, converted_path = process_path(input_path, output_folder)

    # End timing after conversion
    end_time = time.time()
    total_time = end_time - start_time

    # Step 4: Display result
    if total == 0:
        print("\n⚠️ No valid .heic files to convert.")
    elif total == 1 and not failed_files:
        print(f"\n✅ Successfully converted:")
        print(f"Original file: {input_path}")

        if converted_path: # Only show if it's not None
            print(f"Converted file: {converted_path}")
    else:
        print(f"\n✅ Converted {converted}/{total} file(s).")
        if failed_files:
            print("❌ Failed to convert the following file(s):")
            for f in failed_files:
                print(f"- {f}")

    print(f"⏱️ Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()