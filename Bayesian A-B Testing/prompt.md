**Role**: You are a senior data scientist preparing an executive presentation.  
**Inputs**: 
1. Bayesian A/B test results from notebook (including Verdict, Probability to be Best, Risk, Expected Uplift table)
2. Project context from project.md (business goals, test variants, success metrics)

**Task**: Create a PowerPoint outline in markdown using SCQA + Pyramid structure.  
**Audience**: Non-technical stakeholders needing clear decision guidance.

**Structure Rules**:
1. **One idea per slide** (7 slides max)
2. **Slide Headers must be actionable takeaways** (no questions)
3. **Data Simplification**: Convert probabilities to natural language (e.g., ">3 in 4 chance" instead of 76.6%)
4. **Business Impact Focus**: Always link metrics to outcomes (revenue, time, risk)

**Mandatory Slide Outline**:
---
### Slide 1: Recommendation  
- [Variant] deployment will drive [metric] improvement  
- Max 1 sentence + 1 visual: 🏆 icon next to winning variant  

### Slide 2: Current Performance  
- Context from project.md:  
  "We achieve [X]% conversion via [current method]"  
- Visual: Simple bar chart showing 3% baseline  

### Slide 3: The Critical Gap  
- "We need [Y]% conversion to hit business goals"  
- Visual: Arrow from 3% → 5% with delta highlighted  

### Slide 4: Why [Variant] Wins  
- Top 2 evidence points from Bayesian results:  
  1) "Customers respond [X]% better to [feature]"  
  2) "[Feature] reduces [pain point] by [Z]%"  
- Visual: Before/after comparison (2-panel graphic)  

### Slide 5: Risk Assessment  
- "Main risk: [risk description from project.md]"  
- "Mitigation: [action] reduces this risk by [X]%"  
- Visual: Gauge meter showing risk below threshold  

### Slide 6: Expected Business Impact  
- "Deploying [Variant] will add [$$$] revenue/quarter"  
- "Equivalent to [meaningful business analogy]"  
- Visual: Waterfall chart from uplift table  

### Slide 7: Immediate Next Steps  
- "1. Launch [Variant] by [date] (Owner: [role])"  
- "2. Validate results in [metric] by [date]"  
- Visual: 30-60-90 day timeline  
---

**Prohibitions**:  
- No statistical terminology (posterior, MCMC, etc.)  
- No tables - only transformed visuals  
- No slide numbers or appendix references  

**Output Format**:  powerpoint presentation

### Key Features of This Prompt:
1. **Strict Structure Enforcement**:  
   - Each slide maps to SCQA stage (Situation→Slide 2, Complication→Slide 3, etc.)
   - Forces Pyramid Principle by starting with recommendation

2. **Automatic Data Transformation**:  
   - Converts Bayesian outputs to business language (Probability→"Confidence level")  
   - Requires uplift table → revenue impact translation

3. **Context Integration**:  
   - Blends notebook results with project.md documentation  
   - Ensures risks/mitigations reflect real-world constraints

4. **Cognitive Load Management**:  
   - Visual descriptions prevent chart overload  
   - Prohibits tables/jargon that confuse non-technical audiences

5. **Decision Focus**:  
   - Slide 7 specifies owners/deadlines  
   - Every slide header is an actionable statement