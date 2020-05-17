# SchoolZoid
SchoolZoid is a Flask/LAMP app that allows schools to streamline homework submission pipelines for students and instructors. 


## Getting Started with Git

I am going to cut to the chase and teach you relevant bits only. Once Git is initialised in a directory, all files in the directory start getting tracked for changes. Whenever you make a relevant change, you push it to your branch in this remote repository (that is hosted on GitHub) and I approve it and it gets merged into the master (main) branch, which is where the best iteration of the software is.  

Use the following commands to get started with everything.

Clone the repository using the following command - 

```bash
git clone https://www.agamjolly.com/gitcommands.md
```
When more than one person is working in the project and making changes, work is done by using branches. A branch is essentially is a unique set of code changes with a unique name. Each repository can have one or more branches. The main branch — the one where all changes eventually get merged back into, and is called master. This is the official working version of your project, and the one you see when you visit the project repository at github.com/yourname/projectname.

You will make your own branch, make new changes to the branch, and then push the changes to the repository. If you've completed some work, I will approve your changes into the master branch and we can iterate over the app.

Make your own branch using the following command - 
```bash
git checkout -b harsh # Replace "harsh" with your own name.
```

It will show you that you moved from the "master" branch to a new branch called "harsh". The branch "master" is the branch where the newest and finalised iteration of the software is.  

If you make a new file/folder in the project directory, you must inform Git about it. This can be done using - 
```bash
git add . # The "add ." adds all the files in the given directory.
```

Once you have started Git, and made first relevant progress towards the project, you start committing changes to your branch. This can be done using - 

```bash 
git commit -m "Your message stating what you've done to keep track of things."
```

To push your changes to the repository, you need to use the following command - 

```bash
git push origin harsh
```

This should just about sum it up. 
