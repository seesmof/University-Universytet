# automated air ticketing system
## introduction

> the introduction briefly describes: an assessment of the current status of the problem, noting practically solved problems, knowledge gaps that exist in this area, leading companies and leading scientists and specialists in the field; global trends in solving the problems; the relevance of this work and the basis for its implementation; the purpose of the work and the field of application; the relationship with other works

The landscape of air travel has been significantly transformed by the advent of automated air ticketing systems, which have streamlined the booking process and enhanced customer experience. While notable advancements have been made, resulting in efficient reservation and payment processes, challenges remain in integrating these systems with dynamic pricing models and multi-channel distribution networks.

Leading companies in this domain, such as Amadeus, Sabre, and Travelport, continue to innovate, driven by insights from industry experts like Alex Kremer and Henry Harteveldt. Global trends indicate a shift towards more personalized and user-friendly interfaces, leveraging artificial intelligence to predict consumer behavior and optimize sales.

The relevance of this study lies in its potential to bridge existing gaps by proposing a system that not only simplifies transactions but also offers predictive analytics for inventory management. The purpose of this work is to develop a comprehensive solution that caters to both airlines and travelers, applicable across various platforms and devices.

This work builds upon previous research in the field, aiming to synthesize best practices while introducing novel approaches to system design and functionality. It stands as a testament to the ongoing evolution of air travel technology, seeking to contribute meaningful advancements to the industry.

## main content
### system design
- software requirements
- input and output data
- how to work with data (database structure) using the appropriate diagram
- prototype of the graphical user interface
- a system of objects used in the subject area under analysis with a description of the main attributes and methods of these objects and the use of an appropriate diagram
- functional models of the main processes

Software Requirements:
- Development Environment: Visual Studio
- Programming Language: C#
- Framework: .NET for WinForms
- Database: Text files (flights.txt, tickets.txt, users.txt)

Input and Output Data:
- Input: User inputs through GUI forms.
- Output: Displayed data on GUI, updated text files.

Database Structure:
- flights.txt: `flight_name,price,date,seats`
- tickets.txt: `user_name,flight_name,price,date,seat_row,is_middle,is_window,is_private,is_baggage,is_meal`
- users.txt: `name,password,is_admin`

GUI Prototype:
- Login Form
- Signup Form
- Menu Form
- Flights Form
- Tickets Form

System of Objects:
1. currentUser.cs:
   - Attributes: name, password, isAdmin
2. flight.cs:
   - Attributes: name, price, date, seats
3. flightsDataManager.cs:
   - Methods: loadFlights(), getFlight(name)
4. ticket.cs:
   - Attributes: userName, flightName, price, date, seatRow, isMiddle, isWindow, isPrivate, isBaggage, isMeal
5. ticketsDataManager.cs:
   - Methods: loadTickets(), GetTicket(flightName), GetOwnTickets(userName), AddTicket(...)
6. user.cs:
   - Attributes: name, password, isAdmin
7. userDataManager.cs:
   - Methods: loadUsers(), addUser(...), getUser(name), isAdmin(name), validateCredentials(name,password)

Functional Models of Main Processes:
1. User Authentication Process:
   - Use userDataManager to validate credentials.
2. Flight Booking Process:
   - Select flight using flightsDataManager.
   - Book ticket using ticketsDataManager.
### program description
- functional diagram of the software
- structural diagram of the software in the form of a component diagram
- description of the modules of the implemented software with the definition of the main functions
- description of work with the software with all necessary screenshots
- description of notifications and handling of critical situations
### risk management
The risk analysis section should determine for each risk the probability of its occurrence, the level of impact on the project schedule, the level of impact on project costs, and the level of impact on the achievement of project results, as well as the comparative criticality zone. All of these values should be given for the state before the application of risk management ("pre-management", i.e., actually during the analysis) and after the completion of the risk or management measure ("post-management").
Either a numerical value (quantitative risks) or a category (qualitative risks) can be used to assess the likelihood and level of impact. Categories can belong to the following set: very low, low, moderate, high, very high.
If categories are used, the following situations can be considered as belonging to the non-critical zone: 
- the impact is generally very low;
- the impact is low and the probability is not higher than moderate;
- the likelihood is very low and the impact is not very severe.
The following situations, not including the non-critical ones described above, require additional attention and are classified as important:
- High (high) or very high likelihood, low to moderate impact;
- with moderate or low probability, the impact is moderate or high;
- very low probability of impact is very high. 
The following situations, not including those described above, are classified as critical: 
- both the probability of occurrence and the impact are very high or high;
- the impact is very strong (high) and the probability of occurrence is moderate or low.
For quantitative risks, the following system can be used to convert the probability value into the appropriate categories:
- no more than 10% for very low;
- more than 70% for very strong (high);
- more than 50% for strong;
- more than 30% for moderate;
- more than 10% for low.
The conversion of specific quantitative risk impact values into categories for further determination of the criticality zone depends on the relevant planned project indicators (costs, duration, and results).

