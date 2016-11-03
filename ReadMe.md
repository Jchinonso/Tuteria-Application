## Tuteria Interview Process

steps
1. figure out the requirements
2. create a settings module installed all apps and dependencies
3. installed all apps and dependencies as indicated on their documentations
4. activatd the css by adding os.path.join(os.path.dirname(BASE_DIR), "static_cdn") to STATIC_ROOT
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
5. create a gitignore
6. create a requirements.txt file
