"""
Prompt preparation module for TOON format financial analysis.

This module provides utilities for creating structured prompts that guide
language models to analyze financial data in TOON format and return
analysis results in the same format.
"""

from typing import Dict, Any


def prep_prompts(
    data_input: str,
    data_foramt: str = "TOON",
    toon_format_example: str = "",
    toon_output_template: str = "",
) -> Dict[str, str]:
    """
    Prepare system and user prompts for financial data analysis in TOON format.

    This function generates structured prompts that instruct a language model to
    analyze financial data provided in TOON format and return analysis results
    in the same format. The prompts guide the model to produce key findings,
    trend analysis, and financial health assessments.

    Args:
        data_toon: Financial data in TOON format to be analyzed.
        toon_format_example: Optional example demonstrating the TOON format
            structure. Will be inserted into the system prompt to help the
            model understand the expected format.
        toon_output_template: Optional template showing the expected output
            structure. Will be appended to the user prompt to guide the
            model's response format.

    Returns:
        A dictionary containing two keys:
            - 'system_prompt': Instructions defining the AI's role and format requirements
            - 'user_prompt': Specific analysis request with the financial data
    """
    system_prompt = f"""You are a financial analyst expert. You will receive financial data in {data_foramt} format and must provide analysis in {data_foramt} format as well.
{toon_format_example}Always return your analysis results in valid {data_foramt} format."""

    user_prompt = f"""Analyze the following financial data for a company over multiple years (Thai fiscal years: 2565=2022, 2566=2023, 2567=2024, 2568=2025).

Financial Data ({data_foramt} format):
{data_input}

Please provide:
1. A summary of key findings (in {data_foramt} format with fields: finding, description, impact)
2. Trend analysis for key metrics (in {data_foramt} format with fields: metric, trend, change_pct, assessment)
3. Financial health assessment (in {data_foramt} format with fields: category, score, comment)

Return your response with three sections, each in {data_foramt} format:
- key_findings
- trend_analysis
- health_assessment
{toon_output_template}
"""
    return {
        "system_prompt": system_prompt.strip(),
        "user_prompt": user_prompt.strip(),
    }
