from datetime import  date

import FileManager
from Commit import Commit
import click


class Repository:
    def __init__(self,flag=True,hashcode=0, current_commit=-1):
        self.project_path = FileManager.current_path()
        self.commits_dict = {}
        self.hashcode = hashcode
        self.current_commit = current_commit
        #האם זה מאגר משוחזר או חדש(אתחול ראשוני)
        if flag:
            if FileManager.is_exist(FileManager.current_path(),'.wit'):
                raise Exception('This database already exists')
            FileManager.create_folder('.wit',self.project_path)
            FileManager.create_folder('staging',FileManager.join_path(self.project_path,'.wit'))
            FileManager.create_folder('commits',FileManager.join_path(self.project_path,'.wit'))

    def add_commit(self, commit_description):
        self.commits_dict[self.hashcode] = Commit(date.today(), commit_description, self.hashcode)
        self.hashcode+=1

    # ממירה את האוביקט למילון
    def to_dict(self):
         return {
             'project_path': self.project_path,
             #רשימה של כומיטים
             'commits_dict': {hashcode:commit.to_dict() for hashcode, commit in self.commits_dict.items()},
             'hashcode': self.hashcode,
             'current_commit':self.current_commit
         }

     # ממירה את המילון לכומיט
    @classmethod
    def to_repository(cls, data):
        #מופע של המחלקה הנכחית
        #דורסת נתונים אתחלתיים לא רלוונטים לשחזור מופע
       repository = cls(False,data['hashcode'], data['current_commit'])
       for hashcode, commit_data in data['commits_dict'].items():
           commit =  Commit.to_commit(commit_data)
           repository.commits_dict[hashcode]=commit
       return repository


    def wit_add_all(self):
        FileManager.add_files(self.project_path,FileManager.join_path(self.project_path,r'.wit\staging'))

    def wit_add(self,file):
        target_path = FileManager.remove_last_segment(FileManager.join_path(FileManager.join_path(self.project_path,r'.wit\staging'),file))
        #עבור קובץ בודד
        #האם הוא קיים כבר ברמה מקוננת או לא. מכניס אותו למקום המתאים
        if FileManager.is_exist(target_path):
            FileManager.copy_file(FileManager.join_path(self.current_path,file),target_path)
        else:
            FileManager.copy_file(FileManager.join_path(self.current_path,file),FileManager.join_path(self.current_path,r'.wit\staging'))


    def wit_commit(self,message):
        self.add_commit(message)
        prev_commit=FileManager.join_path(FileManager.join_path(self.project_path, r'.wit\commits'), str(self.current_commit))
        new_commit=FileManager.join_path(FileManager.join_path(self.project_path, r'.wit\commits'), str(self.hashcode - 1))
        FileManager.create_folder(str(self.hashcode-1),FileManager.join_path(self.project_path,r'.wit\commits'))
        # מעתיק פעם ראשונה מבלי לשלב בין הקיים לחדש
        FileManager.add_files(FileManager.join_path(self.project_path, r'.wit\staging'),new_commit)
        if self.current_commit!=-1:
            #ממלא את הכומיט החדש בכל ערכי הstaging - בכל מקרה
            #וכן כל מה שלא עודכן לstaging וכן נמצא בכוניט הקודם
            FileManager.copies_files_not_exist_target(prev_commit,new_commit)
        self.current_commit = self.hashcode - 1
        #מרוקנת את תכולת הstaging
        FileManager.remove_all(FileManager.join_path(self.project_path, r'.wit\staging'))


    #לשנות שידפיס לcli ולא לקונסול
    def wit_log(self):
        for i,c in self.commits_dict.items():
             click.echo(c)

    def wit_status(self):
        #אם אין שינויים
        if FileManager.is_empty(FileManager.join_path(self.project_path,r'.wit\staging')):
            print ('No changes')
        else:
            for f in FileManager.list_files_or_polders(FileManager.join_path(self.project_path,r'.wit\staging')):
                click.echo(f)

    def wit_checkout(self, commit_id):
        # בודק אם תיקיית הכומיט קיימת
        commit_path = FileManager.join_path(FileManager.join_path(self.project_path, r'.wit\commits'), str(commit_id))
        if not FileManager.is_exist(commit_path):
            raise Exception(f'Commit {commit_id} does not exist.')
        # דורסת את הפרוייקט הנחי במה ששמור לי בכומיט הרצוי
        FileManager.remove_all(self.project_path)
        # מנתב לכומיט הרצוי ע"י שם הכומיט
        FileManager.add_files(commit_path, self.project_path)
        self.current_commit = commit_id


