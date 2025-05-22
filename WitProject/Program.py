import FileManager
from Repository import Repository
import click

def load():
    if  FileManager.is_exist('.wit', FileManager.current_path()):
        data=FileManager.load_from_json(FileManager.join_path(FileManager.current_path(),'.wit\dataJson.json'))
        return Repository.to_repository(data)
    raise Exception('is not exist repository of wit')

def save(repository):
    data = repository.to_dict()
    FileManager.save_to_json(data,FileManager.join_path(FileManager.current_path(),'.wit\dataJson.json'))





@click.command()
@click.argument('func',type=click.Choice(['wit init','wit add .','wit add','wit commit','wit log','wit status','wit checkout']))
@click.argument('value',type= str,required=False)
def cli(func,value):
    if func == 'wit init':
        rep = Repository()
        save(rep)
    else:
        rep = load()
        if func == 'wit add .':
            rep.wit_add(value)
        elif func == 'wit add':
            rep.wit_add()
        elif func == 'wit commit':
            rep.wit_commit(value)
        elif func == 'wit log':
            rep.wit_log()
        elif func == 'wit status':
            rep.wit_status()
        elif func == 'wit checkout':
            rep.wit_checkout(value)
    save(rep)