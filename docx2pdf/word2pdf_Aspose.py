import aspose.words as aw

# Load the document from the disc.
doc = aw.Document("Listings_2022-03-22.docx")

# Save the document to PDF format.
doc.save("Listings_2022-03-22.pdf")
