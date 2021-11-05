# PDF Comment Extractor
This is done through mupypdf as described on:  https://www.analyticsvidhya.com/blog/2021/06/data-extraction-from-unstructured-pdfs/
Added a tkinter GUI to allow non-progamming users to choose a pdf file for extraction

How it works:
Highlight (also known as annotate) a pdf, include comments for each annotation 
Run the script on the pdf /n
The code will extract annotated words (words under the highlighted rectangle) and save into list1
The comments that come with the annotations are saved in list2
A CSV writer will write list1 and list2 into 2 columns. For each item in the list, it will be written as rows going downwards. 
The CSV will be saved at the same folder the code base in run from

To do list:
Write to accept multiple pdfs
