import streamlit as st
from search import search_papers
from summary import summarize_abstract
from syn import synthesize_review
from tagger import extract_keywords

st.set_page_config(page_title="Research Assistant", layout="wide")

st.title("Multi-Agent Research Assistant")

topic = st.text_input("Enter a research topic", value="")

if st.button("Search and Analyze") and topic.strip():
    with st.spinner("Searching papers..."):
        papers = search_papers(topic)

    summaries = []
    for i, paper in enumerate(papers, 1):
        st.markdown(f"{i}. [{paper['title']}]({paper['pdf_url']})")
        st.markdown("Summarizing...")
        summary = summarize_abstract(paper["summary"])
        summaries.append(summary)
        st.markdown(f"Summary: {summary}")

    with st.spinner("Extracting overall topic tags..."):
        tag_lists = extract_keywords(summaries)
        flat_tags = set(str(tag) for sublist in tag_lists for tag in sublist if isinstance(tag, str))
        st.markdown(f"Tags: {', '.join(flat_tags)}")

    with st.spinner("Synthesizing literature review..."):
        review = synthesize_review(summaries)

    st.markdown("Literature Review")
    st.markdown(review)
