def route_query(query, salary_agent, insurance_agent):
    query_lower = query.lower()
    if "salary" in query_lower or "calculate" in query_lower or "deduction" in query_lower:
        return salary_agent.run(query)
    elif "insurance" in query_lower or "claim" in query_lower or "coverage" in query_lower:
        return insurance_agent.run(query)
    else:
        return "Sorry, I can only answer salary or insurance related questions."


