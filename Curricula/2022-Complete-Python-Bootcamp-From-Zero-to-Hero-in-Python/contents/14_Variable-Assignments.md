#  14. Variable Assignments

-   [00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

Welcome back, everybody.

In this lecture, we're going to be discussing variable assignments.

Now we just saw how to work with numbers, but what do these numbers actually represent?

We had integers and floating point numbers, but we don't actually have a variable name assigned to

them.

So it'd be nice if we can assign these particular data types a variable name to easily reference them

later on in our code.

For example, I could say a variable name.

My underscore dog's is equal to two because I have two dogs.

Now there are a couple of rules for choosing a variable name in Python, and these rules are that names

cannot start a phone number.

There can also be no spaces in the variable name, so you should use an underscore instead.

And you also can't have any of these symbols in a name.

And if you actually forget this list of symbols, if you were to type one of these symbols out in a

variable name, Python will quickly complain and you'd have an error.

So you don't need to worry about memorizing all these.

You'd get the error as you're typing along.

A few more rules about variable names.

It's generally considered best practice according to Pep eight that names are lowercase.

Now there are situations when you become a more advanced programmer where you're going to want to have

kind of global variable names in all caps that are used throughout your code.

But right now, in general, we want to keep all our names lowercase and we'll also want to avoid words

that have a special meaning in Python.

And these are built in keywords like list or STR for string.

You may be wondering, well, how the heck am I supposed to know?

What are the special built in keywords?

Luckily, any development environment that's designed to work with Python will have syntax highlighting

that will alert you that you're using a built in keyword by highlighting it a different color.

And we'll see an example of that in just a little bit.

Before we actually jump to the Jupyter Notebook, though, I want to mention that Python uses dynamic

typing and this means you can reassign variables to different data types.

And this makes Python very flexible in assigning data types, and that's actually different than many

other programming languages that are statically typed.

So let me show you an example of what I mean by this.

In Python.

Something like this is totally okay.

Here I have assigned my dog's variable name equal to two.

And then later on in my code I went ahead and reassigned the same variable name my dogs to a completely

different data type A list, Sammy and Frankie.

Now that's totally okay in Python, but in other languages that would produce an error.

And that's because these other languages are statically typed.

Meaning.

And the other language such as C++, you'd have to say int for integer and then say my dog is equal

to whatever integer value you want, such as one, and then later on in your code you would not be able

to assign it a different data type.

You would not be able to say My dog is equal to Sammy because that's no longer an integer.

Now would result in an error.

So there are some pros and cons to dynamic typing and python the pros is that not having to write out

the actual data type saves you a lot of time and makes it really easy to quickly produce python code.

And it also makes your code very readable because you're just reading that variable name.

Now, this is kind of a double edged sword here because the cons is that this may result in bugs for

unexpected data type, because you're not having these restrictions of data types, especially when

you're dealing with user input.

You may have unexpected data types show up and that can cause problems later on in your operations.

So you should be aware of the data types as you're coding and you can use the special type function

that's built into Python to quickly check the type of any variable.

And we'll show you how to use that in just a little bit.

All right, let's explore all these concepts by jumping to a Jupyter Notebook.

Okay.

Now that we've seen how to use numbers in Python as a calculator, let's see how we can assign names

and create variables.

We're first going to create a very simple variable called A and set it equal to five.

And now that I've run that anywhere in my code, when I call a it's now assign the variable five and

I can reassign it simply by saying A is then equal to something else like ten.

And now if I check A it has ten there and I can also add now objects together.

I could say a plus a and that's going to result in 20 because ten plus ten is equal to 20.

And Python also allows you to do reassignments with a reference to the same object.

Let me show you what I mean by that.

I could say a which is still equal to ten.

I could reassign it to be say something like a is equal to a plus a so what that is saying is take the

current value of a which is ten and reassign it to a plus A So that's ten plus ten.

So after I run this.

A is now going to be equal to 20.

And keep in mind, if I were to run this cell a second time, so notice the inner operator here, it's

going to go from 40 to 42.

If I run a again, it's 40 now and you can keep doing this again and again and you'll keep seeing it

essentially double each time.

So keep that in mind.

This is a little different than in a script environment.

If you're running a PI script, you won't really see that effect because you'll just have that line.

Once in a cell environment, you'd have to run that cell over and over again.

So let's imagine that we don't know what type is a what you can do is use the built in type function.

So that's t p have open and close parentheses and we'll learn how to create our own functions later

on.

But passing the variable there do shift enter and you'll get back.

Python's built in keyword for what the type is, and in this case it's int because it's an integer,

let's reassign it to be a floating point number.

So we'll say 30.1.

Let's check the type of that type of a and it returns back that float.

So these are the same keywords that we saw when we discussed that table of basic data types.

Now, as you previously mentioned, you want to avoid using built in Python keywords as variable names.

And the way you could know if that's happening or not is, let's say I wanted to start assigning INT

equal to four.

So notice what's happening here.

I have syntax highlighting on int and I didn't get that before with a so that means that int here is

a special built in keyword and you shouldn't use it for something like this.

So if you ever see that your variable name is having some special highlighting that a normal variable

name doesn't have, then you should avoid using this.

So definitely don't ever run that.

And if you accidentally ran that as you were following along, or maybe you made some other reassignment

mistake, you can always come here to kernel and select restart the kernel and that will restart the

kernel and it will kind of delete all the variables.

So all variables will be lost.

So if you ever have some weird kind of error happening because you reassign something like list or int,

you can hit restart here, it will restart the kernel and then you'll need to run these cells again

if you ever want to define anything.

Because if we say a here, you'll say, hey, a is not defined, so you need to rerun these cells and

then you have five again.

So last thing I want to note is a simple example where we use variable names.

So I will say my income is equal to 100.

And then in the cell, I will say my tax rate is let's say I have a 10% tax rate.

So 0.1 and I want to figure out what my total taxes paid are.

I will say my taxes is equal to.

My income times.

My tax rate.

So I have that.

And let's check what my taxes are.

How much do I owe?

I'll check my taxes.

And there I have 10.0.

So now I can perform logic with variable names.

And this is a lot more readable than just using integers or floating point numbers because now I have

this nice almost English sentence that says my taxes is equal to my income times my tax rate.

Okay, so we've learned some basic numbers in Python.

We've learned how to do arithmetic, and we've wrapped it up by learning how to do variable assignment

in Python.

Up next, we're going to learn about strings.

I'll see you there.





---
[Previous](./13_Numbers-FAQ.md) | [Next](.)