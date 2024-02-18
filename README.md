# Number-generator
This Python project provides a number generator that yields numbers divisible by both 5 and 7 within a given range.

FILES:
generator.py: Contains the num_generator function that generates the desired numbers.
main_g.py: Reads an input value from a file, calls the generator, and prints the results.
Test_generator.py: Includes unit tests for the num_generator function.

Usage:
Ensure you have Python installed.
Clone this repository or download the files.
Create an input file named input.txt in the input directory. The file should contain a single integer representing the upper limit of the range.
Run main_g.py to generate and display the desired numbers.

Example:
Suppose input.txt contains the value 100. Running main_g.py will output:0,35,70

Unit Tests:
To verify the correctness of the num_generator function, run the unit tests in Test_generator.py. These tests cover various scenarios, including valid input, negative input, zero input, and large input.
