

import sys


usage = """
To run ratapps, please specify which application to
run as an argument. Valid applications are:
  Xmaze
  Openfield
  Whitebox
  SPGAnalysis
"""

try:
    app = sys.argv[1].lower()
except:
    app = "fail"

if app == "xmaze":
    print("Launching XMaze")
    import ratapps.xmaze
    ratapps.xmaze.main()
elif app == "openfield":
    print("Launching Openfield")
    import ratapps.openfield
    ratapps.openfield.main()
elif app == "spganalysis":
    print("Launching SPGAnalysis")
    import ratapps.spganalysis
    ratapps.spganalysis.main()
elif app == "whitebox":
    print("Launching Whitebox")
    import ratapps.whitebox
    ratapps.whitebox.main()

else:
    print(usage)
    sys.exit(0)