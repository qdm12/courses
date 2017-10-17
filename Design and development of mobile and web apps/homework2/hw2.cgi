#!/usr/bin/sh

echo "Content-type: text/html"
# The Content-type: line has to be followed by a blank to be recognized by the browser
echo
echo "<HTML>"
echo "<HEAD><TITLE>Websys Directory Listing</TITLE></HEAD>"
echo "<link rel=\"stylesheet\" type=\"text/css\" href=\"hw2.css\">"
echo "<BODY>"
# the <pre> command tells the browser that the following
# lines are PREFORMATTED, hence don't wrap them together
echo "<pre>"

# comment the next line to turn off debugging output
#set

# QUERY_STRING except for the &'s so we will use sed to change all &'s to spaces in QUERY_STRING then we take the output of 
# that operation and execute it (EVAL) as a shell command
# set fchar=a userid=aab211
# and it must be marked as executable for others (i.e. chmod o+rx hw2.cgi)
# The "eval" line creates a shell variable for each form field
# by issuing a 
#  field1=value1 field2=value2 etc
# The values of these variables can now be used later in the script
# by putting a $ in front of the fieldname
# eval line echos the input line and pipes it to a sed program that changes
# & to blank, hence fchar=a&userid=aab211 becomes 
#  fchar=a userid=aab211

# The line below is the black box that create variables for all of the for fields
######################################################################
eval  ` ( echo $QUERY_STRING | sed -e "s/\&/ /g") `
#####################################################################

if [ -v ${userid} ]; then
    echo "<br><br><h2>The userid parameter was not passed. Please try again.</h2><br><br>"
else
	echo "<div class=\"fullcontainer\">"
    echo "<div style=\"position:absolute;width:70%;left:15%;top:0;font-size:3vw;text-align:center;\">Directory listing for user ${userid}</div>"
    TARGET_PATH=/homedir/grad/${userid:0:1}/$userid/public_html/websys/
    if [ -d "$TARGET_PATH" ]; then
		echo "<div style=\"position:absolute; width:50%;top:4.5%;left:25%;\">"
		echo "<ul>"
        WORDS=($(ls -t))
        # -t to sort by last modified (-c)
		COLOR=blue
        for name in "${WORDS[@]}"
        do
			:
			if [ -d "$TARGET_PATH/$name" ]; then
				COLOR=blue
			else
				case ${name:(-4)} in
					".cgi") COLOR=purple ;;
					"html") COLOR=orange ;;
					".css") COLOR=pink ;;
					*) COLOR=green ;;
				esac
			fi
			echo "<li style=\"font-size:2.5vh;margin:0;top:0;padding:0;\"><a style=\"color:$COLOR;\" target=\"_blank\" href=\"http://websys3.stern.nyu.edu/~$userid/websys/$name\">$name</a></li>"
        done
		echo "</ul>"
		echo "</div>"
		echo "</div>"
        # maybe use */ to display all sub files
        # ls -1 -t -s -h --color=auto /homedir/grad/${userid:0:1}/$userid/public_html/websys/*
        # -l for displaying one entry per row
        # -t to sort by last modified (-c)
        # -s to display sizes, -h for sizes humanly readable
    else
        echo "<br><b>$TARGET_PATH</b> was not found...<br>"
    fi
fi
    
echo "</pre>"
echo "</BODY></HTML>"
