## I deleted a folder by mistake in my Local repository in my laptop. How do I update my local directory from my Github repository

> ````First, navigate to the local repository on your computer using the command line.````

> ````Run the command "git fetch" to download the latest commits from the GitHub repository.````

> ````Run the command "git reset --hard origin/main" to reset your local repository to the state of the GitHub repository. This will delete all the changes in your local repository that are not in the GitHub repository, including the deleted folder.````

Please note that this will overwrite any local changes that you have made since your last commit, and they will be lost permanently. So, it is always good to take backup of the files which you have deleted by mistake and you want to recover them.


