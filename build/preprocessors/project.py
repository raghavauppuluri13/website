from pathlib import Path
from bs4 import BeautifulSoup
import requests

SENTINAL = "PROJECT"


def create_tile(description, img_strs, gh_link):

    combine_imgs = '\n'.join(img_strs)

    return '''\n
<div class="r-stack">
<a class="project-tile" href="{}">
<div class="image-grid">
{}
</div>
<p>{}</p>
</a>
</div>
'''.format(gh_link, combine_imgs, description)


def get_readme_images(user_repo):
    url = f"https://github.com/{user_repo}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all img elements
    images = soup.find_all('img')

    # Generate HTML for each image
    html = [
        f'<img src="{img["src"]}" alt="{img.get("alt", "")}"/>' for img in images if img.get("src")
        and not 'avatar' in str(img)]

    #print(html)

    return html


def get_repo_description(user_repo):
    url = f"https://api.github.com/repos/{user_repo}"
    response = requests.get(url)
    data = response.json()
    return data.get('description', "No description provided")


def process_project_line(line: str, file: Path, root_dir: Path) -> str:
    user_repo = Path(line.strip())
    url = f"https://github.com/{user_repo}"
    html_imgs = get_readme_images(user_repo)
    desc = get_repo_description(user_repo)
    tile = create_tile(desc, html_imgs, url).strip()
    return tile
