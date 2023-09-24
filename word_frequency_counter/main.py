import argparse
from collections import defaultdict
import re


def read_and_count_word_frequency(input_file):
    """
       Read the contents of a file and count word frequency in the file.

       Parameters:
           input_file (file): The file object to be read.
       """
    input_data = input_file.read()
    count_word_frequency(input_data)


def count_word_frequency(input_data):
    """
      Count the frequency of words in the provided content.

      Parameters:
          input_data (str): The text content to be processed.
      """
    pattern = r'[()\[\]{}<>,�^":?/.\-\'=@]'
    words = re.sub(pattern, ' ', input_data).split()
    words = [word.lower() for word in words]
    word_frequency_map = defaultdict(int)

    for word in words:
        if not word.isnumeric():
            word_frequency_map[word] += 1
    print('Word\t\tFrequency')
    print("-" * 40)

    for word, frequency in word_frequency_map.items():
        print(f'{word}\t\t{frequency}')
    print("-" * 40)
    print(f'Total number of words: {len(word_frequency_map)}')


def main():
    """
      Parse command-line arguments, open the input file, and count word frequency in its content.

      This function utilizes the argparse module to handle command-line arguments.
      It opens the specified input text file using argparse.FileType with UTF-8 encoding and error handling.
      The content of the file is read, and the read_and_count_word_frequency function is called to count
      the frequency of words in the content.
      """

    parser = argparse.ArgumentParser(description='Count word frequency in a text file.')
    parser.add_argument('input_filename', type=argparse.FileType('r', encoding='utf-8', errors='replace'),
                        help='Path to the input text file')
    args = parser.parse_args()
    read_and_count_word_frequency(args.input_filename)


if __name__ == '__main__':
    main()
