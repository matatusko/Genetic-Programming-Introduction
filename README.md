# Introduction to Genetic Programming

Ok, maybe introduction is a slightly misleading name, but I'm going through different tutorials and exercises on genetic programming 
and dropping all the notebooks here. Some people might find it useful - if you're a pro with GP then don't even bother - for a while
it will only contain some simple stuff with explanations, mostly written for me. Just thought some people would enjoy it as well :)

# List of notebooks

Here I'll list all the notebooks and the relevant information to each single one, including a brief description of a project and what inspired me to write that code in particular.

Note: I'm having troubles loading up the notebooks I've uploaded here on github, and it appears it's github at fault as others report similar problems. If you get the error message 'Sorry, something went wrong. Reload?', please use [nbviewer](https://nbviewer.jupyter.org/) to load up Jupyter notebook.

### 1 - String Reproduction

Use genetic programming to recreate a given string. Code heavily inspired by the [first tutorial](https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9) on GP I've went through by Louis Nicolle. Really well written so I would highly recommend having a read. I've editted a couple of thing here and there, but mostly is the same thing.

### 2 - Maximizing function

Inspired by Ahmed Gad's [blog post](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6). Basically the idea is to have genetic algorithm to learn the weights in order to maximize a function given 6 inputs. Or, in other words, to see if GA is able to figure out that multiplying positive numbers with high weights will yield higher results, but negative numbers should be multiplied by smaller and also negative number.
