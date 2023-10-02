This is a python script that reads an strace output and prints the libraries that the execution had trouble finding.

Run your snap `snap run --strace <snap-name> 2> output` and then pass the output as a parameter to the script.
