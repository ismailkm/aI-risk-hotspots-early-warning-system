CATEGORY_DEFINITIONS = {
    "Malicious Use & Security": "Incidents where AI was intentionally used for harmful purposes (e.g., scams, deepfakes) or where an AI system was compromised by a security vulnerability.",
    "Fairness, Bias & Discrimination": "Incidents where an AI system produced biased outputs that resulted in unfair or discriminatory treatment of individuals or groups.",
    "Safety, Robustness & Reliability": "Incidents where the AI system failed to perform safely or reliably in a real-world environment, including software bugs, hardware failures, or unpredictable behavior (e.g., autonomous vehicle crashes).",
    "Privacy & Data Protection": "Incidents involving the unauthorized collection, use, or exposure of personal data by AI systems, or other violations of privacy.",
    "Transparency & Explainability": "Incidents where harm was caused or worsened by an inability to understand, interpret, or challenge an AI system's decision-making process.",
    "Societal & Economic Impact": "Incidents representing broad, systemic harms, such as the spread of misinformation at scale, market manipulation, or significant job displacement.",
    "Human-Computer Interaction & Autonomy": "Incidents where the design of the interaction between the human and the AI system led to harm, often due to a lack of human oversight or a confusing interface.",
    "Data Quality & Integrity": "Incidents where the root cause of the harm was flawed, noisy, or unrepresentative data used to train or operate the AI model.",
    "System & Task Mismatch": "Incidents where the AI was technically working as designed, but its core objective was misaligned with the desired, safe outcome (e.g., a recommendation engine optimizing for engagement instead of user well-being).",
    "Uncategorized": "Incidents that could not be confidently assigned to a single, primary harm category."
}

CATEGORY_KEYWORDS = {
    "Malicious Use & Security": ["scam", "fraud", "deepfake", "malicious", "exploit", "cyberattack", "phishing", "malware"],
    "Fairness, Bias & Discrimination": ["bias", "discrimination", "racist", "sexist", "unfair", "algorithmic bias", "prejudice"],
    "Safety, Robustness & Reliability": ["crash", "error", "fail", "accident", "unsafe", "robustness", "unreliable", "malfunction"],
    "Privacy & Data Protection": ["privacy", "leak", "surveillance", "data breach", "exposed", "consent"],
    "Transparency & Explainability": ["explainability", "transparent", "black box", "opaque", "accountability"],
    "Societal & Economic Impact": ["misinformation", "disinformation", "jobs", "economy", "propaganda", "election"],
    "Human-Computer Interaction & Autonomy": ["oversight", "autonomy", "human error", "interface", "automation"],
    "Data Quality & Integrity": ["data quality", "flawed data", "unrepresentative", "noisy data", "labeling error"],
    "System & Task Mismatch": ["misaligned", "objective", "loophole", "reward hacking", "unintended"],
    "Uncategorized": []
}