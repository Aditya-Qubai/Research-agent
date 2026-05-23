from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.summarizer import summarize_text
from agents.critique_agent import critique_text
from agents.concept_agent import extract_concepts
from agents.graph_agent import store_research_graph
from agents.rss_agent import ingest_rss_intelligence
from agents.memory_agent import retrieve_related_intelligence


# Shared workflow state
class ResearchState(TypedDict):

    text: str
    summary: str
    critique: str
    concepts: str
    graph_status: str
    rss_intelligence: str
    memory_context: str


# Summary node
def summary_node(state: ResearchState):

    combined_text = state["text"]

    if state.get("rss_intelligence"):

        combined_text += "\n\n"
        combined_text += state["rss_intelligence"]

    if state.get("memory_context"):

        combined_text += "\n\nPREVIOUS MEMORY:\n"
        combined_text += state["memory_context"]

    summary = summarize_text(combined_text)

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

def rss_node(state: ResearchState):

    rss_data = ingest_rss_intelligence()

    return {
        "rss_intelligence": rss_data
    }

def memory_node(state: ResearchState):

    context = retrieve_related_intelligence(
        state["text"][:300]
    )

    return {
        "memory_context": context
    }

# Build graph
graph = StateGraph(ResearchState)

graph.add_node("summary", summary_node)
graph.add_node("critique", critique_node)
graph.add_node("concepts", concept_node)
graph.add_node("graph", graph_node)
graph.add_node("rss", rss_node)
graph.add_node("memory", memory_node)

# Workflow order
graph.set_entry_point("rss")

graph.add_edge("summary", "critique")
graph.add_edge("critique", "concepts")
graph.add_edge("concepts", "graph")
graph.add_edge("graph", END)
graph.add_edge("rss", "summary")

# Compile workflow
research_workflow = graph.compile()