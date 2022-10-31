#  8. Running Python Code

Welcome back, everyone.

By now we've learned about the command line basics, and we also have installed Python onto our computer.

It's time to actually run our first piece of Python code.

Before we do that, I want to discuss the several different ways you can run Python code and the various

options there are for developing environments for Python.

And there's three main types of environments.

And what I mean by environments is the actual thing you're going to be typing Python code into.

And the three options are text editors full IDs, which stands for Integrated Development Environment,

and then there's notebook environments.

So let's start off with text editors.

Text editors are just general editors for any text file, and that is to say they're designed in a general

format where they can open a text, file, a dot py script, a HTML file, a JS file for JavaScript,

just any variety of file types, you'll be able to open them up and edit them, and they can also be

customized with plug ins and add ons.

And because of that and their general format, they actually aren't designed with only Python in mind.

So you're going to sacrifice a little bit of Python specific functionality, things like autocomplete

for Python or looking up things in the documentation automatically for Python.

Those typically won't be included directly with the text editor.

Instead, you'll have to download them with a plug in or some other add on for text editors.

Keep in mind there's tons of plug ins out there and Python is such a popular programming language,

you can pretty much find any plugin you want already created for you, for the text editors you're working

with.

And the most popular text editors on the market are sublime, text and Atom, and those are both free.

Technically sublime text is an unlimited use free license that you can eventually pay for if you like.

The product Atom is an open source text editor from GitHub, which is completely free and it's open

source.

And later on in this lecture we'll be showing you how to download Sublime text and running Python scripts

with Sublime text.

So that's one option.

The text editor, another really popular option, especially if you're working at a company, is a full

integrated development environment.

And these are development environments that are designed specifically for use cases with Python and

their larger programs.

What I mean by larger is that it's a larger file size.

The text editors from before, those are actually very lightweight programs that you end up adding more

and more to them as you want more plug ins ideas.

They come with everything already, so they have larger programs and because they're ides, it means

there's actually a team of developers or a company behind it being paid to add new features to the environments.

And because of that, there is typically a pro version and a community version where only the community

edition is free and the pro version that has more features.

Maybe they'll have more features for Django web frameworks or web development.

Help those you have to pay for the community editions are free, however, and the pro about this is

that they're designed specifically for Python.

They have lots of extra functionality to help with your Python code, but they are a little more bloated,

a little larger, and it kind of depends on what your workflow style is.

If you like this approach or not, the most popular IDs for Python are probably pie charm.

That's definitely the biggest one out there.

And then Spider is another popular one.

Spider is really popular for people coming in from MATLAB into Python.

Finally, let's talk about notebook environments.

And notebook environments is the environment we're going to be using for the majority of this course.

Later on, we'll move away from notebooks and move towards larger scripts.

But to start off with, we'll go over the notebooks.

And that's because, in my opinion, they're really great for learning.

And the main thing here is that you get to see your input code and your output of the code right next

to each other, and you get to see multiple inputs and multiple outputs all in one nice notebook.

And this is because notebooks use blocks of code that are referred to as cells.

So you can split up your code into different cells and then run pieces of your code by running individual

cells.

And you get to immediately see the output.

That's different than the the approach taken with a text editor or development environment where you

have to develop kind of a larger script first and then run that script at the command line.

That's really great when you do have larger pieces of code that need to interact with each other.

But when you're just starting off, you kind of want to quickly be able to type something in and see

the output, which is why a notebook environment is really great for learning.

The other things that differentiate a notebook environment is that they support inline markdown notes,

so you can write yourself different pieces of notes.

So just normal text is what we mean by markdown notes.

And actually the notebooks we provide for this course have a lot of explanatory text for you.

So you essentially get a book along with the videos that go with this course.

And they also support things like visualizations, images, videos and a lot more.

And because they support all these extra things, they actually have their own special file format that

are not a PI script.

And because of that, typically if you see a PI script on your computer, you can double click on it

and some sort of text editor will automatically open the PI script because notebooks are able to support

all this extra stuff.

They have their own notebook format, which is extension API and B that stood for a Python notebook.

And because of that special format, you can't actually double click on a notebook file.

You need to launch it using the Jupyter Notebook launcher.

So the.

Her notebook is pretty much the most popular, and it's almost the only notebook environment for Python

because of how popular it is.

But it's getting more and more popular, especially in fields of data science and machine learning,

because you can see visualizations and your code input right next to the output.

So we're going to be using that at first to start learning.

But the most important note here is that development environments are actually a very personal choice

and it's really highly dependent on your personal preference.

