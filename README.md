# Academic-Progression-Predictor
This is my python project to predict progression outcomes at the end of each academic year 

Progression outcomes as defined by the University redulations![Academic progression]
(https://github.com/BhanukaHerasinghe/Academic-Progression-Predictor/assets/124506514/1fc10224-9da9-4a85-98ce-d5ff61e28165)


<h1>Part 1 Main Version (Student & Staff Version)</h1>

Part 1 - Staff Version with histogram  -------->  For Staff

Part 1 - Student Version --------->  For Student

1) Students can predict their progress as an outcome using the programme at the conclusion of each academic year. The programme will ask you how many credits you passed, deferred, or failed before displaying the proper progression results for each individual student.
(ex-: exclude , module retriever or exclude , progress )

2) Validation

   ** The Program display "Incorrect Input...!!! Please Input Integer..." if input is the wrong data type.

   ** The program display "Your input integer Out of range" if credits entered are not in the range 0,20,40,60,80,100,and 120.

   ** The program display " Total incorrect" if the total of the pass ,defer , and fail credits is not 120.

   3) Multiple Outcomes & Histogram

      ** A staff member can forecast several students' advancement outcomes using the program's looping functionality.

      ** Until the staff member user hits 'q' to exit, the programme asks for credits at pass, defer, and fail and displays the proper progression for each individual student. To continue, you may use the input 'y' as an alternative.

      ** When 'q' is input, the programme generates a 'histogram' in which each star represents a student who earned a progress outcome in the category range of 'progress, trailing, module retriever, and exclusion. The histogram should be applicable to any number of results and be related to the data input entered by the staff person throughout the programme run.

      ** Show the overall number of pupils as well as the number of students in each category of advancement.

Staff Version with Histogram
      
Please enter student credit at pass: 80

Please enter student credit at defer: 20

Please enter student credit at fail: 20

Do not Progress - module retriever


If you want to add another student credit record

Please Enter 'y' for yes or 'q' to quit and view outcomes: y


Please enter student credit at pass: 60

Please enter student credit at defer: 20

Please enter student credit at fail: 40

Do not Progress - module retriever


If you want to add another student credit record

Please Enter 'y' for yes or 'q' to quit and view outcomes: y


Please enter student credit at pass: 100

Please enter student credit at defer: 20

Please enter student credit at fail: 0

progress (module trailer)


If you want to add another student credit record

Please Enter 'y' for yes or 'q' to quit and view outcomes: y


Please enter student credit at pass: 120

Please enter student credit at defer: 0

Please enter student credit at fail: 0

progress


If you want to add another student credit record

Please Enter 'y' for yes or 'q' to quit and view outcomes: q



================================================================================

Horizontal Histogram

Progress 1  : *

Trailer 1   : *

Retriever 2 : **

Excluded 0  : 


4 outcomes in total.

================================================================================


<h2> Part 2  Vertical Histogram (extension) ( Part 02- Vertical Histogram.py) </h2>

** Extend version of part 01 program to add a vertical histogram 


![Vertical_histogram](https://github.com/BhanukaHerasinghe/Academic-Progression-Predictor/assets/124506514/a3c3dfe1-5a41-4bd7-8808-1189584d211c)


<h3> Part 3 - List /Tuple/Directory (extension) (Part 3 - List,Tuple,Directory.py) </h3>

** Extended version , so that the program uses Python to save  the input progression data to a list,tuple or dirctory. Then access the stored data the list,tuple,directory and print the data in the following format below.

Output : The following should display after the histogram

Progress- 120,0,0

Progress (module trailer)- 100,20,0

Module retriever -  80,20,20

Module retriever -  60,20,40


<h4> Part 4 - Text File (Extension) (Part 4 Text file.py ) </h4>

** This scipt will save input Progression data to a text file. Later in the program ,access the stored data and print out as shown below.

Progress- 120,0,0

Progress (module trailer)- 100,20,0

Module retriever -  80,20,20

Module retriever -  60,20,40






      
