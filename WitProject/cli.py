import FileManager
from Repository import Repository
import click

def load():
    if FileManager.is_exist(FileManager.current_path(), '.wit'):
        data = FileManager.load_from_json(FileManager.join_path(FileManager.current_path(), r'.wit\dataJson.json'))
        print(f"Loaded data: {data}")  # הצגת המידע שהתקבל
        if isinstance(data, dict):  # אם המידע הוא מילון
            return Repository.to_repository(data)
        else:
            raise Exception('Data in .wit is not in the expected format')
    raise Exception('Repository does not exist')


def save(repository):
    # אם המידע הוא אובייקט Repository, ממירים אותו למילון
    if isinstance(repository, Repository):
        data = repository.to_dict()
        print(f"Saving data: {data}")  # הצגת המידע שנשמר
    else:
        data = repository  # אם כבר מדובר במילון, אין צורך להמיר
        print(f"Saving data: {data}")  # הצגת המידע שנשמר

    FileManager.save_to_json(data, FileManager.join_path(FileManager.current_path(), r'.wit\dataJson.json'))


@click.command()
@click.argument('func', type=click.Choice(['init', 'addAll', 'add', 'commit', 'log', 'status', 'checkout']))
@click.argument('value', type=str, required=False)
def cli(func, value):
    if func == 'init':
        rep = Repository()
        save(rep)  # שמירה של האובייקט החדש
    else:
        rep = load()  # טוענים את המידע
        if func == 'addAll':
            rep.wit_add_all()
        elif func == 'add':
            rep.wit_add(value)
        elif func == 'commit':
            rep.wit_commit(value)
        elif func == 'log':
            rep.wit_log()
        elif func == 'status':
            rep.wit_status()
        elif func == 'checkout':
            rep.wit_checkout(value)
        save(rep)  # שמירה של האובייקט או המילון לאחר שינוי


if __name__ == "__main__":
    cli()
