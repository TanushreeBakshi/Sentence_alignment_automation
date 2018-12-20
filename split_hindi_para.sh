sed -e 's/|/.\n/g' < $1 |  sed -e 's/।/.\n/g' | sed -e 's/\?/\?\n/g' | sed -e 's/^ //g' |  sed -n '1h;2,$H;${g;s/^\n$//g;p}' | sed -e 's/^[ ]*$//g' | sed -e 's/! /!\n/g' | sed 's/&gt;/>/g' | sed 's/&lt;/</g' | sed 's/[ ][ ]*/ /g' | sed 's/^ //g' | sed 's/&amp;/\&/g'  >  sen
	grep -v "^$" sen > $2;
rm sen;