So if Python is not your first language and you're already used to using Sublime text editor, or maybe

you've already used Pi charm at work and you have the pro version there and you want to prefer to use

those development environments.

Please feel free to do so.

All the code we show is going to work in any development environment that you choose.

So really, after you see this lecture, choose whichever development environment you prefer.

We provide the notes as IP and files that you can easily convert them or download them as HTML files

or PI scripts.

And all the code we show in the videos runs the same regardless of what environment you're using.

So let's now explore how to run Python code.

We're first going to start with an editor, so we'll download the Sublime Text editor and we'll show

you how you can create a simple PY script and run the file at your command line.

Then we're going to show how to run the same code with a Jupyter Notebook.

So do all this.

We first need to download Sublime Text Editor, so go to w-w-what Sublime text and we'll see you there.

All right, here we are at Sublime text and typically it will auto detect will operating system you're

on and it will have a little button for you saying download for OS Linux or Windows.

It's a very simple text editor and it's probably the most popular text editor in the world and it has

a really interesting pricing scheme.

It's technically not free, but they give you an unlimited free trial where they will just have a little

pop up every once in a while asking you if you're ready to upgrade to buy it.

So again, it's technically not free, but it has an unlimited free trial for the rest of your life.

It will just have a little pop up asking you to purchase the full license.

So click here on download and then select the download for your operating system either OS X Windows,

Windows 64 bit or Linux.

So typically what you should do is just go to the home page and then click whatever download that auto

detected for you.

Once you've downloaded it, we'll go ahead and open the sublime text editor.

Once you've downloaded and installed Sublime text, you should be able to search your computer for Sublime

text.

Click on it, open it up, and it will look something like this.

Next, what we're going to do is actually type out some python code and then save this as a dot py script.

Go ahead and type print, open and close parentheses and then in single quotes or double quotes.

Hello.

World and this will be your first Python script and then select file.

Save as and the reason we're doing that is if you notice right now, there's no syntax highlighting.

That is to say everything is the same color for this font.

So Sublime text editor doesn't actually know that this is a Python script.

What we want to do is save it as and we're going to call this file.

My example.

And you'll notice if you click on all files, you have lots of extensions to choose from.

We're going to choose to save it as a Python file.

So you're going to say my example, save it as a Python file.

The other option you can do is just select all files and then say my example and yourself.

Right.

PY either way is fine.

Go ahead and save it.

Making sure it's a dot py file.

Hit save and now you'll notice Sublime text editor understands that it's a Python script file and it's

performed syntax highlighting to help you read this print as a function.

Helloworld is a string and we're going to be learning a lot more about that and Python in general later

on in your training.

For now, let's see how to actually run this script.

Remember that we've saved it to our desktop, meaning at our command line.

We need to change directories to our desktop so we can run this actual PY file.

Go ahead and open up your command line.

Since I'm on windows, I will open up a command prompt.

If you are on Mac OS or Linux, you'll open up a terminal, then you'll want to change directory to

your actual desktop or wherever you saved this file.

So type CD and then desktop.

To change directory to your desktop and then what you should be able to do is type out Python space

and then begin typing out the name of your file.

In my case, it was example dot pi and to prove to yourself that we're in the correct location, you

should be able to hit tab and it will autocomplete.

So here we say python.

My example Dot Pi and this is how you can run a dot pi script at your command line, hit enter and you

should be able to see Hello world.

Now you successfully created a Python script in your text editor and you ran that script at your command

line.

What you can also do is just type python by itself at your command line hit enter.

And this is a very simple direct connection to Python, allowing you to type Python code directly at

your command line.

We won't really be using this throughout your training because it's only one line at a time and eventually

we'll be using and learning about writing more than one line at a time for code.

But you can also just check it out type print.

Hello.

Enter and you'll notice you have hello as the output.

So this is basically one line at a time.

You can write Python code, then we can type quit open and close parentheses, hit enter and we've quit

out of the python interpreter.

All right, so we just learned how to actually run a Python script at your command line.

Now let's explore the Jupyter Notebook environment and see how that works.

To do so, we'll go to our Anaconda Navigator.

So search your computer for Anaconda Navigator.

Open that up.

And then once you've done that, go ahead and launch the Jupyter Notebook.

Once you click on that launch button, you should notice that your browser automatically opens up to

local host colon either eight, eight, eight, eight or eight, eight, eight, nine or some other

series of numbers.

Keep in mind that while Jupyter Notebook those operate inside of your browser, it does not require

an Internet connection.

Everything is happening locally.

There's no internet connection between Jupyter and some other server somewhere.

