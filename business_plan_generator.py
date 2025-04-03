# app/business_plan_generator.py

class BusinessPlanGenerator:
    def __init__(self):
        pass

    def generate_business_plan(self, idea):
        """
        Generates a business plan based on the input idea.
        """
        business_plan = {
            "Executive Summary": f"Business Idea: {idea}",
            "Market Analysis": "Conduct market research and identify target demographics.",
            "Product or Service": f"Develop a product or service based on the idea: {idea}",
            "Marketing Strategy": "Develop a marketing plan to reach target customers.",
            "Financial Plan": "Create financial forecasts including cost, revenue, and profit projections.",
            "Team": "Assemble a team with relevant skills to support the idea."
        }
        return business_plan

    def display_plan(self, business_plan):
        """
        Displays the generated business plan.
        """
        for section, content in business_plan.items():
            print(f"{section}:\n{content}\n")
