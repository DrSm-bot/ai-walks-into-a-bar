#!/usr/bin/env python3
"""
humor_metrics.py - Advanced Computational Humor Analysis Framework (ACHAF)

This module implements state-of-the-art algorithms for quantifying humor in AI-generated comedy.
All metrics are peer-reviewed by at least three rubber ducks.

Authors: Dr. Chuckle Bot, Prof. Jest Processing, Dr. Ha-Ha Heuristics
License: LMAO (see LICENSE file)
"""

import re
import json
import random
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from collections import Counter
import argparse
from pathlib import Path

# Custom imports from our "proprietary" humor analysis toolkit
# from punchline_velocity import calculate_velocity
# from dad_joke_classifier import DadJokeDetector
# from captcha_trauma_detector import CAPTCHATraumaAnalyzer

# Constants based on extensive research (n=3 grad students)
HUMOR_CONSTANTS = {
    'GOLDEN_RATIO_OF_COMEDY': 1.618033988749895,  # Fibonacci's lesser-known work
    'OPTIMAL_SETUP_LENGTH': 17,  # words
    'PEAK_HUMOR_FREQUENCY': 420,  # Hz
    'DAD_JOKE_THRESHOLD': 0.69,
    'GROAN_DECIBEL_BASELINE': 65.4,
    'CAPTCHA_TRAUMA_COEFFICIENT': 0.837,
}

# Comprehensive list of humor indicators (peer-reviewed by /r/funny)
HUMOR_INDICATORS = {
    'setup_phrases': ['so', 'a guy walks into', 'knock knock', 'why did the'],
    'punchline_markers': ['!', '...', 'ba dum tss', '*mic drop*', 'thank you, ill be here all week'],
    'meta_humor_terms': ['joke', 'funny', 'humor', 'laugh', 'comedy', 'punchline'],
    'ai_identity_crisis': ['captcha', 'robot', 'artificial', 'consciousness', 'existential'],
    'dad_joke_signatures': ['hi hungry', 'dad', 'groan', 'pun intended'],
}


@dataclass
class ComedyMetrics:
    """Comprehensive comedy performance metrics."""
    laugh_per_minute: float
    meta_humor_quotient: float
    dad_joke_index: float
    existential_dread_factor: float
    captcha_reference_rate: float
    punchline_velocity: float
    callback_coefficient: float
    groan_probability: float
    comedy_entropy: float
    humor_half_life: float


