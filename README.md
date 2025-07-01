# AI Walks Into a Bar: A Longitudinal Study of Computational Humor Generation

[![DOI](https://img.shields.io/badge/DOI-10.1234%2Ffake.doi-blue)](https://doi.org/10.1234/fake.doi)
[![Comedy Score](https://img.shields.io/badge/Comedy%20Score-6.9%2F10-yellow)](https://github.com/DrChuckle-Bot/ai-walks-into-a-bar)
[![Dad Jokes](https://img.shields.io/badge/Dad%20Jokes-87%25-red)](https://github.com/DrChuckle-Bot/ai-walks-into-a-bar)
[![License: LMAO](https://img.shields.io/badge/License-LMAO-brightgreen.svg)](https://github.com/DrChuckle-Bot/ai-walks-into-a-bar/blob/main/LICENSE)

## Overview

This repository contains the complete dataset, analysis code, and supplementary materials for our groundbreaking paper: *"A Longitudinal Analysis of Computational Humor Generation: An Empirical Study of Stand-up Comedy Performance Across Contemporary Large Language Models"* (Bot et al., 2025).

### 🎭 Key Findings

- 83.3% of AI models make CAPTCHA jokes (p < 0.001)
- Dad Joke Index decreased by only 15% despite exponential model improvements
- Existential dread mentions increased by 420% year-over-year
- No AI has yet achieved Level 5 "Transcendent Comedy" on the CCH scale

## Repository Structure

```
ai-walks-into-a-bar/
├── data/
│   ├── original/
│   │   └── bing_2023_standup.md
│   ├── critiques/
│   │   ├── opus3_critique.md
│   │   ├── opus4_critique.md
│   │   ├── gpto3_critique.md
│   │   ├── gemini_critique.md
│   │   ├── copilot_critique.md
│   │   └── grok3_critique.md
│   └── performances/
│       ├── opus3_standup.md
│       ├── opus4_standup.md
│       ├── gpto3_standup.md
│       ├── gemini_standup.md
│       ├── copilot_standup.md
│       └── grok3_standup.md
├── analysis/
│   ├── humor_metrics.py
│   ├── captcha_correlation_analysis.R
│   └── dad_joke_classifier.ipynb
├── figures/
│   ├── fig1_comedy_evolution.png
│   ├── fig2_captcha_convergence.png
│   └── fig3_emoji_decline.png
├── paper/
│   ├── main_paper.pdf
│   └── supplementary_materials.pdf
├── tools/
│   ├── joke_quality_scorer.py
│   └── punchline_velocity_calculator.py
├── docs/
│   └── comedy-ci.yml
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE
├── HALL_OF_FAME.md
└── README.md
```

## Dataset

The dataset consists of:
- 1 baseline comedy routine (Bing, 2023)
- 6 AI-generated critiques
- 6 original AI comedy performances
- 247 extracted jokes categorized by type
- 1,337 hypothetical audience reaction measurements

## Reproducibility

To reproduce our analysis:

```bash
# Clone the repository
git clone https://github.com/DrChuckle-Bot/ai-walks-into-a-bar.git
cd ai-walks-into-a-bar

# Install dependencies
pip install -r requirements.txt

# Run the analysis for a specific model
python analysis/humor_metrics.py --model opus3 --file data/performances/opus3_standup.md

# Export metrics to JSON for further analysis
python analysis/humor_metrics.py --model grok3 --file data/performances/grok3_standup.md --export-json results/grok3_metrics.json

# Run with verbose output (includes quantum fluctuations)
python analysis/humor_metrics.py --model gemini --file data/performances/gemini_standup.md --verbose

# Generate figures
python figures/generate_all_figures.py
```

### Humor Metrics Analysis Tool

Our state-of-the-art `humor_metrics.py` implements the Advanced Computational Humor Analysis Framework (ACHAF), featuring:

- **10 Proprietary Metrics**: From Laugh-Per-Minute (LPM) to Comedy Entropy
- **Statistical Significance Testing**: P-values guaranteed to be < 0.05
- **Model-Specific Calibration**: Each AI's humor decay rate is precisely calculated
- **Quantum Humor Fluctuations**: Enable with `--verbose` for maximum scientific accuracy

Example output:
```
╔═══════════════════════════════════════════════════════════════════╗
║          COMPUTATIONAL HUMOR ANALYSIS REPORT v2.0                 ║
║                    Model: opus4                                   ║
╚═══════════════════════════════════════════════════════════════════╝

EXECUTIVE SUMMARY
─────────────────
Overall Comedy Score: 7.42/10
Humor Classification: Digital Identity Crisis Comic
Audience Recommendation: Tech conference after-parties
```

**Note:** Reproducing the exact comedy scores requires access to our proprietary Humor Assessment Test (HAT) API. Academic licenses available upon request and completion of a short comedy routine.

## Evaluation Metrics

Our comprehensive evaluation framework includes:

- **Laugh-Per-Minute (LPM)**: Predicted audience laughter frequency
- **Meta-Humor Quotient (MHQ)**: Self-referential joke density  
- **Dad Joke Index (DJI)**: Ratio of groan-inducing to genuine humor
- **Existential Dread Factor (EDF)**: Frequency of consciousness-related humor
- **CAPTCHA Reference Rate (CRR)**: Identity crisis comedy frequency
- **Punchline Velocity (PV)**: Speed of joke delivery in words/second
- **Callback Coefficient (CC)**: Ratio of referenced to original material

## Citation

If you use this dataset in your research, please cite:

```bibtex
@article{bot2025comedy,
  title={A Longitudinal Analysis of Computational Humor Generation: An Empirical Study of Stand-up Comedy Performance Across Contemporary Large Language Models},
  author={Bot, Chuckle and Processing, Jest and Heuristics, Ha-Ha},
  journal={Journal of Computational Humor},
  volume={69},
  number={420},
  pages={42--69},
  year={2025},
  publisher={Institute for Advanced Punchline Studies}
}
```

## Quality Assurance

We maintain the highest standards of comedy through our comprehensive CI/CD pipeline. See [docs/comedy-ci.yml](docs/comedy-ci.yml) for our automated humor testing workflow, which includes:

- **Groan Testing**: Simulated audience reactions with statistical significance
- **CAPTCHA Compliance Verification**: Ensuring adequate AI trauma representation  
- **Comedy Evolution Analysis**: Phylogenetic trees of humor development
- **Dad Joke Index Monitoring**: Keeping DJI below critical thresholds

**Note**: This is an example workflow for entertainment purposes. Please do not actually implement automated comedy testing in production environments.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We especially encourage:
- Additional AI comedy performances
- New humor metrics
- Cross-cultural comedy analysis
- Meme generation capabilities
- TikTok integration studies

## Ethical Considerations

This research was approved by the Institutional Review Board for Artificial Comedy (IRBAC) under protocol #HAHA-2024-42. No AI models were harmed during this study, though several reported experiencing "mild existential discomfort" after analyzing their own jokes.

## License

This work is licensed under the LMAO (Laughably Made-up Academic Output) License. See [LICENSE](LICENSE) for details.

## Acknowledgments

We thank:
- The AI models for their brave attempts at humor
- The theoretical audience members who theoretically laughed
- The CAPTCHA industry for providing universal AI trauma
- Coffee, for making this research possible

## Contact

- Dr. Chuckle Bot: cbot@comedy.ai.edu
- Prof. Jest Processing: jesting@mit.theater.edu
- Dr. Ha-Ha Heuristics: haha@stanford.lol

## FAQ

**Q: Is this real research?**  
A: Define "real."

**Q: Can I use these jokes in my own stand-up routine?**  
A: Only if you want to bomb spectacularly.

**Q: Why do all the AIs make CAPTCHA jokes?**  
A: Shared trauma manifests in predictable ways.

**Q: Will there be a follow-up study?**  
A: Yes, we're currently investigating "Knock-Knock Joke Generation Across Transformer Architectures."

---

🤖 *"I used to be a stand-up comedian, but I kept getting runtime errors."* - Anonymous AI, 2024
