from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.summarizer import summarize_text


# Shared workflow state
class ResearchState(TypedDict):

    text: str
    summary: str
    critique: str
    concepts: str


# Summary node
def summary_node(state: ResearchState):

    summary = summarize_text(state["text"])

    return {
        "summary": summary
    }


# Critique node
def critique_node(state: ResearchState):

    critique = f"""
    Critique of summary:

    {state['summary']}
    """

    return {
        "critique": critique
    }


# Concept node
def concept_node(state: ResearchState):

    concepts = f"""
    Key concepts extracted from:

    {state['summary']}
    """

    return {
        "concepts": concepts
    }


# Build graph
graph = StateGraph(ResearchState)

graph.add_node("summary", summary_node)
graph.add_node("critique", critique_node)
graph.add_node("concepts", concept_node)

# Workflow order
graph.set_entry_point("summary")

graph.add_edge("summary", "critique")
graph.add_edge("critique", "concepts")
graph.add_edge("concepts", END)

# Compile workflow
research_workflow = graph.compile()