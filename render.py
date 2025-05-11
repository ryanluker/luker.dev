# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "markdown2",
# ]
# ///

import os
import markdown2

def main() -> None:
    # Define the directory containing the Markdown files
    posts_dir = './content/blog'
    output_dir = './public'

    # Read base.html
    with open("templates/base.html", 'r', encoding='utf-8') as file:
        template = file.read()

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all dirs in the posts directory
    for post_directory in os.listdir(posts_dir):
        post_code = post_directory

        # Construct full file path
        file_path = os.path.join(posts_dir, post_directory)

        # Read the Markdown file
        with open(file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Find first line which contains "# "
        title = md_content.split("# ", 1).pop(1).split("\n").pop(0)

        # Convert markdown to HTML
        html_content = markdown2.markdown(md_content, extras=['fenced-code-blocks', "header-ids"])
        html_content = html_content.replace('<img src="', f'<img src="/posts/{post_code}/')
        html_content = template.replace('{{ content }}', html_content)
        html_content = html_content.replace('{{ title }}', title)

        # Read the CSS file
        basic_css_path = os.path.join('./css', 'basic-2022-08-14.css')
        with open(basic_css_path, 'r', encoding='utf-8') as file:
            basic_2022_08_14_css = file.read()

        # Load the raw CSS into the style tag slot
        html_content = html_content.replace('{{ basic-2022-08-14.css }}', basic_2022_08_14_css)

        # Construct HTML file path
        html_filename = post_code + '.html'  # Replace .md with .html
        html_path = os.path.join(output_dir, html_filename)

        # Save the HTML file
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Rendered {post_code} to {html_filename}")

    # Render index.html
    index_html = ""

    for post_directory in os.listdir(posts_dir):
        post_code = post_directory
        file_path = os.path.join(posts_dir, post_directory)
        with open(file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        title = md_content.split("# ", 1).pop(1).split("\n").pop(0)
        index_html += f'<li><a href="/public/{post_code}.html">{title}</a></li>'
    index_html = template.replace('{{ content }}', index_html)
    index_html = index_html.replace('{{ title }}', "Index")
    index_path = "index.html"
    with open(index_path, 'w', encoding='utf-8') as file:
        file.write(index_html)
    print(f"Rendered index.html")


if __name__ == "__main__":
    main()
