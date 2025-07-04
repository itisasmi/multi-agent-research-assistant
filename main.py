from search import search_papers
from summary import summarize_abstract
from syn import synthesize_review
from tagger import extract_keywords

def main():
    topic = input("Enter a research topic: ").strip()
    print(f"\nSearching papers on: {topic}")
    papers = search_papers(topic)

    summaries = []
    tags_list = []

    for i, paper in enumerate(papers, 1):
        print(f"\n Title {i}: {paper['title']}")
        print(f" PDF Link: {paper['pdf_url']}")
        print(" Summarizing...")
        summary = summarize_abstract(paper['summary'])
        summaries.append(summary)
        print(f" Summary: {summary}")
        
        tags = extract_keywords(summary)
        tags_list.append(tags)
        print(f" Tags: {', '.join(tags)}")

    print("\n Synthesizing Literature Review...")
    review = synthesize_review(summaries)
    print("\n Literature Review:\n", review)

    with open("literature_review.md", "w", encoding="utf-8") as f:
        f.write(f" Topic: {topic}\n\n")
        f.write(" 🔍 Paper Summaries\n\n")
        for i, paper in enumerate(papers, 1):
            f.write(f" {i}. [{paper['title']}]({paper['pdf_url']})\n")
            f.write(f"Summary: {summaries[i-1]}\n")
            f.write(f"Tags: {', '.join(tags_list[i-1])}\n\n")
        f.write(" Literature Review\n")
        f.write(review)

if __name__ == "__main__":
    main()
