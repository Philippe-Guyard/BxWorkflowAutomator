import os 
import argparse
import subprocess
    
import create_tutorial
import download_code, download_ressources

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int, default=-1,
                    help='Sets tutorial number (create new if not present)')
parser.add_argument('-s', '--spyder', type=bool, default=False,
                    help='If 1, opens the tutorial folder as a spyder project')
parser.add_argument('-f', '--firefox', type=bool, default=False, 
                    help='If 1, opens the tutorial link in firefox')

parser.add_argument('-c', '--course', type=int, default=101, 
                    help='Number of the course following \'CSE\'. Ex, 101 for CSE101.')

args = vars(parser.parse_args()) #we want to change some values in here, which Namespace doesn't allow

if args['number'] == -1: 
    args['number'] = create_tutorial.get_new_tutorial_num() 

tutorial_num = args['number']
args['dir'] = f'Tutorial_{tutorial_num}'
if not os.path.isdir(args['dir']):
    create_tutorial.create_new_dir(tutorial_num)

course = args['course']

if course == 101:
    args['link'] = f'https://x.strub.nu/agns/CSE101/TD{tutorial_num}/2020/'

    #TODO: This can be optimised by using a common soup
    download_code.get_main_code(args['link'], args['dir'])
    download_ressources.get_txt_files(args['link'], args['dir'])

    if args['firefox']:
        bash_command = 'firefox {0}'.format(args['link'])
        subprocess.run(bash_command.split(), stdout=subprocess.PIPE)


    if args['spyder']:
        bash_command = 'spyder -p {0}'.format(args['dir'])
        subprocess.run(bash_command.split(), stdout=subprocess.PIPE)

elif course == 201:
    args['link'] = f'https://x.strub.nu/agns/CSE201/TD{tutorial_num}/2020/'

    download_code.get_main_code_201(args['link'], args['dir'])

else:
    print(f'Sorry! The course CSE{course} is either unspported or does not exist.')
