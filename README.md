### PyconNg-2019

The official website for PyconNg-2019 visit [link](http://pycon.pythonnigeria.org/)

Event on the 30th October - 2nd November 2019  Wennovation Hub, 50 Ebitu Ukiwe Street. Jabi, Abuja,   Nigeria



### Install Project
    * Create a parent folder 
    * Clone into the parent folder
        * git clone https://github.com/pyung/pyconng-2019.git (HTTPS)
        * git clone git@github.com:pyung/pyconng-2019.git (SSH)
    * cd web
    * Install dependencies
        * pipenv install -r requirements.txt (if using pipenv)
        * pip install -r requirements.txt (if using pip) 

### Create a virtual environment using virtualenv
    * sudo pip3 install virtualenv
    * virtualenv <folder>
    * cd into <folder>
    * source bin/activate
    * pip install

### Create a virtual environment using pipenv
    * Make sure it is installed
        * pip install pipenv (windows developers)
        * sudo pip3 install pipenv (ubuntu developers)
    * Create parent folder
    * CD into parent folder and run pipenv --python 3.7/<or any python-version>
    * pipenv shell
    * pipenv install 


### Contribute
    * fork the repo
    * Clone it locally (git clone https://github.com/<username>/pyconng-2019.git)
    * Add upstream repo (git remote add upstream https://github.com/<username>/pyconng-2019.git)
    * Create a feature/topic branch (`git checkout -b <branch_name>)
    * Code fix/feature (add required tests and make sure the pass)
    * Commit code on feature/topic branch (git add . && git commit -m “awesome”)
    * Checkout master (git checkout master)
    * Pull latest from upstream (git pull upstream master)
    * Checkout feature/topic branch (git checkout <branch_name>)
    * Rebase your changes onto the latest changes in master (git rebase master)
    * Push your fix/feature branch to your fork (git push upstream <branch_name>)




Thanks alot, happy coding &#128526;
