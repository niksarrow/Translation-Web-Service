#!/bin/sh

LOWERCASER=/home/development/nikhils/codebase/tools/mosesdecoder/scripts/tokenizer/lowercase.perl
IN_FILE=/home/development/nikhils/temporary/IITB_speech/test_0.raw
OUT_LOWER=/home/development/nikhils/temporary/IITB_speech/test_0.lower
OUT_FINAL=/home/development/nikhils/temporary/IITB_speech/test_0.txt

$LOWERCASER < $IN_FILE > $OUT_LOWER
sed "/[[:punct:]]*/{ s/[^[:alnum:][:space:]']//g}" $OUT_LOWER > $OUT_FINAL

