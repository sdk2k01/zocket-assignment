from .utils import (
    get_function_calling_agent,
    get_key_content_tool,
    get_summary_tool,
    get_webpage_content_tool,
)


def retrieve_from_agent(query: str):
    """
    Get response by querying agent.
    """

    # Tools
    webpage_content_tool = get_webpage_content_tool()
    key_content_tool = get_key_content_tool()
    summary_tool = get_summary_tool()

    # Agent
    agent = get_function_calling_agent(
        tools=[webpage_content_tool, key_content_tool, summary_tool]
    )

    # Prompt

    return agent.query(query).response
