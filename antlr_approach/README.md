### ANTLR

Example: https://faun.pub/introduction-to-antlr-python-af8a3c603d23

1. Installation: <br>
   ANTLR4 install command:<br>
   `pip install antlr4-python3-runtime==4.7.2`<br>
   Warning! Only 4.7.2 version works with this project.
2. Build project (IDK if it's necessary at this point):<br>
   antlr4 -Dlanguage=Python3 Hello.g4 -visitor -o dist

<br>

3. How to run project in Pycharm:
   1. Go to Hello.g4 file.
   2. Right-click on the 'program' production
   3. CLick 'Test rule program'
   4. Provide input and test if rule works fine.


Btw. Main file is copied from sample project, so it's not compatible with the project yet.