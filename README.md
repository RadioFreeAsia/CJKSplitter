CJKSplitter - Chinese, Japanese, Korean word splitter for ZCTextIndex
=============================================================================

CJKSplitter is a ZCTextIndex splitter for CJK (Chinese-Japenese-Korea) text
stored as Unicode.  It uses a simple, but workable, "hack" instead of trying
to do real word splitting from dictionaries.  Compared to a dictionary based
word splitter, this results in a bigger index and more matches than necessary,
but it is a cheap price to pay for the reduced complexity.

Features
--------

- Uses regular expressions,  compatible with the default English white space
  splitter.

- Much simpler code, easier to install, easier to use.

- Support for multiple encodings (unicode/utf-8/gb18030/gbk/gb2312/mbcs/big5)
  provided by 3 splitters  (more to come):

  * 'CJK splitter': supports unicode/utf-8 encoding. This encoding is
    compatible with version 0.1

  * 'CJK GB splitter': supports unicode/gb18030/gbk/gb2312/mbcs encodings.

  * 'CJK BIG5 splitter': supports unicode/big5/mbcs encodings

- Smaller index storage for CJK: index stored as unicode(2 bytes) rather than
  utf-8(3 bytes)

- Supports English globbing.

- Supports single Chinese charactor search.

About ZOpen
-----------

ZOpen is a professional Zope/Plone consulting company located in Shanghai,
China. We are also the supporter for CZUG.org (China Zope User Group). 
We are trying to make Zope/CMF/Plone works for the Chinese people. 

Contact us with : panjy@zopen.cn
