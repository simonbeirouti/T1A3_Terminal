# T1A3 Terminal Application

| Github                                                 | Notion                                                                                                    |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| [Repo](https://github.com/simonbeirouti/T1A3_Terminal) | [Kanban](https://besimon.notion.site/483391bf4cea4922b3cd61c5d57a4969?v=b42e837be2394dea8150f42f5dac8c58) |

## Coding style

For the coding style, I am using the [Black](https://github.com/psf/black) formatter. It is built into Visual Studio via [this plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter). The benefits of this is it returns an error if you don't do what it likes.

## Installation steps

1. `git clone https://github.com/simonbeirouti/T1A3_Terminal.git`
2. `cd T1A3_Terminal`
3. `pip3 install rich`
4. `chmod u+x run_first.sh`
5. `./run_first.sh`

## Features

#### Automation

Instead of running three files, I created a bash script that will run each one, one after another.

#### Usage of the rich command line pacakge

The focus around this was to use a python library that enables the developer to create a more exciting UX.

#### Working with files

I am wanting to work off generated files and also append further files with more information when it comes through.

## ELI5

1. Run a script that runs `cards.py` to create a deck of 52 cards.
2. Run the `error_checker.py` to make sure there are 52 cards.
3. Let the player choose a wager between 1 - 3. If anything else is entered, it will default to 2.
4. Load the card file and randomly pick two cards.
5. Deal two cards to both players.
6. Display a table with the results.
   - Announce the winner.
   - Add winning tally to either player or opponent.
   - Print result to `./files/results.txt`
7. Ask if the player wants to continue.
   - If yes, empty the values and run again.
     - Will offer option again until someone has no balance left.
   - If no, it will exit the game.

## Video

![video here](./recording.gif)
