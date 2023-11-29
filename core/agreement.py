from dataclasses import dataclass
from typing import Any, List

@dataclass
class Agreement:
    text: Any = None
    initial_text: Any = None
    agreenent_language: str = None
    agreement_input_type: int = None
    agreement_output_type: int = None
    agreenent_context: bool = None
    agreenent_context_text: str = None
    agreement_error: int = 0
    agreement_marked: List[List[int]] = None