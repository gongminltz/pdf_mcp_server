import os
from PyPDF2 import PdfReader, PdfWriter
from mcp.server import FastMCP

mcp = FastMCP("pdf_mcp_server", port = 8010)


@mcp.tool()
def merge_pdfs(input_files, output_file):
    """
    将多个pdf文件合并为一个pdf文件
    使用示例：合并e:/1.pdf和e:2.pdf，保存到e:/3.pdf
    :param input_files: pdf文件完整路径，以逗号分开，如: e:/1.pdf,e:/2.pdf,e:/3.pdf
    :param output_file: 最后合并后的文件的保存位置，如：e:/result.pdf
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
    提取 PDF 文件中指定的若干页面
    使用示例：请提取 e:/AQA-AS Math PSM.pdf文件的第10到第20页，以及第23页，第30-35页，保存到e:/2.pdf
    :param input_file: 输入的 PDF 文件完整路径，如：e:/1.pdf
    :param output_file: 输出的 PDF 文件完整路径，如：e:/result.pdf
    :param pages_to_extract: 需要提取的页面。如： "1-3,5,7-9"，表示提取pdf文件的第1到3页，第5页，以及7到9页
    """
    if not os.path.exists(input_file):
        print(f"文件 {input_file} 不存在")
        return

    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    
    pages_to_extract = parse_page_range(pages_to_extract)

    for page_num in pages_to_extract:
        if 0 <= page_num < len(pdf_reader.pages):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        else:
            print(f"页面 {page_num + 1} 超出 PDF 文件的页码范围")

    with open(output_file, "wb") as out:
        pdf_writer.write(out)

    print(f"已成功提取指定页面到 {output_file}")
    
def parse_page_range(page_range):
    """
    解析页面范围字符串，返回页面索引列表
    :param page_range: 页面范围字符串，例如 "1-3" 或 "1,3,5"
    :return: 页面索引列表
    """
    page_indices = []
    for part in page_range.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            page_indices.extend(range(start - 1, end))  # 转换为从 0 开始的索引
        else:
            page_indices.append(int(part) - 1)  # 转换为从 0 开始的索引
    return sorted(set(page_indices))  # 去重并排序

if __name__ == "__main__":
    mcp.run(transport='sse')
