"""
Example script demonstrating the usage of LLM tools
"""

from ollama_utils import *
from ollama_utils.judge_results import judge_results

import aisuite as ai

def separator(title: str):
  """Prints a section separator"""
  print(f"\n{'='*50}")
  print(f" {title}")
  print('='*50)

def main():
  # Test file writing
  separator("Judge output from a LLM")
  test_prompt = "Sally is 55, John is 18, and Mary is 31. What are their pairwise absolute value age differences?"
  test_output = "Sally is 37 years older than John. Sally is  24 years older than Mary. Mary is 13 years older than John."

  
  client = ai.Client()
  judgement = judge_results(test_prompt, test_output)
  print(f"\n** good ***\n\n{judgement=}")

  bad_test_output = "Sally is 37 years older than John. Sally is  24 years older than Mary. Mary is 15 years older than John."

  judgement = judge_results(test_prompt, bad_test_output)
  print(f"\n** bad ***\n\n{judgement=}")
  
if __name__ == "__main__":
  try:
      main()
  except Exception as e:
      print(f"An error occurred: {str(e)}")

