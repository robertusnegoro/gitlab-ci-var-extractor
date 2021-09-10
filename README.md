# Gitlab CI Var extractor

output to yaml, pipe to stdout

Prereq :
- Gitlab Private Access Token with permission to read CI Var

```
python3 -m venv /path/to/myenv
source /path/to/myenv/bin/activate
pip install -U pip
pip install -Ur requirements.txt

export GITLAB_TOKEN=yourprivateaccesstoken
# change this with your gitlab repo site
export GITLAB_URL=https://gitlab.com

python main.py <group_id> >> filename.yaml

```