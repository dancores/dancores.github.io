import pandas as pd
import jinja2

SHEET_URL = "https://docs.google.com/spreadsheets/d/1DqCJy4qOGNR4UD-PLHOQwyByDBlHdS4NLL-_jd4JS9U/export?format=csv"

df = pd.read_csv(SHEET_URL)
df = df.drop(['Timestamp', 'Contact email'], axis=1)
df = df.reindex(columns=['Core facility name', 'Services', 'Equipment', 'Expertise','Website', 'Address',
       'Organization', 'Access model'])
print(df.columns)
df.Website = df.Website.apply(lambda url: f'<a href="{url}">{url}</a>')
# df['Contact email'] = df['Contact email'].apply(lambda email: f'<a href="mailto:{email}">{email}</a>')


# Generate HTML from template.
template = jinja2.Template("""<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Demo</title>
    <link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
    <script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest" type="text/javascript"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-uWxY/CJNBR+1zjPWmfnSnVxwRheevXITnMqoEIeG1LJrdI0GlVs/9cVSyPYXdcSF" crossorigin="anonymous">
    <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="./table-style.css">
    </head>
    <h1>Danish Core Facilities</h1>
    <body>

        <p>This websites lists Danish Life Science Research core facilities in an easy to search format.
        Please contact Nikolaus Sonnenschein (<a href="mailto:niso@dtu.dk">niso@dtu.dk</a>) or Magali Michaut (<a href="mailto:magali.michaut@sund.ku.dk">magali.michaut@sund.ku.dk</a>) if you are leading a core facility
        in Denmark and would like to add it to this list. For inquiries to the respective facilities, please contact them directly by using the contact information provided on their websites.</p>

        <div class="table-responsive">
            {{ dataframe }}
        </div>

    </body>

    <script defer type="text/javascript">
        let myTable = new simpleDatatables.DataTable("#myTable");
    </script>

</html>"""
)

output_html = template.render(dataframe=df.to_html(table_id="myTable", index=False, escape=False, border = 0, classes='table table-striped'))

# Write generated HTML to file.
with open("build/index.html", "w", encoding="utf-8") as file_obj:
    file_obj.write(output_html)