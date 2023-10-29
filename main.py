import pandas as pd
import os
import uuid

# Finding most recent generated squad file from FM24 in html
directory = r'C:/Users/maldo/OneDrive/Desktop/Football_Manager py/Football-Manager/html files'
file_list = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".html")]
latest_file = max(file_list, key=os.path.getctime)
print(latest_file)

# Read html squad file
squad_rawdata_list = pd.read_html(latest_file, header=0, encoding="utf-8", keep_default_na=False)

# Turning squad rawdata from a list to a dataframe
squad_rawdata = squad_rawdata_list[0]

# calculating scores for 4-2-3-1 Gengen Press
# Sweeper Keeper on Defend Score
squad_rawdata['sk_green'] = ((
    (squad_rawdata['Ref'] * 5) +
    (squad_rawdata['Agi'] * 5)) / 10
    )

squad_rawdata['sk_blue'] = ((
    (squad_rawdata['Acc'] * 2.5) +
    (squad_rawdata['Aer'] * 2.5) +
    (squad_rawdata['Han'] * 2.5) +
    (squad_rawdata['Cmd'] * 2.5) +
    (squad_rawdata['Kic'] * 2.5) +
    (squad_rawdata['1v1'] * 2.5) +
    (squad_rawdata['Pas'] * 2.5) + 
    (squad_rawdata['TRO'] * 2.5) +
    (squad_rawdata['Ant'] * 2.5) +
    (squad_rawdata['Cmp'] * 2.5) +
    (squad_rawdata['Cnt'] * 2.5) +
    (squad_rawdata['Dec'] * 2.5) +
    (squad_rawdata['Pos'] * 2.5) +
    (squad_rawdata['Vis'] * 2.5)) / 35
    )

squad_rawdata['sk_white'] = ((
    (squad_rawdata['Cmp']) +
    (squad_rawdata['Fir']) +
    (squad_rawdata['Thr'])) / 3
    )

squad_rawdata['sk'] = (((squad_rawdata['sk_green']) + (squad_rawdata['sk_blue']) + (squad_rawdata['sk_white'])) / 3)
squad_rawdata.sk = squad_rawdata.sk.round(1)

