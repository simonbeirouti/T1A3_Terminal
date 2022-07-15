# T1A3 Terminal Application

| Github                                                 | Notion                                                                                                    |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| [Repo](https://github.com/simonbeirouti/T1A3_Terminal) | [Kanban](https://besimon.notion.site/483391bf4cea4922b3cd61c5d57a4969?v=b42e837be2394dea8150f42f5dac8c58) |

## Coding style

For the coding style, I am using the [Black](https://github.com/psf/black) formatter. It is built into Visual Studio via [this plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter). The benefits of this is it returns an error if you don't do what it likes.

## Installation steps

1. `git clone https://github.com/simonbeirouti/T1A3_Terminal.git`
2. `cd into T1A3_Terminal`
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

## Implementation plan

- Launch bash script to run python file and generate a csv of the cards to use in program // DONE
- Ask for the user name
  - Welcome them
- Let them know what game they'll be playing
  - Show some basic rules
  - Hand rankings
- Give player some money
  - Generate a random two cards for player and component
  - Remove the cards from the total available cards
- Ask how much they want to bet
- Deal the board
  - Compare the results.
  - Append score to a doc
- Either reward to deduct from score
  - If user reaches 0, show a bitcoin address for lols
  - Don't stop the game until the player ends it
- Handle errors throughout
  - Check if there are 52 cards in the deck
