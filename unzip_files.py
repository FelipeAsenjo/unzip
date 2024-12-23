import os
import zipfile

def unzip_files(folder, first_el, last_el):
    # list of zip files in selected folder
    zip_files = sorted([f for f in os.listdir(folder) if f.endswith('.zip')])
    
    for file in zip_files:
        file_number = int(file.split('-')[-1].split('.')[0])

        if type(file_number) == int:
            print('file_number (starting): ' + str(file_number))
            if file_number >= first_el and file_number <= last_el:

                # full file path
                file_path = os.path.join(folder, file)
                
                output_folder = os.path.join(folder, os.path.splitext(file)[0])
                
                # unzip!
                try:
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(output_folder)
                        print(f"unzipped: {file} in {output_folder}")
                except zipfile.BadZipFile:
                    print(f"Error: {file} invalid zip file. Continue to next file.")

            else:
                if file_number > last_el:
                    print(f"last file in batch: {file}. Stopping the process.")
                    print('file_number (ending): ' + str(file_number))
                    print('last_el: ' + str(last_el))
                    break
                else:
                    print(f"{file}: Skipped...") 
        else:
            print(f"unable to pick file number: {file}")

main_folder_path = r'/mnt/e'
first_file_on_batch = 301
last_file_on_batch = 321

unzip_files(main_folder_path, first_file_on_batch, last_file_on_batch)

