# BxWorkflowAutomator
A collection of scripts to automate workflow at the Bachelor of Ecole Polytechnique.

Note that this project has just started and many ideas have not yet been implemented.  
If you have any tasks you would like to automate (and if this automation will actually help other people in the bachelor), feel free to pm me in 
telegram [@philippeguyard](https://t.me/philippeguyard) or make pull requests to this repo directly.

# Usage

Note that the scripts are avalaible for *Ubuntu only* (for now). Windows and MacOS users are free to write installation instructions for their platforms in separate
pull requests.

- Downloading new cs tutorials
  - You should this script in the folder with all your cs tutorials. Assuming that they are all named Tutorial_1, Tutorial_2..., the script will find the number
  of the latest tutorial which hasn't been created, then create a new folder for it, download all attached .txt files and the default .py file with all the functions and docstrings. 
  - To create new cs tutorials, you have to run the `newcs.sh` script. 
  A detailed instruction on how to add bash scripts to your ubuntu command list can be found [here](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi)
  - You can always see the full argument list by running `python main.py --help`
