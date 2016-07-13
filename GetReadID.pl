#!usr/bin/perl

use strict; 
use warnings; 

open(INFILE, "Reads.txt") 
|| die("Could not open infile");

open(OUTFILE, ">output.txt") 
|| die("Cannot create new outputfile.\n");

while (my $line =<INFILE>){
	chomp($line); 
	my @linearray = split("\t", $line);
	print OUTFILE "$linearray[0]\n";
}

