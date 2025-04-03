import sys

if len(sys.argv) > 1 and sys.argv[1] == "web":
    from gui_streamlit import run_streamlit
    run_streamlit()
else:
    from gui_tkinter import run_tkinter
    run_tkinter()
