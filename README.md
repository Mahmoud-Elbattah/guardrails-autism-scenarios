**Designing Guardrails to Align LLM-Generated Social Scenarios with the Needs of Autistic Learners**

This repository contains code and scenario templates for exploring the use of explicit guardrails to constrain LLM-generated social interaction scenarios designed for autistic learners. The focus is on low-stakes educational contexts and exploratory practice, not on clinical assessment or personalised intervention.

The repository accompanies a paper submitted to HealthINF 2026 and supports transparency and reproducibility.

**Contents**

Guardrails.ipynb – Main notebook for loading the model and running scenarios

scenarios_full.py – Scenario definitions, user-input variants, and guardrails

outputs/ – Generated outputs in JSONL format

**Scenarios**

The scenarios cover everyday academic and social situations (e.g. library interactions, online study groups, emotion recognition). Each scenario includes explicit constraints on tone, language, and response length to support predictable and appropriate dialogue.

**Model and Setup**

Model: Mistral-7B-Instruct-v0.3

Framework: Hugging Face transformers

Runtime: Google Colab

Inference: 4-bit quantised inference

**Scope**

This code is intended for research and educational exploration only. It is not designed for clinical use, diagnosis, or deployment as an assistive system.

**Citation**

Citation details will be added after publication.
