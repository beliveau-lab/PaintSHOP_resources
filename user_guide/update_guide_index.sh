#!/bin/bash

# configure file paths
HTML_FILE="PaintSHOP_user_guide.html"
DEST_FILE="index.html"

# check whether html files differ
diff $HTML_FILE $DEST_FILE > /dev/null
RESULT=$?
if [ $RESULT -eq 0 ]; then
	echo "Files do not differ. Exiting..."
else
	echo "Files differ. Overwriting $DEST_FILE with latest version..."
	cp PaintSHOP_user_guide.html index.html
fi

# success
echo "DONE!"
