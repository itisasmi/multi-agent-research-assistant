from arxiv import Search, SortCriterion

def search_papers(topic, max_results=5):
    search = Search(query=topic, max_results=max_results, sort_by=SortCriterion.Relevance)
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "pdf_url": result.pdf_url,
            "summary": result.summary
        })
    return papers
