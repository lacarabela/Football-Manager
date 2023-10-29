import pandas as pd
import glob
import os

# Finding most recent generated squad file from FM24 in html
file_list = glob.glob(os.path.join(r'C:/Users/maldo/fm24 - py','*'))
latest_file = max(file_list, key=os.path.getctime)

# Read html squad file
squad_rawdata_list = pd.read_html(latest_file, header=0, encoding="utf-8", keep_default_na=False)

# Turning squad rawdata from a list to a dataframe
squad_rawdata = squad_rawdata_list[0]

# calculating scores for 4-2-3-1 Gengen Press

# working

# Pressing forward on attack Score
squad_rawdata['pf_green'] = ((
    (squad_rawdata['Agg'] * 5) +
    (squad_rawdata['Ant'] * 5) +
    (squad_rawdata['Bra'] * 5) +
    (squad_rawdata['Otb'] * 5) +
    (squad_rawdata['Tea'] * 5) + 
    (squad_rawdata['Wor'] * 5) +   
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Sta'] * 5)) / 45
    )

squad_rawdata['pf_blue'] = ((
    (squad_rawdata['Fin'] * 2.5) +
    (squad_rawdata['Fir'] * 2.5) +
    (squad_rawdata['Cmp'] * 2.5) +
    (squad_rawdata['Cnt'] * 2.5) +
    (squad_rawdata['Dec'] * 2.5) +
    (squad_rawdata['Agi'] * 2.5) +
    (squad_rawdata['Bal'] * 2.5) +
    (squad_rawdata['Str'] * 2.5)) / 20
    )

squad_rawdata['pf_white'] = ((
    (squad_rawdata['Cro']) +
    (squad_rawdata['Dri']) +
    (squad_rawdata['Hea']) +
    (squad_rawdata['Lon']) +
    (squad_rawdata['Mar']) +
    (squad_rawdata['Pas']) +
    (squad_rawdata['Tck']) +
    (squad_rawdata['Tec']) +
    (squad_rawdata['Det']) +
    (squad_rawdata['Fla']) +
    (squad_rawdata['Ldr']) +
    (squad_rawdata['Pos']) +
    (squad_rawdata['Vis']) +
    (squad_rawdata['Jum'])) / 14
    )

squad_rawdata['pf'] = ((squad_rawdata['pf_green']) + (squad_rawdata['pf_blue']) + (squad_rawdata['pf_white']))
squad_rawdata.pf = squad_rawdata.pf.round(1)

squad_rawdata

def generate_html(dataframe: pd.DataFrame):
    table_html = dataframe.to_html(table_id="table", index=False)

    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                paging: false,
                order: [[12, 'desc']],
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """

    return html