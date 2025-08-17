from src.crew import DeepResearchCrew
if __name__ == "__main__":
    crew = DeepResearchCrew(research_topic="AI-trender i bærekraftig landbruk 2025")
    result = crew.crew().kickoff(inputs={"research_topic": crew.research_topic})
    print("Forskningsresultat (lagret i outputs/):", result)