# Wing Back Scores
squad_rawdata['wb_green'] = ((
    (squad_rawdata['OtB'] * 5) +
    (squad_rawdata['Wor'] * 5) +
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Sta'] * 5)) / 25
    )

squad_rawdata['wb_blue'] = ((
    (squad_rawdata['Dri'] * 2.5) +
    (squad_rawdata['Mar'] * 2.5) +
    (squad_rawdata['Pas'] * 2.5) +
    (squad_rawdata['Tck'] * 2.5) +
    (squad_rawdata['Tec'] * 2.5) +
    (squad_rawdata['Ant'] * 2.5) +
    (squad_rawdata['Cnt'] * 2.5) +
    (squad_rawdata['Dec'] * 2.5) +
    (squad_rawdata['Agi'] * 2.5)) / 22.5
    )

squad_rawdata['wb_white'] = ((
    (squad_rawdata['Cro']) +
    (squad_rawdata['Pos']) +
    (squad_rawdata['Tea']) +
    (squad_rawdata['Fir']) +
    (squad_rawdata['Bal'])) / 6
    )

squad_rawdata['wb'] = (((squad_rawdata['wb_green']) + (squad_rawdata['wb_blue']) + (squad_rawdata['wb_white'])) / 3)
squad_rawdata.wb = squad_rawdata.wb.round(1)

# Central Defender on Defend Score
squad_rawdata['cd_green'] = ((
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Cmp'] * 5) +
    (squad_rawdata['Jum'] * 5)) / 20
    )

squad_rawdata['cd_blue'] = ((
    (squad_rawdata['Hea'] * 2.5) +
    (squad_rawdata['Mar'] * 2.5) +
    (squad_rawdata['Tck'] * 2.5) +
    (squad_rawdata['Agg'] * 2.5) +
    (squad_rawdata['Ant'] * 2.5) +
    (squad_rawdata['Cnt'] * 2.5) +
    (squad_rawdata['Pos'] * 2.5) +
    (squad_rawdata['Dec'] * 2.5)) / 20
    )

squad_rawdata['cd_white'] = ((
    (squad_rawdata['Bra']) +
    (squad_rawdata['Str'])) / 2
    )

squad_rawdata['cd'] = (((squad_rawdata['cd_green']) + (squad_rawdata['cd_blue']) + (squad_rawdata['cd_white'])) / 3)
squad_rawdata.cd = squad_rawdata.cd.round(1)

# DM Score
squad_rawdata['dm_green'] = ((
    (squad_rawdata['Wor'] * 5) +
    (squad_rawdata['Sta'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Pas'] * 5) +
    (squad_rawdata['Vis'] * 5) +
    (squad_rawdata['Dec'] * 5) +
    (squad_rawdata['Cmp'] * 5)) / 35
    )

squad_rawdata['dm_blue'] = ((
    (squad_rawdata['Ant'] * 2.5) +
    (squad_rawdata['OtB'] * 2.5) +
    (squad_rawdata['Fir'] * 2.5) +
    (squad_rawdata['Tec'] * 2.5) +
    (squad_rawdata['Cnt'] * 2.5) +
    (squad_rawdata['Acc'] * 2.5) +
    (squad_rawdata['Pos'] * 2.5)) / 17.5
    )

squad_rawdata['dm_white'] = ((
    (squad_rawdata['Tea']) +
    (squad_rawdata['Bal']) +
    (squad_rawdata['Str']) +
    (squad_rawdata['Dri']) +
    (squad_rawdata['Lon']) +
    (squad_rawdata['Tck']) +
    (squad_rawdata['Fla']) +
    (squad_rawdata['Agi'])) / 8
    )

squad_rawdata['dm'] = (((squad_rawdata['dm_green']) + (squad_rawdata['dm_blue']) + (squad_rawdata['dm_white'])) / 3)
squad_rawdata.dm = squad_rawdata.dm.round(1)

# Winger Score
squad_rawdata['w_green'] = ((
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Sta'] * 5) +
    (squad_rawdata['Wor'] * 5) +
    (squad_rawdata['Cro'] * 5) +
    (squad_rawdata['Dri'] * 5)) / 30
    )

squad_rawdata['w_blue'] = ((
    (squad_rawdata['Tec'] * 2.5) +
    (squad_rawdata['Agi'] * 2.5) +
    (squad_rawdata['OtB'] * 2.5) +
    (squad_rawdata['Pas'] * 2.5)) / 10
    )

squad_rawdata['w_white'] = ((
    (squad_rawdata['Fir']) +
    (squad_rawdata['Bal']) +
    (squad_rawdata['Pos']) +
    (squad_rawdata['Vis']) +
    (squad_rawdata['Ant']) +
    (squad_rawdata['Cnt']) +
    (squad_rawdata['Agg'])) / 7
    )

squad_rawdata['w'] = (((squad_rawdata['w_green']) + (squad_rawdata['w_blue']) + (squad_rawdata['w_white'])) / 3)
squad_rawdata.w = squad_rawdata.w.round(1)

# Advanced Playmaker Score
squad_rawdata['ap_green'] = ((
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Sta'] * 5) +
    (squad_rawdata['Wor'] * 5) +
    (squad_rawdata['Cmp'] * 5) +
    (squad_rawdata['Dec'] * 5) +
    (squad_rawdata['Pas'] * 5) +
    (squad_rawdata['Ant'] * 5)) / 40
    )

squad_rawdata['ap_blue'] = ((
    (squad_rawdata['Dri'] * 2.5) +
    (squad_rawdata['Fir'] * 2.5) +
    (squad_rawdata['Fla'] * 2.5) +
    (squad_rawdata['Tec'] * 2.5)) / 10
    )

squad_rawdata['ap_white'] = ((
    (squad_rawdata['Agi']) +
    (squad_rawdata['Agg']) +
    (squad_rawdata['Fin']) +
    (squad_rawdata['Vis']) +
    (squad_rawdata['Tea']) +
    (squad_rawdata['OtB'])) / 6
    )

squad_rawdata['ap'] = (((squad_rawdata['ap_green']) + (squad_rawdata['ap_blue']) + (squad_rawdata['ap_white'])) / 3)
squad_rawdata.ap = squad_rawdata.ap.round(1)

# Pressing Forward on Attack Score
squad_rawdata['pf_green'] = ((
    (squad_rawdata['Acc'] * 5) +
    (squad_rawdata['Dri'] * 5) +
    (squad_rawdata['Pac'] * 5) +
    (squad_rawdata['Cmp'] * 5) +
    (squad_rawdata['Fin'] * 5) +
    (squad_rawdata['Wor'] * 5) +   
    (squad_rawdata['Sta'] * 5)) / 35
    )

squad_rawdata['pf_blue'] = ((
    (squad_rawdata['Fir'] * 2.5) +
    (squad_rawdata['Agg'] * 2.5) +
    (squad_rawdata['Ant'] * 2.5) +
    (squad_rawdata['Dec'] * 2.5) +
    (squad_rawdata['OtB'] * 2.5) +
    (squad_rawdata['Bal'] * 2.5)) / 15
    )

squad_rawdata['pf_white'] = ((
    (squad_rawdata['Bra']) +
    (squad_rawdata['Cnt']) +
    (squad_rawdata['Tea']) + 
    (squad_rawdata['Str']) +
    (squad_rawdata['Agi'])) / 5
    )

squad_rawdata['pf'] = (((squad_rawdata['pf_green']) + (squad_rawdata['pf_blue']) + (squad_rawdata['pf_white'])) / 3)
squad_rawdata.pf = squad_rawdata.pf.round(1)

# Generating basic values for Speed and Work Rate to look at depending on the positions necessities
squad_rawdata['Speed'] = ( squad_rawdata['Pac'] + squad_rawdata['Acc'] ) / 2
squad_rawdata['WorkRate'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] ) / 2

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

squad = squad_rawdata[['Inf','Name','Age','Club','Transfer Value','Salary','Nat','Position','Personality','Media Handling','Left Foot', 'Right Foot','Speed','Jum','Str','WorkRate','Height','sk','cd','wb','dm','ap','w','pf']]

# Creating and randomizing the title of the final viewable html file
filename = str(uuid.uuid4()) + ".html"
html = generate_html(squad)
open(filename, "w", encoding="utf-8").write(html)
os_filename = (r'C:/Users/maldo/OneDrive/Desktop/Football_Manager py/Football-Manager/Results' + filename)
