import pandas as pd
import jinja2

SHEET_URL = "https://docs.google.com/spreadsheets/d/1DqCJy4qOGNR4UD-PLHOQwyByDBlHdS4NLL-_jd4JS9U/export?format=csv"

df = pd.read_csv(SHEET_URL)
df = df.drop(['Timestamp', 'Contact email (for internal use only)'], axis=1)
df = df.reindex(columns=['Core facility name', 'Services', 'Equipment', 'Expertise','Website', 'Address',
       'Organization', 'Access model'])
df.Website = df.Website.apply(lambda url: f'<a href="{url}">{url}</a>')
# df['Contact email'] = df['Contact email'].apply(lambda email: f'<a href="mailto:{email}">{email}</a>')

with open('template.html') as f:
    raw_template = f.read()
# Generate HTML from template.
template = jinja2.Template(raw_template)

output_html = template.render(dataframe=df.to_html(table_id="myTable", index=False, escape=False, border = 0, classes='table table-striped'))

# Write generated HTML to file.
with open("build/index.html", "w", encoding="utf-8") as file_obj:
    file_obj.write(output_html)