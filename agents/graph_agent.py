from database.neo4j_db import create_concept_relationship


def store_research_graph():

    # Temporary demo relationships

    create_concept_relationship(
        "Transformers",
        "RELATES_TO",
        "Attention Mechanisms"
    )

    create_concept_relationship(
        "Attention Mechanisms",
        "RELATES_TO",
        "Neural Networks"
    )

    return "Graph relationships stored"