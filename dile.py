import os
import shutil
import streamlit as st
import pandas as pd
from datetime import datetime

# File categories
file_mappings = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def ensure_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        st.error(f"❌ Failed to create directory `{path}`: {e}")

def get_category(file_name):
    try:
        _, ext = os.path.splitext(file_name.lower())
        for category, extensions in file_mappings.items():
            if ext in extensions:
                return category
        return "Others"
    except Exception as e:
        st.warning(f"⚠️ Could not categorize file `{file_name}`: {e}")
        return "Others"

def get_unique_filename(dest_dir, file_name):
    try:
        base, ext = os.path.splitext(file_name)
        counter = 1
        new_name = file_name
        while os.path.exists(os.path.join(dest_dir, new_name)):
            new_name = f"{base}({counter}){ext}"
            counter += 1
        return new_name
    except Exception as e:
        st.warning(f"⚠️ Error generating unique name for `{file_name}`: {e}")
        return file_name

def organize_files(source_dir, selected_extensions):
    log_entries = []
    try:
        files = os.listdir(source_dir)
    except FileNotFoundError:
        st.error("❌ Source directory not found.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Unable to read folder: {e}")
        return pd.DataFrame()

    for file in files:
        try:
            full_path = os.path.join(source_dir, file)
            if os.path.isfile(full_path):
                _, ext = os.path.splitext(file.lower())
                if selected_extensions and ext not in selected_extensions:
                    continue
                category = get_category(file)
                dest_dir = os.path.join(source_dir, category)
                ensure_dir(dest_dir)
                new_name = get_unique_filename(dest_dir, file)
                shutil.move(full_path, os.path.join(dest_dir, new_name))
                log_entries.append({
                    "Original Name": file,
                    "Moved To": f"{category}/{new_name}",
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            st.warning(f"⚠️ Failed to move `{file}`: {e}")
            continue

    return pd.DataFrame(log_entries)

# ================= Streamlit UI =================

st.set_page_config(page_title="📁 File Organizer Pro", layout="centered")
st.title("📁 File Organizer Pro")

st.markdown("Organize files by type with filters, logging, and duplicate handling.")

# Folder input
source_dir = st.text_input("📂 Enter full path of folder to organize:").strip()

# File type filters
st.subheader("🎯 File Type Filters")
all_extensions = sorted({ext for exts in file_mappings.values() for ext in exts})
selected_exts = st.multiselect("Select file types to move", all_extensions, default=all_extensions)

# Run button
if source_dir:
    if os.path.isdir(source_dir):
        if st.button("🚀 Organize Files"):
            try:
                log_df = organize_files(source_dir, selected_exts)
                if not log_df.empty:
                    st.success("✅ Files organized successfully!")
                    st.markdown(f"### 📝 Log for {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    st.dataframe(log_df, use_container_width=True)
                else:
                    st.info("📦 No matching files found to move.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")
    else:
        st.error("❌ Invalid folder path. Please check and try again.")