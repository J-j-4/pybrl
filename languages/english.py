# -*- coding: utf-8 -*-

# English representation for Braille (Unified English - Grade 2)

from __future__ import unicode_literals

do_not_import = False       # Change this if you don't want it imported in the Braille translator

alphabet = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',

    'wh': '100011',
    'of': '111011',
    'ou': '110011',
    'ow': '010101',
    'sh': '100101',
    'st': '001100',
    'th': '100111',
    'ar': '001110',
    'ch': '100001',
    'ed': '110101',
    'en': '010001',
    'er': '110111',
    'gh': '110001',
    'in': '001010',

    'and': '111101',
    'for': '111111',
    'the': '011101',
    'with': '011111',

    'be-': '011000',
    'con-': '010010',
    'dis-': '010011',

    '-bb-': '011000',
    '-cc-': '010010',
    '-ea-': '010000',
    '-ff-': '011010',
    '-gg-': '011011',

    '-ing': '001101',
    '-self': '110100'
 }

contractions = {
    'but' : 'b',
    'can' : 'c',
    'do' : 'd',
    'every' : 'e',
    'from' : 'f',
    'go' : 'g',
    'have' : 'h',
    'just' : 'j',
    'knowledge' : 'k',
    'more' : 'm',
    'not' : 'n',
    'people' : 'p',
    'quite' : 'q',
    'rather' : 'r',
    'so' : 's',
    'that' : 't',
    'still' : 'st',
    'child' : 'ch',
    'us' : 'u',
    'very' : 'v',
    'it' : 'x',
    'you' : 'y',
    'as' : 'z',
    'shall' : 'sh',
    'this' : 'th',
    'which' : 'wh',
    'out' : 'ou',
    'will' : 'w',
    'be' : 'bb',
    'en' : 'enough',
    'to' : 'ff',
    'were' : 'gg',
    'was' : '”'
}

specialCharacters = {
    '!': '011010',
    '$dollar': '000100011100',
    '$quote_close': '001011',
    '$quote_open': '011001',
    '$single_quote_close': '001011001000',
    '$single_quote_open': '000001011001',
    '%accent': '000100',
    '%capital': '000001',
    '%emph': '000101',
    '%number': '001111',
    '%shape': '110101',
    '\'': '001000',
    '(': '000010110001',
    ')': '000010001110',
    ',': '010000',
    '-': '001001',
    '.': '010011',
    '/': '000111001100',
    ':': '010010',
    ';': '011000',
    '?': '011001',
    '[': '000001011011',
    ']': '011011001000',
    '€': '000100100010',
    '@': '000100100000'
}