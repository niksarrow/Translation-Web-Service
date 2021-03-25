SRC=dis
TGT=flu
MASS_PATH=/home/development/nikhils/codebase/MASS/MASS-unsupNMT
TOOLS_PATH=/home/development/nikhils/codebase/seminar/iwslt_2020/tools
DATA_PATH=/home/development/nikhils/WAT/data
PARA_PATH=/home/development/nikhils/WAT/data/swbd/para
MONO_PATH=/home/development/nikhils/WAT/data/swbd/mono
TEXT_PATH=/home/development/nikhils/WAT/data/webservice
PROC_PATH=$DATA_PATH/processed/swbd
BPE_CODES=$PROC_PATH/codes
SRC_VOCAB=$PROC_PATH/vocab.$SRC
TGT_VOCAB=$PROC_PATH/vocab.$TGT
FULL_VOCAB=$PROC_PATH/vocab.$SRC-$TGT
CODES=50000

# fastBPE
FASTBPE_DIR=$TOOLS_PATH/fastBPE
FASTBPE=$FASTBPE_DIR/fast

mkdir -p $PROC_PATH

echo "Applying $SRC BPE codes..."
$FASTBPE applybpe $TEXT_PATH/dis.bpe $TEXT_PATH/dis.txt $BPE_CODES.$CODES

echo "Binarizing ..."
python $MASS_PATH/preprocess.py $FULL_VOCAB $TEXT_PATH/dis.bpe


ln -sf $TEXT_PATH/dis.bpe.pth $TEXT_PATH/test.dis-flu.dis.pth
ln -sf $TEXT_PATH/dis.bpe.pth $TEXT_PATH/test.dis-flu.flu.pth
ln -sf $TEXT_PATH/dis.bpe.pth $TEXT_PATH/valid.dis-flu.dis.pth
ln -sf $TEXT_PATH/dis.bpe.pth $TEXT_PATH/valid.dis-flu.flu.pth
