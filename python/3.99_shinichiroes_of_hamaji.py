i=99;s=', %s.\n'
f=lambda i:'%d shinichiro%s of hamaji on the wall'%(i,'es'[:i*2-2])
while i:print f(i)+s%f(i)[:-12]+{1:'Go to the store and buy some more'+s%f(99)}.get(i,'Take one down and pass it around'+s%f(i-1));i-=1
