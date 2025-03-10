cat assignments.txt |  tr ',' ' ' | tr ' ' '\n' | sort | uniq -c | grep ' b[0-9]'
