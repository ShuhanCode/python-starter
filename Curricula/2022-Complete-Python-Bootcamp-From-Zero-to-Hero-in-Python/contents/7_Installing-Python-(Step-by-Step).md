#  7. Installing Python (Step by Step)

-   [000-Course-Overview-and Installs](https://docs.google.com/presentation/d/1KBNgNB_JnuXtqpz7Tk7PBinCDteB7pmpeRwZQYqODo0/edit#slide=id.g30f1754bdf_0_6)

Welcome everyone to this lecture where we're going to walk through the process step by step of installing

Python with the free anaconda distribution.

Now there are many ways to actually run Python code.

And we have another lecture later on called Running Python Code where we're going to be exploring the

difference between running a Python script or running Python code, a notebook environment such as Jupyter

Notebook.

Either way, before we actually learn how to run that Python code, we still need to install Python

locally on our computer.

So in this installation lecture, we're going to do the following first.

And the main thing about the lecture is we'll install Anaconda distribution for Python.

The Anaconda distribution is going to install the Python programming language and an easy to use development

environment and navigator launch tool.

That's why for this course we choose the Anaconda distribution.

Instead of just going to Python dot org and only downloading Python, the Anaconda distribution will

install the language and a bunch of really useful tools, especially if you're a beginner in programming.

Then we're going to briefly run Jupyter Notebook, the development environment we use throughout the

course.

Keep in mind though, we'll have later lectures that dive much deeper into the details of actually programming

and running Python code.

This is mainly an installation lecture after all that, we'll explore these no install online options.

So a quick note on these no install options.

There are actually now many online no installation necessary python environments that can be run directly

in the browser.

So as long as you have an internet connection, you actually don't need to install anything.

You can just visit a website and run python code while these are not officially part of the course because

these websites can change and sometimes go from a free plan to a paid plan.

We are going to give you a brief tour of these online no install options at the very end of this installation

lecture, just to give you an idea of what's out there.

To begin, we're going to install a python with the free individual anaconda distribution.

It's actually free and open source.

There's nothing you need to pay for here.

And as I mentioned, this distribution includes Python, as well as many other useful libraries, including

the Jupyter Notebook environment, which is where we do our coding in this particular course.

And Anaconda can also be easily installed on any major operating system Windows, Mac, OS or even Linux.

To begin, we have to first go to the downloads website.

You can go to WW, Anaconda, slash downloads and it should take you to the individual product download

page.

Or you can just do a Google search for Anaconda Download and it should take you to that page as well.

I'm going to head over to my browser and go to Anaconda slash downloads, which should redirect me to

the individual downloads page.

Here I am at Google and what you can do is just search anaconda download hit enter and it should take

you to Anaconda products individual and this is the download page we're looking for that individual

edition or if you directly type in Anaconda Forward slash download, it should also redirect you to

this page.

Keep in mind Anaconda does change the look of this page from time to time.

So at a certain point in the future it may look slightly different to you, but overall there should

be some sort of download and install option on this page.

The individual edition is free and open source.

There's nothing you need to pay for and you'll notice that eventually there's going to be a download

button on this page.

What you do is you can just scroll down here.

It's going to talk about the various aspects that are included of Anaconda, really.

It's not just the Python programming language, although that's definitely the biggest part of it.

It includes a bunch of libraries and really useful tools, especially if you're just a beginner.

So what I'm going to do here is I'm just going to scroll down until I get to the getting started with

Anaconda section and the Anaconda installers, which is really what we're looking for here, this Anaconda

installers, and it's probably going to be at the bottom of the page.

Also, if you just scroll all the way back up here and click download, it will automatically take you

to the installer section.

Now, depending on your operating system, you'll want to download the Windows Installer, Mac OS installer

or the Linux installer.

It's kind of up to you depending on which operating system you're actually running.

Now I am running a modern Windows ten software and if you're running a just relatively recently made

computer, you're probably going to want to install the 64 bit graphical installer.

If you're on an extremely old computer, you may want to check if you have a 32 bit graphical installer,

but it's highly likely that if you're on a modern computer, you're going to be installing the 64 bit

graphical installer.

If you are on Mac OS, install or download the graphical installer, not the command line installer.

There's technically the same thing, but graphical installer comes with an easy to use windows.

That's going to match up with exactly what we show on the Windows Installer.

And if you're on Linux you can download the 64 bit installer here.

Since I am on a Windows computer, I'm going to click and download the 64 bit graphical installer and

once you click on that it should begin the download and it will also take you to a thank you for downloading

web page, which you can pretty much ignore.

There's a little getting started here, which is a 12 minute tutorial.

You may want to take a look at that.

There's also a documentation quick start guide where you can click Learn More and it takes you to this

user guide about Anaconda, some more details.

But really what we're going to talk about is just the installation part in this lecture.

In fact, if you click on that user guide, you can click on installation and it has written out step

by step instructions for installing on Windows, installing on Mac OS or installing on Linux.

So depending on what operating system you have, if you really want step by step written out directions,

you can go to Docker, Anaconda, slash, anaconda slash install and it will take you to the documentation

for a variety of setups which we're really just going to show here.

And again, there's not too many steps here.

You just click next and click all the defaults and hit.

I agree.

Let me fast forward until this executable file is done downloading so we can walk through the installation

procedure together.

Once it's running, what we're going to do is set up Anaconda.

So we'll click on next here, go ahead and agree to the license agreement.

And then depending on whether or not you have admin permissions on your computer, you could do just

me or all users.

I'll do just me.

And then I'm going to install it here under Anaconda three.

I would also suggest that you use the default destination folder.

All right.

And here's a very important step for Windows users.

You'll notice it has this checkbox and it says that it's not recommended to check it.

If this is your first installation of Python and you intend to use this distribution of Anaconda as

your main source for actually running Python code, then I would actually recommend that you install

it and add it to your path environment variable.

Basically what this means is that if you were to open up the Windows Command prompt and type python,

it would come first and search for the Anaconda version of Python before looking at any other pre-installed

python.

And if you're following off this course and you intend to use this as your main distribution, then

we actually do recommend adding Anaconda three to my path environment variable.

If later on and you decided not to check this box and want to add it to your path, what you can do

is open up Anaconda three with the Windows Start menu and then select Anaconda 64 bit.

And then this add to path option will essentially be the same thing as clicking this box here for simple

use cases, I actually do recommend that you click this box, so I will go ahead and click that box

and just add it to my path environment variable since I want Anaconda three to be found first, so then

we'll hit install.

In my Anaconda installation is now complete, so I will go ahead and click next and you'll notice it

says Working with Python and Jupyter Notebooks is a breeze of Pi, charm, professional, etc. We don't

actually need to worry about installing PI charm.

It's just another development environment option for you.

There's pretty much a wider range of environments you can choose from.

We'll be using the Anaconda and Jupyter environment just because we feel that is the most accessible

to someone learning Python for the first time and it's free and open source.

So we'll go ahead and skip this little kind of advertisement there.

And then what we're going to do is we're also just going to skip the tutorial and then skip learning

more about Anaconda.

Those are actually the first two links that we showed you earlier and then hit Finish and you should

be good to go.

Okay.

Now that we finished installing Anaconda, let's show you the two ways to run it.

One is through the Anaconda Navigator to do this, search your computer for Anaconda Navigator.

So I'm going to search for Anaconda.

Navigator.

So I'm going to open up the Anaconda Navigator app.

And you may need to run this as an administrator on some computers, specifically on some work computers,

but go ahead and open up and click on Anaconda Navigator in order to run the application.

Upon clicking that, you should see it beginning to initialize.

And sometimes this takes a while, especially on the first time you're running Anaconda Navigator.

So be patient while it loads, but eventually you should see this graphical interface pop up for Anaconda

Navigator.

Here we are.

Anaconda Navigator.

They'll ask you whether or not you want to send reports to Anaconda.

Feel free to send the reports or not send the reports.

I'm just going to hit.

Okay, here and right now, it's loading a little bit more content and there we go.

So now we have Anaconda Navigator, which is essentially a graphical interface for the various development

environments that Anaconda comes with.

You'll notice that it has Jupyter Lab, Jupyter Notebook, a PowerShell prompt for you, as well as

console spider gloves, Orange three and even our studio.

So Anaconda is essentially packaged not just Python, but a bunch of development environments for you.

For the course in general, we are using Jupyter Notebook, not Jupyter Lab, although it's extremely

similar, but Jupyter Notebook.

Just something to keep in mind.

All right.

Now, before we actually launch Jupyter Notebook, what I want to do is finish this tour of Anaconda

Navigator.

On the left hand side, you see the home tab.

There is also the environments tab environments in this case actually stands for virtual environments,

which may be familiar if you've programmed before, it essentially allows you to create a little virtual

environment separate from your base environment to install particular versions of libraries.

We'll talk about this later on in the course.

You can see that I have some environments already.

You should probably just have your base route environment and maybe one more like a new environment.

But for right now, you can go ahead and ignore and skip this tab.

And finally, there is the learning community tabs learning.

It's just a bunch of links to documentation and some training videos you can check out.

It's really leaning really heavily towards data science and machine learning because Anaconda is really

popular with that community.

And speaking of community, you can click on the community tab and it's a bunch of links to events and

forms you can check out.

Again, highly skewed towards data science and machine learning.

Let's come back home.

And once you're home, where you're going to do is hit the launch button underneath Jupiter Notebook.

We won't be working of Jupiter.

For now, it's really similar.

But for now, Jupiter notebook is a simpler of the two.

It's easier to get started at Jupiter Notebook, so click on launch on Jupiter Notebook.

It's going to load for a little bit, but then it's going to redirect you to a Jupiter notebook in your

browser.

And don't be alarmed.

If you notice, it automatically opens your default browser.

We highly recommend Chrome as your default browser and working with Jupiter Notebook so you can check

that out, but it should automatically open the default browser on your computer.

So for example, you can see off screen it actually did this for me.

It went ahead and opened up Jupiter.

So Jupiter does not require the internet to run.

It's just using your browser as a visual interface for you to write code in.

And you notice that it's typically going to launch in your C drive or in your main user drive, depending

if you're using Windows or Mac OS, in which case you should see a directory of all your folders and

files.

So notice in my C drive I can see my desktop folders, documents, downloads, etc. So then if I click

on one of these like desktop, it actually shows me everything I have underneath my desktop folders

and different files there.

I can come back up and this is essentially allowing me to explore files and folders across my computer,

whether they're in documents, downloads, favorites, games, music, etc. What I can also do is create

new folders and new notebook files from here as well.

Let's quickly explore that.

I can click on New.

And you'll see the option for a new notebook and the option to create a new folder as well as a terminal

connection and text file.

We'll ignore those.

For now we can click on new folder and if you click on new folder, it should create a new untitled

folder essentially at the bottom of this list of folders.

So if you scroll down here, eventually you should see something that says like Untitled Folder created

just a few seconds ago, and then if you open it, it's completely empty.

So this would allow you to actually create notebooks inside.

So it says the notebook list is empty because this is just an empty folder.

What I can do then is I could come back up a directory, scroll down and rename this folder.

I can click the checkbox here, untitled folder and if you scroll up it'll say, Do you want to rename

it?

So let's go in and rename it.

Let's call it my python stuff.

Hit rename.

And now let's open it up again.

So it says my python stuff.

I'm going to open up my python stuff.

It says the notebook list is empty.

Let's create our first notebook.

Notebook is what we're actually going to be writing code in.

I will select new says notebook hit Python three and so automatically launch and connect to a new notebook.

We're going to be discovering notebooks in a lot more detail later on in the course when we talk about

running python code.

But just as a really quick tour of what a Jupyter Notebook is, it's essentially an environment where

there's individual cells where you can write python code.

Let's run our very first piece of Python code just using Python as a calculator.

I will say one plus one.

And then what I can do is I can run the cell, I could say cell run cells, and it will run the cell

with the input as one plus one and the output as to I can also type in.

Or actually do shift enter.

I'm not just typing it in.

This is just to show you what I'm about to do.

If I hit shift enter on my keyboard, it will run this cell and then create a new cell underneath it.

So I'm going to do shift enter on my keyboard again.

It runs the cell and creates a new cell underneath it.

This is the main way we're going to be learning how to program throughout the course.

Keep in mind, we do show you how to run spy scripts using something like a text editor, like sublime

text to give you the option of running python code however you prefer.

But for the majority of the course, we use notebooks because it allows us to write notes and just organize

our data and learn better.

Using Python and all the course notes are organized in notebooks.

In fact, if you go back to the very first lecture of the course or check your automated welcome message

as well as the Q&A forums, you'll see that we have this period data link with the complete three or

complete Python three bootcamp with all the sections and notebooks that correspond to those sections.

So I can click on something.

For instance, like the Milestone Project one, click on warm up project exercises, and these are notebooks

hosted on GitHub for you.

And later on we'll actually show you how to download these notebooks.

But you can see that the notebooks allow you to post images, post explanatory text and code all in

one single interface.

This is why they're so useful for learning Python for the very first time.

We're going to talk a lot more about using Jupyter and running code later on, but for right now, you

should have been able to create your first notebook, run some code and keep in mind there's a whole

help tab here for a user interface to this user interface to super helpful.

If you just click on it, it actually takes you through a kind of left and right code to on file names

and stuff you can do within the notebook.

So I highly recommend you actually just click help and take that User Interface tour now before heading

on to the next lecture.

Once we're done with this notebook, we can simply close this tab.

Notice the notebook is actually still running noted by the green little icon.

You can simply check the box and shut down the notebook.

If you shut down the notebook, the code and text is all saved there, but it's not deleted.

If you do want to delete this notebook completely from your computer's memory, check the box and then

hit this little trashcan or trash icon.

And then it's going to say, Hey, do you want to permanently delete this notebook?

Go ahead and hit delete and now it's permanently removed.

Same thing for the folder.

If you go back up a directory and for some reason you will now want to delete this in my python stuff

folder, simply check this box, scroll back up here and hit the trashcan icon.

It's going to ask you, do you want to permanently delete this folder?

Keep in mind Jupiter only allows you to delete folders that are completely empty.

This is a safety concern that we don't accidentally delete a whole folder permanently.

Go ahead and click delete here and you should have been able to delete that folder.

All right.

So in this lecture, we were already able to install Anaconda Launch Anaconda Navigator and launch our

very first Jupyter Notebook.

Coming up next, we're to discuss how to run Python code, both as a dot pi script and within the Jupyter

Notebook.

To end this lecture, I did mention there were some no installation options.

We're going to do a very brief tour of this if you're interested.

If not, go ahead and move on to the next lecture.

Let's give you a brief tour of all the no install options available on the Internet at this time.

All right.

So let's quickly check out some no installation options, the ones we're going to cover.

Just briefly, here are the official try option from Jupyter.

Try that will actually allow you to run a Jupyter notebook with nothing to install directly in your

browser.

Then we'll also check out Google CoLab online notebooks.

You do need a Google account like a Gmail address in order to access those, but it's a pretty cool

feature provided by Google.

And then we'll also check out Repel it or replace it.

And that's a website that allows you just to write some python code, have it interpreted and run.

I should mention there are dozens of these sort of websites and you can find them by just doing a quick

Google search for Python interpreter online and you'll get a ton of options, including the ones shown

here.

But for a very brief note, why would you not want to just use one of these options instead of installing

something locally?

For one thing, it can be hard to upload your own code data or notebooks on one of these free no installation

options.

And also, sometimes they have the free tier that doesn't save your code, and then you have to actually

pay in order to have your code save and run on their service.

So keep that in mind.

And then the third thing is we're not officially supporting any of these no installation options as

part of this course since they could change in the future.

All right.

I'm going to head over to my browser and just give you a brief tour of these options.

The first option is Jupiter dot org slash try.

It's essentially the exact same thing I just showed you locally, but hosted here for free on the cloud.

So you can try the classic Python notebook.

You can also try it with things like Ah and Jupiter Lab to try it out.

You can try a classic notebook and it's going to upload just a temporary instance of a Jupyter notebook.

I actually often use these when I don't want to run Jupyter Notebook locally, and I do want to run

just a quick piece of Python code and have this run a temporary cloud hosted Jupyter Notebook.

Nothing you put here is actually going to get saved, so keep that in mind.

It's just a temporary notebook being hosted in the cloud.

All right.

So once that's fully loaded, it's going to look something like this.

This is essentially a Jupyter notebook.

It's going to tell you your memory limits.

Keep in mind, locally, you obviously don't have memory limits like this.

It's just the memory limit of your computer's RAM or hard drive space.

You can just insert a new cell or say insert cell below.

Here's the new cell type in something like one plus one or print one plus run and then run these cells

and you'll get to see the output and this is Jupyter dot org try really nice to just quickly run a notebook

hosted online and nothing here is actually going to get saved permanently.

You can click save and it will save your changes, but you can't come back to this website and expect

your notebook to be here.

Another option for downloading it here is if I zoom out just a little bit, you can click here on file

download as you can download this as a notebook, markdown latex, HTML, tons of options here.

There's even JavaScript slides revealed JS if you're familiar with that, but that allows you to download

it locally in case you really want it to save any changes there.

I'm going to close out of this option.

Next option is Google Lab Notebooks.

This is a free notebook service from Google, really focused on machine learning and data science.

And you do need a Gmail account to access this.

Go ahead and just Google search Google Cloud notebooks and go to Calabria, search Google.com and you

can click on one of these already pre-made notebooks or you can click on New Notebook and it takes you

to this new Google CoLab notebook.

And here, what's really cool, if you have a Gmail account, it will actually save your notebook and

you can do things like load up data to a Google drive.

The downside is it's not exactly a Jupyter Notebook.

It's kind of a specialized Google version of it.

But you can say something like one plus one here, Click Run or Hit Shift Enter, and it's going to

run that code and then output the results.

And actually right now it's connecting and initializing.

Now that it's connected, you can see it ran to here one plus one.

You are limited on your ram and disk space, but there's a paid tier in case you decide to do really

huge machine learning or deep learning data sets later on in your Python career, this could be an option

for you.

Now I'm going to close this one.

Last one I want to show you is this repellant.

It's a browser based ID, it is collaborative and do have a free tier you can check out.

So if you click on start coding, you do have to make an account, log in and sign up and check out

the pricing on this.

There is a starter edition that's totally free.

So if you want, you can use this.

This will give you a whole lot of CPU power, though, compared to something like.

So keep that in mind.

And really it's kind of meant for collaborative coding environments.

And if you go back here to the Google search of it, you'll notice there's a little Python link here

and you can click here, go to repel it, slash languages, slash Python three, and you should be able

to actually just kind of give it a little test run so I can do something like print one plus one hit

run here and it's going to give me the output to again, there's limits here.

Nothing is going to get saved unless you make an account log in for the best experience with this course.

I do recommend that you work with a local installation.

It's much easier to follow along that way, but I do want to give you some options in case you're on

a computer where for some reason you don't have full admin permissions to install anything.

If that being said, let's move on to the next lecture and really dive into running python code.

I'll see you there.

---
[Previous](./6_Command-Line-Basics.md) | [Next](./8_Running-Python-Code.md)

