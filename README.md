# BxWorkflowAutomator
A collection of scripts to automate workflow at the Bachelor of Ecole Polytechnique.

Note that this project has just started and many ideas have not yet been implemented.  
If you have any tasks you would like to automate (and if this automation will actually help other people in the bachelor), feel free to pm me in 
telegram [@philippeguyard](https://t.me/philippeguyard) or make pull requests to this repo directly.


# Windows prerequisites 

- Make sure you have `git` and `git bash` installed. They can be downloaded from [here](https://git-scm.com/downloads).
- If you are using anaconda python, set [3 new PATH variables](https://stackoverflow.com/questions/54135206/requests-caused-by-sslerrorcant-connect-to-https-url-because-the-ssl-module") (you can edit environmental variables by pressing windows+R, typing SystemPropertiesAdvanced and clicking on environmental variables").


# Usage

Note that the scripts are avalaible for *Ubuntu and Windows* (for now). MacOS users are free to write installation instructions for their platform in separate
pull requests.

## Downloading new cs tutorials
Move to the folder with all your cs tutorials. Assuming that they are all named `Tutorial_1`, `Tutorial_2` ..., the script will find the number
  of the latest tutorial which hasn't been created, then create a new folder for it, download all attached `.txt` files and the default `.py` file with all the functions and docstrings. 
  
To create new cs tutorials, you have to run the `newcs.sh` script. *Windows users* should just use `python main.py` directly. It is also possible to add your own terminal command. **Example for ubuntu users:** create an alias `alias gettut='~/my_scripts/cs_download/newcs.sh'` and just run `gettut` in any folder
  - **Ubuntu users:** A detailed instruction on how to add bash scripts to your ubuntu command list can be found [here](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi)
  - **Windows users:** If you wish to set a permanent DOSKEY/alias for the script see [here](https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd).

For second year  bachelor users, run the script `newcs201.sh` instead, in order to download (and unzip) tutorials for CSE201. More suport for other courses coming soon. Second year content support by [@guruprerana](https://github.com/guruprerana).
  
Note that you can always see the full argument list by running `python main.py --help`
 
