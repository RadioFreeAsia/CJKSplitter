# -*- encoding: UTF-8 -*-

from CJKSplitter import CJKSplitter

words = ['知识库－招聘资料', '大学生']
for word in words:
       print '=====now test:', word
       u = unicode(word, 'utf8').encode('utf8')
       s = CJKSplitter()
       print 'no glob result:'
       for i in s.process([u]):
           print i.encode('utf8')

       print 'glob result:'
       for i in s.process([u], 1):
           print i.encode('utf8')