It just happens to open up and operate in your browser as a convenient graphical interface for you to

program in.

So once you launch Jupyter Notebook.

He'll notice that you can view all the files on your computer.

For example, we can click here on the desktop folder and now I can see that my example, Dot Pi script

we had just created earlier and using the Jupyter Notebook system, you can actually add on and edit

pie files.

So for example, we could add on another print statement here.

New and then save this change so we could say save and then we could also download or rename the file

and a bunch of other stuff.

But we're not going to be using Jupyter for this sort of text editing.

It's probably better to use Sublime Text Editor, but again, it's personal preference.

What we're really going to be using Jupyter Notebook Jupyter for is the notebook system.

So you can click here where it says New and under notebook.

You should see Python three.

Sometimes it says Conda route or something else, but click on what it says under notebook.

Typically it says Python three.

And then you'll notice that we just started a new notebook.

So let's have a quick overview of what this actually is.

Here it says Untitled.

And that's because this notebook that we just created doesn't actually have a title.

And if we click back here to this other tab, you'll notice we just created an untitled IP and B file

that stands for Python Notebook File.

Jupyter Notebooks used to be called Python notebooks, so they kept the file extension name.

And if we want to change this name, all we have to do is go back to this tab, select untitled and

give our notebook a new name.

So you will say my first notebook hit Enter and we've renamed The Notebook as well as the actual file.

You'll notice now it says my first notebook dot I Python notebook extension.

So coming back to this notebook, the notebook uses a cell based system, meaning you write code in

a cell, you run the cell and then see the actual output right below the cell.

So let's try running our simple print statement inside of a cell type print open, close parentheses.

Hello.

And you'll notice that Jupyter Autocomplete some things for you, such as quotes or parentheses.

And then we can run this cell so you can click here on the run button and it will run this cell and

you will see the output directly below.

This is a great system for people who are just starting to learn about Python because they can quickly

iterate and fix mistakes because they have their code and they can see the output directly.

They don't have to be constantly going to the command line and running their scripts again.

It's definitely a personal preference, but this is a nice feature of the notebook for people that are

learning Python and you'll notice that we automatically create another cell below.

Which you can type more python code in.

For example, print new and if you don't want to have to click that run button every time, all you

have to do is do shift enter and that will run a cell again.

That's shift enter to run a cell.

If you just hit enter by itself, you'll just create more new lines.

So it's shift enter to run a cell.

There's lots of other useful hotkeys where you can click on help and then hit keyboard shortcuts and

it will list all the keyboard shortcuts, the most useful ones we'll be teaching you later on, but

you can always explore that yourself.

Now, we also discussed that the notebook system can actually hold markdown text.

That is just normal text.

That is not code that you can just use for yourself to type out notes as you're learning throughout

this boot camp.

So if you click on a cell, you'll notice here it says code.

And that's because this is currently a python code cell.

If you want to make it into just a normal markdown cell, select from this dropdown markdown.

And now this is no longer a code cell.

It's just a cell that will just have normal text in it.

And you'll notice that it no longer has this in right in front of the cell.

So that also indicates that it's just for normal text.

So here you can write yourself.

Just note.

That will help you understand.

And if you do shift enter, it will then display them as just a normal text.

So again, this is no longer code, it's just text for yourself.

And a lot of the notebooks we provide throughout your training will have markdown text as explanation.

And if you ever want to write another code cell, you can just hit on a cell and then make sure that

it's selected code and you should be able to print whatever you want here, shift, enter to run it.

And that's the very basics.

We'll be talking a lot more about notebooks later on throughout your training, but that's really the

basics.

The last thing I want to note is that this special extension of the notebook file, this dot IP and

B means that you actually can't double click on this file on your computer and expect it to open.

So let me show you what I mean by that very quickly.

You'll notice that if I come to my desktop, I can see here my example dot pie, and if I double click

on this, it will actually open up in whatever default program I have for it.

Typically Sublime text editor or whatever other editors you have on your computer.

So you can double click on that PI files, edit them and work with them.

However, if you try double clicking on a dot IP and B file, you'll end up getting something asking

you How do you want to open this file?

Or it will just kind of open up and you'll just see a bunch of scrambled code.

That means that you can only open these special notebook files through the Jupyter Notebook system,

so you'll have to open up Anaconda Navigator, launch a Jupyter Notebook, and then actually find it

throughout your computer and click on it.

All right.

That's the very basics of running Python code.

It's time to actually learn Python.



---
[Previous](./7_Installing-Python-(Step-by-Step).md) | [Next](./9_Getting-the-Notebooks-and-the-Course-Material.md)
