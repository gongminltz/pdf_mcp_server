# pdf_mcp_server
The MCP server used for operating PDFs, currently supports merging PDF files and exporting specified pages from designated PDF files.

Operating Steps:
1 Download pdf_mcp_server.py;
2 Install the dependency package via pip install PyPDF2 or pip3 install PyPDF2;
3 Start the PDF MCP server by running python pdf_mcp_server.py;
4 Configure the PDF MCP server using an MCP client (such as Cherry Studio)
{
    "mcpServers": {
        "pdf_mcp_server": {
          "isActive": true,
          "name": "pdf_mcp_server",
          "type": "sse",
          "description": "pdf操作",
          "baseUrl": "http://127.0.0.1:8010/sse"
        }
    }
}

使用示例：
1 将多个pdf文件合并为一个pdf文件：合并e:/1.pdf和e:2.pdf，保存到e:/3.pdf
2 提取 PDF 文件中指定的若干页面：请提取 e:/AQA-AS Math PSM.pdf文件的第10到第20页，以及第23页，第30-35页，保存到e:/2.pdf
