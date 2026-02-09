import os
from ohmyscrapper import config
import sqlite3
import pandas as pd
import json
from urlicon import urlicon

urlicon.load_dotenv()
import random
import string
import shutil
from datetime import datetime,timedelta
def main():
    clean_dir("./public")
    clean_dir("./public/js")
    clean_dir("./public/css")
    clean_dir("./public/images")

    ensure_dir("./public/js")
    shutil.copy("./templates/js/script.js","./public/js/script.js",)

    ensure_dir("./public/css")
    shutil.copy("./templates/css/style.css","./public/css/style.css",)

    ensure_dir("./public/images")
    shutil.copy("./templates/images/hero.jpeg","./public/images/hero.jpeg",)

    ensure_dir("./public/icons")


    last_date = datetime.today()
    first_date = last_date - timedelta(days=8)

    last_date = "/".join(reversed(str(last_date).split(" ")[0].split("-")))
    first_date = "/".join(reversed(str(first_date).split(" ")[0].split("-")))

    render_items = get_items_string()

    random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    js_file_name = f"js/{random_name}.js"

    last_date = datetime.today()
    first_date = last_date - timedelta(days=8)

    last_date = "/".join(reversed(str(last_date).split(" ")[0].split("-")))
    first_date = "/".join(reversed(str(first_date).split(" ")[0].split("-")))

    write_with_template(template_variable="vagas", content=render_items, template_file_name="data.js", destiny_file_name=js_file_name)
    write_with_template(template_variable="js_file", content=js_file_name, template_file_name="template.html", destiny_file_name="index.html")

    write_with_template(template_variable="last_date", content=last_date, template_file_name="../public/index.html", destiny_file_name="index.html")
    write_with_template(template_variable="first_date", content=first_date, template_file_name="../public/index.html", destiny_file_name="index.html")

    print("website rendered")
    return

def write_with_template(template_variable, content, template_file_name, destiny_file_name):
    with open(f"./templates/{template_file_name}", "r") as f:
        template = f.read()
    template = template.replace("{"+ template_variable+ "}",content)
    with open(f"./public/{destiny_file_name}", "w+") as f:
        f.write(template)


def get_items_string():
    today = str(datetime.today()).split(".")[0]
    first_job_timestamp = str2timestamp(today)

    sql = """
WITH parent_url AS (
        SELECT parent_url FROM urls WHERE parent_url IS NOT NULL AND parent_url != '' GROUP BY parent_url
    ),
    parents AS (
        SELECT
            u.id,
            u.url,
            u.title
            FROM urls u
                INNER JOIN parent_url p
                    ON u.url = p.parent_url
    )
    SELECT
        u.id,
        u.url,
        u.created_at,
        COALESCE(u.title, p.title) as common_title,
        p.url as parent_url,
        p.title as parent_title,
        u.json_ai
        FROM urls u
        LEFT JOIN parents p
            ON u.parent_url = p.url
        WHERE
            u.history = 0
            AND u.ai_processed = 1
            AND u.json_ai != "children-update"
            AND u.json_ai != "empty result"
            AND u.url NOT IN (SELECT url FROM parents)
        ORDER BY u.created_at DESC"""
    conn = get_connection()
    df = pd.read_sql_query(
    sql,
    conn,
    )

    render_items = ""
    render_types = {}
    #for index, row in df.iterrows():
    for index, df_item in df.iterrows():
        published_on = datetime.fromtimestamp(int(df_item["created_at"])).strftime("%d/%m/%y")
        json_item = json.loads(df_item["json_ai"])

        if int(first_job_timestamp) > int(df_item["created_at"]):
            first_job_timestamp = int(df_item["created_at"])

        if len(json_item['local']) == 0:
            json_item['local'] = "Local não Informado"

        if len(json_item['prazo']) == 0:
            json_item['prazo'] = "Prazo não Informado"
        else:
            if str(json_item['prazo'][0]).isdigit():
                json_item['prazo'] = "até " + json_item['prazo']

        icon_url = urlicon.get_url_icon(df_item["url"])
        if icon_url.startswith("https://ui-avatars.com/"):
            icon = icon_url
        else:
            icon_name = df_item["id"]
            icon = f"icons/{icon_name}"
            icon_file_content = urlicon.requests_get(icon_url)
            try:
                with open(f"./public/icons/{icon_name}", "wb") as icon_writer:
                    icon_writer.write(icon_file_content)
            except:
                icon = f"icons/{icon_name}.svg"
                with open(f"./public/icons/{icon_name}.svg", "w+") as icon_writer:
                    icon_writer.write(icon_file_content)

        item = f"""
                id: {json_item['id']},
                title: "{json_item['cargo']}",
                company: "{json_item['contratante']}",
                location: "{json_item['local']}",
                type: "{json_item['tipo']}",
                salary: "{json_item['salario']}",
                description: "Publicado em {published_on}",
                posted: "{json_item['prazo']}",
                tags: [""],
                url: "{df_item["url"]}",
                icon: "{icon}"
        """
        render_items += "{" + item + "} , "
        render_types[json_item['tipo']] = json_item['tipo']
        print('added', df_item["url"])


    render_items = f"[ {render_items} ]"
    return render_items

def get_connection():
    db_file = os.path.join(config.get_dir("db"),config.get_db())
    conn = sqlite3.connect(db_file)
    return conn

def clean_dir(dir_name):
    ensure_dir(dir_path=dir_name)
    files_to_delete = os.listdir(dir_name)
    for file_to_delete in files_to_delete:
        file_to_delete = os.path.join(dir_name,file_to_delete)
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

def str2timestamp(str_date:str,str_format:str='%Y-%m-%d %H:%M:%S'):
    timestamp = str(datetime.strptime(str(str_date), str_format).timestamp()).split(".")[0]
    return timestamp

if __name__ == "__main__":
    main()
