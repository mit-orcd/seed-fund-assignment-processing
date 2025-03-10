# One hand written line for testing whether generated code is working
# For test a.txt and b.txt it tests the number of entries for each document in 
# assu=ignments.txt. Each document should appear twice only.
cat assignments.txt |  tr ',' ' ' | tr ' ' '\n' | sort | uniq -c | grep ' b[0-9]'
