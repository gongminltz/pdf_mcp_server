# pdf_mcp_server
The MCP server used for operating PDFs, currently supports merging PDF files and exporting specified pages from designated PDF files.

Operating Steps:
1 Download pdf_mcp_server.py;
2 Install the dependency package via pip install PyPDF2 or pip3 install PyPDF2;
3 Start the PDF MCP server by running python pdf_mcp_server.py;
4 Configure the PDF MCP server using an MCP client (such as Cherry Studio)
"mcpServers": {
    "pdf_mcp_server": {
      "isActive": true,
      "name": "pdf_mcp_server",
      "type": "sse",
      "description": "pdf操作",
      "baseUrl": "http://127.0.0.1:8010/sse"
    }
}
