from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
    name="read_doc",
    description="Read the contents of a document. The input is the document ID, and the output is the contents of the document."
)
def read_doc(
    doc_id: str = Field(description='Id of the document to read')
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")

    # return docs.get(doc_id, "Document not found.")
    return docs[doc_id]


@mcp.tool(
    name="edit_doc",
    description="Edit the contents of a document. The input is the document ID and the new contents, and the output is the updated contents of the document."
)
def edit_doc(
    doc_id: str = Field(description='Id of the document to edit'),
    old_contents: str = Field(description='Old contents of the document'),
    new_contents: str = Field(description='New contents of the document')
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")

    docs[doc_id].replace(old_contents, new_contents)
    return "success"


# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
