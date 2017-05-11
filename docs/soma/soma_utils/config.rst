EXAMPLE OF A ROI-object KB

| { "1": { # ROI ID "name" : "kitchen table", # OPTIONAL NAME OF THE ROI
|  "pos\_objects" : ["cup", "plate"] # ALLOWED OBJECTS (IF MISSING
EVERYTHING EXCEPT NEG-OBJECT ARE ALLOWED) }, "2": { # ROI ID "name" :
"kitchen counter", # OPTIONAL NAME OF THE ROI "neg\_objects" :
["unknown"] # NOT-ALLOWED OBJECTS (IF MISSING EVERYTHING EXCEPT
POS-OBJECTS ARE NOT-ALLOWED) } "3": { # ROI ID "name" : "meeting room
table", # OPTIONAL NAME OF THE ROI "pos\_objects" : ["projector"], #
ALLOWED OBJECTS (IF MISSING EVERYTHING EXCEPT NEG-OBJECT ARE ALLOWED)
"neg\_objects" : ["cup"] # NOT-ALLOWED OBJECTS (IF MISSING EVERYTHING
EXCEPT POS-OBJECTS ARE NOT-ALLOWED) } } ###
