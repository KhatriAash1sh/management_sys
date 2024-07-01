
from .file_read_write_append import*
def entry(name,Roll_id):
    data=load_students("data.json")
    for i in data:
        if (i[0]==name):
            if (i[1]==Roll_id):
                match=1
                break
        else:
            match=0
    return 0
