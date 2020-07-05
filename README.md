# oiiotool
some scripts using oiio

remove 'Make' and 'Model' from some input image files:
```
docker run -it -v $PWD:$PWD -w $PWD oiiotool remove_spec.py input1.jpeg input2.jpeg ...
```