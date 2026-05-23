from database.retrieve_memory import search_memory


def retrieve_related_intelligence(query):

    results = search_memory(query)

    combined = ""

    for doc, meta in zip(
        results["documents"],
        results["metadata"]
    ):

        combined += f"""

        TITLE:
        {meta['title']}

        SOURCE:
        {meta['source']}

        TIME:
        {meta['timestamp']}

        CONTENT:
        {doc}

        """

    return combined