import os
import shutil
import filecmp
import json


def is_exist(path,name_folder_or_file = ''):
    if len(name_folder_or_file) == 0:
        return os.path.exists(path)
    return  os.path.exists(os.path.join(path,name_folder_or_file))

def remove_last_segment(path):
    return os.path.dirname(path)

def current_path():
    return os.getcwd()

def join_path(path1,path2):
    return os.path.join(path1,path2)

def create_folder(name_folder, path):
    os.mkdir(os.path.join(path,name_folder))

def is_wit_folder(src,names):
    return [name for name in names if name == ".wit"]

def add_files(path1,path2):
    shutil.copytree(path1, path2, ignore=is_wit_folder, dirs_exist_ok=True)

def copy_file(source_path, destination_path):
    shutil.copy(source_path,destination_path)

def is_equals(file1, file2):
    return filecmp.cmp(file1,file2)

def is_empty(path):
    return  len(os.listdir(path))==0

#to save and loading
def save_to_json(obj,filename):
    #דורס את הנתונים הקודמים לפני הכתיבה מחדש
    with open(filename, 'w') as json_file:
        json_file.truncate(0)
    with open(filename,'w') as json_file:
        json.dump(obj,json_file)


def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data=json.load(json_file)
        return data


def copies_files_not_exist_target(src, target):
    for item in os.listdir(src):
        src_item_path = os.path.join(src, item)
        target_item_path = os.path.join(target, item)
        # אם זה קובץ או תיקיה
        if os.path.isdir(src_item_path):
            # אם התיקיה לא קיימת ב-B מעתק אותה
            if not os.path.exists(target_item_path):
                shutil.copytree(src_item_path, target_item_path)
        else:
            # אם הקובץ לא קיים ב-B מעתק אותו
            if not os.path.exists(target_item_path):
                shutil.copy2(src_item_path, target_item_path)

def list_files_or_polders(path):
    return os.listdir(path)

def remove_all(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                if item != '.wit':
                    shutil.rmtree(item_path)  # מוחק תיקיות
            else:
                os.remove(item_path)  # מוחק קבצים
    else:
        raise Exception('path not exist')
