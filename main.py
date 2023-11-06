import pandas as pd
import os
import uuid
import webbrowser
import tkinter as tk
from tkinter import filedialog, ttk
import webbrowser

# https://thepythoncode.com/code/convert-pandas-dataframe-to-html-table-python
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

def browse_file():
    file_path = filedialog.askopenfilename(title="Select HTML File", filetypes=[("HTML Files", "*.html")])
    if file_path:
        analyze = tk.messagebox.askyesno("Analyze File", f"Do you want to analyze {file_path}?")
        if analyze:
            label.config(text=f"Selected file: {file_path}")
            result_filepath = analyze_file(file_path)
            print("Analysis complete")
            if result_filepath:
                print("opening Result")
                tk.messagebox.showinfo("Analysis Completed", f"Analysis results saved to:\n{result_filepath}")
                webbrowser.open(file_path)
            else:
                print("no result filepath")
                print(result_filepath)

def calculate_score(df, stats, weight):
    score = sum(df[stats] *  weight for stats, weight in zip(stats, weight)) / (sum(weight))
    return score.round(1)

def analyze_file(input_file_path):
    weight_key = 5
    weight_preferred = 2.5
    weight_normal =1

    squad_rawdata = pd.read_html(input_file_path, header=0, encoding="utf-8", keep_default_na=False)[0]

    role_definitions = {
        'sk' : {
            'key_stats' : ['Ref', 'Agi'],
            'preferred_stats' : ['Acc', 'Aer', 'Han', 'Cmd', 'Kic', '1v1', 'Pas', 'TRO', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Vis'],
            'normal_stats' : ['Cmp', 'Fir', 'Thr']
        },
        'wb' : {
            'key_stats' : ['OtB', 'Wor', 'Acc', 'Pac', 'Sta'],
            'preferred_stats' : ['Dri', 'Mar', 'Pas', 'Tck', 'Tec', 'Ant', 'Cnt', 'Dec', 'Agi'],
            'normal_stats' : ['Cro', 'Pos', 'Tea', 'Fir', 'Bal']
        },
        'cd' : {
            'key_stats' : ['Acc', 'Pac', 'Cmp', 'Jum'],
            'preferred_stats' : ['Hea', 'Mar', 'Tck', 'Agg', 'Ant', 'Cnt', 'Pos', 'Dec'],
            'normal_stats' : ['Bra', 'Str']
        },
        'dm' : {
            'key_stats' : ['Wor', 'Sta', 'Pac', 'Pas', 'Vis', 'Dec', 'Cmp'],
            'preferred_stats' : ['Ant', 'OtB', 'Fir', 'Tec', 'Cnt', 'Acc', 'Pos'],
            'normal_stats' : ['Tea', 'Bal', 'Str', 'Dri', 'Lon', 'Tck', 'Fla', 'Agi']
        },
        'w' : {
            'key_stats' : ['Acc', 'Pac', 'Sta', 'Wor', 'Cro', 'Dri'],
            'preferred_stats' : ['Tec', 'Agi', 'OtB', 'Pas'],
            'normal_stats' : ['Fir', 'Bal', 'Pos', 'Vis', 'Ant', 'Cnt', 'Agg']
        },
        'ap' : {
            'key_stats' : ['Acc', 'Pac', 'Sta', 'Wor', 'Cmp', 'Dec', 'Pas', 'Ant'],
            'preferred_stats' : ['Dri', 'Fir', 'Fla', 'Tec'],
            'normal_stats' : ['Agi', 'Agg', 'Fin', 'Vis', 'Tea', 'OtB']
        },
        'pf' : {
            'key_stats' : ['Acc', 'Dri', 'Pac', 'Cmp', 'Fin', 'Wor', 'Sta'],
            'preferred_stats' : ['Fir', 'Agg', 'Ant', 'Dec', 'OtB', 'Bal'],
            'normal_stats' : ['Bra', 'Cnt', 'Tea', 'Str', 'Agi']
        }
    }

    squad_rawdata['Speed'] = ( squad_rawdata['Pac'] + squad_rawdata['Acc'] ) / 2
    squad_rawdata['WorkRate'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] ) / 2

    for role, stat_dict in role_definitions.items():
        key_weights = [weight_key] * len(stat_dict['key_stats'])
        squad_rawdata[f'{role}_key'] = calculate_score(squad_rawdata, stat_dict['key_stats'], key_weights)

        preferred_weights = [weight_preferred] * len(stat_dict['preferred_stats'])
        squad_rawdata[f'{role}_preferred'] = calculate_score(squad_rawdata, stat_dict['preferred_stats'], preferred_weights)
        
        normal_weights = [weight_normal] * len(stat_dict['normal_stats'])
        squad_rawdata[f'{role}_normal'] = calculate_score(squad_rawdata, stat_dict['normal_stats'], normal_weights)

        squad_rawdata[role] = ((squad_rawdata[f'{role}_key'] + 
                                squad_rawdata[f'{role}_preferred'] + 
                                squad_rawdata[f'{role}_normal']) /3).round(1)

    squad_data = squad_rawdata[['Inf','Name','Age','Club','Transfer Value','Salary','Nat','Position','Personality','Media Handling','Left Foot', 'Right Foot','Speed','Jum','Str','WorkRate','Height','sk','cd','wb','dm','ap','w','pf']]

    return save_and_output_results(squad_data)

def save_and_output_results(squad_data):
    results_directory = "Results"
    if not os.path.exists(results_directory):
        os.makedirs(results_directory)

    # Creating and randomizing the title of the final viewable html file
    filename = str(uuid.uuid4()) + ".html"
    filepath = os.path.join(results_directory, filename)
    html = generate_html(squad_data)
    open(filepath, "w", encoding="utf-8").write(html)
    print(f"Analysis results saved to {filepath}")
    return filepath

def close_window():
    root.destroy()

colors = {
    "bg": "#3D30A2",
    "secondary_bg": "#F7EFE5",
    "accent": "#7743DB",
}

# Creating main window
root = tk.Tk()
root.title("FM24 Analysis Tool")
root.geometry("800x600")
root.resizable(False, False)
root.configure(background=colors["bg"])

style = ttk.Style()
style.configure('TButton', background=colors["accent"], foreground='black', bordercolor=colors["accent"], font=('Arial', 12, 'bold'))
style.configure('TLabel', background=colors["secondary_bg"], foreground=colors["accent"], font=('Arial', 12))
style.configure('TFrame', background=colors["bg"])

frame = ttk.Frame(root, padding="20", style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor="center")  # This will center the frame in the window

label = ttk.Label(frame, text="", style='TLabel')
label.grid(row=0, column=0, pady=10, sticky="nsew")

# Make browse_button a child of frame
browse_button = ttk.Button(frame, text="Browse HTML File", command=browse_file, style='TButton')
browse_button.grid(row=1, column=0) 

# Making sure exit button is centered and at the bottom 
bottom_frame = ttk.Frame(root, style='TFrame')
bottom_frame.pack(side=tk.BOTTOM,  fill=tk.X, pady=10)

# Exit button creation
exit_button = ttk.Button(bottom_frame, text="EXIT", command=close_window, style='TButton')
exit_button.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
