A=[-0.5 -0.1;0 -0.3];
setlmis([]);
X=lmivar(1,[2 1]);

lmiterm([1 1 1 X],1,A,'s');

lmis=getlmis;
[tmin,xfeas]=feasp(lmis);
XX=dec2mat(lmis,xfeas,X);
X;
XX
eig(XX);
XX*A+A'*XX