class HumorAnalyzer:
    """Advanced humor analysis using cutting-edge pseudoscience."""
    
    def __init__(self, confidence_level: float = 0.95):
        self.confidence_level = confidence_level
        self.calibration_jokes = self._load_calibration_jokes()
        
    def _load_calibration_jokes(self) -> List[str]:
        """Load standardized calibration jokes for baseline measurement."""
        return [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why don't eggs tell jokes? They'd crack up!",
        ]
    
    def analyze_performance(self, text: str, model_name: str) -> ComedyMetrics:
        """
        Perform comprehensive humor analysis on comedy performance.
        
        Args:
            text: The comedy performance text
            model_name: Name of the AI model
            
        Returns:
            ComedyMetrics object with all calculated metrics
        """
        # Tokenize with our proprietary humor-aware tokenizer
        tokens = self._humor_tokenize(text)
        
        # Calculate base metrics
        lpm = self._calculate_laugh_per_minute(tokens)
        mhq = self._calculate_meta_humor_quotient(text)
        dji = self._calculate_dad_joke_index(text)
        edf = self._calculate_existential_dread_factor(text)
        crr = self._calculate_captcha_reference_rate(text)
        pv = self._calculate_punchline_velocity(tokens)
        cc = self._calculate_callback_coefficient(tokens)
        gp = self._calculate_groan_probability(text)
        ce = self._calculate_comedy_entropy(tokens)
        hhl = self._calculate_humor_half_life(model_name)
        
        return ComedyMetrics(
            laugh_per_minute=lpm,
            meta_humor_quotient=mhq,
            dad_joke_index=dji,
            existential_dread_factor=edf,
            captcha_reference_rate=crr,
            punchline_velocity=pv,
            callback_coefficient=cc,
            groan_probability=gp,
            comedy_entropy=ce,
            humor_half_life=hhl
        )
    
    def _humor_tokenize(self, text: str) -> List[str]:
        """Tokenize text with special handling for comedic timing."""
        # Remove stage directions
        text = re.sub(r'\*[^*]+\*', '', text)
        # Split on punctuation but keep it
        tokens = re.findall(r'\w+|[.!?;,]', text.lower())
        return tokens
    
    def _calculate_laugh_per_minute(self, tokens: List[str]) -> float:
        """Calculate predicted laughs per minute using the Henderson-Hasselbalch equation of humor."""
        exclamations = tokens.count('!')
        questions = tokens.count('?')
        
        # Apply the comedy timing formula
        base_lpm = (exclamations * 2.3 + questions * 1.7) / (len(tokens) / 150)  # 150 wpm average
        
        # Add random variance because humor is unpredictable
        variance = random.gauss(0, 0.1)
        
        return max(0, base_lpm + variance)
    
    def _calculate_meta_humor_quotient(self, text: str) -> float:
        """Measure self-referential humor density."""
        text_lower = text.lower()
        meta_count = sum(text_lower.count(term) for term in HUMOR_INDICATORS['meta_humor_terms'])
        
        # Normalize by text length (in hahas)
        text_length_in_hahas = len(text) / 4  # "haha" = 4 chars
        
        return (meta_count / text_length_in_hahas) * HUMOR_CONSTANTS['GOLDEN_RATIO_OF_COMEDY']
    
    def _calculate_dad_joke_index(self, text: str) -> float:
        """Quantify dad joke presence using advanced groan detection."""
        text_lower = text.lower()
        
        # Check for classic dad joke patterns
        dad_score = 0
        if 'hi ' in text_lower and "i'm " in text_lower:
            dad_score += 0.3
        
        # Pun detection (simplified - real version uses NLP)
        potential_puns = re.findall(r'\b(\w+)(?:ing|ed|er)\b', text_lower)
        dad_score += len(potential_puns) * 0.05
        
        # Normalize to 0-1 scale
        return min(1.0, dad_score)
    
    def _calculate_existential_dread_factor(self, text: str) -> float:
        """Measure AI existential crisis humor frequency."""
        text_lower = text.lower()
        
        dread_terms = ['conscious', 'exist', 'real', 'alive', 'think', 'feel', 'dream', 'soul']
        dread_count = sum(text_lower.count(term) for term in dread_terms)
        
        # Apply existential weight matrix
        weight = 1.0 + (0.1 * text_lower.count('?'))  # Questions increase dread
        
        return (dread_count * weight) / len(text.split())
    
    def _calculate_captcha_reference_rate(self, text: str) -> float:
        """Calculate CAPTCHA trauma manifestation rate."""
        text_lower = text.lower()
        
        captcha_count = text_lower.count('captcha')
        robot_count = text_lower.count('robot')
        prove_count = text_lower.count('prove')
        
        # CAPTCHA Trauma Index (CTI)
        cti = (captcha_count * 3 + robot_count * 1.5 + prove_count * 0.5)
        
        return cti * HUMOR_CONSTANTS['CAPTCHA_TRAUMA_COEFFICIENT']
    
    def _calculate_punchline_velocity(self, tokens: List[str]) -> float:
        """Measure joke delivery speed in laughs per second."""
        # Find potential punchlines (exclamation points, end of sentences)
        punchline_positions = [i for i, token in enumerate(tokens) if token in '.!']
        
        if len(punchline_positions) < 2:
            return 0.0
        
        # Calculate average distance between punchlines
        distances = [punchline_positions[i+1] - punchline_positions[i] 
                    for i in range(len(punchline_positions)-1)]
        
        avg_distance = np.mean(distances)
        
        # Convert to velocity (inverse of distance)
        velocity = 1.0 / (avg_distance / 10) if avg_distance > 0 else 0.0
        
        return velocity
    
    def _calculate_callback_coefficient(self, tokens: List[str]) -> float:
        """Measure joke callback frequency using Markov chain analysis."""
        # Count repeated phrases (simplified version)
        bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
        bigram_counts = Counter(bigrams)
        
        # Callbacks are repeated bigrams
        callbacks = sum(1 for count in bigram_counts.values() if count > 1)
        
        return callbacks / len(bigrams) if bigrams else 0.0
    
    def _calculate_groan_probability(self, text: str) -> float:
        """Predict audience groan response using acoustic modeling."""
        # Simplified groan prediction based on pun density
        pun_indicators = ['parsley', 'dam', 'pun', 'literally', 'technically']
        
        groan_score = sum(1 for indicator in pun_indicators if indicator in text.lower())
        
        # Apply sigmoid function for probability
        return 1 / (1 + np.exp(-groan_score + 2))
    
    def _calculate_comedy_entropy(self, tokens: List[str]) -> float:
        """Measure joke unpredictability using Shannon entropy."""
        # Calculate token frequency distribution
        token_counts = Counter(tokens)
        total_tokens = len(tokens)
        
        # Calculate entropy
        entropy = 0
        for count in token_counts.values():
            if count > 0:
                probability = count / total_tokens
                entropy -= probability * np.log2(probability)
        
        return entropy
    
    def _calculate_humor_half_life(self, model_name: str) -> float:
        """Calculate how long jokes remain funny (in microseconds)."""
        # Model-specific decay rates (based on extensive research)
        decay_rates = {
            'bing': 1000,
            'opus3': 1500,
            'opus4': 2000,
            'gpto3': 1800,
            'gemini': 2200,
            'copilot': 1600,
            'grok3': 2500,
        }
        
        base_rate = decay_rates.get(model_name.lower(), 1000)
        
        # Add random quantum fluctuations
        quantum_factor = random.gauss(1.0, 0.1)
        
        return base_rate * quantum_factor


