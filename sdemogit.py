create and launch instance
login as server with username ec2-user instance
use sudo su command to become root user
create one directory
use git init to intialize directory as git local repository
use git config --global user.name "__" to create user for git repo
use git config --global user.email "__" to link mail to repo"
use git config --list to check details
create one file with code -created in git working directory
now check git status -there is untracked file show
use git add . - to add file from wokspace to staging area now file is known to git
use git commit -m "message" - to commit file from stating area to local repository
use git remote add origin <url> -to connect local repo with central repo github
use git push -u origin master -to send file from local repo to central repo
if gives error then first generate ssh key using command-
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
then add ssh key to ssh agent by starting ssh agent - eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
copy ssh key using - cat ~/.ssh/id_rsa.pub
paste this ssh key into github setting ssh and gpg key "new ssh key" and save
now taste the ssh connection to github account - ssh -T git@github.com
now update git remote location - git remote set-url origin git@github.com:Mohandodmise/MohanPracticeDevops.git
<<<<<<< HEAD
now use git push origin master
=======
not use git push origin master

Updation from mumbai server
use git remote add origin <url> -to connect local repo with central repo github
use git pull origin master -to get file from central repo to local repo

>>>>>>> fb4b269c65ec07f8f963fcd384b93ee67182ea7a
