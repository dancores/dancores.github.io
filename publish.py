import pandas as pd
import jinja2

SHEET_URL = "https://docs.google.com/spreadsheets/d/1DqCJy4qOGNR4UD-PLHOQwyByDBlHdS4NLL-_jd4JS9U/export?format=csv"

df = pd.read_csv(SHEET_URL)
df = df.drop(['Timestamp'], axis=1)
df.Website = df.Website.apply(lambda url: f'<a href="{url}">{url}</a>')
df['Contact email'] = df['Contact email'].apply(lambda email: f'<a href="mailto:{email}">{email}</a>')


# Generate HTML from template.
template = jinja2.Template("""<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Demo</title>
    <link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
    <script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest" type="text/javascript"></script>
    <link rel="stylesheet" href="./style.css">
    </head>
    <h1>Danish Core Facilities</h1>
    <body>

        {{ dataframe }}

    </body>

    <script defer type="text/javascript">
        let myTable = new simpleDatatables.DataTable("#myTable");
    </script>

</html>"""
                               )

output_html = template.render(dataframe=df.to_html(table_id="myTable", index=False, escape=False))

# Write generated HTML to file.
with open("index.html", "w", encoding="utf-8") as file_obj:
    file_obj.write(output_html)