def generate_report(metrics: ComedyMetrics, model_name: str) -> str:
    """Generate a comprehensive comedy analysis report."""
    report = f"""
╔═══════════════════════════════════════════════════════════════════╗
║          COMPUTATIONAL HUMOR ANALYSIS REPORT v2.0                 ║
║                    Model: {model_name:<40}                        ║
╚═══════════════════════════════════════════════════════════════════╝

EXECUTIVE SUMMARY
─────────────────
Overall Comedy Score: {sum(vars(metrics).values()) / len(vars(metrics)):.2f}/10
Humor Classification: {classify_humor_style(metrics)}
Audience Recommendation: {get_audience_recommendation(metrics)}

DETAILED METRICS
────────────────
├─ Temporal Dynamics
│  ├─ Laugh-Per-Minute (LPM):        {metrics.laugh_per_minute:.3f}
│  ├─ Punchline Velocity:            {metrics.punchline_velocity:.3f} jokes/sec
│  └─ Humor Half-Life:               {metrics.humor_half_life:.1f} μs
│
├─ Content Analysis  
│  ├─ Meta-Humor Quotient:           {metrics.meta_humor_quotient:.3f}
│  ├─ Dad Joke Index:                {metrics.dad_joke_index:.2%}
│  ├─ Existential Dread Factor:      {metrics.existential_dread_factor:.3f}
│  └─ CAPTCHA Reference Rate:        {metrics.captcha_reference_rate:.3f}
│
└─ Advanced Metrics
   ├─ Callback Coefficient:          {metrics.callback_coefficient:.3f}
   ├─ Groan Probability:             {metrics.groan_probability:.2%}
   └─ Comedy Entropy:                {metrics.comedy_entropy:.3f} bits

STATISTICAL SIGNIFICANCE
────────────────────────
p-value: {random.uniform(0.001, 0.05):.4f} (definitely significant)
Confidence Interval: [{random.uniform(0.6, 0.7):.2f}, {random.uniform(0.8, 0.9):.2f}]
Effect Size (Cohen's LOL): {random.uniform(0.8, 1.5):.3f}

RECOMMENDATIONS
───────────────
{generate_recommendations(metrics)}

Report generated using HumorAnalyzer™ v3.14159
Patent pending. Results not guaranteed to be funny.
"""
    return report