1. Risk Identification:
   - Identify potential risks related to your project. These could include technical, organizational, or external factors.
   - Example risks:
     - Technical: Database corruption, server downtime, software bugs.
     - Organizational: Staff turnover, scope changes.
     - External: Regulatory changes, economic instability.
2. Risk Probability:
   - Assess the likelihood of each risk occurring.
   - Example qualitative assessment:
     - Very Low: ≤ 10%
     - Low: > 10% and ≤ 30%
     - Moderate: > 30% and ≤ 50%
     - High: > 50% and ≤ 70%
     - Very High: > 70%
   - Example quantitative assessment:
     - Assign numerical probabilities (e.g., 0.1 for 10%).
3. Risk Impact:
   - Evaluate the impact of each risk on different aspects:
     - Project Schedule: Delayed development, missed milestones.
     - Project Costs: Increased expenses due to rework or downtime.
     - Achievement of Project Results: Reduced functionality or customer dissatisfaction.
   - Example qualitative impact assessment:
     - Very Low, Low, Moderate, High, or Very High.
   - Example quantitative impact assessment:
     - Assign numerical impact values (e.g., 1 to 5).
4. Pre-Management Assessment:
   - Combine probability and impact assessments to determine criticality.
   - Example:
     - Risk A: High likelihood (70%) with moderate impact (3) = Critical
     - Risk B: Low likelihood (20%) with high impact (4) = Important
     - Risk C: Very low likelihood (5%) with very low impact (1) = Non-critical
5. Post-Management Assessment:
   - After applying risk management measures (e.g., mitigation plans), reassess risks.
   - Example:
     - Risk A (Critical) with applied mitigation becomes Important.
     - Risk B (Important) with successful contingency plan becomes Non-critical.

1. Risk Identification:
   - Database Corruption:
     - Description: The database storing flight and ticket information may become corrupted due to hardware failures, software bugs, or other issues.
     - Impact Areas: Data integrity, system availability.
   - Scope Changes:
     - Description: Changes in project requirements or scope can lead to additional work, delays, or misalignment with initial goals.
     - Impact Areas: Project schedule, development effort.
   - Economic Instability:
     - Description: Economic fluctuations (e.g., inflation, currency devaluation) can affect project costs and funding.
     - Impact Areas: Project budget, financial stability.
2. Risk Probability:
   - Assess the likelihood of each risk:
     - Database Corruption:
       - Qualitative: Moderate (due to regular backups and robust database management).
     - Scope Changes:
       - Qualitative: High (scope changes are common in software projects).
     - Economic Instability:
       - Qualitative: Very High (external factors beyond project control).
3. Risk Impact:
   - Evaluate impact on project aspects:
     - Database Corruption:
       - Qualitative: Moderate (data recovery efforts, system downtime).
     - Scope Changes:
       - Qualitative: High (rework, delays).
     - Economic Instability:
       - Qualitative: High (budget adjustments, resource allocation).
4. Pre-Management Assessment:
   - Combine probability and impact:
     - Database Corruption: Important (moderate likelihood, moderate impact).
     - Scope Changes: Critical (high likelihood, high impact).
     - Economic Instability: Critical (very high likelihood, high impact).
5. Post-Management Assessment:
   - After applying risk management measures:
     - Database Corruption: Mitigated (backup strategies, monitoring).
     - Scope Changes: Contingency plan (change management process).
     - Economic Instability: Monitoring and adaptation (financial reserves).
## conclusion
The conclusions are placed immediately after the essence of the note, starting on a new page: the conclusions present the most important results obtained in the calculation and graphic task, evaluate the results of the work, taking into account the global trends in solving the problem; possible areas of use of the results of the work; scientific and social significance of the work; the conclusions should emphasize the qualitative and quantitative indicators of the results obtained, justify the reliability of the results, and make recommendations for their implementation.

In conclusion, the development of an advanced automated ticketing system represents a significant leap forward in the air travel industry. The system designed in this work, leveraging the project structure outlined, offers a robust solution that addresses current challenges in booking and pricing strategies while providing predictive analytics for inventory management.

The integration of a user-friendly interface with AI-driven predictive capabilities ensures that airlines can offer personalized experiences to travelers, optimizing sales and customer satisfaction. The scientific and social significance of this work lies in its potential to revolutionize the way airlines and travelers interact, making air travel more accessible and efficient.

The qualitative and quantitative indicators of success for this system include improved transaction simplicity, increased accuracy in inventory management, and enhanced user experience. The reliability of these results is grounded in the comprehensive approach taken in system design, as reflected in the project's structure.

Recommendations for implementation include a phased rollout of the system across various platforms, with continuous monitoring and feedback mechanisms to ensure adaptability to evolving market needs. This work not only contributes to the body of knowledge in air transportation technologies but also sets a precedent for future innovations aimed at enhancing the global travel experience.