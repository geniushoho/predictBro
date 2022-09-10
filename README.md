# predictBro
預測哥2Line GX退休金程式

#Version Control
#V1 predict_Bro_in.py
#V2 predict_Bro_20211116.py
#V3 predict_Bro_20211202.py
#Latest predict_Bro_20220908.py


# 如何轉exe檔 by Docker on Mac
cd ~/Downloads/predictBro-master2/
Pyinstaller -F line.py
cp -rf line.spec ~/Downloads/docker-pyinstaller-master/src/
cp -rf line.py ~/Downloads/docker-pyinstaller-master/src/
cd ~/Downloads/docker-pyinstaller-master/src/
rm -rf requirements.txt
pipreqs ./
#turn Docker
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
