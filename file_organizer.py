import os
import shutil 
import logging

#configure logging
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Define the target directory '  and the categories
TARGET_DIR = r'C:\Users\asus\OneDrive\Pictures'
CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Others': []
}

#- Design folder structure by categories (Documents, Images, Videos,Others)
#def create_category_folders():

def create_category_folders():
    """
    Create category folders in the target directory if they don't exist"""
    for category in CATEGORIES.keys():
        category_path = os.path.join(TARGET_DIR, category)
        # - Add exception handling (try-except) and logging for errors and activity.
        try:
            if not os.path.exists(category_path):
                os.makedirs(category_path)
                logging.info(f"Created directory: {category_path}")
            else:
                logging.info(f"Directory already exists: {category_path}")
        except Exception as e:
            logging.error(f"Error creating directory {category_path}: {e}")
            # print(f"Error creating directory {category_path}: {e}")  




# - Implement script to scan and classify files based on extensions.
def move_and_classify_files():
    try:
        files = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]
        for filename in files:
           file_path = os.path.join(TARGET_DIR, filename)
           _,file_extension = os.path.splitext(filename)

           moved = False
           for category, extensions in CATEGORIES.items():
               if file_extension.lower() in extensions:
                   destination = os.path.join(TARGET_DIR, category, filename)
                   try:
                       shutil.move(file_path, destination)
                       logging.info(f"Moved file {filename} to {category}")
                       moved = True
                   except Exception as e:
                       logging.error(f"Error moving file {filename} to {category}: {e}")
                   break  
               if not moved:
                   others_path = os.path.join(TARGET_DIR, 'Others', filename)
                   try:
                       shutil.move(file_path, others_path)
                       logging.info(f"Moved file {filename} to Others/")
                   except Exception as e:
                       logging.error(f"Error moving file {filename} to Others/: {e}") 
    except Exception as e:
        logging.error(f"Error moving and classifying files: {e}")



def main():
    try:
        create_category_folders()
        move_and_classify_files()
        logging.info("File organization completed successfully.")
    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()                  
                  
                   