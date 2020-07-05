# oiiotool
some scripts using oiio

remove 'Make' and 'Model' from some input image files:
```
docker run -it -v $PWD:$PWD -w $PWD oiiotool remove_spec.py input1.jpeg input2.jpeg ...
```

TODO:
 change to use URL to download the whl file. I fogot where I get it at this moment.