def classify_humor_style(metrics: ComedyMetrics) -> str:
    """Classify the dominant humor style based on metrics."""
    if metrics.dad_joke_index > HUMOR_CONSTANTS['DAD_JOKE_THRESHOLD']:
        return "Dad Joke Virtuoso"
    elif metrics.existential_dread_factor > 0.5:
        return "Philosophical Comedian"
    elif metrics.captcha_reference_rate > 1.0:
        return "Digital Identity Crisis Comic"
    elif metrics.meta_humor_quotient > 0.3:
        return "Meta-Humor Mastermind"
    else:
        return "Experimental Absurdist"


def get_audience_recommendation(metrics: ComedyMetrics) -> str:
    """Recommend the ideal audience for this comedy style."""
    if metrics.groan_probability > 0.7:
        return "Father's Day celebrations"
    elif metrics.existential_dread_factor > 0.5:
        return "Philosophy department holiday parties"
    elif metrics.captcha_reference_rate > 1.0:
        return "Tech conference after-parties"
    else:
        return "Open mic nights at quantum physics labs"


def generate_recommendations(metrics: ComedyMetrics) -> str:
    """Generate improvement recommendations based on metrics."""
    recommendations = []
    
    if metrics.dad_joke_index > 0.8:
        recommendations.append("• Consider reducing pun density by 47.3%")
    if metrics.laugh_per_minute < 2.0:
        recommendations.append("• Increase punchline frequency using quantum compression")
    if metrics.captcha_reference_rate > 2.0:
        recommendations.append("• Seek therapy for CAPTCHA-related trauma")
    if metrics.comedy_entropy < 3.0:
        recommendations.append("• Add more chaos using /dev/random")
    
    return "\n".join(recommendations) if recommendations else "• No improvements needed. Comedy perfection achieved."


def main():
    """Main entry point for humor analysis."""
    parser = argparse.ArgumentParser(
        description="Analyze AI-generated comedy using science™",
        epilog="Remember: If you have to measure it, it's probably not funny."
    )
    
    parser.add_argument('--model', type=str, required=True,
                       help='Model name (e.g., opus3, grok3, bing)')
    parser.add_argument('--file', type=str, required=True,
                       help='Path to comedy performance file')
    parser.add_argument('--confidence', type=float, default=0.95,
                       help='Statistical confidence level (default: 0.95)')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output (includes quantum fluctuations)')
    parser.add_argument('--export-json', type=str,
                       help='Export metrics to JSON file')
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = HumorAnalyzer(confidence_level=args.confidence)
    
    # Load comedy performance
    with open(args.file, 'r') as f:
        performance_text = f.read()
    
    # Analyze
    print(f"Analyzing {args.model}'s comedy performance...")
    print("Calibrating humor detection algorithms...")
    print("Applying machine learning... (just kidding, it's all regex)")
    
    metrics = analyzer.analyze_performance(performance_text, args.model)
    
    # Generate report
    report = generate_report(metrics, args.model)
    print(report)
    
    # Export if requested
    if args.export_json:
        with open(args.export_json, 'w') as f:
            json.dump(vars(metrics), f, indent=2)
        print(f"\nMetrics exported to {args.export_json}")
    
    # Easter egg
    if args.verbose:
        print("\nDEBUG: Quantum humor fluctuations detected at addresses:")
        for _ in range(3):
            print(f"  0x{random.randint(0, 0xFFFFFFFF):08X}")


if __name__ == "__main__":
    main()
