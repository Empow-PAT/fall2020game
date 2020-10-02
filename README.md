PyGame Image Text
=================

This is a simple demo of a game in which a figure jumps up and down. Although
simple, it demonstrates many of the key aspects of a layered python module.

There are two ways to play, the "wave" way, in which the figure waves its arms,
and the "strobe" way, in which the figure changes color whenever it jumps. To
play, simply run:

```bash
python run.py [mode]
```

Installation
------------

To install the game, you need only clone the code from github, and then
you can the directory to your python path:

```bash
export PYTHONPATH=$PYTHONPATH:`pwd`
```

Testing
-------

To run tests, simply run
```bash
pytest tests
```

