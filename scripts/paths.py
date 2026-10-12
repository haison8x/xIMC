"""Repository layout shared by the scripts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMC_PAPERS = ROOT / "papers" / "imc"    # keystage{2,3}/{year}[_team|_answer].pdf
IMSO_PAPERS = ROOT / "papers" / "imso"  # {ShortAnswer,Essay,Exploration,Answers}/IMSO_*.pdf
IMAS_PAPERS = ROOT / "papers" / "imas"  # {middle_primary,upper_primary,junior,answers}/{year}_round{1,2}.pdf
DATA = ROOT / "data"                    # extracted problems and categorisations (*.txt)
MINDMAPS = ROOT / "mindmaps"            # generated mind map pages
