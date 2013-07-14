a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
a="/pc/def/map.html";
length=len(a);
b="";
for i in range(0,length-1):
  c=ord(a[i]);
  if c>=97 and c<=122:
    b+=chr((c-95)%26+97);
  else:
    b+=a[i];
print b;
