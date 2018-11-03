﻿# -*- coding: utf-8 -*-
from pythainlp.change import texttoeng, texttothai
from pythainlp.collation import collate
from pythainlp.date import now
from pythainlp.keywords import find_keyword
from pythainlp.rank import rank
from pythainlp.romanization import romanize
from pythainlp.sentiment import sentiment
from pythainlp.soundex import lk82, metasound, udom83
from pythainlp.spell import spell
from pythainlp.tag import pos_tag
from pythainlp.tokenize import etcc, sent_tokenize, tcc, word_tokenize
from pythainlp.util import bigrams, trigrams


thai_alphabets = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"  # 44 chars
thai_numbers = "๐๑๒๓๔๕๖๗๘๙"  # 10
thai_symbols = "ฯ\u0e3a฿ๆ\u0e47\u0e4c\u0e4d\u0e4e\u0e4f\u0e5a\u0e5b"  # 11
thai_tonemarks = "\u0e48\u0e49\u0e4a\u0e4b"  # 4
thai_vowels = "ฤฦะ\u0e31าำ\u0e34\u0e35\u0e36\u0e37\u0e38\u0e39เแโใไ\u0e45"  # 18
thai_characters = "".join(
    [thai_alphabets, thai_vowels, thai_tonemarks, thai_symbols]
)  # 77

__version__ = 1.7
