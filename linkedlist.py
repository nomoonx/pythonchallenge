import urllib2,re
pattern=re.compile(r"\d+");
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";
number="63579";
while True:
  a=urllib2.urlopen(url+number);
  b=a.read();
  print b;
  c=pattern.findall(b);
  number=c[0];

