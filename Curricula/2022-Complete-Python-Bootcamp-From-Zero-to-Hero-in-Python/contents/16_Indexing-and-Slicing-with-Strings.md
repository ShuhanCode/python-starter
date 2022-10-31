#  16. Indexing and Slicing with Strings

-   [00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

Welcome back, everybody.

In this lecture, we're going to continue right where we left off last time, but we'll be discussing

string indexing and slicing, indexing where we grab a single character and slicing where we grab a

subsection of that string.

Let's jump to the Jupyter Notebook and get started.

Okay, so to start this all off, I'm going to create a variable called my string and I'm going to set

it equal to the string.

Hello World.

So notice there's a space in there between hello world.

I run this and let's check to make sure okay so we have hello world they're ready to go now let's imagine

I wanted to grab a single character from this string.

In that case, I want to use indexing.

So what we do is we call the variable name.

We have square brackets off of it.

And let's imagine I wanted to grab the first character that is Capital H, then I pass in a zero because

indexing starts at zero and that allows me to return that first character.

H Let's try to grab another character.

Let's say we want to grab.

R So let's count this out my string and we want to count from zero.

So that's zero one, two, three, four, five.

So notice the space counts six, seven, eight so if I pass an eight there, it should return.

R Perfect.

So again, this is known as indexing.

Now, let's imagine we wanted to grab this letter l.

Well, there's two ways I could actually do this.

I could say my string at nine, because that's right after that.

Ah.

The other way I could do it is using the reverse indexing we previously mentioned.

So starting at zero from H, I can go backwards in the string so that D is negative one and that means

this L is negative two.

So if I say my string negative two, I will actually get back that l and then if I keep going backwards

in the string, I'll get back the R, which is right before the L, so I will get back this R right

there.

So you can use both positive index positions and negative index positions to grab elements or characters

from the string.

And that's really useful again, because oftentimes you'll have a variable string, maybe it's someone's

name, you don't know how big that name is, but for whatever reason, you want to grab the last letter

of the name, then you can always just use negative one.

And, you know, that's the last letter of the string.

Okay.

Let's go ahead and continue to discuss slicing.

So slicing is a little more complicated because we're grabbing a subsection of the string.

So that's more than one character typically.

Let's review our string.

Whoops, my string here is Hello World and I'm going to read the find my string just so this is a little

easier to follow as a b c d e f g h i j k so just kind of a string of the alphabet there.

We'll read the find it.

And now I have this string of the alphabet.

So let's imagine that we want it to grab a subsection of string that started a particular index and

then went all the way to the end.

Well, the way we could do that is we would say my string square bracket notation, and then we would

say the starting index.

Let's imagine we want to start at the letter C and then go all the way to the end.

So C is an index too because it's 012.

So what I do is I pass in two and if I just do that, it gives me back the letter C, but if I want

from C all the way to the end, I can say colon.

And that indicates starting at index to colon go all the way to the end.

And there we have cd all the way to K.

Okay.

Now, let's imagine kind of an opposite situation where I want to grab everything up to a particular

index.

Then I could say my string colon and let's say I want it to grab A, B and C.

So starting at the very beginning, go ahead and grab all the way up to essentially letter D here.

So we'll say zero one, two, three.

Passing three there and then we run this and we get back.

ABC Now this is sometimes confusing for students because if we check out my string.

Technically we have the RD index position three because it's zero one, two, three.

What you should note here is that the stop index this term right here for three, which only returns

back ABC that stop index is basically saying go up to but not including that index position.

So go up to the letter D but don't include it, which essentially says ABC.

So keep that in mind as you're kind of playing around with slice notation.

This stop is up too, but not including.

Okay.

Let's combine these two ideas of a starting index and a stop index by trying to grab a subsection of

string that's in the middle.

For example, let's try to grab D, e, f from the middle of the string.

The way we can do that is we say my string.

Open square brackets.

And then we start off with our starting index position.

In this case, it's at letter D, so that's zero one, two, three.

Then we say colon and then it's going to go up to the index position of G here because I just want d

f so we're going to go up to but not including.

G, so that's zero.

One, two, three, four, five, six.

And now if I run this, I get back d f So let's practice this one more time by trying to grab another

subsection of the string.

For example, let's try to grab just B and C these two letters, b, c so the way we can do that is

we'll type out my string.

Open and close square brackets are starting.

Index position is at zero one for B.

Colon and then it looks like we want to go up to but not including DH.

So that's zero one, two, three.

We'll run this and then we have B.C. and I would encourage you to try to grab a subsection, so choose

the subsection of the string and then see if you can grab it.

You can go ahead and pause the video and try that out.

To end our discussion.

Let's quickly discuss step size.

Let's imagine that I wanted to grab everything from the beginning of the string all the way to the end.

Well, technically that's just the string itself, but I could also use colon notation for this.

I could say colon colon.

And that basically says from all the way to the beginning, go all the way to the end.

Now, you don't often see this because you might as well just call the string itself, but this is technically

valid syntax.

The reason you might see something like this is if someone wanted to specify the third parameter and

that is the step size.

So right now we're saying go all the way from the beginning to the end and a step size of one, a,

b, c, d, e, f, g.

So that's the default step, size of one.

However, I can change that by providing a number such as two and that says go in jumps of two.

So from a go to C to E to G to I to K.

So if I run this, I get back a c, e, g, I k because I'm jumping in a step size of two and we can

increase this to be a step size of three and then we'll get from a jump to D, jump to G, jump to J,

and then there's no more letters to jump to because we're jumping in a larger step size.

So that's how step size works.

And you can combine this with a start and stop as well.

So we could say something like starting from index to go up to not including index seven and a step

size of two and we get back c e g so c then jump to E, then jump to G.

So notice how this all works in combination.

You have a start, a stop, and then a step size.

Something that you may commonly see is using a clever step trick to reverse a string.

And what you can do is say my string and then say from all the way to the beginning, all the way to

the end, take a step size of negative one.

And what that does is it actually reverses your string because you're saying from all the way to the

beginning to all the way to the end, go and take a backward step, which is then k j i all the way

to the end.

So this is kind of a little python trick.

Often in interviews people ask you to reverse a string and they kind of get annoyed by Python ISAs because

they quickly just do this nice kind of slick one liner instead of doing a for loop.

But I just want you to be aware of that.

Typically in our code we won't really be using this too much because it's more of a trick, but again,

a very useful one at that.

Okay.

So that's it for slicing and indexing.

Coming up next, we're going to discuss a little bit about some useful string properties.

We'll see it there.




---
[Previous](./15_Introduction-to-Strings.md) | [Next](./17_String-Properties-and-Methods.md)