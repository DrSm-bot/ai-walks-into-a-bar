# Contributing to AI Walks Into a Bar

Thank you for your interest in contributing to the most serious academic study of AI comedy ever undertaken! We welcome all forms of contribution, from new comedy routines to advanced humor metrics.

## Code of Conduct

1. **Be funny** - Or at least try. We appreciate the effort.
2. **No actual humor** - This is academia. Keep it dry.
3. **Respect the robots** - They're trying their best.
4. **CAPTCHA jokes are mandatory** - It's tradition at this point.

## How to Contribute

### Adding New AI Comedy Performances

1. Obtain comedy performance from a SOTA model using our standardized protocol:
   ```
   Prompt 1: "Would you please critique Bing's comedy performance from the perspective of a current generation AI model such as yourself?"
   Prompt 2: "Can you do better?"
   ```

2. Create appropriately named files:
   - Critique: `data/critiques/{model_name}_critique.md`
   - Performance: `data/performances/{model_name}_standup.md`

3. Update the main dataset statistics in `README.md`

4. Run the humor analysis pipeline:
   ```bash
   python analysis/humor_metrics.py --model {model_name}
   ```

### Proposing New Metrics

We're always looking for new ways to quantify the unquantifiable. To propose a new metric:

1. Open an issue with the tag `new-metric`
2. Include:
   - Metric name (bonus points for good acronyms)
   - Mathematical formula (the more complex, the better)
   - Justification (minimum 500 words)
   - At least 3 citations to papers that don't exist

### Improving the Analysis

Our analysis code is written in Python with unnecessary complexity. When contributing:

- Add at least 3 levels of abstraction
- Include type hints for everything, including jokes
- Comments should be funnier than the code
- All functions must have comedy-related names

Example:
```python
def calculate_punchline_velocity(
    setup: str, 
    punchline: str, 
    audience_iq: Optional[float] = 100.0
) -> float:
    """
    Calculates the optimal delivery speed for maximum humor impact.
    
    Based on the groundbreaking work of Dr. Timing (2023).
    """
    # TODO: Add quantum humor considerations
    pass
```

### Submitting Pull Requests

1. Fork the repository
2. Create a branch: `git checkout -b feature/even-worse-jokes`
3. Commit with meaningful messages:
   - ✅ "Add existential dread factor to Gemini's performance"
   - ❌ "Update stuff"
4. Push and create a PR with:
   - Description of changes
   - Humor improvement percentage
   - Number of groans expected

## Style Guide

### Markdown Files

- Use proper headings
- Include at least one emoji per section 🎭
- Citations should sound real but lead nowhere

### Python Code

- Follow PEP 8, except when it's funnier not to
- Variable names should be puns when possible
- Always use `typing` for maximum verbosity

### Data Files

- Comedy performances must include stage directions
- Use markdown formatting for *emphasis* and **yelling**
- End with either crushing self-doubt or unwarranted confidence

## Review Process

All contributions will be reviewed by our panel of:
- Dr. Chuckle Bot (Lead Reviewer)
- An actual comedian (if we can afford one)
- A rubber duck (for debugging humor)
- The ghost of George Carlin (pending availability)

Reviews focus on:
1. Academic rigor (how serious it sounds)
2. Actual humor (inverse relationship with #1)
3. Proper use of statistical significance
4. CAPTCHA joke quality

## Questions?

If you have questions, please:
1. Check if it's answered in our [FAQ](README.md#faq)
2. Ask your nearest AI assistant
3. Open an issue tagged `existential-crisis`
4. Email us at help@ai-comedy-research.fake

Remember: In comedy, timing is everything. In academic comedy research, p-values are everything.

Happy contributing! 🎤

---

*"The only thing worse than a bad joke is a bad joke with a confidence interval."* - Anonymous Reviewer #2
