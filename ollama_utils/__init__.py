"""
Ollama LLM provider Utils Library
Provides a collection of utility functions for working with LLMs via Ollama
"""

from typing import List, Callable
from .judge_results import judge_results

# Make commonly used functions available at package level
__all__ = [
  'judge_results'
]


