#  17. String Properties and Methods

-   [00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

**Note**

-   `String.prototype.split() - javascript`
```
const str = 'The quick brown fox jumps over the lazy dog.';

const words = str.split(' ');
console.log(words);
// expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

const chars = str.split('');
console.log(chars);
// expected output: ["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "t", "h", "e", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."]

const strCopy = str.split();
console.log(strCopy);
// expected output: Array ["The quick brown fox jumps over the lazy dog."]

```

-   `Python`
```
const my_str = 'The quick brown fox jumps over the lazy dog.';

const words = my_str.split();
print(words);
// expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
```


Welcome back, everyone.

In this lecture, we're going to finish off our discussion about strings by talking about string properties

and string methods.

Let's jump to a notebook and get started.

The first thing we're going to discuss is the immutability of strings and immutability.

It stems from the word mutate, basically means mutate or you cannot mutate or cannot change.

I'm going to show you an example of this.

Let's create a variable called name and set it equal to Sam.

Now let's imagine you want to change this name to Pam.

So change the se for a p.

Well, you may think that you would do something like this.

Say name index at zero and then just set it equal to P.

Now for strings, unfortunately, you can't do this.

If you try to run this code, you'll get an error because strings are immutable, meaning a string object

or str object doesn't support item assignment.

So you can't grab one of these characters, one of these elements in the string and then try to reassign

it this way.

Strings just don't work that way in Python.

Later on, we'll learn about other data types that do support item assignment.

All this means is that if we do want to reassign this s to be a P, we basically have to create a new

string and we can do that with concatenation that is kind of merging two strings together.

So I'm going to comment this out and to create a comment, you just put a hash tag in front of it,

and if you run this, you won't get anything out.

So basically anything of a hash tag, it just commented code that doesn't get run.

Let's explore this example of trying to create the string Pam using what we already have about name.

So the first thing we want to do is try to grab a and m.

So let's use the slice notation that we learned about earlier.

We're going to start at index one and then go all the way to the end.

So let's check that.

So that's am perfect.

So we'll assign this to something like last.

Letters is equal to name one all the way to the end.

So then if I take a look at last letters again, I can use tab to autocomplete here.

It says AM and now what I can do is I can concatenate P to last letters.

And the way you do that is with the plus sign.

So we can say P.

Plus.

Last letters and then we get Pam.

So this is known as string concatenation.

Let's explore a couple more examples.

I'm going to say X is equal to.

Hello World.

And then I could say X plus.

It is beautiful.

Outside.

And then if I run this, I can see hello world.

It is beautiful outside.

Something to keep in mind is note that there's no space here because there was no space at the end of

world and there's no space at the beginning of it.

So it would be nice is if you add a little space there.

So when you run this again hello world, it is beautiful outside.

Now if I do this multiple times with a reassignment so I could say x is equal to x plus, it is beautiful

outside.

Now when I run this I've read the find x so I can see now.

Hello world.

It is beautiful outside.

If I accidentally ran this cell more than one time I add in it is beautiful outside a second time.

So if I run this again, notice how my in numbers are going to change right next to the cell.

Now it says hello world.

It is beautiful outside.

It is beautiful outside and we can keep doing this and you keep adding it on.

So this is string concatenation and it allows you to quickly put strings together.

There's also a multiplication you could do to kind of do multiple string concatenation at once.

Let me show you what that looks like.

So so far, we've used the plus sign to kind of concatenate two strings together or merge them together.

But if you had the letter.

Equal to Z.

And you quickly wanted ten Zs.

What you could do is say letter times ten, and there you could see essentially someone sleeping.

Here is the easy, easy Z ten times.

So that's using multiplication of letters and then that's using a plus sign of letters.

Something to keep in mind when you're performing string concatenation or string multiplication is that

you're going to get errors if you try to concatenate a number with a string.

I want to show you what I mean by that.

Imagine we're doing two plus three.

If we run this, we get five.

That makes sense.

If we do two, the string two plus the string three.

Now that they're strings, it's not going to add them together.

Instead, it's going to perform concatenation.

So here now we get back the string 23 and this is a callback to dynamic typing where we had to be really

careful about the data types.

So keep this sort of problem in mind that your user may end up putting in strings, and then later on

in your code, if you start adding them together, you may end up with an unexpected result, like 23

instead of five.

So this is a really prime example of both the good and bad of Python's ability to be very flexible.

So it's very flexible, meaning you're not getting an error here, but maybe it's a little too flexible

because you expect that five and it gave you back 23.

Later on, we're going to learn about a lot more ways that we can kind of prevent these sort of mistakes

or errors.

Let's continue on by discussing some built in string methods.

So objects in Python usually have built in methods, and these methods themselves are essentially functions

that are inside the object.

And later on, we're going to learn how to create our own functions and our own methods.

For right now, let's go over just a few useful methods.

I'm going to create a new string.

Let's call it X and say it's hello world.

And if I hit x dot and then hit tab, I should see this list pop out in the Jupyter Notebook.

And this is a list of all the attributes and methods that are available on this string object.

Now again, make sure you've already defined X, otherwise you won't see anything.

So make sure you ran that cell that says X Hello world and then you sell, say x dot hit tab and you

should see this list.

So as you can see, there's tons of methods here and we're not going to go over all of them right now.

We're just going to go over the most useful ones that you'll be using later on in this course.

So, so quickly, uppercase everything in a string.

You can say upper open and close parentheses, and it will uppercase everything in the string.

Keep in mind this method is not in place.

That is to say it doesn't actually affect the original string.

If you did want it to affect the original string, you'd have to reassign it.

You'd have to do something like X is equal to the upper version case of X.

So keep that in mind.

I'm not going to run that right now because I want the original X string and if you accidentally do

the reassignment, you can always just say X equals helloworld again.

All right, so we have the upper method.

Something that's really common for beginners as a mistake to make is that the accidentally just do upper

and they forget those open and close parentheses.

And if you run this, it'll just say, hey, this is a function string dot upper.

And basically what Python is saying is, oh, you haven't actually executed this method or function

yet.

Instead you just asked me what it was.

So when you call it without open and close parentheses and you get something that looks like this back,

it means that you haven't actually executed that method or function to occur.

Instead, you just kind of ask Python, Hey, what is this?

So because there's an upper method, there's also a lower method which is going to lowercase every letter

notice here.

Now H and W are lowercase.

Then there's also the split method.

And the split method allows you to quickly create a list off of a string.

So here we can say we have Hello and world.

Now we haven't really discussed lists yet, so they are coming up.

So all I want you to think about right now is that if I use dot split, it will split a string based

on the white space or based on the letter you pass in.

So let me show you what I mean by that.

So I will say X is equal to high.

This is a string.

Run that.

And then if I say X dot split.

I get back everything split by the white space, so I get high.

This is a string nicely organized in a list, however, I could pass in any sequence of characters that

I want to split on.

So by default, split, we'll split on the white space.

But I could actually split it on any letter I want.

So now it's going to split on the ISE.

So if I run this, we should get an interesting result.

And here it's essentially removed all the eyes because it's splitting on them and now the white space

is included.

So I get H and because there's an I there, it removes it and then gets everything until the next I

so space t h and then there's an I there removes it gets everything until the next I, which is an S

space.

So notice that's here and then so on again, another eye and a big portion of string get an I and then

an end G.

So that's how you can use split to quickly create a list out of a string.

And we're going to be covering lists in a lot more detail later on.

OC coming up next we're going to talk about is string formatting for printing.

There's a lot of useful methods you can use to quickly print out other objects along with your strings.

So far, we've only learned how to use print as a basic function where we say print hello.

But there's a lot more power to the print function that we haven't actually seen yet, as well as the

DOT format method.

So let's go ahead and cover that in the next lecture.

We'll see you there.

---
[Previous](./16_Indexing-and-Slicing-with-Strings.md) | [Next](./18_Strings-FAQ.md)