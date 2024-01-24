# Football Manager Squad/Shortlist Analysis Tool

The Football Manager Squad/Shortlist Analysis Tool is an application for Football Manager that allows users to effectively analyze their squads' capabilities, as well as potential players to add to their squad. By importing squad and shortlist data into the tool, users can gain valuable insights into player statistics, performances, and a player's suitability for specific positions.

Built with the Python programming language and leveraging the data processing power of Pandas, this tool transforms raw Football Manager export data into informative HTML tables. Whether you are looking to optimize your team selection, scout for new talent, or enjoy the data-driven aspects of Football Manager, this tool can help elevate your managerial skills.

## Installation

Before running the application, ensure you have Python installed on your system. 
Python can be downloaded from the official website: [python.org](https://www.python.org/downloads/).

After installing Python, download the source code for the Football Manager Squad/Shortlist Analysis Tool.

To install the necessary Python Packages, follow these steps.

1. Open the folder containing the downloaded source code.
2. Move to the folder 'setup_files', and double-click on the 'setup.bat' if you are on a Windows OS or 'setup.sh' if you are on a Unix-based OS like Mac.
3. Follow any on-screen prompts to complete the installation if necessary.

The setup scripts should automatically install the needed packages for the application to function correctly.

## Downloading and Importing Custom Views

To ensure you extract the correct data from Football Manager for use with this tool, please make sure you have downloaded the source code. 
The views that will be imported can be found in the folder named 'FM_views'

### Applying the Views 

Applying view to squad list:

![](https://github.com/lacarabela/Football-Manager/blob/main/readme_extras/view_import_squad.gif)

Applying view to Shortlist:

![](https://github.com/lacarabela/Football-Manager/blob/main/readme_extras/view_import_shortlist.gif)

## Usage

### Preparing Data for Analysis

Before you can analyze your squad and shortlist with the Football Manager Squad/Shortlist Analysis Tool, you need to export the data from Football Manager into an HTML file. Follow these steps to prepare your data:

1. In Football Manager, navigate to the squad or shortlist you wish to analyze.
2. Select all the players you want to include in the analysis, or you could simply use `Ctrl+A` to select all the players.
3. Press `Ctrl+P` to open the print options.
4. Choose to 'Print as a web page' or similar option to generate an HTML file.
5. Save the generated HTML file in a folder that you can easily access later.

![](https://github.com/lacarabela/Football-Manager/blob/main/readme_extras/downloading_squad_rawdata.gif)


### Using the Tool

![](https://github.com/lacarabela/Football-Manager/blob/main/readme_extras/using_tool.gif)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgements

This project was inspired by the video tutorial ["How to Analyze Your Football Manager Squad"](https://www.youtube.com/watch?v=hnAuOakqR90) by Squirrel_plays on YouTube. A special shoutout to them for the idea and for providing a foundation upon which this tool was built upon.

The `generate_html` function used in this project to convert pandas DataFrames to HTML tables was sourced from [x4nth055's GitHub repository](https://github.com/x4nth055/pythoncode-tutorials/tree/master/general/dataframe-to-html).

Third-Party Libraries Used:
- [Pandas](https://pandas.pydata.org/)

## Future Plans

- **Generalization for All Playing Positions:** I plan to generalize the tool's analytical capabilities to accommodate all playing positions within Football Manager. This will allow for a more versatile analysis that is not limited to specific roles on the pitch.

- **Attribute System Enhancement:** By refining the attribute analysis system, I aim to offer a more nuanced and precise evaluation of a player's skills and suitability for various roles, enhancing the tool's utility in squad management and player assessment.

- **Graphical User Interface (GUI) Improvements:** I plan to overhaul the GUI for ease of use, better navigation, and a more aesthetically pleasing design.

- **Creating a Standalone Executable:** To reach a wider audience and facilitate ease of access, I hope to package the tool as a distributable executable, eliminating the need for a separate Python environment or dependency installation.
