from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.summarizer import summarize_text
from agents.critique_agent import critique_text
from agents.concept_agent import extract_concepts
from agents.graph_agent import store_research_graph


# Shared workflow state
class ResearchState(TypedDict):

    text: str
    summary: str
    critique: str
    concepts: str
    graph_status: str


# Summary node
def summary_node(state: ResearchState):

    summary = summarize_text(state["text"])

    return {
        "summary": summary
    }


# Critique node
def critique_node(state: ResearchState):

    critique = critique_text(state["summary"])

    return {
        "critique": critique
    }


# Concept node
def concept_node(state: ResearchState):

    concepts = extract_concepts(state["summary"])

    return {
        "concepts": concepts
    }

def graph_node(state: ResearchState):

    result = store_research_graph()

    return {
        "graph_status": result
    }

# Build graph
graph = StateGraph(ResearchState)

graph.add_node("summary", summary_node)
graph.add_node("critique", critique_node)
graph.add_node("concepts", concept_node)
graph.add_node("graph", graph_node)

# Workflow order
graph.set_entry_point("summary")

graph.add_edge("summary", "critique")
graph.add_edge("critique", "concepts")
graph.add_edge("concepts", "graph")
graph.add_edge("graph", END)

# Compile workflow
research_workflow = graph.compile()