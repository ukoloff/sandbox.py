#
# Hand-made prompts
#
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

src = Path(__file__).parents[1] / "data" / "contexts.yml"
qs = yaml.safe_load(src.open('r', encoding='utf-8'))
print(qs)
