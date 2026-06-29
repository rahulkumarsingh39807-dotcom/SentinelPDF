import pikepdf

def extract_metadata(file_path):
    try:
        with pikepdf.Pdf.open(file_path) as pdf:

            metadata = dict(pdf.docinfo)

            return {
                "title": str(metadata.get("/Title", "Unknown")),
                "author": str(metadata.get("/Author", "Unknown")),
                "creator": str(metadata.get("/Creator", "Unknown")),
                "producer": str(metadata.get("/Producer", "Unknown")),
                "pages": len(pdf.pages),
                "pdf_version": pdf.pdf_version
            }

    except Exception as e:
        return {
            "error": str(e)
        }