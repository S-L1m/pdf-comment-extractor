'''
V1.2- WIP to accept multiple PDFs
To extract annotated / highlighted text in a PDF document along with the/any comments made with the highlights. 
Place the highlights and the comments into a csv file
Adapted code from :
    https://www.analyticsvidhya.com/blog/2021/06/data-extraction-from-unstructured-pdfs/
    comment extraction: https://stackoverflow.com/questions/50801270/extract-comments-from-pdf
    CSV from a previous internal code block/project for word document analysis
'''

import fitz
import csv
import tkinter as tk
from tkinter import filedialog

# Show file selection dialog box
root = tk.Tk()
root.withdraw()
paths = filedialog.askopenfilenames()
root.update()

ls_files = []
all_annots = []
comments = []

ls_files.append(paths)
print(ls_files)

def make_text(words):
    line_dict = {}
    words.sort(key=lambda w: w[0])
    for w in words:
        y1 = round(w[3],1)
        word = w[4]
        line = line_dict.get(y1, [])
        line.append(word)
        line_dict[y1] = line
    lines = list(line_dict.items())
    lines.sort()
    return "n".join([" ".join(line[1]) for line in lines])

for ind_file in ls_files:
    # doc = fitz.open(ind_file)
    with fitz.open("/".join(ind_file)) as f:

        for pageno in range(0, len(f)-1):
            page = f[pageno]
            words = page.get_text("words")
            for annot in page.annots():
                if annot !=None:
                    rec = annot.rect
                    mywords = [w for w in words if fitz.Rect(w[:4]) in rec]
                    ann = make_text(mywords)
                    all_annots.append(ann)

        for i in range(0, len(f)-1):
            page = f[i]
            for annot in page.annots():
                comments.append(annot.info["content"])
        
        with open("pdf_extract.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        # with open(r'''C:\\Users\stefan.lim\Desktop\NTW\pdf_extract.csv''', 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer=csv.writer(csvfile)
            # Write a header line with the file name
            # writer.writerow(ind_file.split("/")[-1], "")
            zip_data = zip(all_annots, comments)
            writer.writerows(zip_data)

    # fitz.close(ind_file)

print(all_annots)
print(comments)

