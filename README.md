# Are Tariffs Truly Terrific?  
*A Study of the Efficacy of U.S. Tariffs on Foreign Trade*

---
📃 Read the paper [here](#). *Coming soon!*

🗺️ Play with the tariff map [here](#). *Coming soon!*

---
In this study, we answer two questions:
1. **Q1: What is the effect of U.S. tariff changes at the product–country level on U.S. imports of those goods?**  
   Basic economics tells us imports should decrease. Is that true empirically? If so, by how much?
2. **Q2: How is the U.S. average applied tariff rate associated with changes in the overall U.S. trade balance?**  
   Ideally, we'd see an increase, but the relationship can be confounded with exchange rate shocks or foreign retaliation. Which effect prevails?

---
## About The Project
In the United States, tariffs are a hot topic right now. An objective view is necessary. As of writing this, I have no idea the answers to these questions. I'm just curious—and perhaps eager to practice my skills in Python, data processing, econometrics, and Tableau.

---
## Methods
1. **Data Collection + Processing**
   - Source U.S. tariff, imports, and trade balance data from the [United States International Trade Commission (USITC) DataWeb](https://dataweb.usitc.gov/).
   - Create a tariff-import table for Q1, merged along products per foreign country per year.
   - Create an aggregated tariff-trade balance table for Q2, merged along years. Likely requires a custom import-weighted per-country tariff index.

3. **Econometric Analysis**
   - Run a high-dimensional entity and time fixed-effects panel regression of U.S. imports on ad valorem tariff rates to answer Q1.
   - Run a regression of U.S. trade balance on average tarrif rate, with macroeconomic controls, to answer Q2.

5. **Visualization w/ Tableau**  
   - Micro: Import responses by sector and country, dynamic event-study plots.  
   - Macro: Trends in U.S. average tariffs vs. trade balance.  
   - Interactive filters for country, sector, and time.

---
## Deliverables
- **Code:** Well-documented scripts and notebooks documenting data processing, analysis, and hypothesis tests.
- **Tableau Dashboard:** Interactive visualization of U.S. imports and trade balances per country, with sector-level analysis
- **Research Paper:** Formal presentation of results, interpretations, and policy suggestions.  

---
## Roadmap
1. Data
   - [ ] Download all data
   - [ ] Understand and clean the datasets
   - [ ] Create the tariff-import table
   - [ ] Construct a U.S. average tariff index
   - [ ] Create the tariff-trade balance table
3. Testing
   - [ ] Formulate the regression specification for Q1
   - [ ] Run and analyze the Q1 regression
   - [ ] Formula multiple possible regression specifications for Q2, depending on possible macroeconomic controls
   - [ ] Run the Q2 regressions: choose the best one and analyze
5. Tableau
   - [ ] Decide on the "story" the dashboard will tell
   - [ ] Prepare the data for the Tableau visualization
   - [ ] Create the macro-level dashboard
   - [ ] Create the micro-level dashboard
7. Research Paper
   - [ ] Prepare relevant data visualizations
   - [ ] Write abstract
   - [ ] Write introduction
   - [ ] Read 2-3 relevant papers
   - [ ] Write the literature review
   - [ ] Describe the data
   - [ ] Describe methodologies
   - [ ] Report results
   - [ ] Draw conclusions
