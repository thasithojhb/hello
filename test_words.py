import unittest

import word_processor

class Mytestcase(unittest.TestCase):

    def test_convert_to_word_list(self):
        results = word_processor.convert_to_word_list("Hello; How, you doing? Its been long.")
        self.assertEqual(['hello','how','you','doing','its','been','long'],results)
    
    def test_words_longer_than(self):
        results = word_processor.words_longer_than(4,'Hello; How, you doing? Its been long.')
        self.assertEqual(['hello', 'doing'], results)
    def test_words_lengths_map(self):
        results = word_processor.words_lengths_map('Hello; How, you doing? Its been long.')
        self.assertEqual({3:3,4:2,5:2},results)
    def test_letters_count_map(self):
        results = word_processor.letters_count_map('Hello; How, you doing? Its been long.')
        self.assertEqual({'a':0,'b':1,'c':0,'d':1,'e':3,'f':0,'g':2,'h':2,'i':2,'j':0,'k':0,'l':3,'m':0,'n':3,
        'o':5,'p':0,'q':0,'r':0,'s':1,'t':1,'u':1,'v':0,'w':1,'x':0,'y':1,'z':0},results)
    def test_most_used_character(self):
        results = word_processor.most_used_character('Hello; How, you doing? Its been long.')
        self.assertEqual('o',results)