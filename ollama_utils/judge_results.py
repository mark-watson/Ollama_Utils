"""
Judge results from LLM generation from prompts
"""

from typing import Optional, Dict, Any
from pathlib import Path
import json
import re

import aisuite as ai

client = ai.Client()

def judge_results(original_prompt: str, llm_gen_results: str) -> Dict[str, str]:
  """
  Takes an original prompt to a LLM and the utput results

  Args:
      original_prompt (str): original pronpt to a LLM
      llm_gen_results (str): output frm the LLM that this function judges for accuracy

  Returns:
      result: str: string that is one character with one of these values:
          - 'B': Bad result
          - 'G': A Good result
  """
  try:

    messages = [
        #{"role": "system", "content": "You are an expert at judging or evaluating output from an LLM, when shown the original prompt. You answer for accurate/good with a Y and for inaccurate/bad with a N, following by a blank line and then your final reasoning."},
        {"role": "user", "content": f"Evaluate if this original prompt:\n\n{original_prompt}\n\nIs accurately answered by this output (Answer Y or N, followed by your reason):\n\n{llm_gen_results}\n"},
    ]

    response = client.chat.completions.create(
                 "ollama:llama3.2:latest", # model="ollama:marco-o1",
                 messages=messages,
                 temperature=0.0)
    r = response.choices[0].message.content.strip()
    print(f"\n\noriginal COT response:\n\n{r}\n\n")
    
    # next two lines only for marco-o1 chain of thought model:
    match = re.search(r'<Output>(.*?)</Output>', r, re.DOTALL)
    r = match.group(1).strip() if match else None
      
    #print(f"Complete response from JUDGE:\n\n{r}\n")
    return {'judgement': r[0], 'reasoning': r[1:].strip()}

  except Exception as e:
      print(f"\n\n***** {e=}\n\n")
      return {'judgement': 'E', 'reasoning': str(e)} # on any error, assign'E' result
