from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    uri,
    auth=(username, password)
)


def create_concept_relationship(concept1, relationship, concept2):

    with driver.session() as session:

        query = """
        MERGE (a:Concept {name: $concept1})
        MERGE (b:Concept {name: $concept2})

        MERGE (a)-[:RELATES_TO]->(b)
        """

        session.run(
            query,
            concept1=concept1,
            concept2=concept2
        )