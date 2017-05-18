apt-get update
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

pip search virtualenv
pip install virtualenv
-------
Installing librdkafka (build librdkafka first,then pykafka)
apt-get install build-essential
mkdir track_it
cd track_it/
virtualenv  venv 
source venv/bin/activate
ls
git clone https://github.com/edenhill/librdkafka.git
ls
cd librdkafka/ 
./configure
make
make install
locate librdkafka.so 

cd ..
git clone https://github.com/Parsely/pykafka.git
cd pykafka/
python setup.py  develop 
(venv) feroz@kafka1:~/track_it$ ls
librdkafka  pykafka  venv
(venv) feroz@kafka1:~/track_it$ pwd
/home/feroz/track_it
-----------------
vim track_it/venv/bin/activate
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
source track_it/venv/bin/activate
