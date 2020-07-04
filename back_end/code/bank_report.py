import urllib.request
from bs4 import BeautifulSoup


class Bank_Report:
    def __init__(self, config, db):
        self.config = config

    def downlad_rbi_page(self):
        html_content = ""
        request = urllib.request.Request(self.config["RBI_URL"])
        page = urllib.request.urlopen(request)
        html_content = page.read()
        return html_content

    def get_bank_links_from_HTML(self, html_content):
        parsed_content = BeautifulSoup(html_content, 'html.parser')
        parsed_table = parsed_content.find('table', class_='tablebg')
        anchor_links = parsed_table.find_all('a')
        bank_links = []
        for anchor_link in anchor_links:
            new_data = {}
            new_data["name"] = str(anchor_link.text)
            new_data["link"] = anchor_link.get('href')
            bank_links.append(new_data)
        return bank_links
