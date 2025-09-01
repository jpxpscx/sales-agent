from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Model
llm = ChatGroq(model="openai/gpt-oss-20b")
# Tool
search_tool = TavilySearch(topic="general", max_results=2)

def generate_insights(company_name, product_name,company_url, company_competitors):
    # Perform the search
    search_query = f"Site:{company_url} company strategy, leadership, competitors, business model"
    search_results = search_tool.invoke(search_query)
    print("Search Results: ", search_results)
    
    messages = [
        SystemMessage(f"You are a sales assistant that provides concise and structured insights."),
        HumanMessage(content=f"""
        Company Info from Tavily: {search_results}
        
        Company: {company_name}
        Product: {product_name}
        Competitors: {company_competitors}
        
        Generate a one-page summary including:
        1. Company strategy related to {product_name}
        2. Possible competitors or partnerships (including {company_competitors})
        3. Leadership and decision-makers relevant to this area
        Format output in clear sections with bullet points.
        """)
    ]

    model_response = llm.invoke(messages)
    print("\n Model Response: ", model_response.content)
    return model_response.content



# ============= UI ==============
st.title("Sales Agent")
st.subheader("Generate a report")
st.divider()

# company name
company_name = st.text_input("Company Name")

# company URL
company_url = st.text_input("Company URL")

# product name
product_name = st.text_input("Product Name")

# company competitors
company_competitors = st.text_input("Company Competitors")

if st.button("Generate Report"):
    if company_name and company_url:
        with st.spinner("Generating Report..."):
            result = generate_insights(company_name, product_name, company_url, company_competitors)
            
            st.divider()
            st.write(result)
    else:
        st.warning("Please enter a company name and URL")