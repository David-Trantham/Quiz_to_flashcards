# Quiz text to anki flashcard import converter
The idea behind this project is to convert quiz results into a format that's importable by anki.
## Capabilities
- Read from a file
- Make list of modifications that need to happen to the text
- Send to output to a file contained within the "output" folder
## Usage
* Make an "input" folder to place the ".txt" files to be turned into flash cards
* On website, select from the title at the top all the way to the bottom of the final question, and copy
* Paste into the text file you've created in the input folder
* Make sure that you find and replace all Quotation marks into single quotes; otherwise they will cause issues
* When main.py is run, all the text files will be turned into flashcards in the "output" folder