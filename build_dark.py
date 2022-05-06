import os

light_file_path = "./math2111.tex"
dark_file_path = "./math2111_dark.tex"

dark_mode_specifiers = r"""
 
\documentclass[12pt, letterpaper]{article}
\usepackage{xcolor}
\pagecolor[rgb]{0,0,0}
\color[rgb]{1, 1, 1}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{fancyhdr}
\usepackage[utf8]{inputenc}
\usepackage{dirtytalk}                      % \say command for quotes
\usepackage{ wasysym }
\usepackage{graphicx}
\usepackage{physics}
\usepackage{esint}
\usepackage{subfiles}

% Dark Mode
% \usepackage{xcolor}
% \pagecolor[rgb]{0,0,0} %black
% \color[rgb]{1, 1, 1} %white


\usepackage{hyperref}
\hypersetup {                                % Formatting for hyperlinks
    colorlinks,
    citecolor=white,
    filecolor=white,
    linkcolor=white,
    urlcolor=white
}

\graphicspath{'./assets/'}								% Path for images

\pagestyle{fancy}
\setlength{\headheight}{15pt}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}	
\title{Higher Several Variable Calculus \\ Math2111 UNSW}
\author{Hussain Nawaz \\ hussain.nwz000@gmail.com}
\date{2022T1}

\rhead{}
\lhead{}

"""

def empty_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"Successfully deleted file at {path}")
    with open(path, "x") as f:
        print(f"Successfully created empty file at {path}")

def add_dark_mode(path):
    with open(path, "w") as f:
        f.write(dark_mode_specifiers)

def append_file(src_path, dest_path):
    with open(dest_path, "a") as dest:
        with open(src_path, "r") as src:
            in_preamble = True
            for line in src:
                if r"\begin{document}" in line:
                    in_preamble = False
                if not in_preamble:
                    dest.write(line)
    print(f"Successfully transferred contents from {src_path} to {dest_path}")
                
def build_dark(path):
    os.system(f"pdflatex {path}")
    return
    

def cleanup():
    return

def main():
    empty_file(dark_file_path)
    add_dark_mode(dark_file_path)
    append_file(light_file_path, dark_file_path)
    build_dark(dark_file_path)
    cleanup()




if __name__ == "__main__":
    main()
    
