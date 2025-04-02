from PyPDF2 import PdfReader
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_bookmarks(reader):
    """Extracts bookmarks from the PDF, returning a dictionary mapping page numbers to bookmark titles."""
    bookmarks = {}

    def _parse_bookmark(outline, parent_title=''):
        if isinstance(outline, list):
            for item in outline:
                _parse_bookmark(item, parent_title)
        else:
            title = f"{parent_title} > {outline.title}" if parent_title else outline.title
            try:
                page_num = reader.get_destination_page_number(outline)
                bookmarks[page_num] = title
            except Exception as e:
                print(f"Error parsing bookmark: {e}")

    try:
        outlines = reader.outline  # Use outline attribute to get bookmarks
        if outlines:
            _parse_bookmark(outlines)
    except Exception as e:
        print(f"Error extracting bookmarks: {e}")

    return bookmarks

def extract_annotations(pdf_path):
    # Open the PDF file
    pypdf_doc = PdfReader(open(pdf_path, "rb"))
    annotations = []

    # Get bookmarks
    bookmarks = extract_bookmarks(pypdf_doc)
    sorted_bookmark_pages = sorted(bookmarks.keys())  # Sort bookmarks by page number

    # Iterate through all pages
    last_bookmark_name = "No Bookmark"
    bookmark_index = 0
    
    for page_num in range(len(pypdf_doc.pages)):
        pypdf_page = pypdf_doc.pages[page_num]
        
        # Update last bookmark if we've passed a bookmark page
        if bookmark_index < len(sorted_bookmark_pages) and page_num >= sorted_bookmark_pages[bookmark_index]:
            last_bookmark_name = bookmarks[sorted_bookmark_pages[bookmark_index]]
            bookmark_index += 1

        # Check if the page contains annotations
        if '/Annots' in pypdf_page:
            annots = pypdf_page['/Annots']
            if isinstance(annots, list):
                rect_annotations = {}

                for annot in annots:
                    annot_obj = annot.get_object()  # Dereference the indirect object
                    subtype = annot_obj.get('/Subtype')
                    contents = annot_obj.get('/Contents', 'No content')
                    rect = tuple(annot_obj.get('/Rect', []))  # Convert ArrayObject to tuple
                    author = annot_obj.get('/T', 'Unknown author')
                    reply_to = annot_obj.get('/IRT')  # Get reply-to reference

                    # Decode bytes to string if necessary
                    if isinstance(contents, bytes):
                        contents = contents.decode('utf-8')
                    if isinstance(author, bytes):
                        author = author.decode('utf-8')

                    # Store annotations by Rect or IRT to associate comments with replies
                    key = rect if reply_to is None else tuple(reply_to.get_object().get('/Rect', rect))

                    if key not in rect_annotations:
                        rect_annotations[key] = []

                    rect_annotations[key].append({
                        "Page": page_num + 1,
                        "Bookmark": last_bookmark_name,  # Use the last bookmark encountered
                        "Annotation Type": subtype,
                        "Content": contents,
                        "Author": author,
                        "Rect": rect,
                        "Is Reply": reply_to is not None
                    })

                # Separate main comments and replies
                for rect, comments in rect_annotations.items():
                    base_comment = None
                    replies = []

                    # Distinguish between main comments and replies
                    for comment in comments:
                        if comment["Is Reply"]:
                            replies.append(comment)
                        else:
                            base_comment = comment

                    if base_comment:
                        annotation_entry = {
                            "Page": base_comment["Page"],
                            "Bookmark": base_comment["Bookmark"],
                            "Annotation Type": base_comment["Annotation Type"],
                            "Main Comment": base_comment["Content"],
                            "Main Author": base_comment["Author"]
                        }

                        # Add replies to separate columns
                        for i, reply in enumerate(replies, start=1):
                            annotation_entry[f"Reply {i}"] = reply["Content"]
                            annotation_entry[f"Reply {i} Author"] = reply["Author"]

                        annotations.append(annotation_entry)

    return annotations

def save_annotations_to_excel(annotations, output_path):
    # Convert the annotations list to a DataFrame
    df = pd.DataFrame(annotations)
    # Save as an Excel file
    df.to_excel(output_path, index=False)

def browse_pdf_file():
    pdf_file.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

def browse_output_excel():
    output_excel.set(filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]))

def process_pdf():
    pdf_path = pdf_file.get()
    output_path = output_excel.get()

    if not pdf_path or not output_path:
        messagebox.showwarning("Input Error", "Please select both PDF file and output Excel file.")
        return

    try:
        annotations = extract_annotations(pdf_path)
        save_annotations_to_excel(annotations, output_path)
        messagebox.showinfo("Success", f"Annotations have been saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Processing Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("PDF Annotation Extractor")

# Variables to store file paths
pdf_file = tk.StringVar()
output_excel = tk.StringVar()

# Create and layout the UI elements
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=pdf_file, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_pdf_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Output Excel File:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=output_excel, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_excel).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Extract Annotations", command=process_pdf).grid(row=2, columnspan=3, pady=20)

# Run the main loop
root.mainloop()
