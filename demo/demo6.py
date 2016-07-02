#coding:utf-8
'''
Created on 2016-6-29

@author: gh


lengends = {('Poe','author'):(1809,1849,1991),
            ('Guudi','architect'):(1852,1906,1987),
            ('Freud','psychoanalyst'):(1856,1939,1990)}
for eachLegend in lengends:
    print 'Name: %s\t Occupation: %s' %eachLegend
    print 'Birth:%s\t Death:%s\t Album: %s\n'%lengends[eachLegend]
    '''
# f = open('test','r')
# longest = 0
# while True:
#     linelin = len(f.readline().strip())
#     if not linelin: break
#     if linelin > longest:
#         longest = linelin
# f.close()
# print longest
#    
# print  max(len(x.strip()) for x in open('test'))
# 
# print range(2,26+4,4)
for each in open('test','r').readlines():
    print each
    
    