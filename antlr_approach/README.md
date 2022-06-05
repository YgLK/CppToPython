--------------------------------------
    ANTLR
-------------------------------------

Example: https://faun.pub/introduction-to-antlr-python-af8a3c603d23

1. Installation:
   ANTLR4 install command:
   `pip install antlr4-python3-runtime==4.7.2`
   Warning! Only 4.7.2 version works with this project.
2. Build project (IDK if it's necessary at this point):
   antlr4 -Dlanguage=Python3 Hello.g4 -visitor -o dist



3. How to run project in Pycharm:
   1. Go to Hello.g4 file.
   2. Right-click on the 'program' production
   3. CLick 'Test rule program'
   4. Provide input and test if rule works fine.


Btw. Main file is copied from sample project, so it needs to be fixed.