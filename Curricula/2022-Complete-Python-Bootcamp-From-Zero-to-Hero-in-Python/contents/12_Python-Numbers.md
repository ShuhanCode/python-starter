# 12. Python Numbers

-   [00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

Hey, everyone, welcome back to this lecture on numbers in Python.

We already briefly mentioned that there's two main number types that we're going to be working with

throughout the course, and that is integers, which are whole numbers and floating point numbers,

which are numbers of a decimal.

We're going to be exploring a little bit of basic math with Python, and then we'll also discuss how

to create variables and assign them values.

Let's open up a Jupyter Notebook and get started.

All right.

So before we actually start typing any code, I wanted to briefly mention that if you ever want to toggle

this toolbar or this header on or off, you can just come here, click view and then select toggle header

or toggle toolbar to turn them on or off.

And typically during the lectures I'll have them off.

So we have as much space for coding as possible.

Let's start off by just going over some basic math, which is pretty straightforward, and it's basically

just using Python as a calculator.

If you want to do additions, it's just an addition sign or a plus sign, two plus one.

If you want to do subtraction, that's just a dash or a minus sign to minus one.

You can use an asterisk for multiplication.

So two times two, and if you want to perform division, that's just a forward slash.

So three divided by two is 1.5.

Okay.

Now let's take a little bit of time to discuss a mathematical operation that you may not have seen before.

It's the modulo or mod operator.

And basically what this does, it returns back the remainder after a division.

For example, if we were to do seven divided by four, we get back 1.75.

And if you were to do this kind of using an elementary school mathematics, you would say seven divided

by four four goes into seven one time with a remainder of three because four plus three is seven.

Let's imagine you actually just wanted to know that remainder the actual number three.

In that case, you can use the MOD operator, which is a percent sine.

So we're going to say seven mod four and it returns back three because seven divided by four, it goes

in one time evenly with a remainder of three.

So for example, we could do 50.

Mod five and if five goes into 50 evenly, then we get back a remainder of zero, which is nice because

it's a way to check if a number is evenly divisible by another number.

That's a really convenient check when you want to check if a number is even or not.

So let's imagine we have an odd number 23 and we want to know if it's even or odd.

Well, I could just look at it, but maybe some time in my code it's disguised as the variable and I

really need to quickly check if it's even or odd.

One way I could do this is simply with a mod two and I know that if mod two results in something other

than zero, then we have an odd number.

Because if I have an even number then when you divide it by two, there should be no remainder or the

remainder should be zero.

So that's the MOD operator again.

It just gives you the back the remainder after you perform a division.

Let's continue with everything else about arithmetic.

You can also perform powers so you can do something like two to the power of three.

So that's just two asterisk signs in a row.

So to the power of three, that's eight.

And then we can also perform order of operations.

Let's imagine that I have the following equation two plus ten multiplied by ten.

Plus three.

If I run that code, I get back 105.

But what if I wanted to actually have two plus ten occur first, then multiply that by the result of

ten plus three.

Right now we're following basic order of operations with math, which is going to perform this multiplication

first before it does this addition.

So it's performing ten times ten, 100 plus two plus three.

So tap our operations happen first the way we want them.

We can use parentheses.

I can say two plus ten multiplied by and in parentheses.

Ten plus three.

And if I run that, I get back 156 the way I want it.

Okay.

So that's the basics of arithmetic and using Python as a calculator.

Hopefully, it was pretty straightforward.

Coming up next, we're going to expand on this by showing you how you can perform variable assignments,

that is to create your own variable name and then assign an object to it.

We'll see you there at the next lecture.




---
[Previous](./11_Introduction-to-Python-Data-Types.md) | [Next](./13_Numbers-FAQ.md)
