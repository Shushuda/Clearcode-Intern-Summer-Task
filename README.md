
# Get Them Memes

A simple **Python class** for getting the most delicious and valuable memes that can fit into your pendrive.

Solves a 0-1 Knapsack problem with a Dynamic Programming algorithm.
The solution should run in O(nW) time and O(nW) space, where n is the number of items and W is the capacity. 
Please refer to [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem) for a very detailed and confusing explanation of how it works.

Done for **Clearcode** as a recruitment task for a **Summer Python Intern** position.

## Getting Started

Download the files as-is or simply clone the repository. Then, import the *calculate* function from *main.py* file and you're good to go!

### Prerequisites

This project uses:

```
Python 3.7
```

as well as following packages:

```
NumPy
```
### How it works

Execute the function with data of following format:

```
usb_size = 1    # size of your pendrive in GB

# a list of 3-element tuples, each with the name, size in MB, and price in caps
memes = [
    ('dolan.jpg', 126, 6),
    ('sad_pepe.png', 221, 10),
    ('t-series.avi', 522, 12),
]
```

Input would look like this:

```
calculate(usb_size, memes)
```
And output would give us this:
```
(28, {'dolan.jpg', 't-series.avi', 'sad_pepe.png'})
```

Perfect memes of the best possible value!

## Running the tests

The class was tested using **unittest** built-in module.

You can run these tests by typing this into terminal:
```
>python test_main.py
```
## Author

* **Weronika Sikora** - [Shushuda](https://github.com/Shushuda)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgements

* [PurpleBooth](https://gist.github.com/PurpleBooth) for creating this amazing README template
