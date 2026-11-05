data = """
Innovative Farm Management
Digitalization In Farm Management
Web-based farm management system
Multi-level automation of farm management information systems
Farm Management Software for Increased Productivity and Competitiveness
Dairy Farm Management Information Systems
Automated farm management system in Uzbekistan
A Farm Management Information System Using Future Internet Technologies
Farm Management Information Systems and Agricultural Production Governance
An Integrated Information Technology Framework for Smart Farming
Analysis of Farm Management Information Systems: Opportunities and Pathways for Future Value
Development of a Layered Architecture for a Single-Farm Fish Farming Management System Using Prototype Method
A Web Application for Farm Management and An Assessment of Its Utility
Farm & Ranch Business Management. Second Edition
""".strip()

lines = data.split("\n")
original_length = len(lines)

unique_lines = set(lines)
unique_length = len(unique_lines)

print("All are unique" if original_length == unique_length else "Not all are unique")
