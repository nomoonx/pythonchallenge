import urllib2,pickle
a=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p");
b=a.read();
object=pickle.loads(b);
for line in object:
  print ''.join(map(lambda pair: pair[0]*pair[1], line))
