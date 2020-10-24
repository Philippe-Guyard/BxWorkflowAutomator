import os 

def get_new_tutorial_num():
    new_tutorial_num = 1
    for subdir in os.listdir():
        if subdir.startswith('Tutorial'):
            num_str = ''
            pointer = -1
            while subdir[pointer].isdigit():
                num_str += subdir[pointer]
                pointer -= 1
            if len(num_str) == 0:
                print(f'Error: invalid dir name: {subdir}')
                exit(0)

            old_tutorial_num = int(num_str)
            if old_tutorial_num >= new_tutorial_num:
                new_tutorial_num = old_tutorial_num + 1

    
    return new_tutorial_num

def create_new_dir(tutorial_num):
    new_dir = f'Tutorial_{tutorial_num}'
    os.mkdir(new_dir)

    return new_dir


def main():
    new_tutorial_num = get_new_tutorial_num()
    new_dir = create_new_dir(new_tutorial_num)
    print(f'Create new dir: {new_dir}')


if __name__ == '__main__':
    main()    