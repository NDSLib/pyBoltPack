from glob import glob
import os


#path = ''
def fileallsearch(path):
    search_path = [path]
    index = 0
    while True:
        try:
            paths = glob(f'{search_path[index]}/*')
        except IndexError:
            break
        for path in paths:
            if os.path.isfile(path):
                #print('isfile!',path)
                yield path
            else:
                search_path.append(path)
        index += 1


