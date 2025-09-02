import os
from PyPDF2 import PdfReader, PdfWriter
from mcp.server import FastMCP

mcp = FastMCP("pdf_merger_mcp_server", port = 8010)


@mcp.tool()
def merge_pdfs(input_files, output_file):
    """
    Merge multiple PDF files into one PDF file.
    :param input_files: Paths of the PDF files to be merged, separated by commas
    :param output_file: Output path of the PDF file.
    """
    pdf_writer = PdfWriter()
    
    input_files = input_files.split(",")
    for input_file in input_files:
        print(f"start merging file {input_file}")
        if not os.path.exists(input_file):
            print(f"file {input_file} does not exist，ignore")
            continue
        pdf_reader = PdfReader(input_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        print(f"file {input_file} has been successfully merged, with a total of {len(pdf_reader.pages)} pages merged.")
    with open(output_file, "wb") as out:
        pdf_writer.write(out)
    print(f"The PDF file has been merged into {output_file}")


@mcp.tool()
def extract_pages(input_file, output_file, pages_to_extract):
    """
    Extract specified pages from a PDF file.
    :param input_file: Input PDF file path
    :param output_file: Output PDF file path
    :param pages_to_extract: List of page indices to extract (starting from 0, the first page is 0), separated by commas
    """
    if not os.path.exists(input_file):
        print(f"file {input_file} does not exist")
        return

    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    pages_to_extract = pages_to_extract.split(",")
    for page_num in pages_to_extract:
        if page_num < len(pdf_reader.pages):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        else:
            print(f"page {page_num} does not exist，ignore")

    with open(output_file, "wb") as out:
        pdf_writer.write(out)
    print(f"The specified pages have been extracted to file {output_file}")
    

if __name__ == "__main__":
    mcp.run(transport='sse')