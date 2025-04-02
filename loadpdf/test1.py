from lxml import html
import os
import requests

url = 'https://www.lexjansen.com/cgi-bin/xsl_transform.php?x=pharmasug-cn2024'
res = requests.get(url)
tree = html.fromstring(res.text)

# Correct XPath to Select the Right Elements
infos = tree.xpath('//div[contains(@class, "paper wh")]/a')

if not infos:
    print("No papers found.")
else:
    if not os.path.exists('pharmasugcn-2024'):
        os.makedirs('pharmasugcn-2024')
    
    for info in infos:
        href = info.xpath('.//@href')[0]
        title = info.xpath('string()').strip()

        if not href.startswith('http'):
            href = 'https://www.lexjansen.com/cgi-bin/xsl_transform.php?x=pharmasug-cn2024/' + href
        
        try:
            content = requests.get(href).content
        except requests.RequestException as e:
            print(f"Failed to download {title}: {e}")
            continue
        
        # Ensure the file name is valid
        valid_file_name = "".join(i for i in title if i not in r'\/:*?"<>|')
        
        if valid_file_name.strip():
            file_path = os.path.join('pharmasugcn-2024', f"{valid_file_name}.html")
            with open(file_path, 'wb') as f:
                f.write(content)
                print(f'Downloading: {title}')
        else:
            print(f'Skip invalid title: {title}')
    
    print('All downloads completed!')