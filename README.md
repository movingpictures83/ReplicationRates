# ReplicationRates
# Language: Python
# Dependency: iRep
# Input: TXT 
# Output: varies
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to compute replication rates for bacteria
using the method of (Brown et al, 2016).  Their method is
able to compute these rates using metagenomics data from
one single timepoint.

This plugin can run using one of their three packages:
iRep (for draft-quality sequences), bPTR (for complete genome sequences), 
and gc_skew.py (a Python script that computes GC skew).
More information can be found here:
https://github.com/christophertbrown/iRep
iRep is avilable under the MIT Open Source License, as is ReplicationRates
and a copy of this license has been included.
Input FASTA and SAM data in our examples/ directory is the same
as those released open source by iRep at the time of this release

The input TXT file contains keyword/value pairs, separated by TABs.  
Required keywords:

package (either iRep, bPTR, or gc_skew.py)
fasta (input FASTA file)

for iRep/bPTR:
sam (input SAM file)

for bPTR:
plot (output PDF file for plot)
coverage (yes or no)

The Output will vary based on the package, as follows:
iRep: Output prefix, for TSV and PDF file
bPTR: TSV
gc_skew.py: none, outputs to screen




