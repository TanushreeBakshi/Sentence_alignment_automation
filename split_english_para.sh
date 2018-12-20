sed 's/[.!?]  */&\n/g' < $1 | sed  '/^$/d' > sen;
grep -v "^$" sen > $2;
rm sen
