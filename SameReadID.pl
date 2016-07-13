#!usr/bin/perl

use strict; 
use warnings; 

open(INFILE1, "temp5n8.txt") 
|| die("Could not open Chr5");
open(INFILE2, "temp8n5.txt") 
|| die("Could not open Chr8");
open(OUTFILE, ">mateInChr8.txt") 
|| die("Cannot create new outputfile.\n");

#create array and save each line as a string in the array
my @chr5n8array;
while (my $line1 = <INFILE1>){
	chomp($line1); 
	push(@chr5n8array, $line1);
}
#print "@chr5n8array";

my @chr8n5array;
while (my $line2 =<INFILE2>){
	chomp($line2); 
	push(@chr8n5array, $line2);
}

#loop through the template names from the chr5 data
for(my $i = 0; $i < scalar(@chr5n8array); $i++){ 
	my $cur = $chr5n8array[$i];
	my @curarr = split("\t", $cur);
	my $tempn = $curarr[0];
	#print "$tempn\n";
	
	for (my $k=0; $k < scalar(@chr8n5array); $k++){
		my $cul = $chr8n5array[$k];
		my @curli = split("\t", $cul);
		my $temp = $curli[0];
		#print "$temp";
		
		if ($temp eq $tempn){
			print OUTFILE "Chr5: @curarr\n";
			print OUTFILE "Chr8: @curli\n\n";
		}
	}
}
close OUTFILE;