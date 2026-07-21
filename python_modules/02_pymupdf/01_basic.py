import pymupdf

doc = pymupdf.open("sample.pdf")

print(len(doc))
print(doc.page_count)
print("Lets check PDF is Encrypted or not : ",doc.is_encrypted)
print(doc.metadata)
print(doc.name)



