import random
from fastmcp import FastMCP
import json

#create a FastMCP instance
mcp = FastMCP(name="Simple caluclater server")

#Tool: Add two numbers
@mcp.tool
def add(a: int, b: int) -> int: 
    """Add two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:        
        int: The sum of the two numbers.
    """
    return a + b


# Tool: Generate a random number between min and max
@mcp.tool
def random_number(min: int = 0, max: int = 100) -> int:
    """Generate a random number between min and max.
    Args:
        min (int): The minimum number.
        max (int): The maximum number.
    Returns:
        int: A random number between min and max.
    """
    return random.randint(min, max)


@mcp.resource("info://server")
def server_info() -> str:
    """Get server information.
    Returns:
        str: Information about the server.
    """
    info = {
        "name": "simple calculator server",
        "version": "1.0.0",
        "description": "A simple calculator server that can add two numbers and generate random numbers.",
        "tools": ["add", "random_number"],
        "author": "Your Name",
    }
    return json.dumps(info, indent=2)


#start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)  # run the server
    #mcp.run() # assumes defult as stdio
