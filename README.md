# Staalmeesters
In this repository you can find different algorithms that try to solve a two-dimensional strip packing problem. In a
two-dimensional packing problem there is a given width and the objective is to pack a set of rectangles within a 
minimum length. The 'Staalmeesters' is a problem whereby we (the steel cutting company) get orders from clients with
sets of rectangles, varying in length and width. The 'staalmeesters' have three rolls of steel at their disposal with various (extra) attributes, width and prizing. Since the buyer wants a minimum price, the sheets in each order need to be cut while minimizing the length of used roll. The price of an order depends on the length of roll that is necessary to cut all sheets. 

## Prerequisites
To use, and experiment with, the scripts in this repository a few things are required. The python scripts are written in python 3. You can download [python here](https://www.python.org/downloads/)
1. Click 'download python 3.6.3' in the yellow bar 
2. Open download file
3. Follow instructions with default settings or tweak if you are a knowledgeable user. 

Furthermore, in the scripts there are several packages used. We advise you to download anaconda or something alike which includes almost every available package for python. This way you are not missing out of useful packages. You can download [anaconda here](https://conda.io/docs/user-guide/install/download.html).
1. Click 'Download Anaconda - free'
2. Select your operating system: Windows, macOS or Linux
3. Click 'download' for the python 3.6 version
4. Open download file
5. Follow instructions with default settings or tweak if you are a knowledgeable user.

From anaconda you will need at least the numpy and matplotlib package. 

## Usage
**Directory explanation**

Staalmeesters contains three main directories; Code, Literature and Progress. The usage of the directory Code will be further explained in 'running tests'. In Literature, you can find papers adressing similar problems. We have read these papers to get a better understanding of the problem at hand and to get useful ideas for algorithms. In Progress we post our notes from tech intervision and the weekly goals we set up at the beginning of the course. In Progress there is another directory named TestFigures, in TestFigures we have posted first figures with results. These are not the end visualisation. 

**Running tests** 

The scripts necessary to run the test and to see which algorithm works the best for an order are stored in the directory: Code. Here you'll find the main scripts for each algorithm and the supporting files. Load_orders is a file mainly consisting of an list of lists in which all orders are stored. Each order can also be summoned using the load_orders file. In classes information about each order can be stored. And lastly helper is a file that contains every function used in the algorithms. Reading through the scripts indicates how each algorithm can be tweaked or used for a certain order. The default setting for each algorithm is order 1 as order and sort_long as sorting method. 

## Built with
- [Python 3](https://www.python.org/downloads/) - The programming language

- [PyCharm](https://www.jetbrains.com/pycharm/) - Used to write scripts in

- [Sublime](https://www.sublimetext.com/) - Used to write scripts in

## Authors
Bastiaanse, Morena

Bisseling, Milou

Bouma, Leonie

## Acknowledgments
Nicole Silverio - for providing useful feedback and ideas during tech intervision

Daan van den Berg - for providing useful feedback on our presentation skills and for the helpful lectures








